
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

            # Click on Performance menu item in left sidebar
            lambda_hooks(driver, "Click on Performance menu item in left sidebar")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Manage Reviews' tab in the top nav bar
            lambda_hooks(driver, "Click on 'Manage Reviews' tab in the top nav bar")
            ui_action(driver = driver, operation_index = str(2))

            # Click on 'Manage Reviews' tab in the top nav bar
            lambda_hooks(driver, "Click on 'Manage Reviews' tab in the top nav bar")
            ui_action(driver = driver, operation_index = str(3))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(4))

            # Click on the green + Add button below Manage Performance Reviews form
            lambda_hooks(driver, "Click on the green + Add button below Manage Performance Reviews form")
            ui_action(driver = driver, operation_index = str(5))

            # wait 5 seconds
            lambda_hooks(driver, "wait 5 seconds")
            ui_action(driver = driver, operation_index = str(6))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            current_url = response = driver.current_url
            user_variables["current_url"] =  current_url
            print("current_url:", current_url)

            # set the value of variable 'assertion_operand_03338a8baab244ea9a1abf0031848975_0' to saveReview
            lambda_hooks(driver, "set the value of variable 'assertion_operand_03338a8baab244ea9a1abf0031848975_0' to saveReview")
            assertion_operand_03338a8baab244ea9a1abf0031848975_0 = "saveReview"
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

            # set the value of variable 'assertion_operand_7d78b800461541fc957296f24910b88c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7d78b800461541fc957296f24910b88c_0' to true")
            assertion_operand_7d78b800461541fc957296f24910b88c_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Supervisor Reviewer' text visibility
            lambda_hooks(driver, "Query 'Supervisor Reviewer' text visibility")
            Supervisor_Reviewer_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Supervisor_Reviewer_visible, dict):
                Supervisor_Reviewer_visible = Supervisor_Reviewer_visible.get("vision_query")
            user_variables["Supervisor_Reviewer_visible"] =  Supervisor_Reviewer_visible
            print("Supervisor_Reviewer_visible:", Supervisor_Reviewer_visible)

            # set the value of variable 'assertion_operand_ea20b42fe04d4681bd7b9aa1f2239c5a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ea20b42fe04d4681bd7b9aa1f2239c5a_0' to true")
            assertion_operand_ea20b42fe04d4681bd7b9aa1f2239c5a_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Review Period Start Date' visibility
            lambda_hooks(driver, "Query 'Review Period Start Date' visibility")
            Review_Period_Start_Date_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Review_Period_Start_Date_visible, dict):
                Review_Period_Start_Date_visible = Review_Period_Start_Date_visible.get("vision_query")
            user_variables["Review_Period_Start_Date_visible"] =  Review_Period_Start_Date_visible
            print("Review_Period_Start_Date_visible:", Review_Period_Start_Date_visible)

            # set the value of variable 'assertion_operand_4bfb7abf910b49a2a1816240edb7d574_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_4bfb7abf910b49a2a1816240edb7d574_0' to true")
            assertion_operand_4bfb7abf910b49a2a1816240edb7d574_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Review Period End Date'
            lambda_hooks(driver, "Query visibility of text 'Review Period End Date'")
            review_period_end_date_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(review_period_end_date_visible, dict):
                review_period_end_date_visible = review_period_end_date_visible.get("vision_query")
            user_variables["review_period_end_date_visible"] =  review_period_end_date_visible
            print("review_period_end_date_visible:", review_period_end_date_visible)

            # set the value of variable 'assertion_operand_ff01b5a39ab048eeb08ca885e8b1d3da_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ff01b5a39ab048eeb08ca885e8b1d3da_0' to true")
            assertion_operand_ff01b5a39ab048eeb08ca885e8b1d3da_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'Due Date' visibility
            lambda_hooks(driver, "Query 'Due Date' visibility")
            Due_Date_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(Due_Date_visible, dict):
                Due_Date_visible = Due_Date_visible.get("vision_query")
            user_variables["Due_Date_visible"] =  Due_Date_visible
            print("Due_Date_visible:", Due_Date_visible)

            # set the value of variable 'assertion_operand_e8cf17dcf3ad45148130004fbe92d576_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e8cf17dcf3ad45148130004fbe92d576_0' to true")
            assertion_operand_e8cf17dcf3ad45148130004fbe92d576_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Query 'Cancel' text visibility
            lambda_hooks(driver, "Query 'Cancel' text visibility")
            Cancel_visible = vision_query(driver = driver, operation_index = str(25))
            if isinstance(Cancel_visible, dict):
                Cancel_visible = Cancel_visible.get("vision_query")
            user_variables["Cancel_visible"] =  Cancel_visible
            print("Cancel_visible:", Cancel_visible)

            # set the value of variable 'assertion_operand_ccfff9612a004d01a9edc06559bfd168_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ccfff9612a004d01a9edc06559bfd168_0' to true")
            assertion_operand_ccfff9612a004d01a9edc06559bfd168_0 = "true"
            ui_action(driver = driver, operation_index = str(26))
            assertion_result = ui_action(driver=driver, operation_index=str(27))
            print("assertion_result: ", assertion_result)

            # Query 'Save' text visibility
            lambda_hooks(driver, "Query 'Save' text visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(28))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_86755774100e4803be343a7022582d8d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_86755774100e4803be343a7022582d8d_0' to true")
            assertion_operand_86755774100e4803be343a7022582d8d_0 = "true"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
            print("assertion_result: ", assertion_result)

            # Query 'Activate' text visibility
            lambda_hooks(driver, "Query 'Activate' text visibility")
            Activate_visible = vision_query(driver = driver, operation_index = str(31))
            if isinstance(Activate_visible, dict):
                Activate_visible = Activate_visible.get("vision_query")
            user_variables["Activate_visible"] =  Activate_visible
            print("Activate_visible:", Activate_visible)

            # set the value of variable 'assertion_operand_c6648ce2f75f4ab38bedb7206719475b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c6648ce2f75f4ab38bedb7206719475b_0' to true")
            assertion_operand_c6648ce2f75f4ab38bedb7206719475b_0 = "true"
            ui_action(driver = driver, operation_index = str(32))
            assertion_result = ui_action(driver=driver, operation_index=str(33))
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
