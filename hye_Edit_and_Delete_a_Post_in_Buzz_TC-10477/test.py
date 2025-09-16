
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

            # Click on 'Share Photos' button in Buzz Newsfeed
            lambda_hooks(driver, "Click on 'Share Photos' button in Buzz Newsfeed")
            ui_action(driver = driver, operation_index = str(1))

            # Upload file from variable 'FILE_Screenshot_2025_09_12_at_7_19_03_E2_80_AFPM_png'
            lambda_hooks(driver, "Upload file from variable 'FILE_Screenshot_2025_09_12_at_7_19_03_E2_80_AFPM_png'")
            ui_action(driver = driver, operation_index = str(2))

            # Click on the 'Share' button in Share Photos popup
            lambda_hooks(driver, "Click on the 'Share' button in Share Photos popup")
            ui_action(driver = driver, operation_index = str(3))

            # Click on the three dots menu icon on the post by Pushpa Raj
            lambda_hooks(driver, "Click on the three dots menu icon on the post by Pushpa Raj")
            ui_action(driver = driver, operation_index = str(4))

            # Click on 'Edit Post' option in post action menu
            lambda_hooks(driver, "Click on 'Edit Post' option in post action menu")
            ui_action(driver = driver, operation_index = str(5))

            # Click on the post content textarea in edit post popup
            lambda_hooks(driver, "Click on the post content textarea in edit post popup")
            ui_action(driver = driver, operation_index = str(6))

            # Type in post edit text area 'edit comment with photo upload'
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['7']['value']}")
            ui_action(driver = driver, operation_index = str(7))

            # Click on the Post button in edit post popup
            lambda_hooks(driver, "Click on the Post button in edit post popup")
            ui_action(driver = driver, operation_index = str(8))

            # Query 'edit comment with photo upload' text visibility
            lambda_hooks(driver, "Query 'edit comment with photo upload' text visibility")
            edit_comment_with_photo_upload_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(edit_comment_with_photo_upload_visible, dict):
                edit_comment_with_photo_upload_visible = edit_comment_with_photo_upload_visible.get("vision_query")
            user_variables["edit_comment_with_photo_upload_visible"] =  edit_comment_with_photo_upload_visible
            print("edit_comment_with_photo_upload_visible:", edit_comment_with_photo_upload_visible)

            # set the value of variable 'assertion_operand_c1b2ba50ef7a4df08f32cb7186c6c3bb_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c1b2ba50ef7a4df08f32cb7186c6c3bb_0' to true")
            assertion_operand_c1b2ba50ef7a4df08f32cb7186c6c3bb_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Click on the three dots menu icon on post by Pushpa Raj
            lambda_hooks(driver, "Click on the three dots menu icon on post by Pushpa Raj")
            ui_action(driver = driver, operation_index = str(12))

            # Click on 'Delete Post' option in post menu
            lambda_hooks(driver, "Click on 'Delete Post' option in post menu")
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
