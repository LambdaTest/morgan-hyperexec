# Standard library imports
import asyncio, ast, io, math, subprocess
import base64
import calendar
import concurrent.futures
import datetime
from datetime import datetime, timezone, timedelta
import http.client as http2
import json
import os
import random
import re
import socket
import colorsys
import string
import sys
import time
import traceback
import unicodedata
import uuid
from enum import Enum, auto
from functools import wraps
from math import sqrt
from pathlib import Path
from typing import Any, Dict, Mapping, Sequence, Union, Tuple
from urllib.parse import urlparse, parse_qs, quote

# Third-party imports
import requests, httpx
from botocore.awsrequest import AWSRequest
from botocore.auth import SigV4Auth, SigV4QueryAuth
from botocore.credentials import Credentials
from selenium import webdriver
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    WebDriverException,
    JavascriptException,
    InvalidArgumentException,
    TimeoutException,
    UnexpectedAlertPresentException
)
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait

try:
    from generative import GenerativeFlow
except Exception as e:
    pass

MAX_WAIT_UNTILTIME = 10
MOBILE_TAGIFY_SCRIPT = None
PLATFORM_NAME = os.getenv('platformName', os.environ.get('PLATFORM', 'ios')).lower()

LAST_HAR_FILE_INDEX = None

smart_variables_cache = None


# Local imports
try:
    # DO NOT REMOVE THIS IMPORT, IT IS REQUIRED FOR THE LOGS TO BE SENT TO SUMO
    import log_utils
except ImportError:
    pass

try:
    from PIL import Image, ImageDraw, ImageFont
except Exception as e:
    pass

try:
    from safari import inject_script
except Exception as e:
    pass

try:
    from utils.constants import get_mobile_tagify_script
    MOBILE_TAGIFY_SCRIPT = get_mobile_tagify_script()
    if not MOBILE_TAGIFY_SCRIPT:
        MOBILE_TAGIFY_SCRIPT = None
except Exception as e:
    pass

try:
    from utils import get_tagify_script
    MOBILE_TAGIFY_SCRIPT = get_tagify_script()
except Exception as e:
    pass

try:
    from selenium_test_agent.llm.instruction import stop_video, resume_video, update_autoheal, create_and_upload_screenshot
    IS_WEBSOCKET_AVAILABLE = True
except Exception as e:
    IS_WEBSOCKET_AVAILABLE = False
    pass

operation_autoheal = False
file_path = sys.argv[6] if len(sys.argv) > 6 else "operations_meta_data"
file_path = f'{file_path}.json'
BROWSER = "chrome"
_LI_NUMERIC_POS_RE = re.compile(r"^li\[\s*\d+\s*]$", re.I)
TEST_STATUS = "passed"

def set_test_status(status):
    global TEST_STATUS
    TEST_STATUS = status

def get_test_status():
    global TEST_STATUS
    return TEST_STATUS

if len(sys.argv) > 1:
    BROWSER = sys.argv[1].lower()
    if BROWSER == "safari":         
        print("Safari Utility Imported")

print("Browser: ", BROWSER)

if not os.path.exists(file_path):
    file_path = "operations_meta_data.json"

if os.getenv("HYPER") == "true":
    folder_name = os.path.abspath(__file__).split("/")[-2]
    file_path = f"extracted_hye_files/{folder_name}/operations_meta_data.json"

root_meta_data = {}

LAST_ACTION_TIMESTAMP = 0
MAX_NETWORK_WAIT = 10
WAIT_BUFFER = 0.2
NETWORK_REQUEST_EVENTS = ["Network.requestWillBeSent"]
NETWORK_RESPONSE_EVENTS = ["Network.responseReceived", "Network.BlockedReason", "Network.loadingFailed"]
NETWORK_WAIT_FOR_ALL_ACTIONS = False
CLICKS_ORDER_ALLOWED_VALUES = ["se_js_ac", "se_ac_js", "js_se_ac", "js_ac_se", "ac_js_se", "ac_se_js", "se_ac", "js_ac", "ac_js", "se", "js", "ac"]
LT_HOOK = ""

global autoheal_frame_info
global autoheal_locators
global autoheal_latency
autoheal_frame_info = ""
autoheal_locators = []
autoheal_latency = 0

def set_autoheal_frame_info(frame_info):
    global autoheal_frame_info
    autoheal_frame_info = frame_info

def set_autoheal_locators(locators):
    global autoheal_locators
    autoheal_locators = locators

def set_autoheal_latency(latency):
    global autoheal_latency
    autoheal_latency = latency

def _dist(c1: Tuple[int, int, int], c2: Tuple[int, int, int]) -> float:
    return sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

RGBA_RE = re.compile(
    r"rgba?\s*\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})"
    r"(?:\s*,\s*[0-9.]+)?\s*\)", re.I
)

def parse_rgb(s: str) -> Tuple[int, int, int]:
    """Extract (R, G, B) ints from 'rgb(...)' or 'rgba(...)'."""
    m = RGBA_RE.fullmatch(s.strip())
    if not m:
        raise ValueError(f"Not a valid rgb/rgba string: {s!r}")
    r, g, b = (int(m.group(i)) for i in range(1, 4))
    if any(v > 255 for v in (r, g, b)):
        raise ValueError("RGB values must be 0-255.")
    return r, g, b

def rgb_to_basic8(rgb: Tuple[int, int, int]) -> str:
    #getting nearest BASIC8 color name from RGB tuple
    r, g, b = [x / 255 for x in rgb]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)  # Hue (0–1), Saturation (0–1), Value (0–1)

    # Threshold for near-grayscale colors
    if s < 0.05:
        return "white" if v > 0.75 else "black"

    hue_deg = h * 360

    # Map hue to BASIC8 buckets
    if 0 <= hue_deg < 15 or hue_deg >= 345:
        return "red"
    elif 15 <= hue_deg < 45:
        return "orange"
    elif 45 <= hue_deg < 70:
        return "yellow"
    elif 70 <= hue_deg < 170:
        return "green"
    elif 170 <= hue_deg < 260:
        return "blue"
    elif 260 <= hue_deg < 320:
        return "purple"
    else:
        return "red"  # wrap-around

def rgba_string_to_name(s: str) -> str:
    """Full pipeline: string → RGB tuple → nearest basic colour name."""
    return rgb_to_basic8(parse_rgb(s))

class FailureCondition(Enum):
    FAIL_BUT_CONTINUE_EXECUTING = "Fail but continue executing"
    FAIL_TEST_IMMEDIATELY = "Fail test immediately"
    WARN_BUT_CONTINUE_EXECUTING = "Warn but continue executing"
    NONE = ""
    
def resolve_mathematical_operand(node, operation_index):
    node_name, node_type = next(iter(node.items()))
    value = None
    if node_type == "runtime_variable":
        value = string_to_float(access_variable_value(get_meta_data_value(operation_index)["variable_dump"], node_name))
    elif node_type == "numeric_literal" or node_type == "parameter":
        value = string_to_float(node_name)
    elif node_type == "predefined_variable":
        predefined_variable = re.findall(r'\{\{(.*?)\}\}', node_name)[0]
        value = string_to_float(access_variable_value(get_meta_data_value(operation_index)["variable_dump"], predefined_variable))
    else:
        return 0
    
    if value is None:
        return 0
    return value

def eval_math(node, operation_index):
    # Leaf
    if isinstance(node, (int, float)):
        return float(node)
    if isinstance(node, dict) and not "op" in node:
        return resolve_mathematical_operand(node, operation_index)
        
    # Branch
    op = node["op"]
    vals = [eval_math(child, operation_index) for child in node["operands"]]
    ops = {
        "add":       lambda a,b: a+b,
        "subtract":  lambda a,b: a-b,
        "multiply":  lambda a,b: a*b,
        "divide":    lambda a,b: a/b,
        "mod":       lambda a,b: a%b,
        "pow":       lambda a,b: a**b,
        "negate":    lambda a: -a,
        "abs":       lambda a: abs(a),
    }
    fn = ops[op]
    return fn(*vals) if len(vals)>1 else fn(vals[0])

def resolve_assertion_operand(node, operation_index):
    print("node in resolve_assertion_operand: ", node)
    node_name, node_type = next(iter(node.items()))
    if node_type == "runtime_variable":
        try:
            value = access_variable_value(get_meta_data_value(operation_index)["variable_dump"], node_name)
        except Exception as e:
            value = access_value(user_variables, node_name) 

    elif node_type == "parameter":
        value = node_name

    elif node_type == "predefined_variable":
        predefined_variable = re.findall(r'\{\{(.*?)\}\}', node_name)[0]
        try:
            value = access_variable_value(get_meta_data_value(operation_index)["variable_dump"], predefined_variable)
        except Exception as e:
            value = access_value(user_variables, predefined_variable)

    print("value in resolve_assertion_operand: ", value, " node_name: ", node_name, " node_type: ", node_type)
    return value


def evaluate_assertion(tree: Mapping[str, Any], operation_index) -> bool:
    op = tree["operator"]
    print("tree in evaluate_assertion: ", tree)

    # ----- logical nodes -----
    if op in {"AND", "OR", "NOT"}:
        ops = tree["operands"]
        if op == "AND":
            return all(evaluate_assertion(t, operation_index) for t in ops)
        if op == "OR":
            return any(evaluate_assertion(t, operation_index) for t in ops)
        print("not evaluate_assertion(ops[0], operation_index): ", ops[0])
        return not evaluate_assertion(ops[0], operation_index)  # NOT

    # ----- atomic nodes -----
    left = resolve_assertion_operand(tree["left_operand"], operation_index)
    right = None
    if tree.get("right_operand", None):
        right = resolve_assertion_operand(tree["right_operand"], operation_index)



    #  apply transforms if present
    if "transform_operands" in tree:
        if op in ["greater_than", "less_than", "greater_than_or_equal", "less_than_or_equal"]:
            if "string_to_float" not in tree["transform_operands"]:
                tree["transform_operands"].append("string_to_float")
        left = _apply_transform(left, tree["transform_operands"])
        if right is not None:
            right = _apply_transform(right, tree["transform_operands"])

    if (type(left) in {int, float} and type(right) in {str}) or (type(left) in {str} and type(right) in {int, float}):
        left = string_to_float(left)
        right = string_to_float(right)

    if (type(left) in {bool} and type(right) in {str}) or (type(left) in {str} and type(right) in {bool}):
        left = str(left).lower()
        right = str(right).lower()

    return _compare_atomic(op, left, right)
        
def _compare_atomic(op: str, a: Any, b: Any) -> bool:
    if op in {"equals", "equal"}  : return a == b
    if op in {"not_equal", "not_equals"}  : return a != b
    if op == "greater_than"   : return a >  b
    if op == "less_than"   : return a <  b
    if op == "greater_than_or_equal"  : return a >= b
    if op == "less_than_or_equal"  : return a <= b
    if op in {"start_with", "starts_with"}: return str(a).lower().startswith(str(b).lower())
    if op in {"end_with",   "ends_with"}  : return str(a).lower().endswith(str(b).lower())
    if op in {"contain", "contains"}      : return str(b).lower() in str(a).lower()
    if op == "lower_case": return str(a) == str(a).lower()
    if op == "upper_case": return str(a) == str(a).upper()
    if op == "length_equals": return are_lengths_equal(str(a),str(b))
    if op == "type_equals": return are_types_equal(str(a),str(b))
    if op == "json_key_exists": return str(b) in _json_obj(a)
    if op == "json_keys_count": return len(_json_obj(a).keys()) == int(b)
    if op == "json_array_length_equals": return len(_json_arr(a)) == int(b)
    if op == "json_array_contains": return b in _json_arr(a)

    raise ValueError(f"Unsupported operator {op}")

def _json_obj(x: Any) -> Mapping[str, Any]:
    
    if isinstance(x, str):
        try:
            # Try loading as proper JSON first
            x = json.loads(x)
        except json.JSONDecodeError:
            try:
                # Safely evaluate Python literals (handles single quotes)
                x = ast.literal_eval(x)
            except (ValueError, SyntaxError) as e:
                print("Could not parse string as JSON or Python literal:", e)
                raise ValueError(f"Invalid JSON or literal provided: {x}") from e

    return x

def _json_arr(x: Any) -> Sequence[Any]:

    if isinstance(x, str):
        try:
            x = json.loads(x)
        except json.JSONDecodeError:
            try:
                x = ast.literal_eval(x)
                if not isinstance(x, (list, tuple)):
                    raise ValueError(f"Parsed object is not a list or tuple: {x}")
            except (ValueError, SyntaxError) as e:
                print("Could not parse string as JSON or Python literal:", e)
                raise ValueError(f"Invalid JSON array or literal provided: {x}") from e
    return x

def _apply_transform(val: Any, transform_name: list) -> Any:
    for transform in transform_name:
        if transform == "string_to_float":
            val = string_to_float(val)
    return val

def get_all_element_attributes(element: WebElement, driver: webdriver.Chrome) -> dict:
    all_attributes_script = """
    var allAttributes = {};
    for (var i = 0; i < arguments[0].attributes.length; i++) {
        allAttributes[arguments[0].attributes[i].name] = arguments[0].attributes[i].value;
    }
    return allAttributes;
    """
    return driver.execute_script(all_attributes_script, element)

def get_section_from_bbox(bbox: dict, driver: webdriver.Chrome) -> str:
    """
    Determine which of the 9 sections of the viewport the element falls into.

    Args:
        bbox: dict with keys 'x', 'y', 'width', 'height' (e.g. element.rect)
        driver: Selenium WebDriver instance

    Returns:
        One of:
        'top-left', 'top-centre', 'top-right',
        'middle-left', 'middle-center', 'middle-right',
        'bottom-left', 'bottom-centre', 'bottom-right'
    """
    # 1) Compute element center
    center_x = bbox['x'] + bbox['width'] / 2
    center_y = bbox['y'] + bbox['height'] / 2

    # 2) Get viewport size
    size = driver.get_window_size()
    vw, vh = size['width'], size['height']

    # 3) Compute horizontal & vertical thirds
    h_third = vw / 3
    v_third = vh / 3

    # 4) Determine column
    if center_x < h_third:
        col = 'left'
    elif center_x < 2 * h_third:
        col = 'center'
    else:
        col = 'right'

    # 5) Determine row
    if center_y < v_third:
        row = 'top'
    elif center_y < 2 * v_third:
        row = 'middle'
    else:
        row = 'bottom'

    # 6) Map to the exact labels you specified
    mapping = {
        ('top', 'left'): 'top-left',
        ('top', 'center'): 'top-centre',
        ('top', 'right'): 'top-right',
        ('middle', 'left'): 'middle-left',
        ('middle', 'center'): 'middle-center',
        ('middle', 'right'): 'middle-right',
        ('bottom', 'left'): 'bottom-left',
        ('bottom', 'center'): 'bottom-centre',
        ('bottom', 'right'): 'bottom-right'
    }

    return mapping[(row, col)]

def sanitize_visible_text(raw: str) -> str:
    """
    - Convert non-breaking spaces to a normal space.
    - Remove control / format characters (zero-width, bidi marks, etc.).
    - Collapse any run of whitespace (space, tab, newline) to a single space.
    - Trim leading / trailing whitespace.
    
    Feel free to extend the 'category' filter or add specific
    character replacements for your domain.
    """
    if not raw:
        return ""

    # &nbsp; → space
    cleaned = raw.replace("\u00A0", " ")

    # Strip control/format chars (Unicode categories Cc = control, Cf = format)
    cleaned = "".join(
        ch for ch in cleaned
        if unicodedata.category(ch) not in {"Cf", "Cc"}
    )

    # Collapse runs of whitespace to a single space
    cleaned = re.sub(r"\s+", " ", cleaned)

    return cleaned.strip()

def safe_value(element: WebElement, driver: webdriver.Chrome, timeout: float = 2.0) -> str:
    """
    Attempts to return meaningful text/value from any element.
    Falls back gracefully when .value is not applicable.
    """
    tag = element.tag_name.lower()
    safe_value = ""

    # 1. Straightforward form controls
    if tag in {"input", "textarea"}:
        print("element.tag: ", element.tag_name)
        # Wait for framework to sync, up to `timeout`
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: element.get_property("value") not in ("", None)
            )
        except Exception:
            pass
        safe_value = element.get_property("value") or ""

    # 2. <select>
    elif tag == "select":
        print("element.tag: ", element.tag_name)
        sel = Select(element)
        options = sel.options
        # Get all values, fallback to text if value is not present
        all_values = [opt.get_attribute("value") or opt.text for opt in options]
        safe_value = ", ".join(all_values)  # Join all values with comma separator

    # 3. contenteditable
    elif element.get_attribute("contenteditable") == "true":
        print("element.tag: ", element.tag_name)
        safe_value = element.get_property("innerText").strip()

    if safe_value == "":
        print("safe_value is empty: ", element.tag_name, " going to fallback to innertext")
        safe_value = element.text

    print("safe_value: ", safe_value)
    return sanitize_visible_text(safe_value)

def switch_to_content_by_selector(driver, frame_info_list):
    """
    Given a Selenium `driver` and a list of frame-info dicts like:
      {
        'type': 'shadow' or 'iframe',
        'selectors': [
          {'selector': '...', 'isXPath': True|False, 'score': int},
          ...
        ],
        'boundingBox': { ... }  # ignored here
      }
    this will walk through each frame in order, drilling into shadow-roots
    or switching into iframes as needed. Returns the final shadow-root
    WebElement (or None if the last frame was an iframe).
    """
    shadow = None

    for frame in frame_info_list:
        # pick selectors sorted by score descending
        sorted_sels = sorted(frame.get('selectors', []),
                             key=lambda s: s.get('score', 0),
                             reverse=True)
        host = None
        # try each selector until one works
        for s in sorted_sels:
            sel = s['selector']
            try:
                if s.get('isXPath', False):
                    if shadow:
                        first_child = shadow.find_element(By.CSS_SELECTOR, ":scope > :not(script):not(style)")
                        host = first_child.find_element(By.XPATH, sel)
                    else:
                        host = driver.find_element(By.XPATH, sel)
                else:
                    host = (shadow or driver).find_element(By.CSS_SELECTOR, sel)
                break
            except (NoSuchElementException, WebDriverException):
                continue
        if host is None:
            raise NoSuchElementException(
                f"Could not locate frame host using any of: {[s['selector'] for s in sorted_sels]}"
            )

        if frame.get('type') == 'iframe':
            # switch into the iframe
            driver.switch_to.frame(host)
            shadow = None

        elif frame.get('type') == 'shadow':
            # enter its shadowRoot
            shadow = driver.execute_script("return arguments[0].shadowRoot", host)

        else:
            # unknown frame type; skip
            continue
    return shadow, host

def set_network_wait_for_all_actions(network_wait_for_all_actions: bool):
    global NETWORK_WAIT_FOR_ALL_ACTIONS
    NETWORK_WAIT_FOR_ALL_ACTIONS = network_wait_for_all_actions

