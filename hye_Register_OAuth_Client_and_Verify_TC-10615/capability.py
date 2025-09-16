
import os
from selenium import webdriver
from UIActions import get_download_folder, root_meta_data

def get_env_bool(key: str, default: bool) -> bool:
    value = os.getenv(key, str(default)).lower()
    return value == "true"

def get_capability(browser, browser_version, resolution, platform, username, access_key, extension_path):
    if browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("devtools.console.stdout.content", True)
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        options.set_preference("dom.webnotifications.enabled", False)
        capabilities = webdriver.DesiredCapabilities.FIREFOX
        capabilities['moz:firefoxOptions'] = {'log': {'level': 'trace'}}
        options.set_preference("signon.rememberSignons", False)  
        options.set_preference("signon.autofillForms", False)    
        options.set_preference("permissions.default.desktop-notification", 2)

    elif browser.lower() == "edge":
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        options.add_argument('--enable-logging')
        options.add_argument('--log-level=0')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False, "profile.default_content_setting_values.notifications": 2, "safebrowsing.enabled": False, "profile.password_manager_leak_detection": False, "signin.allowed_on_next_startup": False}
        options.add_experimental_option("prefs", prefs)
        options.add_extension(extension_path)
        print("Edge Setup Successful")

    elif browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        chrome_options = root_meta_data.get("chrome_options", [])
        for op in chrome_options:
            op_key = op.get("key", "")
            op_type = op.get("type", "")
            if op_type == "file": 
                op_value = os.path.join(get_download_folder(), op.get("value", "")) 
            else: 
                op_value = op.get("value", "")
            if op_type == "no-args":
                options.add_argument(f"{op_key}")
            else:
                options.add_argument(f"{op_key}={op_value}")
        options.add_argument('--enable-logging')
        options.add_argument("--no-sandbox")
        options.add_argument('--log-level=0')
        options.add_argument("ignore-certificate-errors")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False, "profile.default_content_setting_values.notifications": 2, "safebrowsing.enabled": False, "profile.password_manager_leak_detection": False, "signin.allowed_on_next_startup": False}
        options.add_experimental_option("prefs", prefs)
        options.add_extension(extension_path)
        print("Chrome Setup Successful")

    elif browser.lower() == "safari":
        options = webdriver.SafariOptions()
        print("Safari Setup Successful")

    lt_options = {
        "browserName": browser,
        "browserVersion": browser_version,
        "platform": platform,
        "username": username,
        "accessKey": access_key,
        "resolution": resolution,
        "project": "Auteur-Code-Export",
        "w3c": True,
        "plugin": "python-python",
        "tms.tc_id": "TC-10615",
        "name": "Register_OAuth_Client_and_Verify",
        "build": os.getenv("BUILD", "5ea05496-0599-4708-9e54-103183fe433d"),
        "console": os.getenv("CONSOLE", "true"),
        "network": get_env_bool("NETWORK", False),
        "network.full.har": get_env_bool("NETWORK", False),
        "video": get_env_bool("VIDEO", True),
        "visual": get_env_bool("VISUAL", True),
        "tunnel": get_env_bool("TUNNEL", False),
        "performance": get_env_bool("PERFORMANCE", False),
        "dedicatedProxy": get_env_bool("DEDICATED_PROXY", False),
        "idleTimeout": int(os.getenv("IDLE_TIMEOUT", 1800)),
        "accessibility": os.getenv("ACCESSIBILITY", False),
        "hideInternalCommandLogs": True
    }

    if os.getenv("GEO_LOCATION", False):
        lt_options["geoLocation"] = os.getenv("GEO_LOCATION")
    
    custom_headers = root_meta_data.get("custom_headers", {})
    if custom_headers:
        lt_options["customHeaders"] = custom_headers

    options.set_capability("LT:Options", lt_options)

    return options
