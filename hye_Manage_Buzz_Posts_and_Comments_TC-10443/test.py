
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

            # Type in What's on your mind? input textarea 'New Post'
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['2']['value']}")
            ui_action(driver = driver, operation_index = str(2))

            # Click on the Post button in Buzz Latest Posts section
            lambda_hooks(driver, "Click on the Post button in Buzz Latest Posts section")
            ui_action(driver = driver, operation_index = str(3))

            # Click on 0 Comments text in Buzz Latest Posts section
            lambda_hooks(driver, "Click on 0 Comments text in Buzz Latest Posts section")
            ui_action(driver = driver, operation_index = str(4))

            # Click on comment input field with placeholder 'Write your comment...'
            lambda_hooks(driver, "Click on comment input field with placeholder 'Write your comment...'")
            ui_action(driver = driver, operation_index = str(5))

            # Type in comment input field with placeholder 'Write your comment...' 'hello comment'
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['6']['value']}")
            ui_action(driver = driver, operation_index = str(6))

            # Press enter in comment input field with placeholder 'Write your comment...'
            lambda_hooks(driver, "Press enter in comment input field with placeholder 'Write your comment...'")
            ui_action(driver = driver, operation_index = str(7))

            # Query 'Pushpa Raj' text visibility
            lambda_hooks(driver, "Query 'Pushpa Raj' text visibility")
            pushpa_raj_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(pushpa_raj_visible, dict):
                pushpa_raj_visible = pushpa_raj_visible.get("vision_query")
            user_variables["pushpa_raj_visible"] =  pushpa_raj_visible
            print("pushpa_raj_visible:", pushpa_raj_visible)

            # Query 'hello comment' visibility below 'Pushpa Raj'
            lambda_hooks(driver, "Query 'hello comment' visibility below 'Pushpa Raj'")
            hello_comment_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(hello_comment_visible, dict):
                hello_comment_visible = hello_comment_visible.get("vision_query")
            user_variables["hello_comment_visible"] =  hello_comment_visible
            print("hello_comment_visible:", hello_comment_visible)

            # set the value of variable 'assertion_operand_06fe2601f1164045bb814a4891b04aa3_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_06fe2601f1164045bb814a4891b04aa3_0' to true")
            assertion_operand_06fe2601f1164045bb814a4891b04aa3_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Click on 'Edit' link below the comment
            lambda_hooks(driver, "Click on 'Edit' link below the comment")
            ui_action(driver = driver, operation_index = str(12))

            # Type in comment input field below New Post 'hello comment with edit'
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['13']['value']}")
            ui_action(driver = driver, operation_index = str(13))

            # Press enter in comment edit input field below new post
            lambda_hooks(driver, "Press enter in comment edit input field below new post")
            ui_action(driver = driver, operation_index = str(14))

            # Query 'hello comment with edit' visibility
            lambda_hooks(driver, "Query 'hello comment with edit' visibility")
            hello_comment_with_edit_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(hello_comment_with_edit_visible, dict):
                hello_comment_with_edit_visible = hello_comment_with_edit_visible.get("vision_query")
            user_variables["hello_comment_with_edit_visible"] =  hello_comment_with_edit_visible
            print("hello_comment_with_edit_visible:", hello_comment_with_edit_visible)

            # set the value of variable 'assertion_operand_a95f1dbdd0834d72999044b6ce65ef3b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a95f1dbdd0834d72999044b6ce65ef3b_0' to true")
            assertion_operand_a95f1dbdd0834d72999044b6ce65ef3b_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Click on 'Delete' comment action link
            lambda_hooks(driver, "Click on 'Delete' comment action link")
            ui_action(driver = driver, operation_index = str(18))

            # Click on 'Yes, Delete' button in confirmation popup
            lambda_hooks(driver, "Click on 'Yes, Delete' button in confirmation popup")
            ui_action(driver = driver, operation_index = str(19))

            # Click on the three dots menu icon on post by Pushpa Raj
            lambda_hooks(driver, "Click on the three dots menu icon on post by Pushpa Raj")
            ui_action(driver = driver, operation_index = str(20))

            # Click on 'Delete Post' option in post action menu
            lambda_hooks(driver, "Click on 'Delete Post' option in post action menu")
            ui_action(driver = driver, operation_index = str(21))

            # Click on 'Yes, Delete' button in confirmation popup
            lambda_hooks(driver, "Click on 'Yes, Delete' button in confirmation popup")
            ui_action(driver = driver, operation_index = str(22))

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
