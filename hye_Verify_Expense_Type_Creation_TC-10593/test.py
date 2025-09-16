
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

            # Click on 'Claim' menu item in the left side menu
            lambda_hooks(driver, "Click on 'Claim' menu item in the left side menu")
            ui_action(driver = driver, operation_index = str(0))

            # Click on Configuration dropdown in top left
            lambda_hooks(driver, "Click on Configuration dropdown in top left")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Expense Types' menu item in the left side vertical menu
            lambda_hooks(driver, "Click on 'Expense Types' menu item in the left side vertical menu")
            ui_action(driver = driver, operation_index = str(2))

            # Click on the Name input field with placeholder 'Type for hints...'
            lambda_hooks(driver, "Click on the Name input field with placeholder 'Type for hints...'")
            ui_action(driver = driver, operation_index = str(3))

            # Type in Name input field with placeholder 'Type for hints...' 'Ayush'
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['4']['value']}")
            ui_action(driver = driver, operation_index = str(4))

            # Query visibility of text 'Ayush'
            lambda_hooks(driver, "Query visibility of text 'Ayush'")
            ayush_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(ayush_visible, dict):
                ayush_visible = ayush_visible.get("vision_query")
            user_variables["ayush_visible"] =  ayush_visible
            print("ayush_visible:", ayush_visible)

            # Query visibility of text 'No Records Found' below 'Ayush'
            lambda_hooks(driver, "Query visibility of text 'No Records Found' below 'Ayush'")
            no_records_found_visible = vision_query(driver = driver, operation_index = str(6))
            if isinstance(no_records_found_visible, dict):
                no_records_found_visible = no_records_found_visible.get("vision_query")
            user_variables["no_records_found_visible"] =  no_records_found_visible
            print("no_records_found_visible:", no_records_found_visible)

            # set the value of variable 'assertion_operand_d9eaedb152024dc0b662daa1cc0f7ec0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d9eaedb152024dc0b662daa1cc0f7ec0_0' to true")
            assertion_operand_d9eaedb152024dc0b662daa1cc0f7ec0_0 = "true"
            ui_action(driver = driver, operation_index = str(7))
            assertion_result = ui_action(driver=driver, operation_index=str(8))
            print("assertion_result: ", assertion_result)

            # Query 'Name' visibility
            lambda_hooks(driver, "Query 'Name' visibility")
            Name_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(Name_visible, dict):
                Name_visible = Name_visible.get("vision_query")
            user_variables["Name_visible"] =  Name_visible
            print("Name_visible:", Name_visible)

            # set the value of variable 'assertion_operand_aff149081c6d4a9881a3b00301701369_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_aff149081c6d4a9881a3b00301701369_0' to true")
            assertion_operand_aff149081c6d4a9881a3b00301701369_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Query 'Status' text visibility
            lambda_hooks(driver, "Query 'Status' text visibility")
            Status_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Status_visible, dict):
                Status_visible = Status_visible.get("vision_query")
            user_variables["Status_visible"] =  Status_visible
            print("Status_visible:", Status_visible)

            # set the value of variable 'assertion_operand_5e23f3abeed6491882728d8d21597587_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5e23f3abeed6491882728d8d21597587_0' to true")
            assertion_operand_5e23f3abeed6491882728d8d21597587_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(Actions_visible, dict):
                Actions_visible = Actions_visible.get("vision_query")
            user_variables["Actions_visible"] =  Actions_visible
            print("Actions_visible:", Actions_visible)

            # set the value of variable 'assertion_operand_f4c6ac06a0d948f1a1de945d86953bcc_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f4c6ac06a0d948f1a1de945d86953bcc_0' to true")
            assertion_operand_f4c6ac06a0d948f1a1de945d86953bcc_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
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
