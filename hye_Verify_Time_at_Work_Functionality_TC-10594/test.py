
import time
import unittest
import os
import sys
from selenium import webdriver
from capability import get_capability
from UIActions import ui_action, lambda_hooks, vision_query, textual_query, perform_assertion, string_to_float, reload_metadata_root, user_variables, access_value, driver_query_script, get_test_status, SmartVariables
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

            # Click on 'Claim' menu item in the left side navigation panel 
            lambda_hooks(driver, "Click on 'Claim' menu item in the left side navigation panel ")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on the dropdown arrow next to user profile Pushpa Raj 
            lambda_hooks(driver, "Click on the dropdown arrow next to user profile Pushpa Raj ")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on 'Time at Work' section header 
            lambda_hooks(driver, "Click on 'Time at Work' section header ")
            ui_action(driver = driver, operation_index = str(4))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(5))

            # Click on the time at work timer input field 
            lambda_hooks(driver, "Click on the time at work timer input field ")
            ui_action(driver = driver, operation_index = str(6))

            # Type in time at work input field with placeholder 'Type for hints...' 'Ayush' 
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['7']['value']}")
            ui_action(driver = driver, operation_index = str(7))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(8))

            # Click 'Ayush Pathania' in dropdown list
            lambda_hooks(driver, "Click 'Ayush Pathania' in dropdown list")
            ui_action(driver = driver, operation_index = str(9))

            # Click 'View Button'
            lambda_hooks(driver, "Click 'View Button'")
            ui_action(driver = driver, operation_index = str(10))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(11))

            # Query 'No Records Found' visibility
            lambda_hooks(driver, "Query 'No Records Found' visibility")
            no_records_found_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(no_records_found_visible, dict):
                no_records_found_visible = no_records_found_visible.get("vision_query")
            user_variables["no_records_found_visible"] =  no_records_found_visible
            print("no_records_found_visible:", no_records_found_visible)

            # set the value of variable 'assertion_operand_342afd00256d4b9abcfb97a495fdc432_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_342afd00256d4b9abcfb97a495fdc432_0' to true")
            assertion_operand_342afd00256d4b9abcfb97a495fdc432_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Timesheet for Ayush Pathania'
            lambda_hooks(driver, "Query visibility of text 'Timesheet for Ayush Pathania'")
            Timesheet_for_Ayush_Pathania_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(Timesheet_for_Ayush_Pathania_visible, dict):
                Timesheet_for_Ayush_Pathania_visible = Timesheet_for_Ayush_Pathania_visible.get("vision_query")
            user_variables["Timesheet_for_Ayush_Pathania_visible"] =  Timesheet_for_Ayush_Pathania_visible
            print("Timesheet_for_Ayush_Pathania_visible:", Timesheet_for_Ayush_Pathania_visible)

            # set the value of variable 'assertion_operand_f6795209918644e18086a466e2386a8d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f6795209918644e18086a466e2386a8d_0' to true")
            assertion_operand_f6795209918644e18086a466e2386a8d_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Query 'No Timesheets Found' visibility
            lambda_hooks(driver, "Query 'No Timesheets Found' visibility")
            no_timesheets_found_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(no_timesheets_found_visible, dict):
                no_timesheets_found_visible = no_timesheets_found_visible.get("vision_query")
            user_variables["no_timesheets_found_visible"] =  no_timesheets_found_visible
            print("no_timesheets_found_visible:", no_timesheets_found_visible)

            # set the value of variable 'assertion_operand_b90211630d2d4552b0af2c369cfa8b95_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b90211630d2d4552b0af2c369cfa8b95_0' to true")
            assertion_operand_b90211630d2d4552b0af2c369cfa8b95_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
            print("assertion_result: ", assertion_result)

            # Query 'Timesheet Period' visibility
            lambda_hooks(driver, "Query 'Timesheet Period' visibility")
            Timesheet_Period_visible = vision_query(driver = driver, operation_index = str(21))
            if isinstance(Timesheet_Period_visible, dict):
                Timesheet_Period_visible = Timesheet_Period_visible.get("vision_query")
            user_variables["Timesheet_Period_visible"] =  Timesheet_Period_visible
            print("Timesheet_Period_visible:", Timesheet_Period_visible)

            # set the value of variable 'assertion_operand_6749a38e2b9646f49f1ebf46e02fa9f1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6749a38e2b9646f49f1ebf46e02fa9f1_0' to true")
            assertion_operand_6749a38e2b9646f49f1ebf46e02fa9f1_0 = "true"
            ui_action(driver = driver, operation_index = str(22))
            assertion_result = ui_action(driver=driver, operation_index=str(23))
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
