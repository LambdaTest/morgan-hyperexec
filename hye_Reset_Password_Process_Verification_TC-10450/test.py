
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

            # Click on the user dropdown with name Pushpa Raj in top right corner
            lambda_hooks(driver, "Click on the user dropdown with name Pushpa Raj in top right corner")
            ui_action(driver = driver, operation_index = str(0))

            # Click on the Logout link in user dropdown
            lambda_hooks(driver, "Click on the Logout link in user dropdown")
            ui_action(driver = driver, operation_index = str(1))

            # Click on the 'Forgot your password?' link
            lambda_hooks(driver, "Click on the 'Forgot your password?' link")
            ui_action(driver = driver, operation_index = str(2))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Query 'Reset Password' text visibility
            lambda_hooks(driver, "Query 'Reset Password' text visibility")
            reset_password_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(reset_password_visible, dict):
                reset_password_visible = reset_password_visible.get("vision_query")
            user_variables["reset_password_visible"] =  reset_password_visible
            print("reset_password_visible:", reset_password_visible)

            # set the value of variable 'assertion_operand_edbff23379664802b015a5a57364108a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_edbff23379664802b015a5a57364108a_0' to true")
            assertion_operand_edbff23379664802b015a5a57364108a_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query visibility of the specified error message text
            lambda_hooks(driver, "Query visibility of the specified error message text")
            error_message_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(error_message_visible, dict):
                error_message_visible = error_message_visible.get("vision_query")
            user_variables["error_message_visible"] =  error_message_visible
            print("error_message_visible:", error_message_visible)

            # set the value of variable 'assertion_operand_6586196126564153a08706e83966d906_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6586196126564153a08706e83966d906_0' to true")
            assertion_operand_6586196126564153a08706e83966d906_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Click 'Click here' link
            lambda_hooks(driver, "Click 'Click here' link")
            ui_action(driver = driver, operation_index = str(10))

            # Query 'Username' text visibility
            lambda_hooks(driver, "Query 'Username' text visibility")
            Username_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Username_visible, dict):
                Username_visible = Username_visible.get("vision_query")
            user_variables["Username_visible"] =  Username_visible
            print("Username_visible:", Username_visible)

            # set the value of variable 'assertion_operand_1272f69f8b02404f837dc1db8d94c7ab_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1272f69f8b02404f837dc1db8d94c7ab_0' to true")
            assertion_operand_1272f69f8b02404f837dc1db8d94c7ab_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
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
