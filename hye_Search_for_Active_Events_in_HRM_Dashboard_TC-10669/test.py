
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

            # Click on 'Claim' menu item in left side menu 
            lambda_hooks(driver, "Click on 'Claim' menu item in left side menu ")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Configuration' tab in top navigation bar 
            lambda_hooks(driver, "Click on 'Configuration' tab in top navigation bar ")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on 'Events' tab in top navigation bar 
            lambda_hooks(driver, "Click on 'Events' tab in top navigation bar ")
            ui_action(driver = driver, operation_index = str(4))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(5))

            # Click on the punch out timer button in the Time at Work section 
            lambda_hooks(driver, "Click on the punch out timer button in the Time at Work section ")
            ui_action(driver = driver, operation_index = str(6))

            # Type in search input with placeholder 'Type for hints...' 'active' 
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['7']['value']}")
            ui_action(driver = driver, operation_index = str(7))

            # Click on the dashboard quick launch dropdown 
            lambda_hooks(driver, "Click on the dashboard quick launch dropdown ")
            ui_action(driver = driver, operation_index = str(8))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(9))

            # Click on the Search button in orangehrm-left-space 
            lambda_hooks(driver, "Click on the Search button in orangehrm-left-space ")
            ui_action(driver = driver, operation_index = str(10))

            # Query text '(2) Records Found' visibility
            lambda_hooks(driver, "Query text '(2) Records Found' visibility")
            records_found_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(records_found_visible, dict):
                records_found_visible = records_found_visible.get("vision_query")
            user_variables["records_found_visible"] =  records_found_visible
            print("records_found_visible:", records_found_visible)

            # set the value of variable 'assertion_operand_f965b563c26d49b18bd8d4de9582ac85_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f965b563c26d49b18bd8d4de9582ac85_0' to true")
            assertion_operand_f965b563c26d49b18bd8d4de9582ac85_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query 'Active Event' visibility
            lambda_hooks(driver, "Query 'Active Event' visibility")
            Active_Event_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(Active_Event_visible, dict):
                Active_Event_visible = Active_Event_visible.get("vision_query")
            user_variables["Active_Event_visible"] =  Active_Event_visible
            print("Active_Event_visible:", Active_Event_visible)

            # set the value of variable 'assertion_operand_16240e977fac41f28e0367cfcd76aa3d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_16240e977fac41f28e0367cfcd76aa3d_0' to true")
            assertion_operand_16240e977fac41f28e0367cfcd76aa3d_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'Inactive' text visibility
            lambda_hooks(driver, "Query 'Inactive' text visibility")
            Inactive_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(Inactive_visible, dict):
                Inactive_visible = Inactive_visible.get("vision_query")
            user_variables["Inactive_visible"] =  Inactive_visible
            print("Inactive_visible:", Inactive_visible)

            # set the value of variable 'assertion_operand_40f09c7f90cc4891af913a9a80288570_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_40f09c7f90cc4891af913a9a80288570_0' to true")
            assertion_operand_40f09c7f90cc4891af913a9a80288570_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'Active Event name' visibility
            lambda_hooks(driver, "Query 'Active Event name' visibility")
            active_event_name_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(active_event_name_visible, dict):
                active_event_name_visible = active_event_name_visible.get("vision_query")
            user_variables["active_event_name_visible"] =  active_event_name_visible
            print("active_event_name_visible:", active_event_name_visible)

            # set the value of variable 'assertion_operand_2ca53f43ac1b4d86ad07c5f9677a22c1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2ca53f43ac1b4d86ad07c5f9677a22c1_0' to true")
            assertion_operand_2ca53f43ac1b4d86ad07c5f9677a22c1_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Query 'Inactive Event name' visibility
            lambda_hooks(driver, "Query 'Inactive Event name' visibility")
            inactive_event_name_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(inactive_event_name_visible, dict):
                inactive_event_name_visible = inactive_event_name_visible.get("vision_query")
            user_variables["inactive_event_name_visible"] =  inactive_event_name_visible
            print("inactive_event_name_visible:", inactive_event_name_visible)

            # set the value of variable 'assertion_operand_2ce5d4642e094841b473d5c7e56ad02a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2ce5d4642e094841b473d5c7e56ad02a_0' to true")
            assertion_operand_2ce5d4642e094841b473d5c7e56ad02a_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
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