def get_network_wait_for_all_actions() -> bool:
    global NETWORK_WAIT_FOR_ALL_ACTIONS
    return NETWORK_WAIT_FOR_ALL_ACTIONS

def set_last_action_timestamp(timestamp: int):
    global LAST_ACTION_TIMESTAMP
    LAST_ACTION_TIMESTAMP = timestamp

def get_last_action_timestamp() -> int:
    global LAST_ACTION_TIMESTAMP
    return LAST_ACTION_TIMESTAMP

def update_max_network_wait(max_network_wait: float):
    global MAX_NETWORK_WAIT
    MAX_NETWORK_WAIT = max_network_wait

def update_wait_buffer(wait_buffer: float):
    global WAIT_BUFFER
    WAIT_BUFFER = wait_buffer

def process_browser_logs_for_network_events(driver: webdriver.Chrome) -> list:
    """
        Return only logs which have a method that are in (NETWORK_RESPONSE_EVENTS or NETWORK_REQUEST_EVENTS)
        since we're interested in the network events specifically.

        args:
            driver: webdriver.Chrome // Webdriver instance

        returns:
            list // List of network events
    """
    try:
        logs = driver.get_log("performance")
    except Exception as e:
        print(f"[Smart Wait] Error in process_browser_logs_for_network_events: {str(e)}")
        logs = []
    network_events = []
    for entry in logs:
        log = json.loads(entry["message"])["message"]
        if (log["method"] in NETWORK_REQUEST_EVENTS or log["method"] in NETWORK_RESPONSE_EVENTS) and log["params"].get("type") not in ["Other", "Document", "Ping"]:
            network_events.append({"timestamp": entry["timestamp"], "method": log["method"], "requestId": log["params"].get("requestId", ""), "type": log["params"].get("type", "")})
    return network_events

def smart_network_wait(driver: webdriver.Chrome, start_timestamp: int):
    """
        Wait for all network requests to finish.
        This is a blocking call.

        args:
            driver: webdriver.Chrome // Webdriver instance
            start_timestamp: int // Timestamp just before last action was performed
            max_network_wait: int = 10 // Maximum timeout for the wait
            wait_buffer: int = 200 // Buffer to wait for the network requests to finish
    """
    try:
        if BROWSER != "chrome":
            print(f"[Smart Wait] Not supported for {BROWSER}")
            return
        
        start_time = time.time() * 1000
        request_map = {}
        most_recent_network_timestamp = time.time() * 1000

        while True:
            events = process_browser_logs_for_network_events(driver=driver)  # No await needed
            for event in events:
                if event["method"] in NETWORK_REQUEST_EVENTS and event["timestamp"] >= start_timestamp:
                    request_map[event["requestId"]] = {"timestamp": event["timestamp"], "type": event["type"]}
                elif event["method"] in NETWORK_RESPONSE_EVENTS:  # Fixed logical error here
                    if event["requestId"] in request_map:
                        most_recent_network_timestamp = event["timestamp"]
                        del request_map[event["requestId"]]

            if len(request_map) == 0 and (time.time() * 1000 - most_recent_network_timestamp >= WAIT_BUFFER * 1000):
                print(f"[Smart Wait] Waited for: {time.time() * 1000 - start_time} ms")
                return

            if time.time() * 1000 - start_timestamp > MAX_NETWORK_WAIT * 1000:
                print(f"[Smart Wait] Waited for: {time.time() * 1000 - start_time} ms")
                return
    
    except Exception as e:
        print(f"[Smart Wait] Error in smart_network_wait: {str(e)}")


def handle_mobile_native_popups(driver: webdriver.Chrome, popups: list):
    """
        Handle mobile native popups by interacting with them.

        args:
            driver: webdriver.Chrome // Webdriver instance
            popups: list // List of native popups to handle
    """
    driver.switch_to.context("NATIVE_APP")  
    for popup in popups:
        try:
            element = driver.find_element(By.XPATH, f'//*[@text="{popup}"]')
            element.click()
            time.sleep(2)  # Wait for the popup to close
        except Exception as e:
            print(f"[Mobile Popup] Error handling popup: {str(e)}")

    for context in driver.contexts:
        if context != "NATIVE_APP":
            driver.switch_to.context(context)
            break

operations_meta_data = {}
root_meta_data = {}

try:
    with open(file_path, 'r') as f:
        root_meta_data = json.load(f)
except Exception as e:
    root_meta_data = {}

CURRENT_CLICKS_ORDER_CODE = ""
user_variables = root_meta_data.get('variables', {})
user_parameters = root_meta_data.get('parameters', {})
global_variables = root_meta_data.get('global_variables', [])
user_data = {}

def get_download_folder():
    """Returns the system's Downloads folder path and ensures it exists."""
    if os.name == "nt":  # Windows
        downloads_path = Path(os.path.join(os.environ["USERPROFILE"], "Downloads"))
    else:  # macOS and Linux
        downloads_path = Path(os.path.expanduser("~/Downloads"))

    # Ensure the folder exists
    downloads_path.mkdir(parents=True, exist_ok=True)

    return downloads_path

def download_files(media_list):
    """Downloads files from the given list to the system's Downloads folder."""
    download_folder = get_download_folder()
    username: str = os.getenv('LT_USERNAME',user_data.get('username',''))
    accesskey: str = os.getenv('LT_ACCESS_KEY',user_data.get('access_key',''))
    header = {'Authorization' : f"Basic {base64.b64encode(f'{username}:{accesskey}'.encode()).decode()}"}
    
    for media in media_list:
        file_url = f"https://{media['media_url']}"
        file_name = media['name']
        file_path = download_folder / file_name
        
        try:
            response = requests.get(file_url, stream=True, headers=header)
            response.raise_for_status()
            
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            
            print(f"Downloaded: {file_name} -> {file_path}")
        except requests.RequestException as e:
            print(f"Failed to download {file_name}: {e}")

def get_downloads_file_path(file_name):
    """Returns the full path to a file in the system's Downloads folder."""
    if file_name is None:
        raise ValueError("file_name cannot be None")
    
    if os.name == "nt":  # Windows
        downloads_path = Path(os.path.join(os.environ["USERPROFILE"], "Downloads"))
    else:  # macOS and Linux
        downloads_path = Path(os.path.expanduser("~/Downloads"))

    return str(downloads_path / file_name)

if root_meta_data.get('chrome_options', []):
    chrome_options = root_meta_data['chrome_options']
    files_data = []
    for option in chrome_options:
        if option.get('type', "") == "file":
            files_data.append({"name": option.get('value', ""), "media_url": option.get('file_url', "")})
    if files_data:
        download_files(files_data)

if root_meta_data.get('files', None):
    download_files(root_meta_data['files'])

if root_meta_data.get('max_network_wait', None):
    update_max_network_wait(root_meta_data['max_network_wait'])
    print("Updated max network wait to: ", root_meta_data['max_network_wait'])

if root_meta_data.get('network_wait_for_all_actions', None):
    set_network_wait_for_all_actions(root_meta_data['network_wait_for_all_actions'])
    print("Updated network wait for all actions to: ", root_meta_data['network_wait_for_all_actions'])

if root_meta_data.get('wait_buffer', None):
    update_wait_buffer(root_meta_data['wait_buffer'])
    print("Updated wait buffer to: ", root_meta_data['wait_buffer'])

def reload_metadata_root(switch_root="main_flow"):
    global operations_meta_data
    operations_meta_data = root_meta_data[switch_root]

def is_dom_loaded(driver):
    try:
        result = driver.execute_script("""
            const state = {
                readyState: { value: false, error: null },
                jqueryReady: { value: true, error: null },
                ajaxReady: { value: true, error: null },
                angularReady: { value: true, error: null },
                reactReady: { value: true, error: null }
            };

            try {
                state.readyState.value = document.readyState === 'complete';
            } catch (e) {
                state.readyState.error = e.toString();
            }

            try {
                state.jqueryReady.value = (typeof jQuery !== 'undefined') ? jQuery.active === 0 : true;
            } catch (e) {
                state.jqueryReady.error = e.toString();
            }

            try {
                state.ajaxReady.value = (typeof window.Ajax === 'undefined') || window.Ajax.activeRequestCount === 0;
            } catch (e) {
                state.ajaxReady.error = e.toString();
            }

            try {
                if (window.angular && typeof angular.element === 'function' && angular.element(document) && typeof angular.element(document).injector === 'function' && angular.element(document).injector()) {
                    state.angularReady.value = angular.element(document).injector().get('$http').pendingRequests.length === 0;
                }
            } catch (e) {
                state.angularReady.error = e.toString();
            }

            try {
                if (typeof React !== 'undefined' && React.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED) {
                    const root = document.getElementById('root') || document.getElementById('app');
                    if (root){
                        state.reactReady.value = root.childNodes.length > 0;
                    }
                }
            } catch (e) {
                state.reactReady.error = e.toString();
            }

            return state;
        """)

        all_ok = True
        if result:
            for _, val in result.items():
                if not val["value"]:
                    all_ok = False
        else:
            all_ok = False

        return all_ok

    except Exception as e:
        print("🚨 Selenium JS execution error:", str(e))
        if type(e).__name__ == "NoSuchWindowException":
            window_handles = driver.window_handles
            if len(window_handles) > 0:
                driver.switch_to.window(window_handles[0])
        return False

def execute_cdp_command(driver: webdriver.Chrome, cmd: str, params: dict = {}):
  resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
  url = driver.command_executor._url + resource
  body = json.dumps({'cmd': cmd, 'params': params})
  response = driver.command_executor._request('POST', url, body)
  return response.get('value')

def capture_full_page_screenshot(driver: webdriver.Chrome) -> str:
    """
    Captures a full-page screenshot using CDP using the underlying driver.
    
    Args:
        driver: An instance of WebDriver
        
    Returns:
        Base64-encoded PNG screenshot string
    """
    
    # Get the full page dimensions via JS
    metrics = driver.execute_script("""
        return {
            width: Math.max(document.body.scrollWidth, document.documentElement.scrollWidth),
            height: Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)
        }
    """)
    
    device_scale_factor = 1024 / metrics["width"]

    print("Page dimensions - Width: %s, Height: %s, Device Scale Factor: %s", metrics["width"], metrics["height"], device_scale_factor)
    
    # Set the viewport to full page size with a lower device scale factor for low resolution
    execute_cdp_command(driver, "Emulation.setDeviceMetricsOverride", {
        "width": metrics["width"],
        "height": metrics["height"],
        "deviceScaleFactor": device_scale_factor,  # Lower scale factor for low resolution
        "mobile": False
    })

    time.sleep(0.5)

    # Capture screenshot
    screenshot = execute_cdp_command(driver, "Page.captureScreenshot", {
         "format": "png",
         "fromSurface": True,
         "captureBeyondViewport": True
    })

    # Reset viewport (optional)
    execute_cdp_command(driver, "Emulation.clearDeviceMetricsOverride", {})

    return screenshot["data"]  # this is base64 PNG

