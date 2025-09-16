
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

            # Click on 'Performance' menu item in left sidebar
            lambda_hooks(driver, "Click on 'Performance' menu item in left sidebar")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Configure' dropdown in top left next to 'Manage Reviews'
            lambda_hooks(driver, "Click on 'Configure' dropdown in top left next to 'Manage Reviews'")
            ui_action(driver = driver, operation_index = str(2))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on 'Trackers' menu item in Manage Reviews dropdown
            lambda_hooks(driver, "Click on 'Trackers' menu item in Manage Reviews dropdown")
            ui_action(driver = driver, operation_index = str(4))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(5))

            # Click on the green Add button below Performance Trackers
            lambda_hooks(driver, "Click on the green Add button below Performance Trackers")
            ui_action(driver = driver, operation_index = str(6))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(7))

            # Query 'Tracker Name' visibility
            lambda_hooks(driver, "Query 'Tracker Name' visibility")
            Tracker_Name_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Tracker_Name_visible, dict):
                Tracker_Name_visible = Tracker_Name_visible.get("vision_query")
            user_variables["Tracker_Name_visible"] =  Tracker_Name_visible
            print("Tracker_Name_visible:", Tracker_Name_visible)

            # set the value of variable 'assertion_operand_92299edbbd914246895912824dc61f25_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_92299edbbd914246895912824dc61f25_0' to true")
            assertion_operand_92299edbbd914246895912824dc61f25_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Add Performance Tracker' visibility
            lambda_hooks(driver, "Query 'Add Performance Tracker' visibility")
            add_performance_tracker_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(add_performance_tracker_visible, dict):
                add_performance_tracker_visible = add_performance_tracker_visible.get("vision_query")
            user_variables["add_performance_tracker_visible"] =  add_performance_tracker_visible
            print("add_performance_tracker_visible:", add_performance_tracker_visible)

            # set the value of variable 'assertion_operand_1cb5cae27fce42dd9d434c5367967d38_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1cb5cae27fce42dd9d434c5367967d38_0' to true")
            assertion_operand_1cb5cae27fce42dd9d434c5367967d38_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query 'Employee Name' visibility
            lambda_hooks(driver, "Query 'Employee Name' visibility")
            Employee_Name_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(Employee_Name_visible, dict):
                Employee_Name_visible = Employee_Name_visible.get("vision_query")
            user_variables["Employee_Name_visible"] =  Employee_Name_visible
            print("Employee_Name_visible:", Employee_Name_visible)

            # set the value of variable 'assertion_operand_d3f30e1456ed4b7fb7ebd5295f564ab3_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d3f30e1456ed4b7fb7ebd5295f564ab3_0' to true")
            assertion_operand_d3f30e1456ed4b7fb7ebd5295f564ab3_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'Reviewers' text visibility
            lambda_hooks(driver, "Query 'Reviewers' text visibility")
            Reviewers_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(Reviewers_visible, dict):
                Reviewers_visible = Reviewers_visible.get("vision_query")
            user_variables["Reviewers_visible"] =  Reviewers_visible
            print("Reviewers_visible:", Reviewers_visible)

            # set the value of variable 'assertion_operand_356af24bfa1a48608f4132a2dbdc884f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_356af24bfa1a48608f4132a2dbdc884f_0' to true")
            assertion_operand_356af24bfa1a48608f4132a2dbdc884f_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
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
