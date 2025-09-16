
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

            # Click on 'Maintenance' menu item in the left sidebar  
            lambda_hooks(driver, "Click on 'Maintenance' menu item in the left sidebar  ")
            ui_action(driver = driver, operation_index = str(0))

            # wait 4 seconds
            lambda_hooks(driver, "wait 4 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # type ******************* in Password input field
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['2']['value']}")
            ui_action(driver = driver, operation_index = str(2))

            # Click 'Confirm' button
            lambda_hooks(driver, "Click 'Confirm' button")
            ui_action(driver = driver, operation_index = str(3))

            # wait 4 seconds
            lambda_hooks(driver, "wait 4 seconds")
            ui_action(driver = driver, operation_index = str(4))

            # Click on 'Purge Records' dropdown in top left below header  
            lambda_hooks(driver, "Click on 'Purge Records' dropdown in top left below header  ")
            ui_action(driver = driver, operation_index = str(5))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(6))

            # Click on 'Candidate Records' option in Purge Records dropdown  
            lambda_hooks(driver, "Click on 'Candidate Records' option in Purge Records dropdown  ")
            ui_action(driver = driver, operation_index = str(7))

            # wait 5 seconds
            lambda_hooks(driver, "wait 5 seconds")
            ui_action(driver = driver, operation_index = str(8))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            current_url = response = driver.current_url
            user_variables["current_url"] =  current_url
            print("current_url:", current_url)

            # set the value of variable 'assertion_operand_cabe84d777604f8085a321a19213eb92_0' to purgeCandidateData
            lambda_hooks(driver, "set the value of variable 'assertion_operand_cabe84d777604f8085a321a19213eb92_0' to purgeCandidateData")
            assertion_operand_cabe84d777604f8085a321a19213eb92_0 = "purgeCandidateData"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Click on the Search button in Purge Candidate Records section  
            lambda_hooks(driver, "Click on the Search button in Purge Candidate Records section  ")
            ui_action(driver = driver, operation_index = str(12))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(13))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_d7c6b364fb4b48ba804969fe04174ff7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d7c6b364fb4b48ba804969fe04174ff7_0' to true")
            assertion_operand_d7c6b364fb4b48ba804969fe04174ff7_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Click on vacancy input field with placeholder 'Type for hints...'  
            lambda_hooks(driver, "Click on vacancy input field with placeholder 'Type for hints...'  ")
            ui_action(driver = driver, operation_index = str(17))

            # Type in vacancy input field with placeholder 'Type for hints...' 'ayush'  
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['18']['value']}")
            ui_action(driver = driver, operation_index = str(18))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(19))

            # Click 'Search button'
            lambda_hooks(driver, "Click 'Search button'")
            ui_action(driver = driver, operation_index = str(20))

            # wait 5 seconds
            lambda_hooks(driver, "wait 5 seconds")
            ui_action(driver = driver, operation_index = str(21))

            # Query 'Invalid' text visibility
            lambda_hooks(driver, "Query 'Invalid' text visibility")
            Invalid_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(Invalid_visible, dict):
                Invalid_visible = Invalid_visible.get("vision_query")
            user_variables["Invalid_visible"] =  Invalid_visible
            print("Invalid_visible:", Invalid_visible)

            # set the value of variable 'assertion_operand_b2cba29163f54721a592feb76fa1e0e0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b2cba29163f54721a592feb76fa1e0e0_0' to true")
            assertion_operand_b2cba29163f54721a592feb76fa1e0e0_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
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
