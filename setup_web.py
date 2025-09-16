

import platform
import subprocess
import json
import sys
import os
import shutil
import copy
import ast
import re
import base64
import requests

ATMS_URL = os.getenv("ATMS_URL")
LT_USERNAME = os.getenv("LT_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")
IGNORED_KEYS = ['variables', 'files', 'chrome_options', 'wait_buffer', 'max_network_wait', 'network_wait_for_all_actions', 'custom_headers', 'global_variables']

BASIC_AUTH = 'Basic ' + base64.b64encode(f"{LT_USERNAME}:{LT_ACCESS_KEY}".encode()).decode()

RUN_SH = """
#!/bin/bash

# Check if the argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 \"<arguments>\""
  exit 1
fi

# Assign the input to the test variable
test="$1"

# Split the test variable into an array
IFS=" " read -r -a Test <<< "$test"

# Change directory to the first element in the array
cd "${Test[0]}" || { echo "Failed to change directory to ${Test[0]}"; exit 1; }

# Run the Python script with the remaining arguments
python test.py "${Test[1]}" "${Test[2]}" "${Test[3]}" "${Test[4]}" "${Test[5]}" "${Test[6]}"
"""

RUN_BAT = """
@echo off
setlocal enabledelayedexpansion

REM Check if argument is provided
if "%~1"=="" (
    echo Usage: %~nx0 "<arguments>"
    exit /b 1
)

REM Set the variable with the command-line argument
set "test=%~1"

REM Split the variable into an array
set "args=%test%"
for /f "tokens=*" %%A in ("%args%") do (
    for %%B in (%%A) do (
        set /a count+=1
        set "arg[!count!]=%%B"
    )
)

REM Change directory to the first value (arg[1])
cd "!arg[1]!"
if errorlevel 1 (
    echo Failed to change directory to !arg[1]!
    exit /b 1
)

REM Build the command to run python with the remaining arguments
set "cmd=python test.py"
for /l %%I in (2,1,!count!) do (
    set "cmd=!cmd! !arg[%%I]!"
)

REM Execute the python command
%cmd%

REM End script
endlocal
"""

def get_architecture():
    try:
        return platform.machine().lower()
    except Exception as e:
        return "amd64"

