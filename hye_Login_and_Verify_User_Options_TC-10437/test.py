
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

            # Click on user dropdown with name Pushpa Raj in top right corner
            lambda_hooks(driver, "Click on user dropdown with name Pushpa Raj in top right corner")
            ui_action(driver = driver, operation_index = str(0))

            # Query 'About' text visibility
            lambda_hooks(driver, "Query 'About' text visibility")
            About_visible = vision_query(driver = driver, operation_index = str(1))
            if isinstance(About_visible, dict):
                About_visible = About_visible.get("vision_query")
            user_variables["About_visible"] =  About_visible
            print("About_visible:", About_visible)

            # set the value of variable 'assertion_operand_5a25bf8fba864ce2ac46dafc9a083b52_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5a25bf8fba864ce2ac46dafc9a083b52_0' to true")
            assertion_operand_5a25bf8fba864ce2ac46dafc9a083b52_0 = "true"
            ui_action(driver = driver, operation_index = str(2))
            assertion_result = ui_action(driver=driver, operation_index=str(3))
            print("assertion_result: ", assertion_result)

            # Query 'Support' text visibility
            lambda_hooks(driver, "Query 'Support' text visibility")
            Support_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(Support_visible, dict):
                Support_visible = Support_visible.get("vision_query")
            user_variables["Support_visible"] =  Support_visible
            print("Support_visible:", Support_visible)

            # set the value of variable 'assertion_operand_95d56604c8bd4989a7d5e84d35e2ca8c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_95d56604c8bd4989a7d5e84d35e2ca8c_0' to true")
            assertion_operand_95d56604c8bd4989a7d5e84d35e2ca8c_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'Change Password' text visibility
            lambda_hooks(driver, "Query 'Change Password' text visibility")
            change_password_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(change_password_visible, dict):
                change_password_visible = change_password_visible.get("vision_query")
            user_variables["change_password_visible"] =  change_password_visible
            print("change_password_visible:", change_password_visible)

            # set the value of variable 'assertion_operand_6ea6ebcd84b74314a6f25fb51ea1c2b4_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6ea6ebcd84b74314a6f25fb51ea1c2b4_0' to true")
            assertion_operand_6ea6ebcd84b74314a6f25fb51ea1c2b4_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Logout' text visibility
            lambda_hooks(driver, "Query 'Logout' text visibility")
            Logout_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Logout_visible, dict):
                Logout_visible = Logout_visible.get("vision_query")
            user_variables["Logout_visible"] =  Logout_visible
            print("Logout_visible:", Logout_visible)

            # set the value of variable 'assertion_operand_f03b3abaea334ba29cba8862dee4d53e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f03b3abaea334ba29cba8862dee4d53e_0' to true")
            assertion_operand_f03b3abaea334ba29cba8862dee4d53e_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
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
