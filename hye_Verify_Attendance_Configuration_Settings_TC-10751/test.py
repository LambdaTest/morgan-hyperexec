
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

            # Click 'Time'
            lambda_hooks(driver, "Click 'Time'")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click 'Attendance' dropdown
            lambda_hooks(driver, "Click 'Attendance' dropdown")
            ui_action(driver = driver, operation_index = str(2))

            # Click 'Configuration'
            lambda_hooks(driver, "Click 'Configuration'")
            ui_action(driver = driver, operation_index = str(3))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(4))

            # Query 'Save' button visibility
            lambda_hooks(driver, "Query 'Save' button visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_163da5e0c5554b04ac03beba1e1464b4_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_163da5e0c5554b04ac03beba1e1464b4_0' to true")
            assertion_operand_163da5e0c5554b04ac03beba1e1464b4_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query if 'Employee can change current time when punching in/out' text is visible
            lambda_hooks(driver, "Query if 'Employee can change current time when punching in/out' text is visible")
            employee_time_change_text_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(employee_time_change_text_visible, dict):
                employee_time_change_text_visible = employee_time_change_text_visible.get("vision_query")
            user_variables["employee_time_change_text_visible"] =  employee_time_change_text_visible
            print("employee_time_change_text_visible:", employee_time_change_text_visible)

            # set the value of variable 'assertion_operand_34fc66f48ed14b7e94eece3bfe7a2821_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_34fc66f48ed14b7e94eece3bfe7a2821_0' to true")
            assertion_operand_34fc66f48ed14b7e94eece3bfe7a2821_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query if 'Employee can edit/delete own attendance records' text is visible
            lambda_hooks(driver, "Query if 'Employee can edit/delete own attendance records' text is visible")
            employee_edit_delete_attendance_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(employee_edit_delete_attendance_visible, dict):
                employee_edit_delete_attendance_visible = employee_edit_delete_attendance_visible.get("vision_query")
            user_variables["employee_edit_delete_attendance_visible"] =  employee_edit_delete_attendance_visible
            print("employee_edit_delete_attendance_visible:", employee_edit_delete_attendance_visible)

            # set the value of variable 'assertion_operand_5e9022feb6f24568ba13c050f7ab170e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5e9022feb6f24568ba13c050f7ab170e_0' to true")
            assertion_operand_5e9022feb6f24568ba13c050f7ab170e_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query if 'Supervisor can add/edit/delete attendance records of subordinates' text is visible
            lambda_hooks(driver, "Query if 'Supervisor can add/edit/delete attendance records of subordinates' text is visible")
            supervisor_text_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(supervisor_text_visible, dict):
                supervisor_text_visible = supervisor_text_visible.get("vision_query")
            user_variables["supervisor_text_visible"] =  supervisor_text_visible
            print("supervisor_text_visible:", supervisor_text_visible)

            # set the value of variable 'assertion_operand_0aa59c422acc493392232c7d75801dbf_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0aa59c422acc493392232c7d75801dbf_0' to true")
            assertion_operand_0aa59c422acc493392232c7d75801dbf_0 = "true"
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