def get_platform():
    if platform.system() == "Windows":
        try:
            result = subprocess.run(
                ["wmic", "os", "get", "Caption,Version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            output = result.stdout.strip()
            
            if result.returncode != 0:
                raise Exception(f"Error running command: {result.stderr.strip()}")
            
            if "Windows 11" in output:
                return "win11"
            else:
                return "win"
        except Exception as e:
            return f"Error: {e}"
    
    elif platform.system() == "Darwin":
        try:
            result = subprocess.run(
                ["sw_vers"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            output = result.stdout.strip()

            for line in output.splitlines():
                if line.startswith("ProductVersion:"):
                    version = line.split(":")[1].strip()
                    if version.startswith("13."):
                        return "mac13"
                    elif version.startswith("15."):
                        return "mac15"
                    else:
                        return "mac"
                    
            if result.returncode != 0:
                raise Exception(f"Error running command: {result.stderr.strip()}")
        
        except Exception as e:
            return f"Error: {e}"
    
    elif platform.system() == "Linux":
        return "linux"

def fetch_os_and_test_ids(test_run_id: str) -> tuple[dict, dict]:
    url = f"{ATMS_URL}/api/atm/v1/test-run/config/{test_run_id}"

    headers = {
        'Authorization': BASIC_AUTH
    }
    secrets = {}
    test_run_config = {}

    try:
        response = requests.request("GET", url, headers=headers, data={})
        if response.status_code != 200:
            raise Exception(f"Failed to fetch os and test ids: {response.text} || Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching os and test ids: {e}")
    
    print(f"OS, Test IDs and Secrets fetched: {response.json()}")
    test_run_config = response.json()['webTestRunConfig']
    secrets = response.json()['web_secrets']

    return test_run_config, secrets

def get_global_variables():
    print(f"Fetching global variables")
    try:
        url = f"{ATMS_URL}/api/v1/variables?type=variable"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {base64.b64encode(f'{LT_USERNAME}:{LT_ACCESS_KEY}'.encode()).decode()}"
        }
        response = requests.request(method="get", url=url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to make the request. Error: {response.text}")
            raise Exception(f"Failed to make the request. Error: {response.text}")
        
        print(f"Fetched global variables successfully")
        response = response.json()
        data = response["data"]
        global_variables = []
        for variable in data:
            global_variables.append({
                "id": variable["id"],
                "name": variable["name"],
                "value": variable["value"],
                "session_value": variable["value"],
                "is_persist": bool(variable["is_persist"]),
                "environment_id": variable["environment_id"],
                "environment_name": variable["environment_name"]
            })
        return global_variables
        
    except Exception as e:
        print(f"Error fetching global variables: {str(e)}")
        raise

def extract_folders(parent_folder, framework, language, destination_path, config_file_path, uuids=None):
    """
    Extracts 'hye_*' folders from the given parent folder and updates a JSON config file.

    Args:
        parent_folder (str): The root folder containing the UUID subdirectories.
        framework (str): Framework name to filter the paths (e.g., selenium).
        language (str): Language name to filter the paths (e.g., python).
        destination_path (str): Destination directory where the extracted folders will be copied.
        config_file_path (str): Path to the JSON config file to update.
        uuids (dict, optional): Specific {UUID:Version} to process. If None, all UUIDs will be processed.

    Returns:
        None
    """

    def _replace_param_leaf(node: dict, params: dict, keep_tag: str):
        """
        node is assumed to be a single-pair dict whose *value* is 'keep_tag'
        ('parameter' in our use-cases).

        The key may be:
            • plain          →  "discount"          : "parameter"
            • placeholder    →  "${discount}"       : "parameter"
            • double brace   →  "${{discount}}"     : "parameter"

        The function mutates 'node' in place and returns it.
        """
        (raw_key, tag), = node.items()      # unpack single item
        if tag != keep_tag:
            return node                     # nothing to do

        # extract param name
        match = re.compile(r'\$\{\{?([^{}]+?)\}?\}').match(raw_key)
        param_name = match.group(1) if match else raw_key

        new_value = params.get(param_name, "")
        node.clear()
        node[str(new_value)] = tag          # preserve the tag
        return node


    def substitute_in_math_tree(node, params):
        """Recursive substitution for expression_tree."""
        if isinstance(node, list):
            return [substitute_in_math_tree(n, params) for n in node]

        if isinstance(node, dict):
            # inner op node
            if "op" in node and "operands" in node:
                node["operands"] = [substitute_in_math_tree(o, params)
                                    for o in node["operands"]]
                return node

            # leaf possibly containing a parameter
            if len(node) == 1:
                return _replace_param_leaf(node, params, "parameter")

        return node


    def substitute_in_assertion_tree(node, params):
        """Recursive substitution for assertion_tree."""
        if isinstance(node, list):
            for i, n in enumerate(node):
                node[i] = substitute_in_assertion_tree(n, params)
            return node

        if isinstance(node, dict):
            # operator node
            if "operator" in node:
                if "operands" in node:
                    for i, o in enumerate(node["operands"]):
                        node["operands"][i] = substitute_in_assertion_tree(o, params)
                for side in ("left_operand", "right_operand"):
                    if side in node and isinstance(node[side], dict):
                        node[side] = substitute_in_assertion_tree(node[side], params)
                return node

            if len(node) == 1:
                return _replace_param_leaf(node, params, "parameter")

        return node

    def get_latest_version(folder):
        """Finds the latest version (highest numeric folder name) within a directory."""
        version_dirs = [d for d in os.listdir(folder) if d.isdigit()]
        return max(version_dirs, key=int) if version_dirs else None

    def create_operations_metadata_for_instance(test_id, destination_path, config_file, global_variables):
        """Creates the operations metadata for a given test Instance ID."""
        metadata_json_path = os.path.join(destination_path, 'operations_meta_data.json')

        with open(config_file, "r") as file:
            test_configs = json.load(file)

        with open(metadata_json_path, "r") as file:
            data = json.load(file)

        
        for key, test_config in test_configs.items():
            for test in test_config:
                if test.get("test_id") != test_id:
                    continue
                test_instance_id = test.get("test_instance_id")
                test_params = test.get("test_params",{})
                replace_url = str(os.getenv("URL_REPLACEMENT")).split(",")
                pattern_url  = str(os.getenv("URL_PATTERN")).split(",")
                new_metadata = copy.deepcopy(data)
                metadata_keys = new_metadata.keys()
                if "main_flow" in metadata_keys: 
                    for key, test_flow in new_metadata.items():
                        if key == "parameters":
                            for key, value in test_flow.items():
                                if test_params.get(key, None) != None:
                                    test_flow[key] = test_params.get(key)
                            continue       
                        if key == "global_variables":
                            new_metadata[key] = global_variables
                            continue
                        if key in IGNORED_KEYS:
                                continue
                        for key, operation_metadata in test_flow.items():
                            
                            if isinstance(operation_metadata.get('sub_instruction_obj', "{}"), str):
                                sub_instruction_obj = json.loads(operation_metadata.get('sub_instruction_obj', "{}"))
                            else:
                                sub_instruction_obj = operation_metadata.get('sub_instruction_obj', {})

                            params_used = sub_instruction_obj.get('params',{})
                            operation_type  = operation_metadata['operation_type']
                            variables_used = sub_instruction_obj.get('variable',{})
                            if operation_metadata.get('operation_type') == "MATHEMATICAL_OPERATION":
                                operation_metadata['expression_tree'] = substitute_in_math_tree(operation_metadata['expression_tree'], test_params)
                                continue
                            elif operation_metadata.get('operation_type') == "ASSERTION" and operation_metadata.get('use_assertion_v2'):
                                operation_metadata['assertion_tree'] = substitute_in_assertion_tree(operation_metadata['assertion_tree'], test_params)
                                continue
                            operation_metadata['sub_instruction_obj'] = sub_instruction_obj
                            for key, value in params_used.items():
                                old_value = value
                                matches = re.findall(r'\$\{(.*?)\}', value)
                                if len(matches) == 0:
                                    value = test_params.get(value,"")

                                for param in matches:
                                    param_value = test_params.get(param, "")
                                    if param_value == "":
                                        continue
                                    value = value.replace(f"${{{param}}}", str(param_value))

                                if old_value == value:
                                    continue
                                
                                if operation_type not in ["OPEN", "TYPE", "DB_QUERY", "ASSERTION", "NEW_TAB", "SET_VARIABLE"] and len(matches) > 0:
                                    if key == "operation_intent":
                                        operation_metadata['sub_instruction_obj']['operation'] = value
                                    operation_metadata["unresolved"] = True
                                if operation_type == "ASSERTION":
                                    if key == 'operand1':
                                        operation_metadata['queried_value'] = value
                                    if key == 'operand2':
                                        operation_metadata['expected_value'] = value
                                operation_metadata[key] = value
                                if variables_used:
                                    operation_metadata['sub_instruction_obj']['variable'][key] = value
                            operation_metadata['sub_instruction_obj'] = json.dumps(operation_metadata['sub_instruction_obj'])                                                                                                           
                            # Now, replace string 
                            if len(pattern_url) > 0 and pattern_url[0] != "":
                                operation_metadata["is_replace"] = "true"
                            for i in range(len(pattern_url)):
                                for key, value in operation_metadata.items():
                                    if isinstance(value, str):
                                        operation_metadata[key] = value.replace(str(pattern_url[i]), str(replace_url[i]))
                     
                else:
                    for key, operation_metadata in new_metadata.items():
                        if key in IGNORED_KEYS:
                            continue
                        if isinstance(operation_metadata.get('sub_instruction_obj', "{}"), str):
                            sub_instruction_obj = json.loads(operation_metadata.get('sub_instruction_obj', "{}"))
                        else:
                            sub_instruction_obj = operation_metadata.get('sub_instruction_obj', {})

                        params_used = sub_instruction_obj.get('params',{})
                        if operation_metadata.get('operation_type') == "MATHEMATICAL_OPERATION":
                            operation_metadata['expression_tree'] = substitute_in_math_tree(operation_metadata['expression_tree'], test_params)
                            continue
                        elif operation_metadata.get('operation_type') == "ASSERTION" and operation_metadata.get('use_assertion_v2'):
                            operation_metadata['assertion_tree'] = substitute_in_assertion_tree(operation_metadata['assertion_tree'], test_params)
                            continue
                        operation_type  = operation_metadata['operation_type']
                        variables_used = sub_instruction_obj.get('variable',{})
                        operation_metadata['sub_instruction_obj'] = sub_instruction_obj
                        for key, value in params_used.items():
                            old_value = value
                            matches = re.findall(r'\$\{(.*?)\}', value)
                            if len(matches) == 0:
                                value = test_params.get(value,"")

                            for param in matches:
                                param_value = test_params.get(param, "")
                                if param_value == "":
                                    continue
                                value = value.replace(f"${{{param}}}", str(param_value))
                            
                            if old_value == value:
                                continue
                            
                            operation_metadata[key] = value

                            if operation_type not in ["OPEN", "TYPE", "DB_QUERY", "ASSERTION", "NEW_TAB", "SET_VARIABLE"] and len(matches) > 0:
                                if key == "operation_intent":
                                    operation_metadata['sub_instruction_obj']['operation'] = value
                                operation_metadata["unresolved"] = True
                            
                            if operation_type == "ASSERTION":
                                if key == 'operand1':
                                    operation_metadata['queried_value'] = value
                                if key == 'operand2':
                                    operation_metadata['expected_value'] = value  
                                      
                            if variables_used:
                                operation_metadata['sub_instruction_obj']['variable'][key] = value

                        operation_metadata['sub_instruction_obj'] = json.dumps(operation_metadata['sub_instruction_obj'])
                        
                        if len(pattern_url) > 0 and pattern_url[0] != "":
                            operation_metadata["is_replace"] = "true"
                        # Now, replace string 
                        for i in range(len(pattern_url)):
                            for key, value in operation_metadata.items():
                                if isinstance(value, str):
                                    operation_metadata[key] = value.replace(str(pattern_url[i]), str(replace_url[i]))
                
                print(f"new_metadata: {new_metadata}")
                with open(f"{destination_path}/{test_instance_id}.json", "w") as file:
                    json.dump(new_metadata, file, indent=4)

        print(f"Created operations metadata for test ID {test_id}.")

    def update_config_json(test_id, test_name, config_file):
        """Updates the config JSON file with the test name for a given test ID."""
        with open(config_file, "r") as file:
            data = json.load(file)

        updated = False
        for key, tests in data.items():
            for test in tests:
                if test.get("test_id") == test_id:
                    test["test"] = test_name
                    updated = True

        if updated:
            with open(config_file, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Updated {config_file}: Set 'test' for test_id {test_id} to '{test_name}'")
        else:
            print(f"Test ID {test_id} not found in {config_file}.")

    # Validate input paths
    if not os.path.isdir(parent_folder):
        raise FileNotFoundError(f"Parent folder '{parent_folder}' does not exist.")
    if not os.path.isfile(config_file_path):
        raise FileNotFoundError(f"Config file '{config_file_path}' does not exist.")

    os.makedirs(destination_path, exist_ok=True)

    # Process each UUID or all UUIDs in the parent folder
    uuid_list = list(uuids.keys()) if uuids else [uuid for uuid in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, uuid))]
    global_variables = get_global_variables()
    print(f"global_variables: {global_variables}")
    for uuid in uuid_list:
        uuid_folder = os.path.join(parent_folder, uuid)
        if not os.path.isdir(uuid_folder):
            print(f"Warning: UUID folder '{uuid_folder}' does not exist.")
            continue
        
        if uuid in uuids:
            if uuids[uuid] != 0:
                latest_version = uuids[uuid]
                print("Picked the version from the provided UUIDs, version: ", latest_version)
            else:
                latest_version = get_latest_version(uuid_folder)
                print("Picked the latest version, version: ", latest_version)
        else:
            latest_version = get_latest_version(uuid_folder)
            print("Picked the latest version, version: ", latest_version)

        if not latest_version:
            print(f"Warning: No version found for UUID folder '{uuid_folder}'.")
            continue

        search_path = os.path.join(uuid_folder, latest_version, framework, language)
        if not os.path.isdir(search_path):
            print(f"Warning: Path '{search_path}' does not exist.")
            continue

        # Find and copy 'hye_*' folders
        hye_folders = [f for f in os.listdir(search_path) if f.startswith("hye_") and os.path.isdir(os.path.join(search_path, f))]
        for hye_folder in hye_folders:
            source_path = os.path.join(search_path, hye_folder)
            destination = os.path.join(destination_path, hye_folder)
            shutil.copytree(source_path, destination, dirs_exist_ok=True)
            print(f"Copied '{source_path}' to '{destination}'.")
            # Update config.json
            update_config_json(uuid, hye_folder, config_file_path)
            # create operations metadata for instance
            create_operations_metadata_for_instance(uuid, destination, config_file_path, global_variables)

    print(f"Extraction complete. 'hye_*' folders have been copied and {config_file_path} updated.")

def download_martian_binary(platform_name, martian_binary_path):

    martian_binary_linux_url = os.getenv("MARTIAN_BINARY_LINUX_URL")
    martian_binary_mac_amd64_url = os.getenv("MARTIAN_BINARY_MAC_AMD64_URL")
    martian_binary_mac_arm64_url = os.getenv("MARTIAN_BINARY_MAC_ARM64_URL")
    martian_binary_windows_url = os.getenv("MARTIAN_BINARY_WINDOWS_URL")
    
    if platform_name.__contains__("linux"):
        download_command = ["wget", "-O", martian_binary_path, martian_binary_linux_url]
    elif platform_name.__contains__("mac"):
        if get_architecture() == "amd64":
            download_command = ["curl", "-o", martian_binary_path, martian_binary_mac_amd64_url]
        elif get_architecture() == "arm64":
            download_command = ["curl", "-o", martian_binary_path, martian_binary_mac_arm64_url]
        else:
            raise Exception("Unsupported platform.")
    elif platform_name.__contains__("win"):
        download_command = ["curl", "-o", martian_binary_path, martian_binary_windows_url]
    else:
        raise Exception("Unsupported platform.")

    result = subprocess.run(download_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise Exception(f"Error downloading {martian_binary_url}: {result.stderr.strip()}")

    if platform_name.__contains__("linux") or platform_name.__contains__("mac"):
        result = subprocess.run(["chmod", "+x", martian_binary_path])
        if result.returncode != 0:
            raise Exception(f"Error running command: {result.stderr.strip()}")

def pre(config_file_path):
    platform_name = get_platform()

    # Define paths and URLs based on the platform
    if platform_name.__contains__("linux"):
        base_path = "/home/ltuser/foreman/ltuser"
        martian_base_path = "/home/ltuser/scripts"
        download_command = ["wget", "-O"]
        martian_binary_path = os.path.join(martian_base_path, "martian")
        create_bash_for_linux()
    elif platform_name.__contains__("mac"):
        base_path = "/Users/ltuser/foreman/ltuser"
        martian_base_path = "/Users/ltuser/lrc/lambda-node-remote-client"
        download_command = ["curl", "-o"]
        martian_binary_path = os.path.join(martian_base_path, "martian")
        create_bash_for_linux()
    elif platform_name.__contains__("win"):
        base_path = "D:/foreman/ltuser/"
        martian_base_path = "G:/lambda-node-remote-client/"
        download_command = ["curl", "-o"]
        martian_binary_path = os.path.join(martian_base_path, "martian.exe")
        create_bat_for_windows()
    else:
        raise Exception("Unsupported platform.")

    # Paths for extensions
    crx_path = os.path.join(base_path, "dom-watcher.crx")
    xpi_path = os.path.join(base_path, "dom-watcher.xpi")
    safari_path = os.path.join(base_path, "lt_utility.js")

    # Create directory for downloads
    result = subprocess.run(["mkdir", "-p", base_path])
    if result.returncode != 0:
        raise Exception(f"Error creating directory: {result.stderr.strip()}")

    # Load the config.json
    with open(config_file_path, "r") as file:
        data = json.load(file)

    # Ensure platform_name is present in the data
    if platform_name not in data:
        raise KeyError(f"Platform '{platform_name}' not found in {config_file_path}")

    tests = data.get(platform_name, [])

    # Update the extension_path based on the browser type and download the extensions
    for test in tests:
        browser = test.get("browser", "").lower()

        if "firefox" in browser:
            test["extension_path"] = xpi_path
            # Download .xpi if not already downloaded

            # command = download_command + [xpi_path, xpi_url]
            # print("command: ", command)

            # if not os.path.exists(xpi_path):
            #     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            #     if result.returncode != 0:
            #         raise Exception(f"Error downloading {xpi_url}: {result.stderr.strip()}")
        
        elif "chrome" in browser or "edge" in browser:
            test["extension_path"] = crx_path
            # Download .crx if not already downloaded

            # command = download_command + [crx_path, crx_url]
            # print("command: ", command)
            
            # if not os.path.exists(crx_path):
            #     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            #     if result.returncode != 0:
            #         raise Exception(f"Error downloading {crx_url}: {result.stderr.strip()}")
        
        elif "safari" in browser:
            test["extension_path"] = safari_path
            # Download .js if not already downloaded

            # command = download_command + [safari_path, lt_utility_url]
            # print("command: ", command)

            # if not os.path.exists(safari_path):
            #     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            #     if result.returncode != 0:
            #         raise Exception(f"Error downloading {lt_utility_url}: {result.stderr.strip()}")
                
        modules = test.get("modules")
        if modules != None:
            for key, _ in modules.items():
                source_path = os.path.join(os.curdir, "Modules", key)
                repo_test_dir = os.path.join(os.getcwd(), test["test"])  # e.g., /home/ltuser/foreman/morgan-hyperexec/<test>
                destination_path = os.path.join(repo_test_dir, key)
                # Create destination directory if it doesn't exist
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                print(f"Copied Module source:'{source_path}' to destination:'{destination_path}'.")


    # Write back the updated data to config.json
    with open(config_file_path, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Extensions downloaded and JSON file updated for platform: {platform_name}")

def discovery(config_file_path):
    platform = get_platform() 
    with open(config_file_path, "r") as file:
        data = json.load(file)

    tests = data.get(platform, [])
    for test in tests:
        print(f"{test.get('test')} {test.get('browser')} {test.get('version')} {test.get('resolution')} {test.get('platform')} {test.get('extension_path')} {test.get('test_instance_id')}")

def create_bat_for_windows():
    with open("run.bat", "w") as file:
        file.write(RUN_BAT)

def create_bash_for_linux():
    with open("run.sh", "w") as file:
        file.write(RUN_SH)
    
    result = subprocess.run(["chmod", "+x", "run.sh"])
    if result.returncode != 0:
        raise Exception(f"Error running command: {result.stderr.strip()}")
    
if sys.argv[1] == "discovery":
    discovery(config_file_path=str(os.getenv("TEST_RUN_ID"))+".json")
elif sys.argv[1] == "pre":
    pre(config_file_path=sys.argv[2])
elif sys.argv[1] == "extract":
    # Optional uuids argument
    uuids = None
    if len(sys.argv) > 7:
        test_run_id = sys.argv[7]
        os_and_test_ids, secrets = fetch_os_and_test_ids(test_run_id)
        print(f"os_and_test_ids: {os_and_test_ids}")
        uuids = os_and_test_ids['testIds']
        print(f"uuids: {uuids}")

    extract_folders(
        parent_folder=sys.argv[2],
        framework=sys.argv[3],
        language=sys.argv[4],
        destination_path=sys.argv[5],
        config_file_path=sys.argv[6],
        uuids=uuids,
    )
else:
    sys.argv[1] == "platform"
    print(get_platform())
