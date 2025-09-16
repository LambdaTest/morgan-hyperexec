
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

            # Click on 'Qualifications' tab in the left side menu
            lambda_hooks(driver, "Click on 'Qualifications' tab in the left side menu")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on Work Experience + Add button
            lambda_hooks(driver, "Click on Work Experience + Add button")
            ui_action(driver = driver, operation_index = str(4))

            # Query 'Company' text visibility
            lambda_hooks(driver, "Query 'Company' text visibility")
            Company_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(Company_visible, dict):
                Company_visible = Company_visible.get("vision_query")
            user_variables["Company_visible"] =  Company_visible
            print("Company_visible:", Company_visible)

            # set the value of variable 'assertion_operand_ca8795319e6e4bb0892297b5060485f3_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ca8795319e6e4bb0892297b5060485f3_0' to true")
            assertion_operand_ca8795319e6e4bb0892297b5060485f3_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query 'Job Title' visibility
            lambda_hooks(driver, "Query 'Job Title' visibility")
            Job_Title_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Job_Title_visible, dict):
                Job_Title_visible = Job_Title_visible.get("vision_query")
            user_variables["Job_Title_visible"] =  Job_Title_visible
            print("Job_Title_visible:", Job_Title_visible)

            # set the value of variable 'assertion_operand_4ce24ac1bbc841809118846867889d09_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_4ce24ac1bbc841809118846867889d09_0' to true")
            assertion_operand_4ce24ac1bbc841809118846867889d09_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'From'
            lambda_hooks(driver, "Query visibility of text 'From'")
            From_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(From_visible, dict):
                From_visible = From_visible.get("vision_query")
            user_variables["From_visible"] =  From_visible
            print("From_visible:", From_visible)

            # set the value of variable 'assertion_operand_c38d2945ae8d4a89a5fae00fa33feb7d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c38d2945ae8d4a89a5fae00fa33feb7d_0' to true")
            assertion_operand_c38d2945ae8d4a89a5fae00fa33feb7d_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'To'
            lambda_hooks(driver, "Query visibility of text 'To'")
            To_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(To_visible, dict):
                To_visible = To_visible.get("vision_query")
            user_variables["To_visible"] =  To_visible
            print("To_visible:", To_visible)

            # set the value of variable 'assertion_operand_96f02738a3a34e0589ace78b7244c88b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_96f02738a3a34e0589ace78b7244c88b_0' to true")
            assertion_operand_96f02738a3a34e0589ace78b7244c88b_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'Comment' text visibility
            lambda_hooks(driver, "Query 'Comment' text visibility")
            Comment_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(Comment_visible, dict):
                Comment_visible = Comment_visible.get("vision_query")
            user_variables["Comment_visible"] =  Comment_visible
            print("Comment_visible:", Comment_visible)

            # set the value of variable 'assertion_operand_d2e1fd5ce39646b698662fadee1c7f2f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d2e1fd5ce39646b698662fadee1c7f2f_0' to true")
            assertion_operand_d2e1fd5ce39646b698662fadee1c7f2f_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'Cancel' text visibility
            lambda_hooks(driver, "Query 'Cancel' text visibility")
            Cancel_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(Cancel_visible, dict):
                Cancel_visible = Cancel_visible.get("vision_query")
            user_variables["Cancel_visible"] =  Cancel_visible
            print("Cancel_visible:", Cancel_visible)

            # set the value of variable 'assertion_operand_2354b50018a64ff29efd87d996e2e6fa_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2354b50018a64ff29efd87d996e2e6fa_0' to true")
            assertion_operand_2354b50018a64ff29efd87d996e2e6fa_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Query 'Save' text visibility
            lambda_hooks(driver, "Query 'Save' text visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_a87c63befaa14fbb913b83cf41c91b43_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a87c63befaa14fbb913b83cf41c91b43_0' to true")
            assertion_operand_a87c63befaa14fbb913b83cf41c91b43_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
            print("assertion_result: ", assertion_result)

            # Click 'Save Button'
            lambda_hooks(driver, "Click 'Save Button'")
            ui_action(driver = driver, operation_index = str(26))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(27))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_aaed7cb199ec43fca23451ee05f12fac_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_aaed7cb199ec43fca23451ee05f12fac_0' to true")
            assertion_operand_aaed7cb199ec43fca23451ee05f12fac_0 = "true"
            ui_action(driver = driver, operation_index = str(28))
            assertion_result = ui_action(driver=driver, operation_index=str(29))
            print("assertion_result: ", assertion_result)

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(30))

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
