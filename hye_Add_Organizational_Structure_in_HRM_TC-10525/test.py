
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

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click 'Organization' dropdown
            lambda_hooks(driver, "Click 'Organization' dropdown")
            ui_action(driver = driver, operation_index = str(2))

            # Click 'Structure'
            lambda_hooks(driver, "Click 'Structure'")
            ui_action(driver = driver, operation_index = str(3))

            # Click 'Edit'
            lambda_hooks(driver, "Click 'Edit'")
            ui_action(driver = driver, operation_index = str(4))

            # Query '+ADD' button visibility
            lambda_hooks(driver, "Query '+ADD' button visibility")
            add_button_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(add_button_visible, dict):
                add_button_visible = add_button_visible.get("vision_query")
            user_variables["add_button_visible"] =  add_button_visible
            print("add_button_visible:", add_button_visible)

            # set the value of variable 'assertion_operand_ab2a34bb000b4ae4903d52a3b532db77_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ab2a34bb000b4ae4903d52a3b532db77_0' to true")
            assertion_operand_ab2a34bb000b4ae4903d52a3b532db77_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Click '+Add' button
            lambda_hooks(driver, "Click '+Add' button")
            ui_action(driver = driver, operation_index = str(8))

            # Click 'Save' button
            lambda_hooks(driver, "Click 'Save' button")
            ui_action(driver = driver, operation_index = str(9))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_f292bbdcdb2146b29bfc979e294e2ff9_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f292bbdcdb2146b29bfc979e294e2ff9_0' to true")
            assertion_operand_f292bbdcdb2146b29bfc979e294e2ff9_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(13))

            # Click 'Edit' link
            lambda_hooks(driver, "Click 'Edit' link")
            ui_action(driver = driver, operation_index = str(14))

            # Query '+ADD' button visibility
            lambda_hooks(driver, "Query '+ADD' button visibility")
            add_button_visible_a1e8a6 = vision_query(driver = driver, operation_index = str(15))
            if isinstance(add_button_visible_a1e8a6, dict):
                add_button_visible_a1e8a6 = add_button_visible_a1e8a6.get("vision_query")
            user_variables["add_button_visible_a1e8a6"] =  add_button_visible_a1e8a6
            print("add_button_visible_a1e8a6:", add_button_visible_a1e8a6)

            # set the value of variable 'assertion_operand_9b9386abb9124f7290cf4b5dbf205654_0' to false
            lambda_hooks(driver, "set the value of variable 'assertion_operand_9b9386abb9124f7290cf4b5dbf205654_0' to false")
            assertion_operand_9b9386abb9124f7290cf4b5dbf205654_0 = "false"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
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
