
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

            # Click on 'Buzz' menu item in the left side menu
            lambda_hooks(driver, "Click on 'Buzz' menu item in the left side menu")
            ui_action(driver = driver, operation_index = str(0))

            # Click on the 'What's on your mind?' textarea
            lambda_hooks(driver, "Click on the 'What's on your mind?' textarea")
            ui_action(driver = driver, operation_index = str(1))

            # Type in What's on your mind? text area 'posting'
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['2']['value']}")
            ui_action(driver = driver, operation_index = str(2))

            # Click on the Post button
            lambda_hooks(driver, "Click on the Post button")
            ui_action(driver = driver, operation_index = str(3))

            # Click on the 0 Comments text in Buzz Latest Posts section
            lambda_hooks(driver, "Click on the 0 Comments text in Buzz Latest Posts section")
            ui_action(driver = driver, operation_index = str(4))

            # Type in comment input field with placeholder 'Write your comment...' 'commenting'
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['5']['value']}")
            ui_action(driver = driver, operation_index = str(5))

            # Press enter in comment input field with placeholder 'Write your comment...'
            lambda_hooks(driver, "Press enter in comment input field with placeholder 'Write your comment...'")
            ui_action(driver = driver, operation_index = str(6))

            # Click on the 'Like' text button in post comment action
            lambda_hooks(driver, "Click on the 'Like' text button in post comment action")
            ui_action(driver = driver, operation_index = str(7))

            # Click on the three dots menu on post by Pushpa Raj at 01:15 PM
            lambda_hooks(driver, "Click on the three dots menu on post by Pushpa Raj at 01:15 PM")
            ui_action(driver = driver, operation_index = str(8))

            # Click on 'Delete Post' option in post action menu
            lambda_hooks(driver, "Click on 'Delete Post' option in post action menu")
            ui_action(driver = driver, operation_index = str(9))

            # Click on 'Yes, Delete' button in confirmation popup
            lambda_hooks(driver, "Click on 'Yes, Delete' button in confirmation popup")
            ui_action(driver = driver, operation_index = str(10))

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
