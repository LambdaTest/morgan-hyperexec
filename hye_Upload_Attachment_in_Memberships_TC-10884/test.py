
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

            # Click on 'My Info' menu item in left side menu
            lambda_hooks(driver, "Click on 'My Info' menu item in left side menu")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Memberships' tab in the left side menu
            lambda_hooks(driver, "Click on 'Memberships' tab in the left side menu")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on Add button in Attachments section
            lambda_hooks(driver, "Click on Add button in Attachments section")
            ui_action(driver = driver, operation_index = str(4))

            # Query 'Add Attachment' visibility
            lambda_hooks(driver, "Query 'Add Attachment' visibility")
            add_attachment_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(add_attachment_visible, dict):
                add_attachment_visible = add_attachment_visible.get("vision_query")
            user_variables["add_attachment_visible"] =  add_attachment_visible
            print("add_attachment_visible:", add_attachment_visible)

            # set the value of variable 'assertion_operand_bca2da26428b45cbb65bfc85902d452e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_bca2da26428b45cbb65bfc85902d452e_0' to true")
            assertion_operand_bca2da26428b45cbb65bfc85902d452e_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query 'Select File' text visibility
            lambda_hooks(driver, "Query 'Select File' text visibility")
            select_file_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(select_file_visible, dict):
                select_file_visible = select_file_visible.get("vision_query")
            user_variables["select_file_visible"] =  select_file_visible
            print("select_file_visible:", select_file_visible)

            # set the value of variable 'assertion_operand_1e5c0c4f1ce44e37b91cf63406a22ab9_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1e5c0c4f1ce44e37b91cf63406a22ab9_0' to true")
            assertion_operand_1e5c0c4f1ce44e37b91cf63406a22ab9_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Browse' text visibility
            lambda_hooks(driver, "Query 'Browse' text visibility")
            Browse_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Browse_visible, dict):
                Browse_visible = Browse_visible.get("vision_query")
            user_variables["Browse_visible"] =  Browse_visible
            print("Browse_visible:", Browse_visible)

            # set the value of variable 'assertion_operand_8704191c30074d72bff5e0dc95912bd7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8704191c30074d72bff5e0dc95912bd7_0' to true")
            assertion_operand_8704191c30074d72bff5e0dc95912bd7_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query 'No File Selected' text visibility
            lambda_hooks(driver, "Query 'No File Selected' text visibility")
            no_file_selected_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(no_file_selected_visible, dict):
                no_file_selected_visible = no_file_selected_visible.get("vision_query")
            user_variables["no_file_selected_visible"] =  no_file_selected_visible
            print("no_file_selected_visible:", no_file_selected_visible)

            # set the value of variable 'assertion_operand_544f64db6d614d87b5aead14c2d0457b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_544f64db6d614d87b5aead14c2d0457b_0' to true")
            assertion_operand_544f64db6d614d87b5aead14c2d0457b_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Accepts up to 1 MB'
            lambda_hooks(driver, "Query visibility of text 'Accepts up to 1 MB'")
            accepts_up_to_1_MB_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(accepts_up_to_1_MB_visible, dict):
                accepts_up_to_1_MB_visible = accepts_up_to_1_MB_visible.get("vision_query")
            user_variables["accepts_up_to_1_MB_visible"] =  accepts_up_to_1_MB_visible
            print("accepts_up_to_1_MB_visible:", accepts_up_to_1_MB_visible)

            # set the value of variable 'assertion_operand_c97a7ec1c3b24b9e9a0f9635d3db7360_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c97a7ec1c3b24b9e9a0f9635d3db7360_0' to true")
            assertion_operand_c97a7ec1c3b24b9e9a0f9635d3db7360_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'Comment' text visibility
            lambda_hooks(driver, "Query 'Comment' text visibility")
            Comment_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(Comment_visible, dict):
                Comment_visible = Comment_visible.get("vision_query")
            user_variables["Comment_visible"] =  Comment_visible
            print("Comment_visible:", Comment_visible)

            # set the value of variable 'assertion_operand_23880d51692b4ede99afcec8ac6b0b2d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_23880d51692b4ede99afcec8ac6b0b2d_0' to true")
            assertion_operand_23880d51692b4ede99afcec8ac6b0b2d_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Query 'Type comment here' visibility
            lambda_hooks(driver, "Query 'Type comment here' visibility")
            Type_comment_here_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(Type_comment_here_visible, dict):
                Type_comment_here_visible = Type_comment_here_visible.get("vision_query")
            user_variables["Type_comment_here_visible"] =  Type_comment_here_visible
            print("Type_comment_here_visible:", Type_comment_here_visible)

            # set the value of variable 'assertion_operand_042cb93b89b64e24b7bff0d0be2f2af5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_042cb93b89b64e24b7bff0d0be2f2af5_0' to true")
            assertion_operand_042cb93b89b64e24b7bff0d0be2f2af5_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
            print("assertion_result: ", assertion_result)

            # Query 'Cancel' text visibility
            lambda_hooks(driver, "Query 'Cancel' text visibility")
            Cancel_visible = vision_query(driver = driver, operation_index = str(26))
            if isinstance(Cancel_visible, dict):
                Cancel_visible = Cancel_visible.get("vision_query")
            user_variables["Cancel_visible"] =  Cancel_visible
            print("Cancel_visible:", Cancel_visible)

            # set the value of variable 'assertion_operand_cded5f4aef40489cae8ec4a91fd567e0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_cded5f4aef40489cae8ec4a91fd567e0_0' to true")
            assertion_operand_cded5f4aef40489cae8ec4a91fd567e0_0 = "true"
            ui_action(driver = driver, operation_index = str(27))
            assertion_result = ui_action(driver=driver, operation_index=str(28))
            print("assertion_result: ", assertion_result)

            # Query 'Save' text visibility
            lambda_hooks(driver, "Query 'Save' text visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(29))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_2ed50cc894234316be818751ecf89db6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2ed50cc894234316be818751ecf89db6_0' to true")
            assertion_operand_2ed50cc894234316be818751ecf89db6_0 = "true"
            ui_action(driver = driver, operation_index = str(30))
            assertion_result = ui_action(driver=driver, operation_index=str(31))
            print("assertion_result: ", assertion_result)

            # Upload file from variable 'FILE_Screenshot_2025_09_12_at_7_19_03_E2_80_AFPM_png'
            lambda_hooks(driver, "Upload file from variable 'FILE_Screenshot_2025_09_12_at_7_19_03_E2_80_AFPM_png'")
            ui_action(driver = driver, operation_index = str(32))

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(33))

            # Query 'No Records Found' visibility
            lambda_hooks(driver, "Query 'No Records Found' visibility")
            no_records_found_visible = vision_query(driver = driver, operation_index = str(34))
            if isinstance(no_records_found_visible, dict):
                no_records_found_visible = no_records_found_visible.get("vision_query")
            user_variables["no_records_found_visible"] =  no_records_found_visible
            print("no_records_found_visible:", no_records_found_visible)

            # set the value of variable 'assertion_operand_c49ebc80402d4af5861ee89071fa34e6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c49ebc80402d4af5861ee89071fa34e6_0' to true")
            assertion_operand_c49ebc80402d4af5861ee89071fa34e6_0 = "true"
            ui_action(driver = driver, operation_index = str(35))
            assertion_result = ui_action(driver=driver, operation_index=str(36))
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
