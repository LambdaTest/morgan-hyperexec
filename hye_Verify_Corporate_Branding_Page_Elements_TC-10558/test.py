
import time
import unittest
import os
import sys
from selenium import webdriver
from capability import get_capability
from UIActions import ui_action, lambda_hooks, vision_query, perform_assertion, string_to_float, reload_metadata_root, user_variables, access_value, driver_query_script, get_test_status, SmartVariables
import UIActions
from lambdatest_selenium_driver import smartui_snapshot
from orangehrm_login_module_1_1 import orangehrm_login_module_1_1


username = os.getenv("LT_USERNAME")
access_key = os.getenv("LT_ACCESS_KEY")
plan = os.getenv("PLAN", False)
hub = os.getenv("HYE_HUB")
browser = sys.argv[1] if len(sys.argv) > 1 else "chrome"
browser_version = sys.argv[2] if len(sys.argv) > 2 else "latest"
resolution = sys.argv[3] if len(sys.argv) > 3 else "1920x1080"
platform = sys.argv[4] if len(sys.argv) > 4 else "linux"
extension_path = sys.argv[5] if len(sys.argv) > 5 else "/home/ltuser/foreman/ltuser/dom-watcher.crx"
sys.argv = [sys.argv[0]]

options = get_capability(browser, browser_version, resolution, platform, username, access_key, extension_path)

class FirstSampleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@{}/wd/hub".format(
                username, access_key, hub
            ),
            options=options,
        )
        
        if browser.lower() == "firefox":
            webdriver.Firefox.install_addon(self.driver, path=extension_path, temporary=True)
            print("Firefox Setup Successful")
    

    def test_demo_site(self):
        status = "failed"
        driver = self.driver
        smart = SmartVariables()

        try:
            driver.implicitly_wait(15)
            driver.set_page_load_timeout(180)
            driver.set_script_timeout(120)
            if not plan:
                driver.set_window_size(1512, 982)
            reload_metadata_root()


            # MODULE_CALL
            reload_metadata_root("410579e1-c957-41d9-b25c-91ac8457c707_0")
            orangehrm_login_module_1_1(driver)

            reload_metadata_root()

            # Click 'Admin'
            lambda_hooks(driver, "Click 'Admin'")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click 'Corporate Branding'
            lambda_hooks(driver, "Click 'Corporate Branding'")
            ui_action(driver = driver, operation_index = str(2))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            url = response = driver.current_url
            user_variables["url"] =  url
            print("url:", url)

            # set the value of variable 'assertion_operand_71167d37de4e4c0997c6f00d1fe2cd7d_0' to addTheme
            lambda_hooks(driver, "set the value of variable 'assertion_operand_71167d37de4e4c0997c6f00d1fe2cd7d_0' to addTheme")
            assertion_operand_71167d37de4e4c0997c6f00d1fe2cd7d_0 = "addTheme"
            ui_action(driver = driver, operation_index = str(4))
            assertion_result = ui_action(driver=driver, operation_index=str(5))
            print("assertion_result: ", assertion_result)

            # Query 'Primary Color' text visibility
            lambda_hooks(driver, "Query 'Primary Color' text visibility")
            Primary_Color_visible = vision_query(driver = driver, operation_index = str(6))
            if isinstance(Primary_Color_visible, dict):
                Primary_Color_visible = Primary_Color_visible.get("vision_query")
            user_variables["Primary_Color_visible"] =  Primary_Color_visible
            print("Primary_Color_visible:", Primary_Color_visible)

            # set the value of variable 'assertion_operand_ac630c0770e844ddbf39806cf32da6e0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ac630c0770e844ddbf39806cf32da6e0_0' to true")
            assertion_operand_ac630c0770e844ddbf39806cf32da6e0_0 = "true"
            ui_action(driver = driver, operation_index = str(7))
            assertion_result = ui_action(driver=driver, operation_index=str(8))
            print("assertion_result: ", assertion_result)

            # Query 'Client Logo' visibility
            lambda_hooks(driver, "Query 'Client Logo' visibility")
            Client_Logo_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(Client_Logo_visible, dict):
                Client_Logo_visible = Client_Logo_visible.get("vision_query")
            user_variables["Client_Logo_visible"] =  Client_Logo_visible
            print("Client_Logo_visible:", Client_Logo_visible)

            # set the value of variable 'assertion_operand_9bfbf9165a1e4eeab82bbeaac3e26981_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_9bfbf9165a1e4eeab82bbeaac3e26981_0' to true")
            assertion_operand_9bfbf9165a1e4eeab82bbeaac3e26981_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Query 'Logo Banner' visibility
            lambda_hooks(driver, "Query 'Logo Banner' visibility")
            Logo_Banner_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Logo_Banner_visible, dict):
                Logo_Banner_visible = Logo_Banner_visible.get("vision_query")
            user_variables["Logo_Banner_visible"] =  Logo_Banner_visible
            print("Logo_Banner_visible:", Logo_Banner_visible)

            # set the value of variable 'assertion_operand_58131ddedc7643dfa24181935f829d7d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_58131ddedc7643dfa24181935f829d7d_0' to true")
            assertion_operand_58131ddedc7643dfa24181935f829d7d_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query 'Client Banner' visibility
            lambda_hooks(driver, "Query 'Client Banner' visibility")
            Client_Banner_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(Client_Banner_visible, dict):
                Client_Banner_visible = Client_Banner_visible.get("vision_query")
            user_variables["Client_Banner_visible"] =  Client_Banner_visible
            print("Client_Banner_visible:", Client_Banner_visible)

            # set the value of variable 'assertion_operand_7abd411a919c42de82357661076b7abc_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7abd411a919c42de82357661076b7abc_0' to true")
            assertion_operand_7abd411a919c42de82357661076b7abc_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Query if 'Browse' text is visible
            lambda_hooks(driver, "Query if 'Browse' text is visible")
            browse_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(browse_visible, dict):
                browse_visible = browse_visible.get("vision_query")
            user_variables["browse_visible"] =  browse_visible
            print("browse_visible:", browse_visible)

            # set the value of variable 'assertion_operand_ebb9877f089d4c90b0ce12303c600136_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ebb9877f089d4c90b0ce12303c600136_0' to true")
            assertion_operand_ebb9877f089d4c90b0ce12303c600136_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
            print("assertion_result: ", assertion_result)

            status = get_test_status()

        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            # Update the status at the end
            if driver is not None:
                driver.execute_script(f"lambda-status={status}")

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
