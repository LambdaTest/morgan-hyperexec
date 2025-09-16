
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

            # Click on 'Manage Reviews' tab in the top nav bar
            lambda_hooks(driver, "Click on 'Manage Reviews' tab in the top nav bar")
            ui_action(driver = driver, operation_index = str(2))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on 'Manage Reviews' option in the dropdown below 'Manage Reviews' tab
            lambda_hooks(driver, "Click on 'Manage Reviews' option in the dropdown below 'Manage Reviews' tab")
            ui_action(driver = driver, operation_index = str(4))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(5))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            current_url = response = driver.current_url
            user_variables["current_url"] =  current_url
            print("current_url:", current_url)

            # set the value of variable 'assertion_operand_455aa89406474e9b954e082db28c9558_0' to searchPerformanceReview
            lambda_hooks(driver, "set the value of variable 'assertion_operand_455aa89406474e9b954e082db28c9558_0' to searchPerformanceReview")
            assertion_operand_455aa89406474e9b954e082db28c9558_0 = "searchPerformanceReview"
            ui_action(driver = driver, operation_index = str(7))
            assertion_result = ui_action(driver=driver, operation_index=str(8))
            print("assertion_result: ", assertion_result)

            # Query 'Manage Performance Reviews' visibility
            lambda_hooks(driver, "Query 'Manage Performance Reviews' visibility")
            Manage_Performance_Reviews_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(Manage_Performance_Reviews_visible, dict):
                Manage_Performance_Reviews_visible = Manage_Performance_Reviews_visible.get("vision_query")
            user_variables["Manage_Performance_Reviews_visible"] =  Manage_Performance_Reviews_visible
            print("Manage_Performance_Reviews_visible:", Manage_Performance_Reviews_visible)

            # set the value of variable 'assertion_operand_5469c1e443a74fa1a36df6e224d4708a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5469c1e443a74fa1a36df6e224d4708a_0' to true")
            assertion_operand_5469c1e443a74fa1a36df6e224d4708a_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Query 'Employee Name' visibility
            lambda_hooks(driver, "Query 'Employee Name' visibility")
            Employee_Name_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Employee_Name_visible, dict):
                Employee_Name_visible = Employee_Name_visible.get("vision_query")
            user_variables["Employee_Name_visible"] =  Employee_Name_visible
            print("Employee_Name_visible:", Employee_Name_visible)

            # set the value of variable 'assertion_operand_44aeece3bbe24dbba7504bcb6fabbf38_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_44aeece3bbe24dbba7504bcb6fabbf38_0' to true")
            assertion_operand_44aeece3bbe24dbba7504bcb6fabbf38_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query 'Job Title' visibility
            lambda_hooks(driver, "Query 'Job Title' visibility")
            Job_Title_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(Job_Title_visible, dict):
                Job_Title_visible = Job_Title_visible.get("vision_query")
            user_variables["Job_Title_visible"] =  Job_Title_visible
            print("Job_Title_visible:", Job_Title_visible)

            # set the value of variable 'assertion_operand_d4d20bef2ec74911aec1fc0457353f4c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d4d20bef2ec74911aec1fc0457353f4c_0' to true")
            assertion_operand_d4d20bef2ec74911aec1fc0457353f4c_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Query 'Review Status' visibility
            lambda_hooks(driver, "Query 'Review Status' visibility")
            Review_Status_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(Review_Status_visible, dict):
                Review_Status_visible = Review_Status_visible.get("vision_query")
            user_variables["Review_Status_visible"] =  Review_Status_visible
            print("Review_Status_visible:", Review_Status_visible)

            # set the value of variable 'assertion_operand_f185dacbc89540f1ac0b9f1f0f1c14f8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f185dacbc89540f1ac0b9f1f0f1c14f8_0' to true")
            assertion_operand_f185dacbc89540f1ac0b9f1f0f1c14f8_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
            print("assertion_result: ", assertion_result)

            # Query 'Include' text visibility
            lambda_hooks(driver, "Query 'Include' text visibility")
            Include_visible = vision_query(driver = driver, operation_index = str(21))
            if isinstance(Include_visible, dict):
                Include_visible = Include_visible.get("vision_query")
            user_variables["Include_visible"] =  Include_visible
            print("Include_visible:", Include_visible)

            # set the value of variable 'assertion_operand_8a632282bdd945baa015b25311623261_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8a632282bdd945baa015b25311623261_0' to true")
            assertion_operand_8a632282bdd945baa015b25311623261_0 = "true"
            ui_action(driver = driver, operation_index = str(22))
            assertion_result = ui_action(driver=driver, operation_index=str(23))
            print("assertion_result: ", assertion_result)

            # Query 'Reviewer' text visibility
            lambda_hooks(driver, "Query 'Reviewer' text visibility")
            Reviewer_visible = vision_query(driver = driver, operation_index = str(24))
            if isinstance(Reviewer_visible, dict):
                Reviewer_visible = Reviewer_visible.get("vision_query")
            user_variables["Reviewer_visible"] =  Reviewer_visible
            print("Reviewer_visible:", Reviewer_visible)

            # set the value of variable 'assertion_operand_dc42ebc3adb946939b4eecdb709f8e03_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_dc42ebc3adb946939b4eecdb709f8e03_0' to true")
            assertion_operand_dc42ebc3adb946939b4eecdb709f8e03_0 = "true"
            ui_action(driver = driver, operation_index = str(25))
            assertion_result = ui_action(driver=driver, operation_index=str(26))
            print("assertion_result: ", assertion_result)

            # Query 'From Date' visibility
            lambda_hooks(driver, "Query 'From Date' visibility")
            From_Date_visible = vision_query(driver = driver, operation_index = str(27))
            if isinstance(From_Date_visible, dict):
                From_Date_visible = From_Date_visible.get("vision_query")
            user_variables["From_Date_visible"] =  From_Date_visible
            print("From_Date_visible:", From_Date_visible)

            # set the value of variable 'assertion_operand_51cdd135c42b43548f20b61895f0f0f5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_51cdd135c42b43548f20b61895f0f0f5_0' to true")
            assertion_operand_51cdd135c42b43548f20b61895f0f0f5_0 = "true"
            ui_action(driver = driver, operation_index = str(28))
            assertion_result = ui_action(driver=driver, operation_index=str(29))
            print("assertion_result: ", assertion_result)

            # Query 'To Date' text visibility
            lambda_hooks(driver, "Query 'To Date' text visibility")
            To_Date_visible = vision_query(driver = driver, operation_index = str(30))
            if isinstance(To_Date_visible, dict):
                To_Date_visible = To_Date_visible.get("vision_query")
            user_variables["To_Date_visible"] =  To_Date_visible
            print("To_Date_visible:", To_Date_visible)

            # set the value of variable 'assertion_operand_797bb4c89ed445e1b60eccab2d5b33ca_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_797bb4c89ed445e1b60eccab2d5b33ca_0' to true")
            assertion_operand_797bb4c89ed445e1b60eccab2d5b33ca_0 = "true"
            ui_action(driver = driver, operation_index = str(31))
            assertion_result = ui_action(driver=driver, operation_index=str(32))
            print("assertion_result: ", assertion_result)

            # Query 'Reset' text visibility
            lambda_hooks(driver, "Query 'Reset' text visibility")
            Reset_visible = vision_query(driver = driver, operation_index = str(33))
            if isinstance(Reset_visible, dict):
                Reset_visible = Reset_visible.get("vision_query")
            user_variables["Reset_visible"] =  Reset_visible
            print("Reset_visible:", Reset_visible)

            # set the value of variable 'assertion_operand_66bbd201f4f24e40bf86ee2981b252bb_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_66bbd201f4f24e40bf86ee2981b252bb_0' to true")
            assertion_operand_66bbd201f4f24e40bf86ee2981b252bb_0 = "true"
            ui_action(driver = driver, operation_index = str(34))
            assertion_result = ui_action(driver=driver, operation_index=str(35))
            print("assertion_result: ", assertion_result)

            # Query 'Search' visibility
            lambda_hooks(driver, "Query 'Search' visibility")
            Search_visible = vision_query(driver = driver, operation_index = str(36))
            if isinstance(Search_visible, dict):
                Search_visible = Search_visible.get("vision_query")
            user_variables["Search_visible"] =  Search_visible
            print("Search_visible:", Search_visible)

            # set the value of variable 'assertion_operand_17c3a6c65ae048c4a1e9d928c2565a8b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_17c3a6c65ae048c4a1e9d928c2565a8b_0' to true")
            assertion_operand_17c3a6c65ae048c4a1e9d928c2565a8b_0 = "true"
            ui_action(driver = driver, operation_index = str(37))
            assertion_result = ui_action(driver=driver, operation_index=str(38))
            print("assertion_result: ", assertion_result)

            # Query '+ Add' text visibility
            lambda_hooks(driver, "Query '+ Add' text visibility")
            add_text_visible = vision_query(driver = driver, operation_index = str(39))
            if isinstance(add_text_visible, dict):
                add_text_visible = add_text_visible.get("vision_query")
            user_variables["add_text_visible"] =  add_text_visible
            print("add_text_visible:", add_text_visible)

            # set the value of variable 'assertion_operand_daca838672ef446ea04b09f3eb146277_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_daca838672ef446ea04b09f3eb146277_0' to true")
            assertion_operand_daca838672ef446ea04b09f3eb146277_0 = "true"
            ui_action(driver = driver, operation_index = str(40))
            assertion_result = ui_action(driver=driver, operation_index=str(41))
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
