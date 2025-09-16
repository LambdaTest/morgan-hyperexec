
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

            # Click on the 'What's on your mind?' text area in Buzz Newsfeed
            lambda_hooks(driver, "Click on the 'What's on your mind?' text area in Buzz Newsfeed")
            ui_action(driver = driver, operation_index = str(1))

            # Type in What's on your mind? input textarea 'Feed's comment'
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['2']['value']}")
            ui_action(driver = driver, operation_index = str(2))

            # Click on the Post button in Buzz Newsfeed
            lambda_hooks(driver, "Click on the Post button in Buzz Newsfeed")
            ui_action(driver = driver, operation_index = str(3))

            # Query 'Feed's comment' visibility
            lambda_hooks(driver, "Query 'Feed's comment' visibility")
            feed_comment_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(feed_comment_visible, dict):
                feed_comment_visible = feed_comment_visible.get("vision_query")
            user_variables["feed_comment_visible"] =  feed_comment_visible
            print("feed_comment_visible:", feed_comment_visible)

            # set the value of variable 'assertion_operand_2f0f33d565334ab187e44988a2c3095e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2f0f33d565334ab187e44988a2c3095e_0' to true")
            assertion_operand_2f0f33d565334ab187e44988a2c3095e_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Click on the three dots menu icon
            lambda_hooks(driver, "Click on the three dots menu icon")
            ui_action(driver = driver, operation_index = str(7))

            # Click on 'Delete Post' text button
            lambda_hooks(driver, "Click on 'Delete Post' text button")
            ui_action(driver = driver, operation_index = str(8))

            # Click on 'Yes, Delete' button with trash icon
            lambda_hooks(driver, "Click on 'Yes, Delete' button with trash icon")
            ui_action(driver = driver, operation_index = str(9))

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
