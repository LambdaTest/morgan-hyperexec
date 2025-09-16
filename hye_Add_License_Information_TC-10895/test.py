
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

            # Click 'My Info' from the left side panel
            lambda_hooks(driver, "Click 'My Info' from the left side panel")
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

            # Scroll to the bottom of the page
            lambda_hooks(driver, "Scroll to the bottom of the page")
            ui_action(driver = driver, operation_index = str(4))

            # Click on Add button in License section
            lambda_hooks(driver, "Click on Add button in License section")
            ui_action(driver = driver, operation_index = str(5))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(6))

            # Click on the license type dropdown arrow in Add License section
            lambda_hooks(driver, "Click on the license type dropdown arrow in Add License section")
            ui_action(driver = driver, operation_index = str(7))

            # Click on the issued date calendar icon
            lambda_hooks(driver, "Click on the issued date calendar icon")
            ui_action(driver = driver, operation_index = str(8))

            # Click on the expiry date calendar icon
            lambda_hooks(driver, "Click on the expiry date calendar icon")
            ui_action(driver = driver, operation_index = str(9))

            # Click on the calendar icon next to Issued Date input
            lambda_hooks(driver, "Click on the calendar icon next to Issued Date input")
            ui_action(driver = driver, operation_index = str(10))

            # Click on the Save button in Add License section
            lambda_hooks(driver, "Click on the Save button in Add License section")
            ui_action(driver = driver, operation_index = str(11))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_f3a1a77f666c4ff7b84fcdfec48093f2_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f3a1a77f666c4ff7b84fcdfec48093f2_0' to true")
            assertion_operand_f3a1a77f666c4ff7b84fcdfec48093f2_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(15))

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
