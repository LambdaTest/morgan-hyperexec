
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

            # Click on 'Maintenance' menu item in left sidebar 
            lambda_hooks(driver, "Click on 'Maintenance' menu item in left sidebar ")
            ui_action(driver = driver, operation_index = str(0))

            # wait 5 seconds
            lambda_hooks(driver, "wait 5 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # type ******************* in Password input field
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['2']['value']}")
            ui_action(driver = driver, operation_index = str(2))

            # Click 'Conform' button
            lambda_hooks(driver, "Click 'Conform' button")
            ui_action(driver = driver, operation_index = str(3))

            # wait 5 seconds
            lambda_hooks(driver, "wait 5 seconds")
            ui_action(driver = driver, operation_index = str(4))

            # Click on past employee input field with placeholder 'Type for hints...' 
            lambda_hooks(driver, "Click on past employee input field with placeholder 'Type for hints...' ")
            ui_action(driver = driver, operation_index = str(5))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(6))

            # Click on 'Access Records' tab in the top nav bar 
            lambda_hooks(driver, "Click on 'Access Records' tab in the top nav bar ")
            ui_action(driver = driver, operation_index = str(7))

            # Click on employee name input field with placeholder 'Type for hints...' 
            lambda_hooks(driver, "Click on employee name input field with placeholder 'Type for hints...' ")
            ui_action(driver = driver, operation_index = str(8))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(9))

            # Type in employee name input field with placeholder 'Type for hints...' 'ayush' 
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['10']['value']}")
            ui_action(driver = driver, operation_index = str(10))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(11))

            # Click 'Ayush Pathania' in dropdown list
            lambda_hooks(driver, "Click 'Ayush Pathania' in dropdown list")
            ui_action(driver = driver, operation_index = str(12))

            # Click on the green Search button in Download Personal Data section 
            lambda_hooks(driver, "Click on the green Search button in Download Personal Data section ")
            ui_action(driver = driver, operation_index = str(13))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(14))

            # Query text '0007' visibility
            lambda_hooks(driver, "Query text '0007' visibility")
            text_0007_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(text_0007_visible, dict):
                text_0007_visible = text_0007_visible.get("vision_query")
            user_variables["text_0007_visible"] =  text_0007_visible
            print("text_0007_visible:", text_0007_visible)

            # set the value of variable 'assertion_operand_fa56d590d8be489c9458e56c7a32378d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_fa56d590d8be489c9458e56c7a32378d_0' to true")
            assertion_operand_fa56d590d8be489c9458e56c7a32378d_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Query 'Employee Id' visibility
            lambda_hooks(driver, "Query 'Employee Id' visibility")
            Employee_Id_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(Employee_Id_visible, dict):
                Employee_Id_visible = Employee_Id_visible.get("vision_query")
            user_variables["Employee_Id_visible"] =  Employee_Id_visible
            print("Employee_Id_visible:", Employee_Id_visible)

            # set the value of variable 'assertion_operand_d9d4185a926d4957b6a8bc3f466c76fe_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d9d4185a926d4957b6a8bc3f466c76fe_0' to true")
            assertion_operand_d9d4185a926d4957b6a8bc3f466c76fe_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
            print("assertion_result: ", assertion_result)

            # Query 'Employee Full Name' visibility
            lambda_hooks(driver, "Query 'Employee Full Name' visibility")
            Employee_Full_Name_visible = vision_query(driver = driver, operation_index = str(21))
            if isinstance(Employee_Full_Name_visible, dict):
                Employee_Full_Name_visible = Employee_Full_Name_visible.get("vision_query")
            user_variables["Employee_Full_Name_visible"] =  Employee_Full_Name_visible
            print("Employee_Full_Name_visible:", Employee_Full_Name_visible)

            # set the value of variable 'assertion_operand_3cbbcda34fb340a09a8809ce3ac4c27c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3cbbcda34fb340a09a8809ce3ac4c27c_0' to true")
            assertion_operand_3cbbcda34fb340a09a8809ce3ac4c27c_0 = "true"
            ui_action(driver = driver, operation_index = str(22))
            assertion_result = ui_action(driver=driver, operation_index=str(23))
            print("assertion_result: ", assertion_result)

            # Query 'Download' text visibility
            lambda_hooks(driver, "Query 'Download' text visibility")
            Download_visible = vision_query(driver = driver, operation_index = str(24))
            if isinstance(Download_visible, dict):
                Download_visible = Download_visible.get("vision_query")
            user_variables["Download_visible"] =  Download_visible
            print("Download_visible:", Download_visible)

            # set the value of variable 'assertion_operand_e98e9555aa624678b173d190c25e339f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e98e9555aa624678b173d190c25e339f_0' to true")
            assertion_operand_e98e9555aa624678b173d190c25e339f_0 = "true"
            ui_action(driver = driver, operation_index = str(25))
            assertion_result = ui_action(driver=driver, operation_index=str(26))
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
