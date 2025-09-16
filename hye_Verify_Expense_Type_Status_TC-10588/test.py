
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

            # Click on 'Expense Types' menu item in the left side navigation under Claim
            lambda_hooks(driver, "Click on 'Expense Types' menu item in the left side navigation under Claim")
            ui_action(driver = driver, operation_index = str(2))

            # Click on the status dropdown collapse arrow
            lambda_hooks(driver, "Click on the status dropdown collapse arrow")
            ui_action(driver = driver, operation_index = str(3))

            # Query 'Active' text visibility
            lambda_hooks(driver, "Query 'Active' text visibility")
            Active_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(Active_visible, dict):
                Active_visible = Active_visible.get("vision_query")
            user_variables["Active_visible"] =  Active_visible
            print("Active_visible:", Active_visible)

            # set the value of variable 'assertion_operand_8648cd2ff591426b863c1a8ef685bf3b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8648cd2ff591426b863c1a8ef685bf3b_0' to true")
            assertion_operand_8648cd2ff591426b863c1a8ef685bf3b_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'Inactive' text visibility
            lambda_hooks(driver, "Query 'Inactive' text visibility")
            Inactive_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(Inactive_visible, dict):
                Inactive_visible = Inactive_visible.get("vision_query")
            user_variables["Inactive_visible"] =  Inactive_visible
            print("Inactive_visible:", Inactive_visible)

            # set the value of variable 'assertion_operand_4a53d9b935cf46558a21f75c72b8670b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_4a53d9b935cf46558a21f75c72b8670b_0' to true")
            assertion_operand_4a53d9b935cf46558a21f75c72b8670b_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Active' text visibility
            lambda_hooks(driver, "Query 'Active' text visibility")
            Active_visible_1ee766 = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Active_visible_1ee766, dict):
                Active_visible_1ee766 = Active_visible_1ee766.get("vision_query")
            user_variables["Active_visible_1ee766"] =  Active_visible_1ee766
            print("Active_visible_1ee766:", Active_visible_1ee766)

            # set the value of variable 'assertion_operand_69f07832d1884291923d6e0609d5840d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_69f07832d1884291923d6e0609d5840d_0' to true")
            assertion_operand_69f07832d1884291923d6e0609d5840d_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Click on the status dropdown arrow in Expense Types filter
            lambda_hooks(driver, "Click on the status dropdown arrow in Expense Types filter")
            ui_action(driver = driver, operation_index = str(13))

            # Query 'Inactive' text visibility
            lambda_hooks(driver, "Query 'Inactive' text visibility")
            Inactive_visible_cabbde = vision_query(driver = driver, operation_index = str(14))
            if isinstance(Inactive_visible_cabbde, dict):
                Inactive_visible_cabbde = Inactive_visible_cabbde.get("vision_query")
            user_variables["Inactive_visible_cabbde"] =  Inactive_visible_cabbde
            print("Inactive_visible_cabbde:", Inactive_visible_cabbde)

            # set the value of variable 'assertion_operand_2c9aa64663c74890857a35410d3e0a84_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2c9aa64663c74890857a35410d3e0a84_0' to true")
            assertion_operand_2c9aa64663c74890857a35410d3e0a84_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
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