def make_tagged_screenshot(screenshot_base64, rects, driver):
        """
        Draw colored borders around rectangles and add labeled squares
        
        Args:
            screenshot_base64: Screenshot image as base64-encoded string
            rects: Dictionary with keys and rect coordinates {'key': {'left': x, 'top': y, 'width': w, 'height': h}}
            output_path: Path to save the annotated image (optional)
            border_width: Width of the border lines
        
        Returns:
            Path to the annotated image
        """
        def generate_random_color():
            """Generate a random bright color"""
            # Generate random hue, with high saturation and value for bright colors
            hue = random.random()
            saturation = random.uniform(0.7, 1.0)
            value = random.uniform(0.8, 1.0)
                
            # Convert HSV to RGB
            rgb = colorsys.hsv_to_rgb(hue, saturation, value)
            return tuple(int(c * 255) for c in rgb)

        def are_rectangles_disjoint(r1, r2):

            def is_inside(inner, outer):
                return (inner[0] >= outer[0] and inner[1] >= outer[1] and inner[2] <= outer[2] and inner[3] <= outer[3])

            if is_inside(r1, r2) or is_inside(r2, r1):
                return False

            if not (r1[2] <= r2[0] or r1[0] >= r2[2] or r1[3] <= r2[1] or r1[1] >= r2[3]):   
                return False
            return True
        
        try:
            # Decode base64 screenshot
            image_data = base64.b64decode(screenshot_base64)
            image = Image.open(io.BytesIO(image_data))
            original_image = image.copy()
            draw = [ImageDraw.Draw(image)]
            ratio = driver.execute_script("return window.devicePixelRatio;")
            for key, rect in rects.items():
                if rect['x'] * ratio > image.width and rect['x'] <= image.width:
                    ratio = 1

            status_bar_height = 0
            if PLATFORM_NAME == 'ios':
                try:
                    # to subtract the status bar height in ios
                    status_bar_height = driver.execute_script("mobile: deviceScreenInfo").get('statusBarSize',0).get('height', 0)
                except Exception as e:
                    status_bar_height = 0

            # Font paths
            font_paths = [
                "serif.ttf"
            ]

            # Process each rectangle
            tagifified_images = [image]
            image_to_rect_mapping = [[]]
            max_image_num = 1
            for key, rect in rects.items():
                color = generate_random_color()
                left, top, width, height = rect['x'] * ratio , ((rect['top'] + status_bar_height) * ratio), rect['width'] * ratio, rect['height'] * ratio
                x1, y1 = int(left), int(top)
                x2, y2 = int(left + width), int(top + height)

                image_num = 0
                for index in range(0, max_image_num):
                    if index >= len(image_to_rect_mapping):
                        image_to_rect_mapping.append([])
                    rects = image_to_rect_mapping[index]
                    is_space_available = True
                    for rect in rects:
                        if not are_rectangles_disjoint([x1, y1, x2, y2], [rect['x1'], rect['y1'], rect['x2'], rect['y2']]):
                            is_space_available = False
                            break

                    if is_space_available or index+1 == max_image_num:
                        image_num = index
                        image_to_rect_mapping[image_num].append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})
                        break
                if image_num >= len(tagifified_images):
                    tagifified_images.append(original_image.copy())
                    draw.append(ImageDraw.Draw(tagifified_images[image_num]))

                for i in range(3):
                    draw[image_num].rectangle([x1-i, y1-i, x2+i, y2+i], outline=color, fill=None)

                square_width = min(40, width // 2)
                square_height = min(40, height // 2)

                draw[image_num].rectangle([x2-square_width, y2-square_height, x2, y2], outline=color, fill=color)

                text_color = (255, 255, 255) if sum(color) < 382 else (0, 0, 0)  # White text for dark bg, black for light bg

                for font_path in font_paths:
                    try:
                        draw[image_num].text(
                            xy=(x2 - square_width + 3, y2 - square_height + 3),
                            text=key,
                            fill= text_color,
                            font=ImageFont.truetype(font_path, max( 1, min(square_height, square_width) - 5))
                        )
                        break
                    except IOError:
                        continue

            with io.BytesIO() as buffer:
                if tagifified_images[0].mode == 'RGBA':
                    tagifified_images[0] = tagifified_images[0].convert('RGB')
                tagifified_images[0].save(buffer, format="JPEG", optimize=True, quality=50)
                return base64.b64encode(buffer.getvalue()).decode('utf-8') , ratio

        except Exception as e:
            print(f"✗ Error creating annotated image: {e}")
            return None


def set_user_variables(variables:dict):
    global user_variables
    user_variables = variables

def set_user_parameters(parameters:dict):
    global user_parameters
    user_parameters = parameters

def set_global_variables(variables:list):
    global global_variables
    global_variables = variables

def replace_variables_in_script(script: str, variables: dict) -> str:
    pattern = r'//Variables start.*?//Variables end\n*'
    find_variables = re.findall(pattern, script, re.DOTALL)
    updated_script = script
    if find_variables:
        updated_variables = ""
        for key,value in variables.items():
            if f"const {key} " in find_variables[0]:
                if isinstance(value, str):
                    value = json.dumps(value)
                    updated_variables += f"const {key} = {value};\n"
                else:
                    value = json.dumps(value)
                    updated_variables += f"const {key} = {value};\n"
        updated_script = script.replace(find_variables[0], f"//Variables start\n{updated_variables}//Variables end\n")
    return updated_script

class SmartVariables:
    def __init__(self):
        # Instance attributes
        current_datetime = datetime.now()
        self.current_date = current_datetime.strftime("%Y-%m-%d")
        self.current_day = current_datetime.strftime("%d")
        self.current_month_number = current_datetime.strftime("%m")
        self.current_year = current_datetime.strftime("%Y")
        self.current_month = current_datetime.strftime("%B")
        self.current_hour = current_datetime.strftime("%H")
        self.current_minute = current_datetime.strftime("%M")
        self.current_timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        self.current_timezone = time.strftime("%Z")

        self.next_day = (current_datetime + timedelta(days=1)).strftime("%Y-%m-%d")
        self.previous_day = (current_datetime - timedelta(days=1)).strftime("%Y-%m-%d")
        self.start_of_week = (current_datetime - timedelta(days=current_datetime.weekday())).strftime("%Y-%m-%d")
        self.end_of_week = (current_datetime + timedelta(days=6-current_datetime.weekday())).strftime("%Y-%m-%d")
        self.start_of_month = (current_datetime.replace(day=1)).strftime("%Y-%m-%d")
        self.end_of_month = (current_datetime.replace(day=calendar.monthrange(current_datetime.year, current_datetime.month)[1])).strftime("%Y-%m-%d")

        self.random_int = str(random.randint(100, 999))
        self.random_float = str(round(random.uniform(1, 100), 2))
        self.random_string_8 = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.random_string_56 = ''.join(random.choices(string.ascii_letters + string.digits, k=56))
        self.random_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@example.com"
        self.random_phone = f"{random.randint(1000000000,9999999999)}"

        # Environment and system info constants
        self.user_name = os.getenv('LT_USERNAME', '') or user_data.get("username", "")
        self.os_type = sys.argv[4] if len(sys.argv) > 4 else "linux"
        self.os_version = "latest"
        self.browser_name = sys.argv[1] if len(sys.argv) > 1 else "Chrome"
        self.browser_version = sys.argv[2] if len(sys.argv) > 2 else "latest"

        # Location and IP information
        self.country = "India"
        self.city = "Doddaballapura"
        self.latitude = "13.2257"
        self.longitude = "77.5750"
        self.ip_address = "143.110.182.88"

    def get(self, name: str):
        return getattr(self, name)
        
class Heal:
    def __init__(self, operation_idx: str, driver: webdriver.Chrome):
        self.operation_idx = operation_idx
        self.driver: webdriver.Chrome = driver
        self.current_action: dict = get_meta_data_value(operation_idx)
        self.prev_actions:list[dict] = []
        self.tagified_image: str = ""
        self.untagged_image_base64: str = ""
        self.xpath_mapping: dict = {}
        self.tags_description: dict = {}
        self.page_source: str = ""
        self.session_id: str = driver.session_id

        self.test_id: str = os.getenv('TEST_ID', user_data.get('test_id',''))
        self.username: str = os.getenv('LT_USERNAME', user_data.get('username',''))
        self.accesskey: str = os.getenv('LT_ACCESS_KEY', user_data.get('access_key',''))
        self.commit_id: str = os.getenv('COMMIT_ID', user_data.get('commit_id',''))
        self.org_id: int = int(os.getenv('REQUEST_ID', user_data.get('org_id', '0')))
        self.page_source: str = ""
        self.code_export_id:str = uuid.uuid4().hex[:16]
        self.automind_url = os.environ.get('AUTOMIND_URL', user_data.get('automind_url', 'https://kaneai-api.lambdatest.com'))
        self.operation: str = ""
        self.image_base64: str = ""
        self.dimensions: list = []
        self.use_query_v2: bool = get_meta_data_value(operation_idx).get('use_query_v2', False)
        self.mobile_tagify = MOBILE_TAGIFY_SCRIPT
        self.version = user_data.get("version", get_meta_data_value(operation_idx).get("version", "v1"))

    def execute_async_js(self, script: str):

        result = self.driver.execute_script(f"""
        return new Promise((resolve) => {{
            (async function() {{
                try {{
                    const result = await {script};
                    resolve(result);
                }} catch (error) {{
                    console.error('Async JS error:', error);
                    resolve(null);
                }}
            }})();
        }});
        """)
        return result
        
    def resolve(self) -> requests.Response:
        attempt = 1
        max_attempt = 2

        while (max_attempt >= attempt):
            attempt += 1

            if self.mobile_tagify:
                self.driver.execute_script(self.mobile_tagify)
                tagify_response = self.driver.execute_script("return tagifyWebpage(false,true);")
                self.xpath_mapping = tagify_response.get("xpaths", {})
                self.tags_description = tagify_response.get("descriptions", {})
                self.tagified_image, ratio = make_tagged_screenshot(screenshot_base64=self.driver.get_screenshot_as_base64(),rects=tagify_response.get("rects", {}), driver=self.driver)
            
            else:
                if self.driver.capabilities['browserName'].lower() == "safari":
                    inject_script(self.driver)

                before_screenshot = self.driver.get_screenshot_as_base64()

                if IS_WEBSOCKET_AVAILABLE:
                    asyncio.run(stop_video(self.driver.session_id))

                # Execute tagifyWebpage and wait for it to complete
                self.execute_async_js("tagifyWebpage(false,true)")

                xpath_mapping = self.execute_async_js("fetchJsonData(\"JSONOutput\")")
                self.xpath_mapping = json.loads(xpath_mapping)

                tags_description = self.execute_async_js("fetchJsonData(\"descOutput\")")
                self.tags_description = json.loads(tags_description)

                self.tagified_image = self.driver.get_screenshot_as_base64()

                # First remove tags and wait for completion
                self.execute_async_js("removeLTTags()")
                
                # Then clear the data structures
                self.driver.execute_script("annotations = [];JSONOutput = {};nodeData = {};")

                if IS_WEBSOCKET_AVAILABLE:
                    asyncio.run(resume_video(self.driver.session_id))

            payload = json.dumps({
                "code_export_id": self.code_export_id,
                "username": self.username,
                "org_id": self.org_id,
                "commit_id": self.commit_id,
                "current_action":self.current_action,
                "tagified_image": self.tagified_image,
                "xpath_mapping": self.xpath_mapping,
                "tags_description": self.tags_description,
                "accesskey": self.accesskey,
                "test_id": self.test_id,
                "session_id": self.driver.session_id
            })

            headers = {'Content-Type': 'application/json', 'Authorization' : f"Basic {base64.b64encode(f'{self.username}:{self.accesskey}'.encode()).decode()}" }

            print("Heal Resolve... code_export_id: ", self.code_export_id)
            response = requests.request("POST", url=f"{self.automind_url}/v1/heal/resolve", headers=headers, data=payload)

            return response
            
        return response

    def list_xpaths(self) -> requests.Response:
        attempt = 1
        max_attempt = 2

        while (max_attempt >= attempt):
            attempt += 1

            if self.mobile_tagify:
                self.driver.execute_script(self.mobile_tagify)
                if self.current_action['operation_type'].__contains__("QUERY"):
                    tagify_response = self.driver.execute_script("return tagifyWebpage(false,true);")
                else:
                    tagify_response = self.driver.execute_script("return tagifyWebpage();")
                self.xpath_mapping = tagify_response.get("xpaths", {})
                self.tags_description = tagify_response.get("descriptions", {})
                self.untagged_image_base64 = self.driver.get_screenshot_as_base64()
                self.page_source = tagify_response.get("outerHTML", "")
                self.tagified_image , ratio = make_tagged_screenshot(screenshot_base64=self.untagged_image_base64,rects=tagify_response.get("rects", {}), driver=self.driver)
            
            else:
                if self.driver.capabilities['browserName'].lower() == "safari":
                    inject_script(self.driver)

                before_screenshot = self.driver.get_screenshot_as_base64()
                self.untagged_image_base64 = before_screenshot

                if IS_WEBSOCKET_AVAILABLE:
                    asyncio.run(stop_video(self.driver.session_id))

                if self.current_action['operation_type'].__contains__("QUERY"):
                    # Execute tagifyWebpage and wait for it to complete
                    self.execute_async_js("tagifyWebpage(false,true)")
                
                elif self.current_action['operation_type'].lower() == "scroll_until_element":
                    self.execute_async_js("tagifyWebpage(true,false,true)")

                elif self.current_action['operation_type'].__contains__("SCROLL"): 
                    self.execute_async_js("tagifyWebpage(true,false)")
                
                else:
                    # Execute tagifyWebpage and wait for it to complete
                    self.execute_async_js("tagifyWebpage()")

                xpath_mapping = self.execute_async_js("fetchJsonData(\"JSONOutput\")")
                self.xpath_mapping = json.loads(xpath_mapping)

                tags_description = self.execute_async_js("fetchJsonData(\"descOutput\")")
                self.tags_description = json.loads(tags_description)

                self.page_source = self.driver.execute_script("return document.body.outerHTML")

                if self.current_action['operation_type'].lower() == "scroll_until_element":
                    self.tagified_image = capture_full_page_screenshot(self.driver)
                else:
                    self.tagified_image = self.driver.get_screenshot_as_base64()

                # First remove tags and wait for completion
                self.execute_async_js("removeLTTags()")
                
                # Then clear the data structures
                self.driver.execute_script("annotations = [];JSONOutput = {};nodeData = {};")

                if IS_WEBSOCKET_AVAILABLE:
                    asyncio.run(resume_video(self.driver.session_id))

            payload = json.dumps({
                "code_export_id": self.code_export_id,
                "current_action":self.current_action,
                "prev_actions": self.prev_actions,
                "xpath_mapping": self.xpath_mapping,
                "tagified_image": self.tagified_image,
                "commit_id": self.commit_id,
                "test_id": self.test_id,
                "username": self.username,
                "accesskey": self.accesskey,
                "tags_description": self.tags_description,
                "org_id": self.org_id,
                "page_source": self.page_source,
                "session_id": self.driver.session_id,
                "use_query_v2": self.use_query_v2, 
                "untagged_image_base64": self.untagged_image_base64
            })

            headers = {'Content-Type': 'application/json', 'Authorization' : f"Basic {base64.b64encode(f'{self.username}:{self.accesskey}'.encode()).decode()}" }

            print("Heal List Xpaths... code_export_id: ", self.code_export_id)
            response = requests.request("POST", url=f"{self.automind_url}/v1/heal/xpaths", headers=headers, data=payload)
            
            return response
            
        return response
    
    def resolve_xpath(self) -> requests.Response:
        if self.mobile_tagify:
            self.driver.execute_script(self.mobile_tagify)
            if self.current_action['operation_type'].__contains__("QUERY"):
                tagify_response = self.driver.execute_script("return tagifyWebpage(false,true);")
            else:
                tagify_response = self.driver.execute_script("return tagifyWebpage();")
            self.xpath_mapping = tagify_response.get("xpaths", {})
            self.tags_description = tagify_response.get("descriptions", {})
            self.page_source = tagify_response.get("outerHTML", "")
            self.tagified_image , ratio = make_tagged_screenshot(screenshot_base64=self.driver.get_screenshot_as_base64(),rects=tagify_response.get("rects", {}),  driver=self.driver)
            
        else:
            if self.driver.capabilities['browserName'].lower() == "safari":
                inject_script(self.driver)

            if IS_WEBSOCKET_AVAILABLE:
                asyncio.run(stop_video(self.driver.session_id))

            if self.current_action['operation_type'].__contains__("QUERY"):
                # Execute tagifyWebpage and wait for it to complete
                self.execute_async_js("tagifyWebpage(false,true)")
            else:
                # Execute tagifyWebpage and wait for it to complete
                self.execute_async_js("tagifyWebpage()")

            xpath_mapping = self.execute_async_js("fetchJsonData(\"JSONOutput\")")
            self.xpath_mapping = json.loads(xpath_mapping)

            tags_description = self.execute_async_js("fetchJsonData(\"descOutput\")")
            self.tags_description = json.loads(tags_description)

            self.page_source = self.driver.execute_script("return document.body.outerHTML")
            self.tagified_image = self.driver.get_screenshot_as_base64()

            # First remove tags and wait for completion
            self.execute_async_js("removeLTTags()")
            
            # Then clear the data structures
            self.driver.execute_script("annotations = [];JSONOutput = {};nodeData = {};")

            if IS_WEBSOCKET_AVAILABLE:
                asyncio.run(resume_video(self.driver.session_id))

        payload = json.dumps({
            "code_export_id": self.code_export_id,
            "current_action":self.current_action,
            "xpath_mapping": self.xpath_mapping,
            "tagified_image": self.tagified_image,
            "commit_id": self.commit_id,
            "test_id": self.test_id,
            "username": self.username,
            "accesskey": self.accesskey,
            "tags_description": self.tags_description,
            "org_id": self.org_id,
            "page_source": self.page_source,
            "session_id": self.driver.session_id,
        })

        headers = {'Content-Type': 'application/json', 'Authorization' : f"Basic {base64.b64encode(f'{self.username}:{self.accesskey}'.encode()).decode()}" }
        

        print("Heal Resolve Xpath... code_export_id: ", self.code_export_id)
      
        response = requests.request("POST", url=f"{self.automind_url}/v1/heal/resolve", headers=headers, data=payload)
        print("RESPONSE TEXT: ", response.text)
        
        return response

    def textual_query(self, outer_html: str) -> requests.Response:
        self.page_source = outer_html
        
        payload = json.dumps({
            "code_export_id": self.code_export_id,
            "username": self.username,
            "org_id": self.org_id,
            "commit_id": self.commit_id,
            "current_action": self.current_action,
            "accesskey": self.accesskey,
            "test_id": self.test_id,
            "page_source": self.page_source,
        })

        headers = {'Content-Type': 'application/json', 'Authorization' : f"Basic {base64.b64encode(f'{self.username}:{self.accesskey}'.encode()).decode()}" }

        print("Heal Textual Query... code_export_id: ", self.code_export_id)
        
        response = requests.request("POST", f"{self.automind_url}/v1/heal/query", headers=headers, data=payload)

        return response

    def vision_query(self) -> requests.Response:
        attempt = 1
        max_attempt = 2

        while (max_attempt >= attempt):
            attempt += 1
            if self.mobile_tagify:
                self.driver.execute_script(self.mobile_tagify)
                tagify_response = self.driver.execute_script("return tagifyWebpage(false,true);")
                self.xpath_mapping = tagify_response.get("xpaths", {})
                self.tags_description = tagify_response.get("descriptions", {})
                self.untagged_image_base64 = self.driver.get_screenshot_as_base64()
                self.tagified_image , ratio = make_tagged_screenshot(screenshot_base64=self.untagged_image_base64,rects=tagify_response.get("rects", {}), driver=self.driver)

            else:
                if self.driver.capabilities['browserName'].lower() == "safari":
                    inject_script(self.driver)
                
                before_screenshot = self.driver.get_screenshot_as_base64()
                self.untagged_image_base64 = before_screenshot
                
                if IS_WEBSOCKET_AVAILABLE:
                    asyncio.run(stop_video(self.driver.session_id))

                # Execute tagifyWebpage and wait for it to complete
                self.execute_async_js("tagifyWebpage(false,true)")
                
                # Now that tagifyWebpage is complete, get the tags description
                tags_description = self.execute_async_js("fetchJsonData(\"descOutput\")")
                self.tags_description = json.loads(tags_description)

                if IS_WEBSOCKET_AVAILABLE:
                    xpath_mapping = self.execute_async_js("fetchJsonData(\"JSONOutput\")")
                    self.xpath_mapping = json.loads(xpath_mapping)
                    
                self.tagified_image = self.driver.get_screenshot_as_base64()
                
                # First remove tags and wait for completion
                self.execute_async_js("removeLTTags()")
                
                # Then clear the data structures
                self.driver.execute_script("annotations = [];JSONOutput = {};nodeData = {};")

                if IS_WEBSOCKET_AVAILABLE:
                    asyncio.run(resume_video(self.driver.session_id))

            payload = json.dumps({
                "code_export_id": self.code_export_id,
                "current_action":self.current_action,
                "tagified_image": self.tagified_image,
                "commit_id": self.commit_id,
                "test_id": self.test_id,
                "username": self.username,
                "accesskey": self.accesskey,
                "tags_description": self.tags_description,
                "org_id": self.org_id,
                "session_id": self.driver.session_id,
                "untagged_image_base64": self.untagged_image_base64,
                "use_query_v2": self.use_query_v2,
                "version": self.version
            })

            headers = {'Content-Type': 'application/json', 'Authorization' : f"Basic {base64.b64encode(f'{self.username}:{self.accesskey}'.encode()).decode()}" }


            print("Heal Vision Query... code_export_id: ", self.code_export_id)
            print("Kane Version: ", self.version)
            response = requests.request("POST", url=f"{self.automind_url}/v1/heal/vision", headers=headers, data=payload)

            if IS_WEBSOCKET_AVAILABLE:
                try:
                    resp_json = response.json() if hasattr(response, "json") else {}
                except Exception:
                    resp_json = {}
                    
                tag_id = str(resp_json.get("tag_id", "0"))
                if tag_id and tag_id != "0":
                    try:
                        asyncio.run(create_and_upload_screenshot(tag_id=tag_id, tags_xpath_map=self.xpath_mapping or {}, untagged_screenshot=self.untagged_image_base64 or "", tagified_image=self.tagified_image or "", session_id=self.session_id, instruction_id=self.current_action['instruction_id'], operation_id=self.current_action['operation_id']))
                    except Exception:
                        print("Error in creating and uploading screenshot")
                        traceback.print_exc()

            return response
            
        return response
    
    def coordinate(self,operation_index) -> requests.Response:
            attempt = 1
            max_attempt = 3
            while (max_attempt >= attempt):
                attempt += 1
                headers = {'Content-Type': 'application/json', 'Authorization' : f"Basic {base64.b64encode(f'{self.username}:{self.accesskey}'.encode()).decode()}" }
                self.dimensions = self.driver.execute_script("return [window.innerWidth, window.innerHeight]")
                self.image_base64 = self.driver.get_screenshot_as_base64()
                self.operation = get_meta_data_value(operation_index).get('operation_intent', None)
                payload = json.dumps({
                    "code_export_id": self.code_export_id,
                    "image": self.image_base64,
                    "dimensions": self.dimensions,
                    "operation": self.operation,
                    "current_action": self.current_action,
                    "commit_id": self.commit_id,
                    "test_id": self.test_id,
                    "username": self.username,
                    "accesskey": self.accesskey,
                    "org_id": self.org_id
                })

                print(f"Heal coordinates.. codeExportId: {self.code_export_id}, orgId: {self.org_id}, testId: {self.test_id}, commitId: {self.commit_id}")
                response = requests.request("POST", url=f"{self.automind_url}/v1/heal/coordinates", headers=headers, data=payload)
                print(f"Coordinate API response status: {response.status_code} response body: {response.text}")
                if response.status_code == 200:
                    return response
                else:
                    continue

            return response
    
    def db_query(self) -> requests.Response:
        attempt = 1
        max_attempt = 2

        while (max_attempt >= attempt):
            attempt += 1
            db_details = self.current_action.get("db_details", {})
            query = self.current_action.get("db_query_decoded", "")
            db_bytes = query.encode('utf-8')

            encoded = base64.b64encode(db_bytes)
            encoded_query = encoded.decode('utf-8')
            db_details['tunnel_id'] = os.getenv('LT_PROXY_TUNNEL_ID', 0)
            payload = json.dumps({
                "payload": db_details,
                "query": encoded_query
            })
            print("DB Query Payload: ", payload)
            headers = {'Content-Type': 'application/json', 'Authorization' : f"Basic {base64.b64encode(f'{self.username}:{self.accesskey}'.encode()).decode()}" }

            print("Heal DB Query... code_export_id: ", self.code_export_id)
            
            response = requests.request("POST", url=f"{self.automind_url}/db-query", headers=headers, data=payload)
            if response.status_code == 200:
                return response.json()
            else:
                continue
            
        return response
    
    def to_json(self):

        json_payload = {
            "code_export_id": self.code_export_id,
            "current_action": self.current_action,
            "prev_actions": self.prev_actions,
            "xpath_mapping": self.xpath_mapping,
            "tagified_image": self.tagified_image,
            "commit_id": self.commit_id,
            "test_id": self.test_id,
            "username": self.username,
            "accesskey": self.accesskey,
            "tags_description": self.tags_description,
            "org_id": self.org_id,
            "page_source": self.page_source
        }
        with open("payload.json", "w") as f:
            json.dump(json_payload , f)

class TestVariable:
    def __init__(self, global_variables = [], environment_id = 0):
        self.username: str = os.getenv('LT_USERNAME',user_data.get('username',''))
        self.access_key: str = os.getenv('LT_ACCESS_KEY',user_data.get('access_key',''))
        self.global_variables = global_variables
        self.url = os.getenv("ATMS_URL", user_data.get('atms_url', ''))
        self.environment_id = environment_id

    def get_variable_value_by_name(self, variable_name: str):
        url = f"{self.url}/api/v1/variables/{variable_name}?environment_id={self.environment_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {base64.b64encode(f'{self.username}:{self.access_key}'.encode()).decode()}"
        }
        
        response = requests.request("GET", url=url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to make the request. Error: {response.text}")
        
        try:
            response = response.json()
        except ValueError as e:
            raise Exception(f"Failed to parse JSON response. Error: {str(e)}")
        return response["data"]
    
    def update_session_variable_value(self, variable_name: str, value: str):
        for variable in self.global_variables:
            if variable.get("name") == variable_name and variable.get("environment_id") == self.environment_id:
                variable["session_value"] = value
                break
        set_global_variables(self.global_variables)
    
    def update_session_variable_value_by_id(self, variable_id: int, value: str):
        for variable in self.global_variables:
            if variable.get("id") == int(variable_id):
                variable["session_value"] = value
                break
        set_global_variables(self.global_variables)

    def get_session_variable_value(self, variable_name: str):
        for variable in self.global_variables:
            if variable.get("name") == variable_name and variable.get("environment_id") == self.environment_id:
                if "session_value" in variable:
                    return variable.get("session_value")
                else:
                    return variable.get("value")
        return None

    def update_variable_value(self, variable_id: str, value: str):
        url = f"{self.url}/api/v1/variables/{variable_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {base64.b64encode(f'{self.username}:{self.access_key}'.encode()).decode()}"
        }
        payload = {
            "value": value,
            "value_type": "string"
        }
        response = requests.request("PUT", url=url, headers=headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"Failed to make the request. Error: {response.text}")
        
        try:
            response = response.json()
        except ValueError as e:
            raise Exception(f"Failed to parse JSON response. Error: {str(e)}")
        return response
    
class element_to_be_input_and_text(object):
    def __call__(self, driver): 
        focused_element = driver.execute_script("return document.activeElement;")
        if focused_element.tag_name.lower() == "input" or focused_element.tag_name.lower() == "textarea" or focused_element.get_attribute("contenteditable") == "true":
            return focused_element
        else:
            return False

def click(element: WebElement, driver, clicks_order_code: str = "se_js_ac", max_wait_until_time: int = MAX_WAIT_UNTILTIME):
    """
    Clicks order code Usage:
        se -> Selenium click
        ac -> ActionChain click
        js -> JavaScript click

        Ex: se_ac_js -> Order will be Selenium click, ActionChain click, JavaScript click

    """
    if not element:
        raise Exception("Element is not found")
    
    click_order = clicks_order_code.split("_")
    for method in click_order:
        if method == 'se':  # Selenium click (WebDriverWait + click)
            try:
                print("Max wait until time: ", max_wait_until_time)
                WebDriverWait(driver, max_wait_until_time).until(EC.element_to_be_clickable(element)).click()
                print("Selenium click successful.")
                set_clicks_order_code("se")
                return
            except Exception as e:
                print("Selenium click failed: ", str(e))
                
        elif method == 'ac':  # ActionChains click
            try:
                actions = ActionChains(driver)
                actions.move_to_element(element).click().perform()
                print("ActionChain click successful.")
                set_clicks_order_code("ac")
                return
            except Exception as e:
                print("ActionChain click failed: ", str(e))

        elif method == 'js':  # JavaScript click
            try:
                if driver.capabilities['browserName'].lower() != "safari" and (MOBILE_TAGIFY_SCRIPT is None):
                    attached_listeners = driver.execute_script("""
                        const element = arguments[0];
                        return new Promise((resolve) => {
                            (async function() {
                                try {
                                    const result = await getAttachedEventsLT(element, ['click']);
                                    console.log("Attached listeners in JS click: ", result);
                                    resolve(result);
                                } catch (error) {
                                    console.error('Async JS error:', error);
                                    resolve(null);
                                }
                            })();
                        });
                    """, element)

                    print("Attached listeners in JS click: ", attached_listeners)
                    if not attached_listeners or (attached_listeners and not attached_listeners.get("click", False)):
                        print("Not Attempting JavaScript click since element does not have a click listener.")
                        continue
                driver.execute_script("arguments[0].click();", element)
                print("JavaScript click successful.")
                set_clicks_order_code("js")
                return
            except WebDriverException as e:
                print(f"JavaScript click failed: {str(e)}.")
            
                
    raise("All click methods failed.")

def conditions_met(driver):
    # Check if the document is fully loaded
    document_ready = driver.execute_script("return document.readyState") == "complete"

    # Inject code to track active API requests
    driver.execute_script("""
    if (typeof window.activeRequests === 'undefined') {
        window.activeRequests = 0;
        (function(open) {
            XMLHttpRequest.prototype.open = function() {
                window.activeRequests++;
                this.addEventListener('readystatechange', function() {
                    if (this.readyState === 4) {
                        window.activeRequests--;
                    }
                }, false);
                open.apply(this, arguments);
            };
        })(XMLHttpRequest.prototype.open);
    }
    """)


    # Check if any API requests are in progress
    active_requests = driver.execute_script("return window.activeRequests;")
    
    # Return True only if both conditions are met
    return document_ready and active_requests == 0

def autoheal_logging(operation_idx: str, frame_info, locators, start_timestamp: float, is_success: bool):
    try:
        import log_utils 
        org_id = os.getenv("ORG_ID", "")
        username = os.getenv("LT_USERNAME", "")
        test_id = os.getenv("TEST_ID", "")
        commit_id = os.getenv("COMMIT_ID", "")
        execution = {
            "test_run_id" : os.getenv("TEST_RUN_ID", ""),
            "task_id" : os.getenv("TASK_ID", ""),
            "test_id": test_id,
            "selector" : {
                "before" : get_meta_data_value(operation_idx).get('selector', None),
                "after" : {
                   "frame": frame_info,
                   "locator": locators
                }
            },
            "framework":"selenium",
            "language":"python",
            "heal_strategy": "list_xpath",
            "latency_seconds": (time.time() - start_timestamp),
            "result": "success" if is_success else "failure"
        }
        log_utils.log_autoheal_selector(org_id = org_id, test_id = test_id, test_version = commit_id, username = username, execution = execution)
    except Exception as e:
        pass

def retry(driver: webdriver.Chrome, operation_idx: str):
    print("Retrying()...")

    set_operation_autoheal(True)  # Update the global variable to enable autoheal
    start_timestamp = time.time()
    WebDriverWait(driver, 180, poll_frequency=1).until(conditions_met)

    response = Heal(operation_idx, driver).list_xpaths()

    if response.status_code == 200:
        response_dict = json.loads(response.text)
        xpaths = response_dict
        lambda_hooks(driver, "Locator Autohealed ")
        frame_info = xpaths.get('frameInformation', "")
        locators = xpaths.get('xpaths', [])

        set_operation_autoheal(True)
        set_autoheal_frame_info(frame_info)
        set_autoheal_locators(locators)
        set_autoheal_latency(time.time() - start_timestamp)

        print("XPaths Autohealed: ", xpaths)
        return xpaths
    else:
        print("Error in Getting Xpaths")
        return {}

def go_to_url(driver: webdriver.Chrome, url: str):
    try:
        WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
        driver.get(url)

    except TimeoutException:
        driver.get(url) 



def vision_query(driver: webdriver.Chrome, operation_index: str):
    native_popups = get_meta_data_value(operation_index).get('native_popups', [])
    if native_popups != []:
        handle_mobile_native_popups(driver, popups=native_popups)
    result = None

    try:
        wait_time = get_operation_wait_time(operation_index)
        if wait_time:
            print(f"Waiting '{wait_time} seconds' before performing vision query....")
            time.sleep(wait_time)

        # Replace variable in the 'operation_intent'
        sub_instruction_obj = get_meta_data_value(operation_index).get('sub_instruction_obj', {})
        if isinstance(sub_instruction_obj, str):
            sub_instruction_obj = json.loads(sub_instruction_obj)
        if isinstance(sub_instruction_obj, dict):
            if 'variable' in sub_instruction_obj:
                if 'operation_intent' in sub_instruction_obj['variable']:
                    get_meta_data_value(operation_index)['operation_intent'] = get_variable_value(sub_instruction_obj['variable']['operation_intent'], variables=user_variables)
        
        if not NETWORK_WAIT_FOR_ALL_ACTIONS:
            smart_network_wait(driver=driver, start_timestamp=get_last_action_timestamp())
        set_last_action_timestamp(time.time() * 1000)
        
        print("Operation Intent: ", get_meta_data_value(operation_index)['operation_intent'])
        response = Heal(operation_index, driver).vision_query()
        print("Vision Response: ", response.text)
        response = json.loads(response.text)
            
        if "error" in response:
           raise Exception(f"Error in vision query: {response['error']}")
        if "message" in response:
            raise Exception(f"Error in vision query: {response['message']}")
        
        result = response
        if 'vision_query' in result and result['vision_query'] != "":
            update_global_variable(operation_index, result['vision_query'])

    except Exception as e:
        time.sleep(get_meta_data_value(operation_index)['retries_delay'])
        if  not get_meta_data_value(operation_index)['optional_flag']:
            raise e
        elif get_meta_data_value(operation_index)['optional_flag']:
            print(f"Failed to execute visual_query after. Error: {e}")

        print(f"Retrying visual_query due to Error: {str(e)[:50]}....")

    return result


def switch_to_content(driver, frames, shadow = ""):
    for frame in frames:
        key, value = list(frame.items())[0]
        if key == "iframe":
            if shadow == "":
                if isinstance(value,list):
                    for index in range(len(value)):
                        try:
                            iframe = driver.find_element(By.XPATH, value[index])
                            break
                        except:
                            continue
                else:
                    iframe = driver.find_element(By.XPATH, value)
                driver.switch_to.frame(iframe)
            else:
                iframe = shadow.find_element(By.XPATH,value)
                driver.switch_to.frame(iframe)
                shadow = ""
        elif key == "shadow":
            if shadow!="":
                shadow_childrens = shadow.find_element(By.XPATH, value)
                shadow = driver.execute_script("return arguments[0].shadowRoot.children[0]", shadow_childrens)
            else:
                shadow = driver.execute_script("return arguments[0].shadowRoot.children[0]", driver.find_element(By.XPATH,value))
    return shadow

def set_clicks_order_code(order: str):
    global CURRENT_CLICKS_ORDER_CODE, CLICKS_ORDER_ALLOWED_VALUES
    if order in CLICKS_ORDER_ALLOWED_VALUES:
        CURRENT_CLICKS_ORDER_CODE = order.lower()

def get_clicks_order_code():
    global CURRENT_CLICKS_ORDER_CODE
    return CURRENT_CLICKS_ORDER_CODE



def execute_js(user_js_code: str, driver: webdriver.Chrome) -> dict:
    try:
        user_js_code += "\n"
        lines_before_user_code = 2

        # Wrap the user's code to capture the return value and handle errors
        wrapped_js_code = f"(function() {{ try {{ return (function() {{ {user_js_code} }})(); }} catch(e) {{ e.stack = e.stack.replace(/<anonymous>:(\\d+):/g, function(match, lineNumber) {{ lineNumber = parseInt(lineNumber) - {lines_before_user_code}; return '<anonymous>:' + lineNumber + ':'; }}); return {{error: e.stack}}; }} }})();"

        if not NETWORK_WAIT_FOR_ALL_ACTIONS:
            smart_network_wait(driver=driver, start_timestamp=get_last_action_timestamp())
        set_last_action_timestamp(time.time() * 1000)
        
        client_response_js = driver.execute_script("return " + wrapped_js_code)

        if isinstance(client_response_js, dict) and 'error' in client_response_js:
            # An error occurred during execution
            error_stack = client_response_js['error']
            lines = error_stack.split('\n')
            error_message = lines[0].strip()
            error_line = None
            
            # Extract the line number from the stack trace
            if len(lines) > 1:
                match = re.search(r'<anonymous>:(\d+):', lines[1])
                if match:
                    error_line = int(match.group(1))
            
            return {
                'value': '',
                'error': error_message,
                'line': error_line
            }
        else:
            # Successful execution
            try:
                # Attempt to serialize the return value
                json.dumps(client_response_js)
                if client_response_js is None or client_response_js == '':
                    client_response_js = "null"
                return {
                    'value': client_response_js,
                    'error': '',
                    'line': None
                }
            except (TypeError, OverflowError):
                # If serialization fails, convert the return value to a string
                return {
                    'value': str(client_response_js),
                    'error': '',
                    'line': None
                }
    except (JavascriptException, WebDriverException) as e:
        # Handle exceptions raised by Selenium
        return {
            'value': '',
            'error': str(e),
            'line': None
        }
    except Exception as e:
        # Catch any other exceptions
        return {
            'value': '',
            'error': str(e),
            'line': None
        }

def are_lengths_equal(value1, value2):

    def get_length(val):
        try:
            if val.isdigit():  # If the value is a numeric string
                return int(val)  # Treat it as a length
        except Exception:
            pass
        return len(val)  # Otherwise, calculate the length of the string

    # Calculate lengths
    length1 = get_length(value1)
    length2 = get_length(value2)
    print(length1, length2)
    # Compare lengths
    return length1 == length2


def get_type(val):
    try:
        # Check if the value is a type name (e.g., "int", "str")
        # Map it to the actual Python type
        return {
            "int": int,
            "str": str,
            "float": float,
            "bool": bool,
            "list": list,
            "dict": dict,
            "tuple": tuple,
            "set": set,
        }.get(val, type(eval(val)))  # Try to evaluate if it's not a type name
    except:
        return str  # Default to string if it can't be evaluated

def are_types_equal(value1, value2):
    type_map = {
        "int": int,
        "str": str,
        "float": float,
        "bool": bool,
        "boolean": bool,
        "list": list,
        "dict": dict,
        "tuple": tuple,
        "set": set,
    }

    def to_type(val):
        if isinstance(val, str):
            v = val.strip().lower()
            if "true" in v or "false" in v:
                return bool
            if v in type_map:
                return type_map[v]
            try:
                return type(eval(val))
            except:
                return str
        return type(val)


    t1 = to_type(value1)
    t2 = to_type(value2)
    return t1 == t2

def get_meta_data_value(operation_index):
    """
    Safely get operation data from operations_meta_data regardless of whether the key is int or str.
    
    Args:
        operation_index: The operation index (can be int or str)
        
    Returns:
        The operation data dictionary or None if not found
    """
    # Try with string key first
    str_key = str(operation_index)
    if str_key in operations_meta_data:
        return operations_meta_data[str_key]
    
    # Try with integer key
    try:
        int_key = int(operation_index)
        if int_key in operations_meta_data:
            return operations_meta_data[int_key]
    except (ValueError, TypeError):
        pass
        
    return None

def find_element(driver, locators, operation_idx = 0, shadow=None, host=None):
    print("Finding element...")

    upload_file = False 
    operation_meta_data = get_meta_data_value(operation_idx)
    if operation_meta_data.get('operation_type') == "UPLOAD":
        upload_file = True
    
    if upload_file:
        time.sleep(2)
    
    driver.implicitly_wait(6)  # Set initial implicit wait to 6 seconds
    
    wait_times = [10, 3, 2, 1, 1, 1]  # Define wait times for each iteration
    if isinstance(locators[0], str):
        for i, locator in enumerate(locators):
            try:
                # Set implicit wait time based on the iteration index
                driver.implicitly_wait(max(5-(2*i), 1))
                if shadow:
                    element = shadow.find_element(By.XPATH, locator)
                else:
                    element = driver.find_element(By.XPATH, locator)
                return element
            except:
                pass
    else:
        for i, locator in enumerate(locators):
            by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
            try:
                driver.implicitly_wait(max(5-(2*i), 1))
                if shadow:
                    if by_method == By.XPATH:
                        if host:
                            first_child = driver.execute_script("""
                            const host = arguments[0];
                            const children = host.shadowRoot ? Array.from(host.shadowRoot.children) : [];
                            return children.filter(el => 
                                el.tagName.toLowerCase() !== 'script' && 
                                el.tagName.toLowerCase() !== 'style'
                            )[0];
                        """, host)
                        else:
                            first_child = shadow.find_element(By.CSS_SELECTOR, ":scope > :not(script):not(style)")
                        element = first_child.find_element(by_method, locator['selector'])
                    else:
                        element = shadow.find_element(by_method, locator['selector'])
                else:

                    element = driver.find_element(by_method, locator['selector'])
                return element
            except Exception as e:

                pass
    driver.implicitly_wait(15)  # Reset implicit wait
    return None  # Return None if no element was found or retry exhausted

def lambda_hooks(driver: webdriver.Chrome, argument: str):
    try:
        global LT_HOOK
        argument = get_variable_value(argument, user_variables)
        
        if LT_HOOK != "":
            driver.execute_script(f"lambda-testCase-end={LT_HOOK}")
        
        if argument != "":
            driver.execute_script(f"lambda-testCase-start={argument}")
            LT_HOOK = argument
            print(f"\n{argument}")
    except:
        print(f"\n{argument}")

def replace_apivar(request_args):
    for (key,value) in request_args.items():
        if isinstance(value, str):
            request_args[key]=get_variable_value(request_args[key], user_variables)
        elif isinstance(value, dict):
            for (key2,value2) in value.items():
                if isinstance(value2, str):
                    request_args[key][key2]=get_variable_value(request_args[key][key2], user_variables)
    return request_args  

def execute_api(driver: webdriver.Chrome, method: str, url: str, headers: str, body: str,params: dict,timeout: int, verify:bool, settings: dict = {}, host: str = "127.0.0.1",port: str = "22000") -> dict:
    url, headers, body, params = replace_apivar({'url': url,'headers': headers,'body': body,'params': params}).values()
    parsed_url = urlparse(url)

    # normalise headers
    if (not headers) or (not isinstance(headers, dict)):
        headers = {}
    else:
        headers = {k.lower(): v for k, v in headers.items()}
        
    if body is not None:
        body = get_effective_body(headers=headers,body=body)
        
    if not all([parsed_url.scheme, parsed_url.netloc]):
        return {'status':400,'message':'Invalid URL'}
    if(url.startswith("wss://") or url.startswith("ws://")):
        return {'status':400,'message':'Websockets not supported'}
    for key in headers:
        if(headers[key]=='text/event-stream'):
            return {'status':400,'message':'Sse not supported'}
    
    start=time.time()
    
    if not NETWORK_WAIT_FOR_ALL_ACTIONS:
        smart_network_wait(driver=driver, start_timestamp=get_last_action_timestamp())
    set_last_action_timestamp(start * 1000)
    
    try:
        if method.upper() == "GET":
            response = httpx.get(url, headers=headers, params=params, timeout=timeout, proxy=f"http://{host}:{port}", verify=verify, follow_redirects=settings.get('automatically_follow_redirect', True) if settings else True)
        elif method.upper() == "POST":
            response = httpx.post(url, headers=headers, data=body, params=params, timeout=timeout, proxy=f"http://{host}:{port}", verify=verify, follow_redirects=settings.get('automatically_follow_redirect', True) if settings else True)
        elif method.upper() == "PUT":
            response = httpx.put(url, headers=headers, data=body, params=params, timeout=timeout, proxy=f"http://{host}:{port}", verify=verify, follow_redirects=settings.get('automatically_follow_redirect', True) if settings else True)
        elif method.upper() == "DELETE":
            response = httpx.delete(url, headers=headers, params=params, timeout=timeout, proxy=f"http://{host}:{port}", verify=verify, follow_redirects=settings.get('automatically_follow_redirect', True) if settings else True)
        elif method.upper() == "PATCH":
            response = httpx.patch(url, headers=headers, data=body, params=params, timeout=timeout, proxy=f"http://{host}:{port}", verify=verify, follow_redirects=settings.get('automatically_follow_redirect', True) if settings else True)
    except Exception as e:
        return {'status':400,'message':"API request failed " + str(e)}
    
    end=time.time()
    
    test_api_resp = {
        "status" : response.status_code,
        "headers" : response.headers,
        "cookies" : response.cookies,
        "body" : response.content,
        "time" : (end-start)*1000
    }
    
    checker=[]
    for key in test_api_resp:
        checker.append(key)
    for i in range(0,len(checker)):
        key=checker[i]
        try:
            json.dumps(test_api_resp[key])  # Try to serialize the value
        except (TypeError, ValueError):
            if isinstance(test_api_resp[key], bytes):
                try:
                    test_api_resp["response_body"] = json.loads(test_api_resp[key].decode('utf-8'))
                except (TypeError, ValueError):
                    test_api_resp["response_body"] = {"html":test_api_resp[key].decode('utf-8')}
                test_api_resp[key]=list(test_api_resp[key].decode('utf-8'))
            else:
                test_api_resp[key]=[{k:v} for k,v in test_api_resp[key].items()]
            for i in range(0,len(test_api_resp[key])):
                try:
                    json.dumps(test_api_resp[key][i])
                except (TypeError, ValueError):
                    test_api_resp[key][i] = str(test_api_resp[key][i])
    return test_api_resp

def replace_secrets(text: str) -> str:
    matches = re.findall(r'\{\{(.*?)\}\}', text)
    for match in matches:
        keys = match.split('.')
        if len(keys) == 3 and keys[0] == 'secrets':
            secret_value = os.getenv(keys[2], '')
            text = text.replace(f"{{{{{match}}}}}", secret_value)

    return text

def get_effective_body_and_params(method:str ,url: str,body:str ,auth_payload = {}) -> Tuple[Dict[str, Any], Dict[str, str]]:
    data = auth_payload.get('data', {})

    if auth_payload.get("type") == "aws-signature":
        region = data.get('region','us-east-1')
        session_token = data.get('session_token')
        access_key = data.get('access_key')
        secret_key = data.get('secret_key')
        service_name = data.get('service_name','')

        awsRequest = AWSRequest(
            method=method,
            url=url,
            data=body
        )
        if service_name.lower() == 's3':
            awsRequest.context["payload_signing_enabled"] = False

        # Create signer and sign request
        credentials = Credentials(access_key, secret_key, session_token)

        if data.get("add_to") == "params":
            SigV4QueryAuth(credentials, service_name, region).add_auth(awsRequest)
            parsed_url = urlparse(awsRequest.url)
            params = parse_qs(parsed_url.query)
            params = {k: v[0] if len(v) == 1 else v for k, v in params.items()}
            return params,{}
        
        SigV4Auth(credentials, service_name, region).add_auth(awsRequest)
        headers = dict(awsRequest.headers)
        return {}, headers
    
    return {} , {}



def get_effective_body(headers: dict, body: str):
    try:
        content_type = headers.get("Content-Type", "").lower()
        if is_binary_content_type(content_type=content_type) and body:
            data = json.loads(body)
            if "file_url" in data:
                url = data["file_url"]
                if not url.startswith(("http://", "https://")):
                    url = "http://" + url
                response = requests.get(url)
                response.raise_for_status()
                return response.content
            elif "file_path" in data:
                file_name = Path(data["file_path"]).name
                file_path = get_downloads_file_path(file_name)
                with open(file_path, 'rb') as f:
                    binary_data = f.read()
                    return binary_data
    except Exception as e:
        print(f"Error in get_effective_body: {e}")

    return body


def is_binary_content_type(content_type: str) -> bool:
    binary_types = {
        "application/octet-stream",
        "application/pdf",
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    }
    return (content_type in binary_types or content_type.startswith(("image/", "audio/", "video/","text/")))



def replace_secrets_in_dict(
    d: Dict[str, str]
) -> Dict[str, str]:

    new_dict = {}
    for k, v in d.items():
        replaced_key = replace_secrets(k)
        replaced_value = replace_secrets(v)
        if replaced_key == 'Authorization' and not replaced_value.startswith('Bearer') and not replaced_value.startswith('AWS') and len(replaced_value.split(':')) == 2:
            username = replaced_value.split(':')[0]
            access_key = replaced_value.split(':')[1]
            replaced_value = f"Basic {base64.b64encode(f'{username}:{access_key}'.encode()).decode()}"
        new_dict[replaced_key] = replaced_value
        
    return new_dict


def perform_assertion(operand1, operator, operand2, operation_index = 0, intent = "", driver = None):
    meta_data = get_meta_data_value(operation_index) or {}
    native_popups = meta_data.get('native_popups', [])
    if native_popups != []:
        handle_mobile_native_popups(driver, popups=native_popups)
    operation_data = get_meta_data_value(operation_index) or {}
    hard_assertion = operation_data.get('hard_assertion', False)
    sub_instruction_obj = operation_data.get('sub_instruction_obj', {})
    if isinstance(sub_instruction_obj, str):
        sub_instruction_obj = json.loads(sub_instruction_obj)
    is_string_to_float = operation_data.get('string_to_float', False)
    failure_condition = operation_data.get('failure_condition', '')
    if isinstance(sub_instruction_obj, dict) and 'json' not in operator:
        if 'params' in sub_instruction_obj:
            if 'operand1' in sub_instruction_obj['params']:
                new_value = get_parameter_value(sub_instruction_obj['params']['operand1'], user_parameters)
                if is_string_to_float:
                    operand1 = string_to_float(new_value)
                else:
                    operand1 = new_value.lower()
            if 'operand2' in sub_instruction_obj['params']:
                new_value = get_parameter_value(sub_instruction_obj['params']['operand2'], user_parameters)
                if is_string_to_float:
                    operand2 = string_to_float(new_value)
                else:
                    operand2 = new_value.lower()
        if 'variable' in sub_instruction_obj:
            if 'operand1' in sub_instruction_obj['variable']:
                new_value = get_variable_value(sub_instruction_obj['variable']['operand1'], user_variables)
                if is_string_to_float:
                    operand1 = string_to_float(new_value)
                else:
                    operand1 = str(new_value).lower()
            if 'operand2' in sub_instruction_obj['variable']:
                new_value = get_variable_value(sub_instruction_obj['variable']['operand2'], user_variables)
                if is_string_to_float:
                    operand2 = string_to_float(new_value)
                else:
                    operand2 = str(new_value).lower()

    is_replace = operation_data.get('is_replace', "false")
    if is_replace == "true":
        operand2 = str(operation_data.get('expected_value')).lower()
        operator_name = operation_data.get("operator")
        intent = f"assert if {operand1} is {operator_name} {operand2}"
        
    if is_string_to_float:
        operand1 = string_to_float(operand1)
        operand2 = string_to_float(operand2)

    try:
          if operator in ["json_key_exists", "json_keys_count", "json_array_length", "json_array_contains", "json_value_equals"]:
            if operator == "json_key_exists":
                assert operand2 in operand1.keys(), f"Key '{operand2}' does not exist in the JSON object."
            elif operator == "json_keys_count":
                assert len(operand1.keys()) == int(operand2), f"Expected {operand2} keys, but found {len(operand1.keys())}."
            elif operator == "json_array_length":
                assert len(operand1) == int(operand2), f"Expected array length {operand2}, but found {len(operand1)}."
            elif operator == "json_array_contains":
                assert operand2 in operand1, f"Array does not contain the value '{operand2}'."
            elif operator == "json_value_equals":
                if not (isinstance(operand1, type(operand2)) or isinstance(operand2, type(operand1))):
                    raise AssertionError(f"Type mismatch: expected {type(operand2)}, but found {type(operand1)}.")
                if operand1 != operand2:
                    raise AssertionError(f"Expected value '{operand2}', but found '{operand1}'.")
          elif operator == "==":
              assert operand1 == operand2, f"Expected {operand1} to equal {operand2}"
          elif operator == "!=":
              assert operand1 != operand2, f"Expected {operand1} to not equal {operand2}"
          elif operator == "true":
              assert operand1, f"Expected true, got {operand1}"
          elif operator == "false":
              assert not operand1, f"Expected false, got {operand1}"
          elif operator == "is_null":
              assert operand1 is None, "Expected operand to be None"
          elif operator == "not_null":
              assert operand1 is not None, "Expected operand to be not None"
          elif operator == "contains":
              assert operand2 in operand1, f"Expected {operand2} to be in {operand1}"
          elif operator == "not_contains":
              assert operand2 not in operand1, f"Expected {operand2} to not be in {operand1}"
          elif operator == ">":
              assert operand1 > operand2, f"Expected {operand1} to be greater than {operand2}"
          elif operator == "<":
              assert operand1 < operand2, f"Expected {operand1} to be less than {operand2}"
          elif operator == ">=":
              assert operand1 >= operand2, f"Expected {operand1} to be greater than or equal to {operand2}"
          elif operator == "<=":
              assert operand1 <= operand2, f"Expected {operand1} to be less than or equal to {operand2}"
          elif operator == "length_equals":
              assert len(operand1) == operand2, f"Expected length of {operand1} to be {operand2}"
          elif operator == "type_equals":
              assert type(operand1) == operand2, f"Expected type of {operand1} to be {operand2}"

          lambda_hooks(driver, f"Assertion  passed: '{intent}'")
          return True
    except Exception as e:
          lambda_hooks(driver, f"Assertion failed: '{intent}' - {str(e)}")
          print(f"Assertion check failed: '{intent}' - {str(e)}")
          if hard_assertion:
              status = "failed"
              driver.execute_script(f"lambda-status={status}")
              raise e
          if not IS_WEBSOCKET_AVAILABLE:
            if failure_condition == FailureCondition.FAIL_TEST_IMMEDIATELY.value or failure_condition == FailureCondition.NONE.value:
                  raise RuntimeError(f"Assertion failed: '{intent}' - {str(e)}")
            elif failure_condition == FailureCondition.FAIL_BUT_CONTINUE_EXECUTING.value:
                  set_test_status("failed")
          return False

def update_meta_data(operation_index, response):
    print("Updating meta data...")
    try:
        operations_meta_data[str(operation_index)].update(response)
    except Exception as e:
        operations_meta_data[int(operation_index)].update(response)
    
def handle_unresolved_operations(operations_meta_data, operation_index, driver):
    operation_index = int(operation_index)
    unresolved_operation = get_meta_data_value(operation_index)
    agent = unresolved_operation['agent']
    if agent == "Vision Agent":
        WebDriverWait(driver, 30, poll_frequency=3).until(conditions_met)
        
        max_attempts = 3
        for attempt in range(1, max_attempts + 1):
            try:
                healer = Heal(operation_index, driver)
                response = healer.resolve()
                response = response.json()
                response['locator'] = [response['xpath']]
                response['frame'] = json.dumps(response.get('frameInformation', ""))
                update_meta_data(operation_index, response)
                break  # Success, exit the retry loop
            except Exception as e:
                print(f"Attempt {attempt} failed for operation {operation_index}: {str(e)}")
                if attempt == max_attempts:
                    print(f"All {max_attempts} attempts failed for operation {operation_index}. Error: {str(e)}")
                    raise e  # Re-raise the exception after all attempts are exhausted
                time.sleep(2)  # Wait 2 seconds before retrying
        

# throttle network
def execute_network_throttle(driver, is_mobile_offline: bool, network_throttle: dict):
    value = network_throttle.get("value")

    try:
        if value != "custom":
            driver.execute_script(f"updateNetworkProfile={value}")
            print(f"Throttling Successfully Applied With Network Profile: {value}")
        else:
            download_speed = network_throttle.get("download_speed", 0)
            upload_speed = network_throttle.get("upload_speed", 0)
            latency = network_throttle.get("latency", 0)
            driver.execute_script(f"customNetworkProfile:{{ \\\"downloadSpeed\\\": {download_speed},\\\"uploadSpeed\\\" : {upload_speed}, \\\"latency\\\": {latency} }}")
            print(f"Throttling Successfully Applied With Custom Network Profile: downloadSpeed: {download_speed}, uploadSpeed: {upload_speed}, latency: {latency}")
        
        time.sleep(2) # wait for 2 seconds to apply the network throttle
    except Exception as e:
        raise Exception(f"Error executing network throttle: {e}")


# initialize network throttle
def initialize_network_throttle(driver):
    
    value = os.getenv("NETWORK_PROFILE", "default")

    if value != "default":
        network_throttle = {
            "value": value,
            "download_speed": int(os.getenv("DOWNLOAD_SPEED", 0)),
            "upload_speed": int(os.getenv("UPLOAD_SPEED", 0)),
            "latency": int(os.getenv("LATENCY", 0))
        }
        
        execute_network_throttle(driver, is_mobile_offline=False, network_throttle=network_throttle)

def string_to_float(input_string):
    # If already a numeric type, return as is
    if isinstance(input_string, (float, int)):
        return input_string
    
    # Try direct conversion first, which handles scientific notation
    try:
        return float(input_string)
    except ValueError:
        # Handle negative sign
        is_negative = '-' in input_string
        
        # Filter to keep only digits and decimal point
        a = ''.join(filter(lambda x: x.isdigit() or x == '.', input_string))
        
        if a == "":
            return 0
        
        # Apply negative sign if needed
        result = float(a)
        if is_negative:
            result = -result
            
        return result

def heal_query(driver: webdriver, operation_index: str, outer_html: str):

    response = Heal(operation_index, driver).textual_query(outer_html)
    response_dict = json.loads(response.text)

    if 'regex' in response_dict:
        regex_pattern = response_dict.get('regex')
        lambda_hooks(driver, "Regex Autohealed ")
        print("REGEX FROM AUTOMIND: ", regex_pattern)
        return regex_pattern
    elif 'error' in response_dict or response.status_code == 500:
        print("Error encountered, retrying...")
    else:
        print("Error in Getting Regex")
        
    return ""
   
def populate_attributes(element: WebElement, driver: webdriver.Chrome, requested_attribute: str):
    """
    Get a specific attribute from a web element.
    
    Args:
        element: WebElement to get attribute from
        driver: Selenium WebDriver instance
        requested_attribute: Name of the attribute to retrieve
        
    Returns:
        The value of the requested attribute
    """
    attribute_getters = {
        "tag_name": lambda: element.tag_name if element.tag_name else "",
        "text": lambda: safe_value(element, driver),
        "id": lambda: element.get_attribute("id") if element.get_attribute("id") else "",
        "class": lambda: element.get_attribute("class") if element.get_attribute("class") else "",
        "href": lambda: element.get_attribute("href") if element.get_attribute("href") else "",
        "src": lambda: element.get_attribute("src") if element.get_attribute("src") else "",
        "enabled": lambda: element.is_enabled(),
        "checked": lambda: element.is_selected(),
        "selected": lambda: element.is_selected(),
        "aria_label": lambda: element.get_attribute("aria-label") if element.get_attribute("aria-label") else "",
        "role": lambda: element.aria_role if element.aria_role else "",
        "displayed": lambda: element.is_displayed(),
        "size": lambda: element.size if element.size else {},
        "background_color": lambda: rgba_string_to_name(element.value_of_css_property("background-color")) if element.value_of_css_property("background-color") else "",
        "color": lambda: rgba_string_to_name(element.value_of_css_property("color")) if element.value_of_css_property("color") else "",
        "font_size": lambda: element.value_of_css_property("font-size") if element.value_of_css_property("font-size") else "",
        "font_weight": lambda: element.value_of_css_property("font-weight") if element.value_of_css_property("font-weight") else "",
        "border_radius": lambda: element.value_of_css_property("border-radius") if element.value_of_css_property("border-radius") else "",
        "z_index": lambda: element.value_of_css_property("z-index") if element.value_of_css_property("z-index") else "",
        "opacity": lambda: element.value_of_css_property("opacity") if element.value_of_css_property("opacity") else "",
        "transform": lambda: element.value_of_css_property("transform") if element.value_of_css_property("transform") else "",
        "aria_expanded": lambda: element.get_attribute("aria-expanded") if element.get_attribute("aria-expanded") else "",
        "value": lambda: safe_value(element, driver),
        "placeholder": lambda: element.get_attribute("placeholder") if element.get_attribute("placeholder") else "",
        "location": lambda: get_section_from_bbox(element.rect, driver),
        "custom_attributes_dict": lambda: get_all_element_attributes(element, driver),
        "disabled": lambda: not element.is_enabled(),
    }
    
    if requested_attribute == "custom_attribute_name":
        requested_attribute = "custom_attributes_dict"

    if requested_attribute == "attributes":
        return driver.execute_script("return Array.from(arguments[0].attributes).map(attr => attr.name);",element)
    
    if requested_attribute not in attribute_getters:
        raise ValueError(f"Unknown attribute: {requested_attribute}")
        
    return attribute_getters[requested_attribute]()

def access_variable_value(variable_dump:dict, name:str):

    keys = name.split('.')

    if keys[0] == 'smart' and len(keys) == 2:
        value = variable_dump.get(name)
        return value

    value = variable_dump

    for key in keys:

        while '[' in key and ']' in key:
            # Handle nested list indexing
            base_key, index = key.split('[', 1)
            index = int(index.split(']')[0])
            value = value[base_key] if base_key else value
            value = value[index]
            key = key[key.index(']') + 1:]  # Move to the next part of the key

        if key:  # Handle any remaining dictionary key
            value = value[key]
    return value

# get prev operation wait time
def get_prev_operation_wait_time(operation_index: str) -> float:
    wait_time = 0
    try:
        prev_op_index = str(int(operation_index) - 1)
        prev_op_end_time = operations_meta_data.get(prev_op_index, {}).get('operation_end', '')
        curr_op_start_time = get_meta_data_value(operation_index).get('operation_start', '')
        
        if prev_op_end_time and curr_op_start_time:
            # Define the datetime format
            format = "%Y-%m-%d %H:%M:%S.%f"
            
            # Convert strings to datetime objects
            datetime1 = datetime.strptime(prev_op_end_time, format)
            datetime2 = datetime.strptime(curr_op_start_time, format)
            
            # Calculate the difference in seconds
            wait_time =  (datetime2 - datetime1).total_seconds()
    except Exception as e:
        print(f"Error getting prev operation wait time: {e}")
    
    return wait_time

def get_operation_wait_time(operation_index: str, default_wait_time: float = 5, max_additional_wait_time: float = 5) -> float:
    wait_time: float = 0
    try:
        explicit_wait = float(get_meta_data_value(operation_index).get('explicit_wait', 0))
        wait_time = explicit_wait
        
        # get additional wait time depending on prev operation end time: to avoid delay in screen loading or slow internet issues
        additional_wait = default_wait_time
        prev_op_wait_time = get_prev_operation_wait_time(operation_index)
        if prev_op_wait_time > additional_wait:
            additional_wait = prev_op_wait_time
        
        # limit additional wait time in order to avoid false negatives or long waiting time
        additional_wait = min(additional_wait, max_additional_wait_time)
        
        wait_time += additional_wait
    except Exception as e:
        print(f"Error getting wait time: {e}")
        wait_time += default_wait_time # add default wait time
    
    return wait_time



def clear(driver, element, cordiantes):
    if cordiantes is not None:
        x = float(cordiantes.split(",")[0].replace("[", ""))
        y = float(cordiantes.split(",")[1].replace("]", ""))

        # First action: move and click
        click_action = ActionBuilder(driver)
        click_action.pointer_action.move_to_location(x, y)
        click_action.pointer_action.click()
        click_action.perform()

        # Second action: select all text
        select_action = ActionBuilder(driver)
        select_action.key_action.key_down(Keys.CONTROL)
        select_action.key_action.send_keys("a")
        select_action.key_action.key_up(Keys.CONTROL)
        select_action.perform()

        # Third action: delete the selected text
        delete_action = ActionBuilder(driver)
        delete_action.key_action.send_keys(Keys.DELETE)
        delete_action.perform()
    else:
        try:
            element.click()
        except:
            driver.execute_script("arguments[0].click();", element)

        if MOBILE_TAGIFY_SCRIPT != None:
            current_value = element.get_attribute('value')
        else:
            current_value = driver.execute_script("return arguments[0].value;", element)

        try:
            if current_value:
                try:
                    driver.execute_script("arguments[0].setSelectionRange(arguments[0].value.length, arguments[0].value.length);", element)
                except:
                    pass
                n = len(current_value)
                for i in range(n):
                    element.send_keys(Keys.BACKSPACE)
            if element.get_attribute("contenteditable") == "true":
                # First select all content
                driver.execute_script("""
                    const element = arguments[0];
                    const range = document.createRange();
                    range.selectNodeContents(element);
                    const selection = window.getSelection();
                    selection.removeAllRanges();
                    selection.addRange(range);
                """, element)
                
                # Then delete the selection
                element.send_keys(Keys.DELETE)

        except Exception as e:
            print(f"Error clearing element: {e}")
            try:
                driver.execute_script("arguments[0].value = '';", element)
            except Exception as e:
                print(f"Error setting value to empty: {e}")

def query(driver: webdriver.Chrome, operation_index: int):
    native_popups = get_meta_data_value(operation_index).get('native_popups', [])
    if native_popups != []:
        handle_mobile_native_popups(driver, popups=native_popups)
    locators = get_meta_data_value(operation_index)['locator']
    regex_pattern = get_meta_data_value(operation_index)['regex_pattern']
    utility = get_meta_data_value(operation_index)['string_to_float']
    element = find_element(driver, locators)
    
    if element is None and utility:
        return 0
    elif element is None and not utility:
        return ""
    
    html = element.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
    regex = base64.b64decode(regex_pattern).decode("utf-8")
    match = re.search(fr"{regex}", html)
    if utility:
        return string_to_float(match.group(1)) if match else 0
    return match.group(1) if match else ""

operations_meta_data = {}

def set_operations_meta_data(data):
    global operations_meta_data
    operations_meta_data = data
    
def set_user_data(data):
    global user_data
    user_data = data

def move_to_start_of_input(element,focused_element=None):
    placeholder = element.get_attribute("placeholder") if element.get_attribute("placeholder") else ""
    if MOBILE_TAGIFY_SCRIPT == None and ( element.get_attribute("type") in ["date","time"] or all(part in placeholder.lower() for part in ['dd', 'mm', 'yy']) or element.get_attribute("autocomplete") != "" ):
        for i in range(10):
            if focused_element:
                focused_element.send_keys(Keys.ARROW_LEFT)
            else:
                element.send_keys(Keys.ARROW_LEFT)

def select_option(driver, select_element, option):
    text_value = option.split("::")
    print("select option", text_value)
    value, text = text_value[0], text_value[1]
    option_values = driver.execute_script("""
        const select = arguments[0];
        return Array.from(select.options).map(option => option.value);
    """, select_element)
    print("option values", option_values)
    if value in option_values:
        driver.execute_script("""
            const select = arguments[0];
            const value = arguments[1];
            select.value = value;
            select.dispatchEvent(new Event('input', { bubbles: true }));
            select.dispatchEvent(new Event('change', { bubbles: true }));
        """, select_element, value)
    else:
        # find value of the option with the text
        value = driver.execute_script("""
            const select = arguments[0];
            return Array.from(select.options).find(option => option.textContent === arguments[1]).value;
        """, select_element, text)
        if value:
            driver.execute_script("""
                const select = arguments[0];
                const value = arguments[1];
                select.value = value;
                select.dispatchEvent(new Event('input', { bubbles: true }));
                select.dispatchEvent(new Event('change', { bubbles: true }));
            """, select_element, value)
        else:
            raise ValueError("Option not found")

def handle_totp_variable(match: str) -> str:
    name = match.split(".")[1]
    key = user_variables.get(f"{name}", "")
    if key.startswith('{{secrets.'):
        key = key.replace("}}", "")
        key = key.replace("{{", "")
        key = os.getenv(key.split('.')[2], '')
    return generate_totp_code(key) 

def access_value(mapping, path):
    global smart_variables_cache
    try:
        keys = path.split('.')
        if keys[0] == 'smart' and len(keys) == 2:
            smart_variables = None
            if smart_variables_cache != None:
                smart_variables = smart_variables_cache
            else:
                smart_variables = SmartVariables()
                smart_variables_cache = smart_variables
            
            return smart_variables.get(keys[1])
        
        if keys[0] == 'global' and len(keys) == 2:
            test_variable = TestVariable(global_variables=global_variables)
            variable = test_variable.get_variable_value_by_name(keys[1])
            value = variable["value"]
            if not variable["is_persist"]:
                session_variable_value = test_variable.get_session_variable_value(keys[1])
                if session_variable_value is not None:
                    value = session_variable_value
            return value
        
        if keys[0] == 'environment' and len(keys) == 2:
            test_variable = TestVariable(global_variables=global_variables, environment_id=int(os.getenv("ENVIRONMENT_ID", user_data.get('environment_id', 0))))
            variable = test_variable.get_variable_value_by_name(keys[1])
            return variable["value"]

        value = mapping
        for key in keys:
            while '[' in key and ']' in key:
                base_key, index = key.split('[', 1)
                index = int(index.split(']')[0])
                value = value[base_key] if base_key else value
                value = value[index]
                key = key[key.index(']') + 1:] 
            if key: 
                value = value[key]

        return str(value)
    except (KeyError, IndexError, ValueError, TypeError):
        return None

def get_parameter_value(value: str, parameters : dict = {}) -> str:
    matches = re.findall(r'\$\{(.*?)\}', value)
    new_value = value
    if matches:
        for match in matches:
            accessed_value = access_value(parameters, match)
            if accessed_value is not None:
                new_value = new_value.replace("${"+match+"}", str(accessed_value))
    return new_value

def generate_totp_code(secret):
    try:
        import pyotp
        cleaned_secret = secret.replace('-', '').replace(' ', '').upper()
        
        if not cleaned_secret:
            return None
            
        # Generate TOTP code
        totp = pyotp.TOTP(cleaned_secret)
        code = totp.now()
            
        return code
    except Exception as e:
        print(f"Error generating TOTP code: {e}")
        return secret

def get_variable_value(value: str, variables : dict = user_variables) -> str:
    matches = re.findall(r'\{\{(.*?)\}\}', value)
    new_value = value
    if matches:
        for match in matches:
            if match.split(".")[0] == "global":
                test_variable = TestVariable(global_variables=global_variables)
                variable = test_variable.get_variable_value_by_name(match.split(".")[1])
                variable_value = variable["value"]
                if not variable["is_persist"]:
                    session_variable_value = test_variable.get_session_variable_value(match.split(".")[1])
                    if session_variable_value is not None:
                        variable_value = session_variable_value
                new_value = new_value.replace("{{"+match+"}}", str(variable_value))
                continue

            if match.split(".")[0] == "environment":
                test_variable = TestVariable(global_variables=global_variables, environment_id=int(os.getenv("ENVIRONMENT_ID", user_data.get('environment_id', 0))))
                variable_value = test_variable.get_variable_value_by_name(match.split(".")[1])["value"]
                new_value = new_value.replace("{{"+match+"}}", str(variable_value))
                continue
            
            if match.split(".")[0] == 'smart' and match.split(".")[1].startswith('totp_'):
                new_value = new_value.replace("{{"+match+"}}", str(handle_totp_variable(match)))
                continue
            if match.split(".")[0] == "secrets" and len(match.split(".")) == 3:
                new_value = new_value.replace("{{"+match+"}}", os.getenv(match.split('.')[2], ''))
                continue
            accessed_value = access_value(variables, match)
            if accessed_value is not None:
                new_value = new_value.replace("{{"+match+"}}", str(accessed_value))
    return new_value

def switch_to_frame(driver:webdriver.Chrome,operation_index:str,shadow = None,max_retries=3,frame_info=""):
    for index in range(1,max_retries + 2):
        if index!=1:
            driver.switch_to.default_content()
            frame_info = retry(driver=driver,operation_idx=operation_index).get('frameInformation')
            frame_info = json.dumps(frame_info)
        try:
            if frame_info and frame_info != "":
                frames = json.loads(frame_info)
                for frame in frames:
                    key, value = list(frame.items())[0]
                    if key == "iframe":
                        if shadow == None:
                            if isinstance(value,list):
                                for index in range(0,len(value)):
                                    try:
                                        iframe = driver.find_element(By.XPATH, value[index])
                                        break
                                    except:
                                        continue
                            else:
                                iframe = driver.find_element(By.XPATH, value)
                            driver.switch_to.frame(iframe)
                        else:
                            iframe = shadow.find_element(By.XPATH, value)
                            driver.switch_to.frame(iframe)
                            shadow = None
                    elif key == "shadow":
                        if shadow != None:
                            shadow_childrens = shadow.find_element(By.XPATH, value)
                            shadow = driver.execute_script("return arguments[0].shadowRoot.children[0]", shadow_childrens)
                        else:
                            shadow = driver.execute_script("return arguments[0].shadowRoot.children[0]", driver.find_element(By.XPATH, value))
            return shadow
        except Exception as e:
            pass
    return "unresolved"

def canvas_autoheal_wrapper(operation_index,driver):
    response = Heal(operation_index, driver).coordinate(operation_index=operation_index)
    response_data = response.json()
    x = response_data["coordinate"][0]
    y = response_data["coordinate"][1]
    return x,y

def isShiftingRequired(element,placeholder):
    if element.get_attribute("type") in ["date","time"] or all(part in placeholder.lower() for part in ['dd', 'mm', 'yy']) or element.get_attribute("autocomplete") != "":
        return True
    return False

def clear_element(driver, element):
    try:
        current_value = element.get_attribute('value')
        if current_value:
            n = len(current_value)
            for i in range(n):
                element.send_keys(Keys.BACKSPACE)
        if element.get_attribute("contenteditable") == "true":
            # First select all content
            driver.execute_script("""
                const element = arguments[0];
                const range = document.createRange();
                const selection = window.getSelection();
                range.selectNodeContents(element);
                selection.removeAllRanges();
                selection.addRange(range);
            """, element)
            # Then delete the selection
            element.send_keys(Keys.DELETE)
    except Exception as e:
        print(f"Error clearing element via send keys: {e}")
        if MOBILE_TAGIFY_SCRIPT:
            driver.execute_script("arguments[0].value = ''", element)

def wait_for_dom(driver):
    result = is_dom_loaded(driver)
    if isinstance(result, tuple):
        is_loaded, error_msg = result
        if not is_loaded:
            print(f"DOM loading error: {error_msg}")
        return is_loaded
    return result

def is_action_unresolved(action: str, sub_instruction_obj: dict, operation_index: int = 0) -> bool:
    if action == "GENERATIVE":
        return False
    valid_actions = ["CLICK", "HOVER", "CLEAR", "ENTER"]
    # check if variable has been change
    current_operation_intent = sub_instruction_obj.get('operation')
    
    sub_instruction_obj_intent = sub_instruction_obj.get("variable", {}).get("operation_intent", "")
    sub_instruction_obj_intent = get_variable_value(sub_instruction_obj_intent, user_variables)

    if sub_instruction_obj_intent == current_operation_intent:
        return False
    
    return action in valid_actions and isinstance(sub_instruction_obj, dict) and len(sub_instruction_obj.get("variable", {})) > 0

def set_operation_autoheal(value: bool):
    global operation_autoheal
    operation_autoheal = value

def get_operation_autoheal() -> bool:
    return operation_autoheal

def update_autoheal_selector(driver: webdriver.Chrome, operation_index: str, frame_info: dict, locators: list, latency_in_seconds: float, is_success: bool, selectors: str = "") -> None:
    """
    Helper function to update autoheal selector with frame info and locators.
    
    Args:
        driver: WebDriver instance
        operation_index: Current operation index
        frame_info: Frame information string
        locators: List of locators to update
        latency_in_seconds: Latency in seconds
        is_success: Whether the autoheal was successful
        selectors: Autohealed selectors
    """
    
    update_autoheal(
        session_id=driver.session_id,
        instruction_id=get_meta_data_value(operation_index).get('instruction_id', ''),
        operation_id=get_meta_data_value(operation_index).get('operation_id', ''),
        frame_info=frame_info,
        locator=locators,
        autoheal=True,
        latency_second=latency_in_seconds,
        is_success=is_success,
        selectors=selectors
    )
    set_operation_autoheal(True)

def find_dict_with_kv(data, key, value):
    if isinstance(data, dict):
        if data.get(key) == value:
            return data
        for v in data.values():
            result = find_dict_with_kv(v, key, value)
            if result:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_dict_with_kv(item, key, value)
            if result:
                return result
    return None

def decode_body_payload(network_queried_data: dict):
    if "application/json" in network_queried_data.get("response", {}).get("content", {}).get("mimeType", ""):
        if "base64" in network_queried_data.get("response", {}).get("content", {}).get("encoding", ""):
            if network_queried_data.get("response", {}).get("content", {}).get("text", "") != "":
                decoded_text = base64.b64decode(network_queried_data.get("response", {}).get("content", {}).get("text")).decode("utf-8")
                network_queried_data["response"]["content"]["text"] = json.loads(decoded_text)
            else:
                network_queried_data["response"]["content"]["text"] = {}
        else:
            if network_queried_data.get("response", {}).get("content", {}).get("text", "") != "":
                network_queried_data["response"]["content"]["text"] = json.loads(network_queried_data.get("response", {}).get("content", {}).get("text"))
            else:
                network_queried_data["response"]["content"]["text"] = {}
    
    if "application/json" in network_queried_data.get("request", {}).get("postData", {}).get("mimeType", ""):
        if "base64" in network_queried_data.get("request", {}).get("postData", {}).get("encoding", ""):
            if network_queried_data.get("request", {}).get("postData", {}).get("text", "") != "":
                decoded_text = base64.b64decode(network_queried_data.get("request", {}).get("postData", {}).get("text")).decode("utf-8")
                network_queried_data["request"]["postData"]["text"] = json.loads(decoded_text)
            else:
                network_queried_data["request"]["postData"]["text"] = {}
        else:
            if network_queried_data.get("request", {}).get("postData", {}).get("text", "") != "":
                network_queried_data["request"]["postData"]["text"] = json.loads(network_queried_data.get("request", {}).get("postData", {}).get("text"))
            else:
                network_queried_data["request"]["postData"]["text"] = {}
    return network_queried_data


def poll_network_logs(method, network_url, index, polling_interval, max_polling_time, network_log_id=None):
    num_tries = 0
    queried_content = None
    print(f"method: {method} | network_url: {network_url} | network_log_id: {network_log_id}")
    if network_log_id is not None:
        url = f"http://127.0.0.1:8181/logs/entry?id={network_log_id}"
        response = requests.get(url)
        api_content = response.json().get("entry", {})
        if api_content != {}:
            queried_content = decode_body_payload(api_content)
            return queried_content

    while (queried_content is None and num_tries < max_polling_time / polling_interval):
        num_tries += 1
        print("polling network logs from server....")
        url = "http://127.0.0.1:8181/logs"
        response = requests.get(url)
        with open("response.json", "w") as f:
            json.dump(response.json(), f, indent=4)
        new_index = 0
        for entry in response.json()["log"]["entries"]:
            if entry["request"]["method"] == method and entry["request"]["url"] == network_url:
                new_index+=1
                if new_index == int(index):
                    queried_content = entry
                    break
        time.sleep(polling_interval)
    if queried_content is None:
        return ""
    else:
        new_network_log_id = queried_content.get("_id", "")
        print(f"new_network_log_id: {new_network_log_id}")
        start_time = time.time()
        api_entry = requests.get(f"http://127.0.0.1:8181/logs/entry?id={new_network_log_id}")
        queried_content = api_entry.json().get("entry", {})
        print(f"time taken to get entry from har logs file: {time.time() - start_time} seconds")
        if queried_content == {}:
            return ""

        queried_content = decode_body_payload(queried_content)
        return queried_content
    

def driver_query_script(driver: webdriver.Chrome, type: str, attributes: list, field: str, polling_interval: int = 2, max_polling_time: int = 10):
    print("polling interval in driver_query_script: ", polling_interval)
    print("max polling time in driver_query_script: ", max_polling_time)
    print("attributes in driver_query_script: ", attributes)
    try:
        if type == "cookie":
            queried_content = driver.get_cookies()

        elif type == "local_storage":
            queried_content = driver.execute_script("const items = {}; for (let i = 0; i < localStorage.length; i++) { const key = localStorage.key(i); items[key] = localStorage.getItem(key); } return items;")

        elif type == "session_storage":
            queried_content = driver.execute_script("const items = {}; for (let i = 0; i < sessionStorage.length; i++) { const key = sessionStorage.key(i); items[key] = sessionStorage.getItem(key); } return items;")
        
        elif type == "network_log":
            method = attributes[0]["method"]
            network_url = attributes[0]["url"]
            network_log_id = attributes[0].get("network_log_id", None)
            index = attributes[0]["index"]
            queried_content = None
            queried_content = poll_network_logs(method, network_url, index, polling_interval, max_polling_time, network_log_id)
            return queried_content

        for dict in attributes:
            for key, value in dict.items():
                if key == "index":
                    queried_content = queried_content[int(value)]
                else:
                    query_arr = value
                    if len(query_arr) == 1:
                        queried_content = queried_content.get(query_arr[0], '')
                    else:
                        queried_content = find_dict_with_kv(queried_content, query_arr[0], query_arr[1])
                        if queried_content is None:
                            raise ValueError(f"Key {query_arr[0]} with value {query_arr[1]} not found in queried content.")

        if field == "len":
            return len(queried_content)
        elif field == "keys":
            return list(queried_content.keys())
        elif field == "values":
            return list(queried_content.values())
        else:
            return queried_content

    except Exception as e:
        raise ValueError(f"Error in driver_query_script: {str(e)}")      

def execute_api_action(driver: webdriver.Chrome, operation_index: str):

    original_payload = operations_meta_data[operation_index]
    payload = original_payload.copy()
    payload["headers"] = replace_secrets_in_dict(payload.get("headers", {}))
    
    auth = payload.get("authorization", {})
    if isinstance(auth, dict) and auth and auth.get('data'):
        auth_data = replace_apivar(auth.get("data").copy())
        auth['data'] = auth_data
        payload["authorization"] = auth

    url, headers, body, params = replace_apivar({'url':payload["url"], 'headers':payload["headers"].copy(), 'body':payload["body"], 'params':payload["params"].copy()}).values()
    
    payload["url"]=url
    payload["headers"]=headers
    payload["body"]=body
    payload["params"]=params

    
    # execute via lambda hook
    args = {
            "command": "executeAPI",
            "testId":  driver.session_id,
            "payload": payload
        }
    response = driver.execute_script("lambda-kane-ai", args)
    
    return response

def update_global_variable(operation_index: int, value: str):
    is_global_variable = get_meta_data_value(operation_index).get("is_global_variable", False)
    is_global_variable_persist = get_meta_data_value(operation_index).get("is_global_variable_persist", False)
    global_variable_id = get_meta_data_value(operation_index).get("global_variable_id", None)
    test_variable = TestVariable(global_variables=global_variables)
    if is_global_variable and is_global_variable_persist:
        test_variable.update_variable_value(global_variable_id, str(value))
        print(f"Global variable updated with value {value}")
    elif is_global_variable and not is_global_variable_persist:
        test_variable.update_session_variable_value_by_id(global_variable_id, str(value))

def last_step_is_positional_li(xpath: str) -> bool:
    """
    Returns True only when the *last* node in `xpath`
    is a list item with a numeric index, e.g.

        //ul/li[3]        -> True
        //section/li[1]   -> True
        //ul/li           -> False   (no index)
        //ul/li[last()]   -> False   (non-numeric)
        //div[2]/li[4]/a  -> False   (last node is <a>)
    """
    if not xpath:
        return False

    # 1. Trim whitespace and any trailing slash (in case user wrote "…/")
    last_step = xpath.strip().rstrip("/").split("/")[-1]

    # 2. Test "li[N]" pattern
    return bool(_LI_NUMERIC_POS_RE.fullmatch(last_step))

def input_value(element, driver, operation_index, clicks_order_code, wait_for_element_timeout, coordinates=None):
    try:
        if coordinates is not None:
            x,y=canvas_autoheal_wrapper(operation_index,driver)
            actions = ActionBuilder(driver)
            actions.pointer_action.move_to_location(x, y)
            actions.pointer_action.click()
            actions.key_action.send_keys(" "+get_meta_data_value(operation_index).get('value', None))
            actions.perform()
        else:

            clear(driver, element, coordinates)
            click(element, driver, clicks_order_code, wait_for_element_timeout)
            wait = WebDriverWait(driver, 10)
            try:
                focused_element = wait.until(element_to_be_input_and_text())
                move_to_start_of_input(element,focused_element)
                if get_meta_data_value(operation_index).get("manual_interaction_tag", "") != "" and element.get_attribute("type") == "date":
                    driver.execute_script("arguments[0].value = arguments[1];", focused_element, get_meta_data_value(operation_index).get('value', ''))
                elif (MOBILE_TAGIFY_SCRIPT != None and element.get_attribute("maxlength") == "1") or (focused_element.get_attribute("pattern") and '[0-9]{2}' in focused_element.get_attribute("pattern")):
                    for char in get_meta_data_value(operation_index).get('value', ''):
                        focused_element.send_keys(char)
                        focused_element = wait.until(element_to_be_input_and_text())
                else:
                    
                    focused_element.send_keys(get_meta_data_value(operation_index).get('value', None))
            except Exception as e:
                print("Error sending keys to focused element. Falling back to js for send keys in input / type events: ", e.__str__())
                driver.execute_script("arguments[0].value = arguments[1];", element, get_meta_data_value(operation_index).get('value', ''))
                driver.execute_script("arguments[0].dispatchEvent(new Event('input', {bubbles: true}));", element)

        try:
            # need to check if the value entered is correct
            if element.get_attribute("value") and element.get_attribute("value") != "" and element.get_attribute("value") != get_meta_data_value(operation_index).get('value', None):
                print("value is not correct, clearing and sending chars one by one")
                print("value: ", element.get_attribute("value"))
                print("expected value: ", get_meta_data_value(operation_index).get('value', None))
                driver.execute_script("arguments[0].value = arguments[1];", element, "")
                for char in get_meta_data_value(operation_index).get('value', ''):
                    element.send_keys(char)
                    time.sleep(0.1)

        except Exception as e:
            print("Error in input_value: ", e.__str__())
            raise e

    except Exception as e:
        print("Error in input_value: ", e.__str__())
        raise e

def ui_action(driver: webdriver.Chrome, operation_index: int = 0):
    global operation_autoheal
    global TEST_STATUS
    global smart_variables_cache
    set_operation_autoheal(False)
    set_autoheal_frame_info("")
    set_autoheal_locators([])
    set_autoheal_latency(0)

    if NETWORK_WAIT_FOR_ALL_ACTIONS:
        smart_network_wait(driver=driver, start_timestamp=get_last_action_timestamp())
        
    max_retries = 4
    global operations_meta_data, CLICKS_ORDER_ALLOWED_VALUES
    action = get_meta_data_value(operation_index)['operation_type']
    locators = get_meta_data_value(operation_index).get('locator', None)
    frame_info = get_meta_data_value(operation_index).get('frame', None)
    selector = get_meta_data_value(operation_index).get('selector', None)
    user_vars_list = get_meta_data_value(operation_index).get('user_variables', '')
    clicks_order_code = get_meta_data_value(operation_index).get('clicks_order_code', "se_js_ac")
    if clicks_order_code not in CLICKS_ORDER_ALLOWED_VALUES:
        clicks_order_code = "se_js_ac"
    sub_instruction_obj = get_meta_data_value(operation_index).get('sub_instruction_obj', {})
    native_popups = get_meta_data_value(operation_index).get('native_popups', [])
    if native_popups != []:
        handle_mobile_native_popups(driver, popups=native_popups)

    if isinstance(sub_instruction_obj, str):
        sub_instruction_obj = json.loads(sub_instruction_obj)
        
    if user_vars_list != '':
        user_vars_list = json.loads(user_vars_list)
        
    if isinstance(sub_instruction_obj, dict):
        if 'params' in sub_instruction_obj:
            for key, value in sub_instruction_obj['params'].items():
                if not isinstance(value, str):
                    continue
                new_value = get_parameter_value(value, user_parameters)
                if new_value != value:
                    get_meta_data_value(operation_index)[key] = new_value
                    if 'variable' in sub_instruction_obj and key in sub_instruction_obj['variable']:
                        sub_instruction_obj['variable'][key] = new_value

        if 'variable' in sub_instruction_obj:
            for key, value in sub_instruction_obj['variable'].items():
                if not isinstance(value, str):
                    continue
                new_value = get_variable_value(value, user_variables)
                if new_value != value:
                    if "SCROLL" in  action:
                        get_meta_data_value(operation_index)["scroll_value"] = new_value
                    else:
                        get_meta_data_value(operation_index)[key] = new_value
    
    username = None
    access_key = None
    autohealed_selectors = ""

    if user_data:
        username = user_data.get('username')
        access_key = user_data.get('access_key')

    cordinates = None
    try:
        if locators is not None:
            if locators[0][0] == "[" and locators[0][-1] == "]":
                cordinates = locators[0]
            else:
                cordinates = None
    except Exception as e:
        cordinates = None
        print("Error in ui_action: ", e.__str__(), "locators: ", locators)

    if locators is not None and len(locators) > 0:
        if last_step_is_positional_li(locators[0]):
            update_meta_data(operation_index, {"unresolved": True})
    if (get_meta_data_value(operation_index).get("unresolved", False) or is_action_unresolved(action, sub_instruction_obj, operation_index)) and cordinates is None:
        if 'variable' in sub_instruction_obj and 'operation_intent' in sub_instruction_obj['variable']:
            get_meta_data_value(operation_index)['operation_intent'] = get_variable_value(sub_instruction_obj['variable']['operation_intent'], user_variables)
        if 'agent' in sub_instruction_obj:
            get_meta_data_value(operation_index)['agent'] = sub_instruction_obj['agent']
        print("Operation Intent: ", get_meta_data_value(operation_index)['operation_intent'])
        if cordinates is None:
            handle_unresolved_operations(operations_meta_data, operation_index, driver)
        selector = None

    locators = get_meta_data_value(operation_index).get('locator', None)
    frame_info = get_meta_data_value(operation_index).get('frame', None)
    wait_for_element_timeout = int(get_meta_data_value(operation_index).get('wait_for_element_timeout', 0))
    if wait_for_element_timeout == 0:
        wait_for_element_timeout = MAX_WAIT_UNTILTIME
    failure_condition = get_meta_data_value(operation_index).get('failure_condition', None)

    if get_meta_data_value(operation_index)['operation_type'].lower() not in ("js_dialog", "wait"):
        try:
            WebDriverWait(driver, 10).until(wait_for_dom)
        except Exception as e:
            print("failed to load dom within expected timeout")  

    if get_meta_data_value(operation_index)['operation_type'].lower() not in ("js_dialog", "switch_tab"):
        driver.switch_to.default_content()
          
    # check if get_meta_data_value(operation_index)['tag'] is valid double digit number
    try:
        if locators is not None:
            if locators[0][0] == "[" and locators[0][-1] == "]":
                cordinates = locators[0]
            else:
                cordinates = None
    except Exception as e:
        cordinates = None
        print("Error in ui_action: ", e.__str__())
    regex = None
    if 'regex_pattern' in get_meta_data_value(operation_index):
        regex_pattern = get_meta_data_value(operation_index)['regex_pattern']
        regex = base64.b64decode(regex_pattern).decode("utf-8")
    html = ""
    
    attempts = 1
    while attempts <= max_retries + 1:
        try:
            reset_implicit_wait = False

            if get_meta_data_value(operation_index).get('explicit_wait', 0):
                # WebDriverWait(driver, explicit_wait).until(EC.presence_of_element_located((By.XPATH, locator)))
                time.sleep(get_meta_data_value(operation_index)['explicit_wait'])

            if get_meta_data_value(operation_index)['implicit_wait'] != 0:
                driver.implicitly_wait(get_meta_data_value(operation_index)['implicit_wait'])
                reset_implicit_wait = True

            shadow = None
            host = None
            if frame_info and frame_info != "":
                frames = json.loads(frame_info)
                if selector and 'frameInfo' in selector and selector['frameInfo'] and len(selector['frameInfo']) > 0:
                    shadow, host = switch_to_content_by_selector(driver, selector['frameInfo'])
                else:
                    shadow = switch_to_frame(driver=driver, operation_index=operation_index, shadow=shadow, max_retries=max_retries, frame_info=frame_info)
                    if shadow == "unresolved":
                        raise Exception("Unable to resolve frameInformation")
            if selector and selector!="":
                locators = selector['locators']
                
            element_wheel_check = False
            if locators and cordinates is None:
                element = find_element(driver=driver, locators=locators, operation_idx=operation_index, shadow=shadow, host=host)
                if not element:
                    raise NoSuchElementException(f"Element not found for locator: {locators}")
                try:
                    element_wheel_check = True if all(event in driver.execute_script("return arguments[0].eventListenerList;", element) for event in ["wheel", "touchmove"]) else False
                except Exception as e:
                    pass
            else:
                element = None
            scroll_sleep_time = 1  
            time.sleep(0.2)

            if operation_autoheal and element and IS_WEBSOCKET_AVAILABLE:
                autohealed_selectors = driver.execute_script("return LT_KANE.LocatorBuilder.getAllLocatorsTagify(arguments[0])", element)
                print("AUTOHEALED SELECTORS -> -> ", autohealed_selectors)

            if action.lower() not in ["script", "api"]:
                set_last_action_timestamp(time.time() * 1000)
                
            if action.lower() == "textual_query":
                if element is not None:
                    selected_attribute_name = get_meta_data_value(operation_index).get('query_info_dict', {}).get('selected_attribute_name', None)
                    if selected_attribute_name is None:
                        raise Exception("Selected attribute name is not found in the query_info_dict")
                    query_response = populate_attributes(element, driver, selected_attribute_name)
                    print("unmodified query_response in query: ", query_response)
                    if element.tag_name == "img" or element.tag_name == "canvas":
                        use_prompt_query_response = True
                        return {}, query_response, use_prompt_query_response
                    else:
                        use_prompt_query_response = False
                    if selected_attribute_name in ["text", "value"]:
                        regex_pattern = get_meta_data_value(operation_index).get('regex_pattern', None)
                        if regex_pattern:
                            regex_pattern = base64.b64decode(regex_pattern).decode("utf-8")
                            print("Regex pattern in textual query: ", regex_pattern)
                            element_html = element.get_attribute("outerHTML")
                            query_response = re.findall(regex_pattern, element_html)
                            if len(query_response) > 0:
                                query_response = query_response[0]
                                update_global_variable(operation_index, query_response)
                            else:
                                query_response = ""
                                use_prompt_query_response = True
                    print("modified query_response in query: ", query_response)
                    return {}, query_response, use_prompt_query_response
                else:
                    return {}, None, True
                
            elif action.lower() == "mathematical_operation":
                get_meta_data_value(operation_index)["math_result_variable_name"] = eval_math(get_meta_data_value(operation_index)["expression_tree"], operation_index)
                print("mathematical operation result: ", get_meta_data_value(operation_index)["math_result_variable_name"], " : ", get_meta_data_value(operation_index)["math_result_variable_name"])
                return get_meta_data_value(operation_index)["math_result_variable_name"]
            
            elif action.lower() == "assertion":
                print("assertion_tree in ui_action: ", get_meta_data_value(operation_index)["assertion_tree"])
                assertion_value = evaluate_assertion(get_meta_data_value(operation_index)["assertion_tree"], operation_index)
                if not assertion_value and not IS_WEBSOCKET_AVAILABLE:
                    if failure_condition == FailureCondition.FAIL_TEST_IMMEDIATELY.value or failure_condition == FailureCondition.NONE.value:
                        raise RuntimeError(f"Assertion failed: '{get_meta_data_value(operation_index)['assertion_tree']}'")
                    elif failure_condition == FailureCondition.FAIL_BUT_CONTINUE_EXECUTING.value:
                        print(f"Assertion failed: '{get_meta_data_value(operation_index)['assertion_tree']}'")
                        set_test_status("failed")
                return assertion_value
            
            elif 'click' in action.lower():
                if get_meta_data_value(operation_index).get('mi_keypress_info', None) != None:
                    try:
                        value = json.loads(get_meta_data_value(operation_index)['mi_keypress_info'])
                    except:
                        pass
                    actions = ActionChains(driver)
                    for key_dict in value.get("true_keys", []):
                        key = list(key_dict.keys())[0].split("Key")[0].upper()
                        if key == "META":
                            key = "CONTROL"
                        actions.key_down(getattr(Keys, key))  # Press the key
                    actions.click(element)  # Perform the click action
                    for key_dict in value.get("true_keys", []):
                        key = list(key_dict.keys())[0].split("Key")[0].upper()
                        actions.key_up(getattr(Keys, key))  # Release the key
                    actions.perform()  # Execute the action chain
                else:
                    if cordinates is not None:
                        x,y=canvas_autoheal_wrapper(operation_index,driver)   
                        actions = ActionBuilder(driver)
                        actions.pointer_action.move_to_location(x, y)
                        actions.pointer_action.click()
                        actions.perform()

                    else:
                        click(element=element, driver=driver, clicks_order_code=clicks_order_code, max_wait_until_time=wait_for_element_timeout)

            elif action.lower() == 'hover':
                if cordinates is not None:
                    x,y=canvas_autoheal_wrapper(operation_index,driver)
                    actions = ActionBuilder(driver)
                    actions.pointer_action.move_to_location(x, y)
                    actions.perform()
                else:
                    ActionChains(driver).move_to_element(element).perform()

            elif action.lower() == 'type' or action.lower() == 'input':
                input_value(element, driver, operation_index, clicks_order_code, wait_for_element_timeout, cordinates)
            
            elif action.lower() == 'search':
  
                if frame_info and frame_info != "":
                    if cordinates is not None:
                        print("in canvas for else condition frame info")

                        x,y=canvas_autoheal_wrapper(operation_index,driver)
                        actions = ActionBuilder(driver)
                        actions.pointer_action.move_to_location(x, y)
                        actions.pointer_action.click()
                        actions.perform()  # Ensure click is executed before typing
                        to_type = get_meta_data_value(operation_index).get('value', None)
                        keyboard_actions = ActionBuilder(driver)
                        keyboard_actions.key_action.send_keys(to_type)
                        keyboard_actions.key_action.send_keys(Keys.RETURN)  # This simulates pressing Enter
                        keyboard_actions.perform()  # Execute the keyboard actions  
                    else:
                        click(element, driver, clicks_order_code, wait_for_element_timeout)
                    
                        driver.execute_script("arguments[0].value = '';", element)
                        element.send_keys(get_meta_data_value(operation_index).get('value', None))
                        element.send_keys(Keys.RETURN)
                else:
                    if cordinates is not None:
                        
                        x,y=canvas_autoheal_wrapper(operation_index,driver)
                        actions = ActionBuilder(driver)
                        actions.pointer_action.move_to_location(x, y)
                        actions.pointer_action.click()
                        actions.perform()  # Ensure click is executed before typing

                        # Get value to type
                        to_type = get_meta_data_value(operation_index).get('value', None)

                        keyboard_actions = ActionBuilder(driver)
                        keyboard_actions.key_action.send_keys(to_type)
                        keyboard_actions.key_action.send_keys(Keys.RETURN)  # This simulates pressing Enter
                        keyboard_actions.perform()  # Execute the keyboard actions  
                    else:
                        clear_element(driver=driver, element=element)
                        click(element, driver, clicks_order_code, wait_for_element_timeout)
                        wait = WebDriverWait(driver, 10)
                        focused_element = wait.until(element_to_be_input_and_text())
                        input_element = wait.until(EC.element_to_be_clickable(focused_element))
                        driver.execute_script("arguments[0].value = '';", input_element)
                        input_element.send_keys(get_meta_data_value(operation_index).get('value', None))
                        input_element.send_keys(Keys.RETURN)
            
            elif action.lower() == 'upload':
                value = get_meta_data_value(operation_index).get('value', None)
                file_path = get_downloads_file_path(value)
                element.send_keys(file_path)

            elif action.lower() == 'scroll_element_top_bottom':
                scroll_direction = get_meta_data_value(operation_index)['scroll_direction']
                scroll_values = {
                    'down':  ('deltaY', 1),
                    'up':    ('deltaY', -1),
                    'left':  ('deltaX', -1),
                    'right': ('deltaX', 1)
                }

                if element_wheel_check and scroll_direction in scroll_values:
                    axis, multiplier = scroll_values[scroll_direction]
                    dimension = 'scrollHeight' if axis == 'deltaY' else 'scrollWidth'
                    driver.execute_script(
                        f"let event = new WheelEvent('wheel', {{bubbles: true, cancelable: true, {axis}: {multiplier} * arguments[0].{dimension}}}); arguments[0].dispatchEvent(event);",
                        element
                    )
                elif scroll_direction in scroll_values:
                    _, multiplier = scroll_values[scroll_direction]
                    x = element.get_property('scrollWidth') if scroll_direction in ['left', 'right'] else 0
                    y = element.get_property('scrollHeight') if scroll_direction in ['up', 'down'] else 0
                    if multiplier < 0:
                        x = int(x) * multiplier
                        y = int(y) * multiplier
                    driver.execute_script("arguments[0].scrollBy(arguments[1], arguments[2]);", element, x, y)
                time.sleep(scroll_sleep_time)
                
            elif action.lower() == 'scroll_element_by_pixels' or action.lower() == 'scroll_element_pixels':
                scroll_value = int(get_meta_data_value(operation_index).get('scroll_value', 100))
                direction = get_meta_data_value(operation_index)['scroll_direction']
                is_wheel = element_wheel_check

                delta_map = {
                    'up': (0, -scroll_value),
                    'down': (0, scroll_value),
                    'left': (-scroll_value, 0),
                    'right': (scroll_value, 0)
                }

                deltaX, deltaY = delta_map.get(direction, (0, 0))

                if is_wheel:
                    driver.execute_script(
                        "let event = new WheelEvent('wheel', {bubbles: true, cancelable: true, deltaX: arguments[1], deltaY: arguments[2]}); arguments[0].dispatchEvent(event);",
                        element, deltaX, deltaY
                    )
                else:
                    driver.execute_script(
                        "arguments[0].scrollBy(arguments[1], arguments[2]);",
                        element, deltaX, deltaY
                    )
                time.sleep(scroll_sleep_time)
                
            elif action.lower() == 'scroll_element_by_percentage' or action.lower() == 'scroll_element_percentage':
                direction = get_meta_data_value(operation_index)['scroll_direction']
                value = int(get_meta_data_value(operation_index).get('scroll_value', 10)) / 100

                axis = 'Y' if direction in ['up', 'down'] else 'X'
                dim = 'Height' if axis == 'Y' else 'Width'
                sign = -1 if direction in ['up', 'left'] else 1

                total = driver.execute_script(f"return arguments[0].scroll{dim};", element)
                pixels = total * value * sign

                if element_wheel_check:
                    driver.execute_script(
                        f"arguments[0].dispatchEvent(new WheelEvent('wheel', {{bubbles: true, cancelable: true, delta{axis}: {pixels}}}));", element)
                else:
                    x = pixels if axis == 'X' else 0
                    y = pixels if axis == 'Y' else 0
                    driver.execute_script("arguments[0].scrollBy(arguments[1], arguments[2]);", element, x, y)
                time.sleep(scroll_sleep_time)

            elif action.lower() == 'scroll_element_by_times' or action.lower() == 'scroll_element_times':
                direction = get_meta_data_value(operation_index)['scroll_direction']
                multiplier = int(get_meta_data_value(operation_index).get('scroll_value', 1))
                axis = 'Y' if direction in ['up', 'down'] else 'X'
                sign = -1 if direction in ['up', 'left'] else 1
                dim = 'clientHeight' if axis == 'Y' else 'clientWidth'

                if element_wheel_check:
                    script = f"""
                        let amount = {sign} * {multiplier} * arguments[0].{dim};
                        let event = new WheelEvent('wheel', {{bubbles: true, cancelable: true, delta{axis}: amount}});
                        arguments[0].dispatchEvent(event);
                    """
                else:
                    script = f"""
                        let amount = {sign} * {multiplier} * arguments[0].{dim};
                        arguments[0].scrollBy({{'X': [amount, 0], 'Y': [0, amount]}}['{axis}'][0], {{'X': [amount, 0], 'Y': [0, amount]}}['{axis}'][1]);
                    """
                if element.tag_name.lower() != "body":
                    driver.execute_script(script, element)
                else:
                    driver.execute_script(f"""
                        let amount = {sign} * {multiplier} * document.documentElement.{dim};
                        window.scrollBy({{'X': [amount, 0], 'Y': [0, amount]}}['{axis}'][0], {{'X': [amount, 0], 'Y': [0, amount]}}['{axis}'][1]);
                    """)
                time.sleep(scroll_sleep_time)
                
            elif action.lower() == 'enter':
                element.send_keys(Keys.RETURN)

            elif action.lower() == 'clear':
                if cordinates is not None:
                    x,y=canvas_autoheal_wrapper(operation_index,driver)

                    # First action: move and click
                    click_action = ActionBuilder(driver)
                    click_action.pointer_action.move_to_location(x, y)
                    click_action.pointer_action.click()
                    click_action.perform()

                    # Second action: select all text
                    select_action = ActionBuilder(driver)
                    select_action.key_action.key_down(Keys.CONTROL)
                    select_action.key_action.send_keys("a")
                    select_action.key_action.key_up(Keys.CONTROL)
                    select_action.perform()

                    # Third action: delete the selected text
                    delete_action = ActionBuilder(driver)
                    delete_action.key_action.send_keys(Keys.DELETE)
                    delete_action.perform() 
                else:
                    clear_element(driver=driver, element=element)

            elif action.lower() == 'refresh':
                driver.refresh()

            elif action.lower() == 'open':
                try:
                    driver.get(get_meta_data_value(operation_index)['url'])
                except TimeoutException as e:
                    raise e

            elif action.lower() == 'scroll_top_bottom':
                if get_meta_data_value(operation_index)['scroll_direction'] == 'up':
                    driver.execute_script('window.scrollTo(0, -document.documentElement.scrollHeight)')
                elif get_meta_data_value(operation_index)['scroll_direction'] == 'down':
                    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')
                time.sleep(scroll_sleep_time)
                
            elif action.lower() == 'scroll_pixels':
                if get_meta_data_value(operation_index)['scroll_direction'] == 'up':
                    driver.execute_script(f"window.scrollBy(0, -{int(get_meta_data_value(operation_index)['scroll_value'])})")
                elif get_meta_data_value(operation_index)['scroll_direction'] == 'down':
                    driver.execute_script(f"window.scrollBy(0, {int(get_meta_data_value(operation_index)['scroll_value'])})")
                time.sleep(scroll_sleep_time)
                
            elif action.lower() == 'scroll_percentage':
                total_height = driver.execute_script("return document.body.scrollHeight")
                scroll_pixels = total_height * (int(get_meta_data_value(operation_index)['scroll_value']) / 100)
                if get_meta_data_value(operation_index)['scroll_direction'] == 'up':
                    driver.execute_script(f'window.scrollBy(0, -{scroll_pixels})')
                elif get_meta_data_value(operation_index)['scroll_direction'] == 'down':
                    driver.execute_script(f'window.scrollBy(0, {scroll_pixels})')
                time.sleep(scroll_sleep_time)
                
            elif action.lower() == 'scroll_times':
                if get_meta_data_value(operation_index)['scroll_direction'] == 'up':
                    driver.execute_script(f"scroll_height = {int(get_meta_data_value(operation_index)['scroll_value'])}*window.innerHeight; window.scrollBy(0, -scroll_height)")
                elif get_meta_data_value(operation_index)['scroll_direction'] == 'down':
                    driver.execute_script(f"scroll_height = {int(get_meta_data_value(operation_index)['scroll_value'])}*window.innerHeight; window.scrollBy(0, scroll_height)")
                time.sleep(scroll_sleep_time)
                
            elif action.lower() == 'navigate':
                if get_meta_data_value(operation_index)['navigation_direction'] == 'back':
                    driver.back()
                elif get_meta_data_value(operation_index)['navigation_direction'] == 'forward':
                    driver.forward()

            elif action.lower() == 'new_tab':
                if get_meta_data_value(operation_index).get('url', ''):
                    try:
                        driver.execute_script(f"window.open('{get_meta_data_value(operation_index)['url']}')")
                        driver.switch_to.window(driver.window_handles[-1])
                    except TimeoutException as e:
                        raise e
                else:
                    try:
                        driver.execute_script("window.open()")
                        driver.switch_to.window(driver.window_handles[-1])
                        driver.get("https://www.google.com")
                    except TimeoutException as e:
                        raise e

            elif action.lower() == 'wait':
                time.sleep(int(get_meta_data_value(operation_index)['value']))

            elif action.lower() == 'close_tab':
                driver.switch_to.window(driver.window_handles[get_meta_data_value(operation_index)['tab_index']])
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])

            elif action.lower() == 'switch_tab':
                driver.switch_to.window(driver.window_handles[get_meta_data_value(operation_index)['tab_index']])

            elif action.lower() == 'switch_frame':
                driver.switch_to.frame(element)

            elif action.lower() == 'switch_to_default_content':
                driver.switch_to.default_content()

            elif action.lower() == "scroll_to":
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                time.sleep(scroll_sleep_time)
                
            elif action.lower() == "scroll":
                try:
                    value = json.loads(get_meta_data_value(operation_index)['mi_scroll_info'])
                except:
                    pass
                for scroll_target, scroll_dict in value.items():
                    if scroll_target == "document":
                        window_scroll_script = f"window.scrollTo({value['document']['windowScrollX']}, {value['document']['windowScrollY']});"
                        driver.execute_script(window_scroll_script)
                    else:
                        element_scroll_script = f'"arguments[0].scrollLeft = {scroll_dict["scrollLeft"]}; arguments[0].scrollTop = {scroll_dict["scrollTop"]};", driver.find_element(By.XPATH, "{scroll_target}")'
                        driver.execute_script(element_scroll_script)
                time.sleep(scroll_sleep_time)
                
            elif action.lower() == "sendkeys":
                key = getattr(Keys, get_meta_data_value(operation_index)['key'].split(".")[1].upper())
                element.send_keys(key)

            elif action.lower() == "select":                            
                select_option(driver, element, get_meta_data_value(operation_index)['value'])

            elif action.lower() == "script":
                user_js_code = get_meta_data_value(operation_index)['js_snippet']
                user_js_code = replace_variables_in_script(user_js_code, user_variables)
                js_script_resp = execute_js(user_js_code=user_js_code, driver=driver)
                if "error" in js_script_resp and js_script_resp["error"] != "":
                    raise Exception(js_script_resp)
                if "value" in js_script_resp and js_script_resp["value"] != "null" and len(user_vars_list) > 0:
                    user_vars_list[0]["variable_value"] = js_script_resp["value"]
                    user_variables[user_vars_list[0]["name"]] = js_script_resp["value"]
                    update_global_variable(operation_index, js_script_resp["value"])
                
                return js_script_resp
            
            elif action.lower() == "api":

                if get_meta_data_value(operation_index).get("mobile_browser", False) == True:
                    response = execute_api_action(driver, operation_index)

                else:
                    method = get_meta_data_value(operation_index)["method"]
                    url = get_meta_data_value(operation_index)["url"]
                    headers = get_meta_data_value(operation_index)["headers"]
                    headers = replace_secrets_in_dict(headers)
                    body = get_meta_data_value(operation_index)["body"]
                    params = get_meta_data_value(operation_index)["params"]
                    timeout = (get_meta_data_value(operation_index).get("timeout", 6000))/1000
                    verify = get_meta_data_value(operation_index).get("verify", False)
                    settings = get_meta_data_value(operation_index).get("settings", {})
                    auth = get_meta_data_value(operation_index).get("authorization",{})
                    port = get_meta_data_value(operation_index).get("port", "22000")
                    host = get_meta_data_value(operation_index).get("host", "127.0.0.1")

                    if get_meta_data_value(operation_index).get("is_mobile"):
                        host = get_meta_data_value(operation_index).get("proxy_host", "127.0.0.1")
                        port = get_meta_data_value(operation_index).get("proxy_port", "22000")

                    if auth != {} and auth.get("data"):
                        auth_data = replace_apivar(auth.get("data").copy())
                        auth['data'] = auth_data
                        auth_params,auth_headers = get_effective_body_and_params(method=method,url=url,body=body,auth_payload=auth)
                        headers.update(replace_secrets_in_dict(auth_headers))
                        params.update(replace_secrets_in_dict(auth_params))
                        
                    response = asyncio.run(asyncio.to_thread(execute_api, driver, method, url, headers, body, params, timeout, verify, settings, host, port))
                if len(user_vars_list) > 0:
                    user_variables[user_vars_list[0]["name"]] = response
                if "body" in response:
                    del response["body"]
                return response
            
            elif action.lower() == "js_dialog" :
                alert = driver.switch_to.alert
                dialog_action = get_meta_data_value(operation_index).get('dialog_action', '')
                text = get_meta_data_value(operation_index).get('value', '')
                if dialog_action == "accept":
                    if text:
                        alert.send_keys(text)
                    alert.accept()
                    print("Alert accepted")         
                else:
                    alert.dismiss()

                time.sleep(3)  
                
            elif action.lower() == "set_variable":
                 if get_meta_data_value(operation_index).get("user_variables", "") != "":
                    user_vars_list = json.loads(get_meta_data_value(operation_index)["user_variables"])
                    variable_name = user_vars_list[0]["name"]
                    if get_meta_data_value(operation_index).get("variable_value", "") != "":
                        variable_value = get_meta_data_value(operation_index)["variable_value"]
                    else:
                        variable_value = user_vars_list[0]["value"]
                    user_variables[variable_name] = variable_value  

            elif action.lower() == "db_query":
                response = Heal(operation_idx = str(operation_index), driver = driver).db_query()
                user_variables[user_vars_list[0]["name"]] = response
            
            elif action.lower() == "scroll_until_element":
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                
            elif action.lower() == 'network_throttle':
                network_throttle_payload = get_meta_data_value(operation_index)["network_throttle"]

                if not network_throttle_payload:
                    raise ValueError("Network throttle payload is missing")
                
                is_mobile_offline = get_meta_data_value(operation_index).get("is_mobile_offline", False)

                execute_network_throttle(driver, is_mobile_offline = is_mobile_offline, network_throttle = network_throttle_payload)
            elif action.lower() == "generative":
                flow = GenerativeFlow(
                    server_url=os.environ.get('AUTOMIND_URL', user_data.get('automind_url', 'https://kaneai-api.lambdatest.com')), 
                    username=os.environ.get('LT_USERNAME', user_data.get('username', '')),
                    accesskey=os.environ.get('LT_ACCESS_KEY', user_data.get('access_key', '')),
                    driver=driver, 
                    request_id=get_meta_data_value(operation_index)['instruction_id']
                )
                flow.set_ui_auction_executor(ui_action)
                flow.set_operations_meta_data_executor(set_operations_meta_data)
                try:
                    # Run the complete automation loop
                    outcome = json.loads(get_meta_data_value(operation_index)['sub_instruction_obj']).get("outcome", "")
                    result = asyncio.run(flow.run_automation_loop(
                        objective=get_meta_data_value(operation_index)['operation_intent'],
                        expected_output=outcome,
                    ))
                except Exception as e:
                    raise e
                finally:
                    asyncio.run(flow.cleanup())
                    reload_metadata_root()
                    
            else:
                raise ValueError("Invalid action: {}".format(action))
            
            if reset_implicit_wait:
                driver.implicitly_wait(30)

            if operation_autoheal:
                if IS_WEBSOCKET_AVAILABLE:
                    update_autoheal_selector(driver, operation_index, autoheal_frame_info, autoheal_locators, autoheal_latency, True, autohealed_selectors)
                else:
                    try:
                        autoheal_logging(operation_index, autoheal_frame_info, autoheal_locators, autoheal_latency, True)
                    except Exception as e:
                        print("Error in autoheal_logging")
                        pass
            break
            
        except Exception as e:
            print(f'error: {traceback.format_exc()}')

            # remove this after confirming retries in js script error

            if operation_autoheal:
                if IS_WEBSOCKET_AVAILABLE:
                    update_autoheal_selector(driver, operation_index, autoheal_frame_info, autoheal_locators, autoheal_latency, False, autohealed_selectors)
                else:
                    try:
                        autoheal_logging(operation_index, autoheal_frame_info, autoheal_locators, autoheal_latency, False)
                    except Exception as e:
                        print("Error in autoheal_logging")

            if action.lower() == "script":
                raise e
            attempts += 1
            time.sleep(get_meta_data_value(operation_index)['retries_delay'])
            if attempts == max_retries + 1 and isinstance(e, TimeoutException):
                raise e
            if attempts == max_retries + 1 and not get_meta_data_value(operation_index)['optional_flag'] and not IS_WEBSOCKET_AVAILABLE:
                if failure_condition == FailureCondition.FAIL_BUT_CONTINUE_EXECUTING.value:
                    print(f"Failed to execute action: {action} on locator: {get_meta_data_value(operation_index)['locator']}. Error: {e}")
                    set_test_status("failed")
                    break
                elif failure_condition == FailureCondition.WARN_BUT_CONTINUE_EXECUTING.value:
                    print(f"Failed to execute action: {action} on locator: {get_meta_data_value(operation_index)['locator']}. Error: {e}")
                    break

            if attempts == max_retries + 1 and not get_meta_data_value(operation_index)['optional_flag']:
                raise RuntimeError(f"Failed to execute action: {action} on locator: {get_meta_data_value(operation_index)['locator']}. Error: {e}")            
            elif attempts == max_retries + 1 and get_meta_data_value(operation_index)['optional_flag']:
                print(f"Failed to execute action: {action} on locator: {get_meta_data_value(operation_index)['locator']}. Error: {e}")
                break
            if e.__str__() == "Element not found" or e.__str__() == "Outer HTML not found" or e.__str__().__contains__("no such element") or isinstance(e, NoSuchElementException):
                print(f"Element not found. Autohealing locators...")
                list_xpaths = retry(driver=driver, operation_idx=operation_index)
                locators = list_xpaths.get('xpaths')
                frame_info = list_xpaths.get('frameInformation', "")  
                if frame_info != "":
                    frame_info  = json.dumps(frame_info)
                selector = None
            elif e.__str__() == "Regex not found":
                print(f"Regex not found. Autohealing regex...")
                regex = heal_query(driver=driver, operation_index=operation_index, outer_html=html)
                set_operation_autoheal(True)
            elif e.__str__().__contains__("Selector Error") and attempts == 2:
                print(f"Selector Error. Autohealing selector...")
                print(f"Fallback to xpath")
                list_xpaths = retry(driver=driver, operation_idx=operation_index)
                locators = list_xpaths.get('xpaths', None)
                frame_info = list_xpaths.get('frameInformation', "")        
                if frame_info != "":
                    frame_info  = json.dumps(frame_info)
                selector = None
            print(f"Retrying due to Error: {str(e)[:50]}....")
        finally:
            smart_variables_cache = None