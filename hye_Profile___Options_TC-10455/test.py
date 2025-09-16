
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

            # Click on the user dropdown with name Pushpa Raj in the top right corner
            lambda_hooks(driver, "Click on the user dropdown with name Pushpa Raj in the top right corner")
            ui_action(driver = driver, operation_index = str(0))

            # Click on the help icon in the top right corner
            lambda_hooks(driver, "Click on the help icon in the top right corner")
            ui_action(driver = driver, operation_index = str(1))

            # Query if 'Company Name: NetFunda' is displayed
            lambda_hooks(driver, "Query if 'Company Name: NetFunda' is displayed")
            company_name_netfunda_displayed = vision_query(driver = driver, operation_index = str(2))
            if isinstance(company_name_netfunda_displayed, dict):
                company_name_netfunda_displayed = company_name_netfunda_displayed.get("vision_query")
            user_variables["company_name_netfunda_displayed"] =  company_name_netfunda_displayed
            print("company_name_netfunda_displayed:", company_name_netfunda_displayed)

            # set the value of variable 'assertion_operand_c063c2f887d64d2591aee4154dada115_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c063c2f887d64d2591aee4154dada115_0' to true")
            assertion_operand_c063c2f887d64d2591aee4154dada115_0 = "true"
            ui_action(driver = driver, operation_index = str(3))
            assertion_result = ui_action(driver=driver, operation_index=str(4))
            print("assertion_result: ", assertion_result)

            # Click 'x' icon
            lambda_hooks(driver, "Click 'x' icon")
            ui_action(driver = driver, operation_index = str(5))

            # Click on user dropdown with name Pushpa Raj in top right corner
            lambda_hooks(driver, "Click on user dropdown with name Pushpa Raj in top right corner")
            ui_action(driver = driver, operation_index = str(6))

            # Click on 'Support' link in user dropdown menu
            lambda_hooks(driver, "Click on 'Support' link in user dropdown menu")
            ui_action(driver = driver, operation_index = str(7))

            # Query 'Customer Support' text visibility
            lambda_hooks(driver, "Query 'Customer Support' text visibility")
            Customer_Support_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Customer_Support_visible, dict):
                Customer_Support_visible = Customer_Support_visible.get("vision_query")
            user_variables["Customer_Support_visible"] =  Customer_Support_visible
            print("Customer_Support_visible:", Customer_Support_visible)

            # set the value of variable 'assertion_operand_10a6457de5764a5f82c4e57e4c0ebc18_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_10a6457de5764a5f82c4e57e4c0ebc18_0' to true")
            assertion_operand_10a6457de5764a5f82c4e57e4c0ebc18_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Click on user dropdown with name Pushpa Raj in top right corner
            lambda_hooks(driver, "Click on user dropdown with name Pushpa Raj in top right corner")
            ui_action(driver = driver, operation_index = str(11))

            # Click on 'Change Password' link in user dropdown menu
            lambda_hooks(driver, "Click on 'Change Password' link in user dropdown menu")
            ui_action(driver = driver, operation_index = str(12))

            # Query 'Update Password' text visibility
            lambda_hooks(driver, "Query 'Update Password' text visibility")
            update_password_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(update_password_visible, dict):
                update_password_visible = update_password_visible.get("vision_query")
            user_variables["update_password_visible"] =  update_password_visible
            print("update_password_visible:", update_password_visible)

            # set the value of variable 'assertion_operand_2e5b39338b1b47b0aa3e2cab69198ad2_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2e5b39338b1b47b0aa3e2cab69198ad2_0' to true")
            assertion_operand_2e5b39338b1b47b0aa3e2cab69198ad2_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
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
