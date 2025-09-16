
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
            lambda_hooks(driver, "Click on 'Claim' menu item in the left side menu ")
            ui_action(driver = driver, operation_index = str(0))

            # Click on Configuration tab in the topbar 
            lambda_hooks(driver, "Click on Configuration tab in the topbar ")
            ui_action(driver = driver, operation_index = str(1))

            # Click 'Events' in dropdownlist
            lambda_hooks(driver, "Click 'Events' in dropdownlist")
            ui_action(driver = driver, operation_index = str(2))

            # Click on the time at work summary bar in the dashboard center 
            lambda_hooks(driver, "Click on the time at work summary bar in the dashboard center ")
            ui_action(driver = driver, operation_index = str(3))

            # Type in time at work input with placeholder 'Type for hints...' 'active' 
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['4']['value']}")
            ui_action(driver = driver, operation_index = str(4))

            # Click on the caret up icon in dropdown arrow 
            lambda_hooks(driver, "Click on the caret up icon in dropdown arrow ")
            ui_action(driver = driver, operation_index = str(5))

            # Click on the Search button 
            lambda_hooks(driver, "Click on the Search button ")
            ui_action(driver = driver, operation_index = str(6))

            # wait 5 seconds
            lambda_hooks(driver, "wait 5 seconds")
            ui_action(driver = driver, operation_index = str(7))

            # Query text '(2) Record Found' visibility
            lambda_hooks(driver, "Query text '(2) Record Found' visibility")
            record_found_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(record_found_visible, dict):
                record_found_visible = record_found_visible.get("vision_query")
            user_variables["record_found_visible"] =  record_found_visible
            print("record_found_visible:", record_found_visible)

            # set the value of variable 'assertion_operand_e7baf9814fa74a94804f1b6cb106e0b1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e7baf9814fa74a94804f1b6cb106e0b1_0' to true")
            assertion_operand_e7baf9814fa74a94804f1b6cb106e0b1_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Click on the checkbox for Active Event in the claims list 
            lambda_hooks(driver, "Click on the checkbox for Active Event in the claims list ")
            ui_action(driver = driver, operation_index = str(11))

            # Query 'Deleted Selected' text visibility
            lambda_hooks(driver, "Query 'Deleted Selected' text visibility")
            Deleted_Selected_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Deleted_Selected_visible, dict):
                Deleted_Selected_visible = Deleted_Selected_visible.get("vision_query")
            user_variables["Deleted_Selected_visible"] =  Deleted_Selected_visible
            print("Deleted_Selected_visible:", Deleted_Selected_visible)

            # set the value of variable 'assertion_operand_ea10c33f363e4718844594bb7e3cb059_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ea10c33f363e4718844594bb7e3cb059_0' to true")
            assertion_operand_ea10c33f363e4718844594bb7e3cb059_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Click on the Reset button in the Events filter section 
            lambda_hooks(driver, "Click on the Reset button in the Events filter section ")
            ui_action(driver = driver, operation_index = str(15))

            # wait 5 seconds
            lambda_hooks(driver, "wait 5 seconds")
            ui_action(driver = driver, operation_index = str(16))

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
