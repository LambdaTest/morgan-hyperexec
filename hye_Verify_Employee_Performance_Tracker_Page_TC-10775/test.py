
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

            # Click on 'Employee Trackers' tab in the top nav bar
            lambda_hooks(driver, "Click on 'Employee Trackers' tab in the top nav bar")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            current_url = response = driver.current_url
            user_variables["current_url"] =  current_url
            print("current_url:", current_url)

            # set the value of variable 'assertion_operand_cd8d41bafb6647be8d3cbcc425d737bd_0' to viewEmployeePerformanceTrackerList
            lambda_hooks(driver, "set the value of variable 'assertion_operand_cd8d41bafb6647be8d3cbcc425d737bd_0' to viewEmployeePerformanceTrackerList")
            assertion_operand_cd8d41bafb6647be8d3cbcc425d737bd_0 = "viewEmployeePerformanceTrackerList"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'Employee Performance Tracker' visibility
            lambda_hooks(driver, "Query 'Employee Performance Tracker' visibility")
            Employee_Performance_Tracker_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(Employee_Performance_Tracker_visible, dict):
                Employee_Performance_Tracker_visible = Employee_Performance_Tracker_visible.get("vision_query")
            user_variables["Employee_Performance_Tracker_visible"] =  Employee_Performance_Tracker_visible
            print("Employee_Performance_Tracker_visible:", Employee_Performance_Tracker_visible)

            # set the value of variable 'assertion_operand_b48ebd068b704c6fae2b6657053a110a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b48ebd068b704c6fae2b6657053a110a_0' to true")
            assertion_operand_b48ebd068b704c6fae2b6657053a110a_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Employee Name' visibility
            lambda_hooks(driver, "Query 'Employee Name' visibility")
            Employee_Name_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Employee_Name_visible, dict):
                Employee_Name_visible = Employee_Name_visible.get("vision_query")
            user_variables["Employee_Name_visible"] =  Employee_Name_visible
            print("Employee_Name_visible:", Employee_Name_visible)

            # set the value of variable 'assertion_operand_8e7be80f5a4e4ebd84050e374222379e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8e7be80f5a4e4ebd84050e374222379e_0' to true")
            assertion_operand_8e7be80f5a4e4ebd84050e374222379e_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Include' text visibility
            lambda_hooks(driver, "Query 'Include' text visibility")
            Include_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Include_visible, dict):
                Include_visible = Include_visible.get("vision_query")
            user_variables["Include_visible"] =  Include_visible
            print("Include_visible:", Include_visible)

            # set the value of variable 'assertion_operand_dade373a813f4671946a0e7c5e4373f4_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_dade373a813f4671946a0e7c5e4373f4_0' to true")
            assertion_operand_dade373a813f4671946a0e7c5e4373f4_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Reset' text visibility
            lambda_hooks(driver, "Query 'Reset' text visibility")
            Reset_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Reset_visible, dict):
                Reset_visible = Reset_visible.get("vision_query")
            user_variables["Reset_visible"] =  Reset_visible
            print("Reset_visible:", Reset_visible)

            # set the value of variable 'assertion_operand_8d98c07eabc24118846bff1c43d61031_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8d98c07eabc24118846bff1c43d61031_0' to true")
            assertion_operand_8d98c07eabc24118846bff1c43d61031_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Search' visibility
            lambda_hooks(driver, "Query 'Search' visibility")
            Search_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Search_visible, dict):
                Search_visible = Search_visible.get("vision_query")
            user_variables["Search_visible"] =  Search_visible
            print("Search_visible:", Search_visible)

            # set the value of variable 'assertion_operand_999045adf77b4b0db733c8f64aed29b1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_999045adf77b4b0db733c8f64aed29b1_0' to true")
            assertion_operand_999045adf77b4b0db733c8f64aed29b1_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'No Records Found' visibility
            lambda_hooks(driver, "Query 'No Records Found' visibility")
            no_records_found_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(no_records_found_visible, dict):
                no_records_found_visible = no_records_found_visible.get("vision_query")
            user_variables["no_records_found_visible"] =  no_records_found_visible
            print("no_records_found_visible:", no_records_found_visible)

            # set the value of variable 'assertion_operand_08a361e46ff347d9bc84d33e5d23efb1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_08a361e46ff347d9bc84d33e5d23efb1_0' to true")
            assertion_operand_08a361e46ff347d9bc84d33e5d23efb1_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Query 'Employee Name' visibility
            lambda_hooks(driver, "Query 'Employee Name' visibility")
            Employee_Name_visible_ccb576 = vision_query(driver = driver, operation_index = str(25))
            if isinstance(Employee_Name_visible_ccb576, dict):
                Employee_Name_visible_ccb576 = Employee_Name_visible_ccb576.get("vision_query")
            user_variables["Employee_Name_visible_ccb576"] =  Employee_Name_visible_ccb576
            print("Employee_Name_visible_ccb576:", Employee_Name_visible_ccb576)

            # set the value of variable 'assertion_operand_3059e998ecf14629b77b6736e992ed82_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3059e998ecf14629b77b6736e992ed82_0' to true")
            assertion_operand_3059e998ecf14629b77b6736e992ed82_0 = "true"
            ui_action(driver = driver, operation_index = str(26))
            assertion_result = ui_action(driver=driver, operation_index=str(27))
            print("assertion_result: ", assertion_result)

            # Query 'Tracker' visibility
            lambda_hooks(driver, "Query 'Tracker' visibility")
            Tracker_visible = vision_query(driver = driver, operation_index = str(28))
            if isinstance(Tracker_visible, dict):
                Tracker_visible = Tracker_visible.get("vision_query")
            user_variables["Tracker_visible"] =  Tracker_visible
            print("Tracker_visible:", Tracker_visible)

            # set the value of variable 'assertion_operand_9297041e34244dcbaaba098002d4bff8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_9297041e34244dcbaaba098002d4bff8_0' to true")
            assertion_operand_9297041e34244dcbaaba098002d4bff8_0 = "true"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
            print("assertion_result: ", assertion_result)

            # Query 'Added Date' text visibility
            lambda_hooks(driver, "Query 'Added Date' text visibility")
            added_date_visible = vision_query(driver = driver, operation_index = str(31))
            if isinstance(added_date_visible, dict):
                added_date_visible = added_date_visible.get("vision_query")
            user_variables["added_date_visible"] =  added_date_visible
            print("added_date_visible:", added_date_visible)

            # set the value of variable 'assertion_operand_0954b117d2af4a4396366dbac9db33c5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0954b117d2af4a4396366dbac9db33c5_0' to true")
            assertion_operand_0954b117d2af4a4396366dbac9db33c5_0 = "true"
            ui_action(driver = driver, operation_index = str(32))
            assertion_result = ui_action(driver=driver, operation_index=str(33))
            print("assertion_result: ", assertion_result)

            # Query 'Modified Date' text visibility
            lambda_hooks(driver, "Query 'Modified Date' text visibility")
            Modified_Date_visible = vision_query(driver = driver, operation_index = str(34))
            if isinstance(Modified_Date_visible, dict):
                Modified_Date_visible = Modified_Date_visible.get("vision_query")
            user_variables["Modified_Date_visible"] =  Modified_Date_visible
            print("Modified_Date_visible:", Modified_Date_visible)

            # set the value of variable 'assertion_operand_68fdab5a049d435a986abddc26c9e4a2_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_68fdab5a049d435a986abddc26c9e4a2_0' to true")
            assertion_operand_68fdab5a049d435a986abddc26c9e4a2_0 = "true"
            ui_action(driver = driver, operation_index = str(35))
            assertion_result = ui_action(driver=driver, operation_index=str(36))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible = vision_query(driver = driver, operation_index = str(37))
            if isinstance(Actions_visible, dict):
                Actions_visible = Actions_visible.get("vision_query")
            user_variables["Actions_visible"] =  Actions_visible
            print("Actions_visible:", Actions_visible)

            # set the value of variable 'assertion_operand_845ef07854c3453f916e10e1620f19cf_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_845ef07854c3453f916e10e1620f19cf_0' to true")
            assertion_operand_845ef07854c3453f916e10e1620f19cf_0 = "true"
            ui_action(driver = driver, operation_index = str(38))
            assertion_result = ui_action(driver=driver, operation_index=str(39))
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
