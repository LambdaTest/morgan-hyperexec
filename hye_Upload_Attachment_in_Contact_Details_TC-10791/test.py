
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

            # Click on 'My Info' menu item in left sidebar
            lambda_hooks(driver, "Click on 'My Info' menu item in left sidebar")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click 'Contact Details' tab in left side menu under 'Personal Details'
            lambda_hooks(driver, "Click 'Contact Details' tab in left side menu under 'Personal Details'")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on 'Add' button below Attachments section
            lambda_hooks(driver, "Click on 'Add' button below Attachments section")
            ui_action(driver = driver, operation_index = str(4))

            # scroll down once
            lambda_hooks(driver, "scroll down once")
            ui_action(driver = driver, operation_index = str(5))

            # Upload file from variable '/home/kaneai/Downloads/Screenshot+2025-09-12+at+7.19.03%E2%80%AFPM.png'
            lambda_hooks(driver, "Upload file from variable '/home/kaneai/Downloads/Screenshot+2025-09-12+at+7.19.03%E2%80%AFPM.png'")
            ui_action(driver = driver, operation_index = str(6))

            # Query 'Add Attachment' visibility
            lambda_hooks(driver, "Query 'Add Attachment' visibility")
            Add_Attachment_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(Add_Attachment_visible, dict):
                Add_Attachment_visible = Add_Attachment_visible.get("vision_query")
            user_variables["Add_Attachment_visible"] =  Add_Attachment_visible
            print("Add_Attachment_visible:", Add_Attachment_visible)

            # set the value of variable 'assertion_operand_c903a6f4b04340bb87e0d4748d7f60d9_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c903a6f4b04340bb87e0d4748d7f60d9_0' to true")
            assertion_operand_c903a6f4b04340bb87e0d4748d7f60d9_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Select File' visibility
            lambda_hooks(driver, "Query 'Select File' visibility")
            select_file_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(select_file_visible, dict):
                select_file_visible = select_file_visible.get("vision_query")
            user_variables["select_file_visible"] =  select_file_visible
            print("select_file_visible:", select_file_visible)

            # set the value of variable 'assertion_operand_833be9bea86447a0b1096f4b0854ee0e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_833be9bea86447a0b1096f4b0854ee0e_0' to true")
            assertion_operand_833be9bea86447a0b1096f4b0854ee0e_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Browse' text visibility
            lambda_hooks(driver, "Query 'Browse' text visibility")
            Browse_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Browse_visible, dict):
                Browse_visible = Browse_visible.get("vision_query")
            user_variables["Browse_visible"] =  Browse_visible
            print("Browse_visible:", Browse_visible)

            # set the value of variable 'assertion_operand_13e4edcb6c344cacaf0cd0b9bba548a1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_13e4edcb6c344cacaf0cd0b9bba548a1_0' to true")
            assertion_operand_13e4edcb6c344cacaf0cd0b9bba548a1_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Comment' text visibility
            lambda_hooks(driver, "Query 'Comment' text visibility")
            Comment_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Comment_visible, dict):
                Comment_visible = Comment_visible.get("vision_query")
            user_variables["Comment_visible"] =  Comment_visible
            print("Comment_visible:", Comment_visible)

            # set the value of variable 'assertion_operand_c0b18ea91aec4a6cb04db0917e17b7c2_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c0b18ea91aec4a6cb04db0917e17b7c2_0' to true")
            assertion_operand_c0b18ea91aec4a6cb04db0917e17b7c2_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Cancel' text visibility
            lambda_hooks(driver, "Query 'Cancel' text visibility")
            Cancel_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Cancel_visible, dict):
                Cancel_visible = Cancel_visible.get("vision_query")
            user_variables["Cancel_visible"] =  Cancel_visible
            print("Cancel_visible:", Cancel_visible)

            # set the value of variable 'assertion_operand_70f3680bb8fa4e5ca671af5805c7326d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_70f3680bb8fa4e5ca671af5805c7326d_0' to true")
            assertion_operand_70f3680bb8fa4e5ca671af5805c7326d_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'Save' text visibility
            lambda_hooks(driver, "Query 'Save' text visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_e7f8a88e5f0f496eafb85900d8d4b8f0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e7f8a88e5f0f496eafb85900d8d4b8f0_0' to true")
            assertion_operand_e7f8a88e5f0f496eafb85900d8d4b8f0_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(25))

            # Query 'No Records Found' visibility
            lambda_hooks(driver, "Query 'No Records Found' visibility")
            no_records_found_visible = vision_query(driver = driver, operation_index = str(26))
            if isinstance(no_records_found_visible, dict):
                no_records_found_visible = no_records_found_visible.get("vision_query")
            user_variables["no_records_found_visible"] =  no_records_found_visible
            print("no_records_found_visible:", no_records_found_visible)

            # set the value of variable 'assertion_operand_9abac0840db541c1b87fae0f9bcb295e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_9abac0840db541c1b87fae0f9bcb295e_0' to true")
            assertion_operand_9abac0840db541c1b87fae0f9bcb295e_0 = "true"
            ui_action(driver = driver, operation_index = str(27))
            assertion_result = ui_action(driver=driver, operation_index=str(28))
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
