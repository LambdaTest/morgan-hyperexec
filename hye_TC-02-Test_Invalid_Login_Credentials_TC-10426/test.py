
import time
import unittest
import os
import sys
from selenium import webdriver
from capability import get_capability
from UIActions import ui_action, lambda_hooks, vision_query, perform_assertion, string_to_float, reload_metadata_root, user_variables, access_value, driver_query_script, get_test_status, SmartVariables
import UIActions
from lambdatest_selenium_driver import smartui_snapshot


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


            # navigate to 'https://orange-hrm.lambdatestinternal.com/orangehrm-5.7' website
            lambda_hooks(driver, f"open url {UIActions.operations_meta_data['0']['url']}")
            ui_action(driver = driver, operation_index = str(0))

            # Query 'Username input box' visibility
            lambda_hooks(driver, "Query 'Username input box' visibility")
            Username_input_box_visible = vision_query(driver = driver, operation_index = str(1))
            if isinstance(Username_input_box_visible, dict):
                Username_input_box_visible = Username_input_box_visible.get("vision_query")
            user_variables["Username_input_box_visible"] =  Username_input_box_visible
            print("Username_input_box_visible:", Username_input_box_visible)

            # set the value of variable 'assertion_operand_a9f7fcb3c9014017ac2400b2adbbf5c8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a9f7fcb3c9014017ac2400b2adbbf5c8_0' to true")
            assertion_operand_a9f7fcb3c9014017ac2400b2adbbf5c8_0 = "true"
            ui_action(driver = driver, operation_index = str(2))
            assertion_result = ui_action(driver=driver, operation_index=str(3))
            print("assertion_result: ", assertion_result)

            # type 'pushpa.raj' in Username
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['4']['value']}")
            ui_action(driver = driver, operation_index = str(4))

            # type ********* in Password input field
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['5']['value']}")
            ui_action(driver = driver, operation_index = str(5))

            # Click 'Login'
            lambda_hooks(driver, "Click 'Login'")
            ui_action(driver = driver, operation_index = str(6))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(7))

            # Query 'Invalid credentials' text visibility
            lambda_hooks(driver, "Query 'Invalid credentials' text visibility")
            invalid_credentials_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(invalid_credentials_visible, dict):
                invalid_credentials_visible = invalid_credentials_visible.get("vision_query")
            user_variables["invalid_credentials_visible"] =  invalid_credentials_visible
            print("invalid_credentials_visible:", invalid_credentials_visible)

            # set the value of variable 'assertion_operand_6f455e46dd414af69d5162624caffae4_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6f455e46dd414af69d5162624caffae4_0' to true")
            assertion_operand_6f455e46dd414af69d5162624caffae4_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
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
