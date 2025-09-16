
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

            # Click 'Timesheet' dropdown
            lambda_hooks(driver, "Click 'Timesheet' dropdown")
            ui_action(driver = driver, operation_index = str(2))

            # Click 'My Timesheet'
            lambda_hooks(driver, "Click 'My Timesheet'")
            ui_action(driver = driver, operation_index = str(3))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(4))

            # Query 'My Timesheet' text visibility
            lambda_hooks(driver, "Query 'My Timesheet' text visibility")
            my_timesheet_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(my_timesheet_visible, dict):
                my_timesheet_visible = my_timesheet_visible.get("vision_query")
            user_variables["my_timesheet_visible"] =  my_timesheet_visible
            print("my_timesheet_visible:", my_timesheet_visible)

            # set the value of variable 'assertion_operand_6129ff6f1ed14cc498db210d3188a954_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6129ff6f1ed14cc498db210d3188a954_0' to true")
            assertion_operand_6129ff6f1ed14cc498db210d3188a954_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query if 'Status: Not Submitted' text is visible
            lambda_hooks(driver, "Query if 'Status: Not Submitted' text is visible")
            status_not_submitted_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(status_not_submitted_visible, dict):
                status_not_submitted_visible = status_not_submitted_visible.get("vision_query")
            user_variables["status_not_submitted_visible"] =  status_not_submitted_visible
            print("status_not_submitted_visible:", status_not_submitted_visible)

            # set the value of variable 'assertion_operand_e61fe4793c6946899c4f21f09eefbc15_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e61fe4793c6946899c4f21f09eefbc15_0' to true")
            assertion_operand_e61fe4793c6946899c4f21f09eefbc15_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Click 'Edit' button
            lambda_hooks(driver, "Click 'Edit' button")
            ui_action(driver = driver, operation_index = str(11))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(12))

            # Query 'Edit Timesheet' text visibility
            lambda_hooks(driver, "Query 'Edit Timesheet' text visibility")
            edit_timesheet_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(edit_timesheet_visible, dict):
                edit_timesheet_visible = edit_timesheet_visible.get("vision_query")
            user_variables["edit_timesheet_visible"] =  edit_timesheet_visible
            print("edit_timesheet_visible:", edit_timesheet_visible)

            # set the value of variable 'assertion_operand_77ad9875029f407e82f11e64363fe45b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_77ad9875029f407e82f11e64363fe45b_0' to true")
            assertion_operand_77ad9875029f407e82f11e64363fe45b_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Click 'Add Row' button
            lambda_hooks(driver, "Click 'Add Row' button")
            ui_action(driver = driver, operation_index = str(16))

            # Click 'Delete' icon
            lambda_hooks(driver, "Click 'Delete' icon")
            ui_action(driver = driver, operation_index = str(17))

            # Click 'Delete' icon
            lambda_hooks(driver, "Click 'Delete' icon")
            ui_action(driver = driver, operation_index = str(18))

            # Click 'save' button
            lambda_hooks(driver, "Click 'save' button")
            ui_action(driver = driver, operation_index = str(19))

            # Query 'Select a Project' text visibility
            lambda_hooks(driver, "Query 'Select a Project' text visibility")
            select_a_project_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(select_a_project_visible, dict):
                select_a_project_visible = select_a_project_visible.get("vision_query")
            user_variables["select_a_project_visible"] =  select_a_project_visible
            print("select_a_project_visible:", select_a_project_visible)

            # set the value of variable 'assertion_operand_2f106e198c0c484aa92c37b21e7a7ee6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2f106e198c0c484aa92c37b21e7a7ee6_0' to true")
            assertion_operand_2f106e198c0c484aa92c37b21e7a7ee6_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Query if 'Select an Activity' text is visible
            lambda_hooks(driver, "Query if 'Select an Activity' text is visible")
            select_an_activity_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(select_an_activity_visible, dict):
                select_an_activity_visible = select_an_activity_visible.get("vision_query")
            user_variables["select_an_activity_visible"] =  select_an_activity_visible
            print("select_an_activity_visible:", select_an_activity_visible)

            # set the value of variable 'assertion_operand_b5bd38eb672f4e32859dcd37055fc2bc_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b5bd38eb672f4e32859dcd37055fc2bc_0' to true")
            assertion_operand_b5bd38eb672f4e32859dcd37055fc2bc_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
            print("assertion_result: ", assertion_result)

            # Click 'Reset' button
            lambda_hooks(driver, "Click 'Reset' button")
            ui_action(driver = driver, operation_index = str(26))

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
