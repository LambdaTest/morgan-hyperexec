
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

            # Click 'Qualification' dropdown
            lambda_hooks(driver, "Click 'Qualification' dropdown")
            ui_action(driver = driver, operation_index = str(2))

            # Click 'skills' dropdown
            lambda_hooks(driver, "Click 'skills' dropdown")
            ui_action(driver = driver, operation_index = str(3))

            # Click '+Add' button
            lambda_hooks(driver, "Click '+Add' button")
            ui_action(driver = driver, operation_index = str(4))

            # type 'abc' in name
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['5']['value']}")
            ui_action(driver = driver, operation_index = str(5))

            # Click 'Save' button
            lambda_hooks(driver, "Click 'Save' button")
            ui_action(driver = driver, operation_index = str(6))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(7))

            # Query if 'abc' text is displayed on viewport
            lambda_hooks(driver, "Query if 'abc' text is displayed on viewport")
            abc_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(abc_visible, dict):
                abc_visible = abc_visible.get("vision_query")
            user_variables["abc_visible"] =  abc_visible
            print("abc_visible:", abc_visible)

            # set the value of variable 'assertion_operand_3f474e5590ac48f8929ac69a530a4ee7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3f474e5590ac48f8929ac69a530a4ee7_0' to true")
            assertion_operand_3f474e5590ac48f8929ac69a530a4ee7_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Click 'Delete' icon
            lambda_hooks(driver, "Click 'Delete' icon")
            ui_action(driver = driver, operation_index = str(11))

            # Click 'Yes,Delete' button
            lambda_hooks(driver, "Click 'Yes,Delete' button")
            ui_action(driver = driver, operation_index = str(12))

            # wait 5 seconds
            lambda_hooks(driver, "wait 5 seconds")
            ui_action(driver = driver, operation_index = str(13))

            # Query 'abc' text visibility
            lambda_hooks(driver, "Query 'abc' text visibility")
            abc_visible_c06dfa = vision_query(driver = driver, operation_index = str(14))
            if isinstance(abc_visible_c06dfa, dict):
                abc_visible_c06dfa = abc_visible_c06dfa.get("vision_query")
            user_variables["abc_visible_c06dfa"] =  abc_visible_c06dfa
            print("abc_visible_c06dfa:", abc_visible_c06dfa)

            # set the value of variable 'assertion_operand_ceb8c7f23c484fb6afe57142049e2ef3_0' to false
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ceb8c7f23c484fb6afe57142049e2ef3_0' to false")
            assertion_operand_ceb8c7f23c484fb6afe57142049e2ef3_0 = "false"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
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
