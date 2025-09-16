
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

            # Click on 'My Info' menu item in the left side menu
            lambda_hooks(driver, "Click on 'My Info' menu item in the left side menu")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Job' tab in the left side menu under 'My Info'
            lambda_hooks(driver, "Click on 'Job' tab in the left side menu under 'My Info'")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Query 'Job Details' visibility
            lambda_hooks(driver, "Query 'Job Details' visibility")
            Job_Details_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(Job_Details_visible, dict):
                Job_Details_visible = Job_Details_visible.get("vision_query")
            user_variables["Job_Details_visible"] =  Job_Details_visible
            print("Job_Details_visible:", Job_Details_visible)

            # set the value of variable 'assertion_operand_609c3530ba1744d09388dc2d3aa28523_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_609c3530ba1744d09388dc2d3aa28523_0' to true")
            assertion_operand_609c3530ba1744d09388dc2d3aa28523_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'Joined Date' visibility
            lambda_hooks(driver, "Query 'Joined Date' visibility")
            joined_date_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(joined_date_visible, dict):
                joined_date_visible = joined_date_visible.get("vision_query")
            user_variables["joined_date_visible"] =  joined_date_visible
            print("joined_date_visible:", joined_date_visible)

            # set the value of variable 'assertion_operand_eb707204cd48442e8af43ff48c33c23d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_eb707204cd48442e8af43ff48c33c23d_0' to true")
            assertion_operand_eb707204cd48442e8af43ff48c33c23d_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Job title' visibility
            lambda_hooks(driver, "Query 'Job title' visibility")
            Job_title_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Job_title_visible, dict):
                Job_title_visible = Job_title_visible.get("vision_query")
            user_variables["Job_title_visible"] =  Job_title_visible
            print("Job_title_visible:", Job_title_visible)

            # set the value of variable 'assertion_operand_7bbac0cf54404038aa06455d3300222f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7bbac0cf54404038aa06455d3300222f_0' to true")
            assertion_operand_7bbac0cf54404038aa06455d3300222f_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Job Specification' visibility
            lambda_hooks(driver, "Query 'Job Specification' visibility")
            Job_Specification_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Job_Specification_visible, dict):
                Job_Specification_visible = Job_Specification_visible.get("vision_query")
            user_variables["Job_Specification_visible"] =  Job_Specification_visible
            print("Job_Specification_visible:", Job_Specification_visible)

            # set the value of variable 'assertion_operand_332508ce1fa8405fbb5ab64384a53e15_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_332508ce1fa8405fbb5ab64384a53e15_0' to true")
            assertion_operand_332508ce1fa8405fbb5ab64384a53e15_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Job Category' visibility
            lambda_hooks(driver, "Query 'Job Category' visibility")
            Job_Category_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Job_Category_visible, dict):
                Job_Category_visible = Job_Category_visible.get("vision_query")
            user_variables["Job_Category_visible"] =  Job_Category_visible
            print("Job_Category_visible:", Job_Category_visible)

            # set the value of variable 'assertion_operand_7880779ca36d4518b93ef60f2ab3e02e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7880779ca36d4518b93ef60f2ab3e02e_0' to true")
            assertion_operand_7880779ca36d4518b93ef60f2ab3e02e_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Sub unit' visibility
            lambda_hooks(driver, "Query 'Sub unit' visibility")
            Sub_unit_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Sub_unit_visible, dict):
                Sub_unit_visible = Sub_unit_visible.get("vision_query")
            user_variables["Sub_unit_visible"] =  Sub_unit_visible
            print("Sub_unit_visible:", Sub_unit_visible)

            # set the value of variable 'assertion_operand_7c49bb73422d4f129b0c7e45e068920a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7c49bb73422d4f129b0c7e45e068920a_0' to true")
            assertion_operand_7c49bb73422d4f129b0c7e45e068920a_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'Location' visibility
            lambda_hooks(driver, "Query 'Location' visibility")
            Location_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(Location_visible, dict):
                Location_visible = Location_visible.get("vision_query")
            user_variables["Location_visible"] =  Location_visible
            print("Location_visible:", Location_visible)

            # set the value of variable 'assertion_operand_ef51f3e23a2e4902b7ac738a44326aa8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ef51f3e23a2e4902b7ac738a44326aa8_0' to true")
            assertion_operand_ef51f3e23a2e4902b7ac738a44326aa8_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Query 'Employment Status' visibility
            lambda_hooks(driver, "Query 'Employment Status' visibility")
            Employment_Status_visible = vision_query(driver = driver, operation_index = str(25))
            if isinstance(Employment_Status_visible, dict):
                Employment_Status_visible = Employment_Status_visible.get("vision_query")
            user_variables["Employment_Status_visible"] =  Employment_Status_visible
            print("Employment_Status_visible:", Employment_Status_visible)

            # set the value of variable 'assertion_operand_2a74a8ed8ee84900b742d36333a71029_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2a74a8ed8ee84900b742d36333a71029_0' to true")
            assertion_operand_2a74a8ed8ee84900b742d36333a71029_0 = "true"
            ui_action(driver = driver, operation_index = str(26))
            assertion_result = ui_action(driver=driver, operation_index=str(27))
            print("assertion_result: ", assertion_result)

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            current_url = response = driver.current_url
            user_variables["current_url"] =  current_url
            print("current_url:", current_url)

            # set the value of variable 'assertion_operand_5d19813d7b444ee4a93369bc3851b759_0' to viewjobDetails
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5d19813d7b444ee4a93369bc3851b759_0' to viewjobDetails")
            assertion_operand_5d19813d7b444ee4a93369bc3851b759_0 = "viewjobDetails"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
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
