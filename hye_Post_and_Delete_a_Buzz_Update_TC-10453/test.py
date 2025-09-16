
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

            # Type in What's on your mind? input textarea 'test'
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['2']['value']}")
            ui_action(driver = driver, operation_index = str(2))

            # Click on the Post button in Buzz Newsfeed
            lambda_hooks(driver, "Click on the Post button in Buzz Newsfeed")
            ui_action(driver = driver, operation_index = str(3))

            # Click on the heart icon below post by Pushpa Raj
            lambda_hooks(driver, "Click on the heart icon below post by Pushpa Raj")
            ui_action(driver = driver, operation_index = str(4))

            # Query '1 Like' visibility
            lambda_hooks(driver, "Query '1 Like' visibility")
            like_text_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(like_text_visible, dict):
                like_text_visible = like_text_visible.get("vision_query")
            user_variables["like_text_visible"] =  like_text_visible
            print("like_text_visible:", like_text_visible)

            # set the value of variable 'assertion_operand_46c43b8efe954d3c888981d96c019442_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_46c43b8efe954d3c888981d96c019442_0' to true")
            assertion_operand_46c43b8efe954d3c888981d96c019442_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Click on the red heart icon below post by Pushpa Raj
            lambda_hooks(driver, "Click on the red heart icon below post by Pushpa Raj")
            ui_action(driver = driver, operation_index = str(8))

            # Query '0 Likes' visibility
            lambda_hooks(driver, "Query '0 Likes' visibility")
            zero_likes_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(zero_likes_visible, dict):
                zero_likes_visible = zero_likes_visible.get("vision_query")
            user_variables["zero_likes_visible"] =  zero_likes_visible
            print("zero_likes_visible:", zero_likes_visible)

            # set the value of variable 'assertion_operand_be23fbe7f4e04926970472deb6947085_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_be23fbe7f4e04926970472deb6947085_0' to true")
            assertion_operand_be23fbe7f4e04926970472deb6947085_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Click on the three dots menu icon on post by Pushpa Raj
            lambda_hooks(driver, "Click on the three dots menu icon on post by Pushpa Raj")
            ui_action(driver = driver, operation_index = str(12))

            # Click on 'Delete Post' option in post action menu
            lambda_hooks(driver, "Click on 'Delete Post' option in post action menu")
            ui_action(driver = driver, operation_index = str(13))

            # Click on the Yes, Delete button with trash icon
            lambda_hooks(driver, "Click on the Yes, Delete button with trash icon")
            ui_action(driver = driver, operation_index = str(14))

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
