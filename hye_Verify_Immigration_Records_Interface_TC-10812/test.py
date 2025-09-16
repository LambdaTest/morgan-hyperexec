
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

            # Click on Immigration tab in left side menu
            lambda_hooks(driver, "Click on Immigration tab in left side menu")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on Add button in Assigned Immigration Records section
            lambda_hooks(driver, "Click on Add button in Assigned Immigration Records section")
            ui_action(driver = driver, operation_index = str(4))

            # Query 'Passport radio button' selection state
            lambda_hooks(driver, "Query 'Passport radio button' selection state")
            passport_radio_selected = vision_query(driver = driver, operation_index = str(5))
            if isinstance(passport_radio_selected, dict):
                passport_radio_selected = passport_radio_selected.get("vision_query")
            user_variables["passport_radio_selected"] =  passport_radio_selected
            print("passport_radio_selected:", passport_radio_selected)

            # set the value of variable 'assertion_operand_9bac195a6c0f47df9f4c54f86f0761a0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_9bac195a6c0f47df9f4c54f86f0761a0_0' to true")
            assertion_operand_9bac195a6c0f47df9f4c54f86f0761a0_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query 'Number' text visibility
            lambda_hooks(driver, "Query 'Number' text visibility")
            Number_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Number_visible, dict):
                Number_visible = Number_visible.get("vision_query")
            user_variables["Number_visible"] =  Number_visible
            print("Number_visible:", Number_visible)

            # set the value of variable 'assertion_operand_e3974eebe75547c78cee269b95f61518_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e3974eebe75547c78cee269b95f61518_0' to true")
            assertion_operand_e3974eebe75547c78cee269b95f61518_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Issued Date' visibility
            lambda_hooks(driver, "Query 'Issued Date' visibility")
            Issued_Date_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Issued_Date_visible, dict):
                Issued_Date_visible = Issued_Date_visible.get("vision_query")
            user_variables["Issued_Date_visible"] =  Issued_Date_visible
            print("Issued_Date_visible:", Issued_Date_visible)

            # set the value of variable 'assertion_operand_b8f59bca568544dcb640c494c7afcb9b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b8f59bca568544dcb640c494c7afcb9b_0' to true")
            assertion_operand_b8f59bca568544dcb640c494c7afcb9b_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query 'Expiry Date' visibility
            lambda_hooks(driver, "Query 'Expiry Date' visibility")
            Expiry_Date_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(Expiry_Date_visible, dict):
                Expiry_Date_visible = Expiry_Date_visible.get("vision_query")
            user_variables["Expiry_Date_visible"] =  Expiry_Date_visible
            print("Expiry_Date_visible:", Expiry_Date_visible)

            # set the value of variable 'assertion_operand_d7a70e2ee21246fea6b2e4bf7e0e739e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d7a70e2ee21246fea6b2e4bf7e0e739e_0' to true")
            assertion_operand_d7a70e2ee21246fea6b2e4bf7e0e739e_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'Eligible Status' visibility
            lambda_hooks(driver, "Query 'Eligible Status' visibility")
            Eligible_Status_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(Eligible_Status_visible, dict):
                Eligible_Status_visible = Eligible_Status_visible.get("vision_query")
            user_variables["Eligible_Status_visible"] =  Eligible_Status_visible
            print("Eligible_Status_visible:", Eligible_Status_visible)

            # set the value of variable 'assertion_operand_a811e6428c2144a59bc15d1420fecccf_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a811e6428c2144a59bc15d1420fecccf_0' to true")
            assertion_operand_a811e6428c2144a59bc15d1420fecccf_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'Issued By' text visibility
            lambda_hooks(driver, "Query 'Issued By' text visibility")
            Issued_By_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(Issued_By_visible, dict):
                Issued_By_visible = Issued_By_visible.get("vision_query")
            user_variables["Issued_By_visible"] =  Issued_By_visible
            print("Issued_By_visible:", Issued_By_visible)

            # set the value of variable 'assertion_operand_9f41bfa2971e4bd9a3595db191fcac15_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_9f41bfa2971e4bd9a3595db191fcac15_0' to true")
            assertion_operand_9f41bfa2971e4bd9a3595db191fcac15_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Query 'Eligible Review Date' visibility
            lambda_hooks(driver, "Query 'Eligible Review Date' visibility")
            eligible_review_date_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(eligible_review_date_visible, dict):
                eligible_review_date_visible = eligible_review_date_visible.get("vision_query")
            user_variables["eligible_review_date_visible"] =  eligible_review_date_visible
            print("eligible_review_date_visible:", eligible_review_date_visible)

            # set the value of variable 'assertion_operand_7e935de22f01404c83ccfac5f6e568f6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7e935de22f01404c83ccfac5f6e568f6_0' to true")
            assertion_operand_7e935de22f01404c83ccfac5f6e568f6_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
            print("assertion_result: ", assertion_result)

            # Query 'Comments' visibility
            lambda_hooks(driver, "Query 'Comments' visibility")
            Comments_visible = vision_query(driver = driver, operation_index = str(26))
            if isinstance(Comments_visible, dict):
                Comments_visible = Comments_visible.get("vision_query")
            user_variables["Comments_visible"] =  Comments_visible
            print("Comments_visible:", Comments_visible)

            # set the value of variable 'assertion_operand_97a5ffea80e1449eac6d1375a9db0c91_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_97a5ffea80e1449eac6d1375a9db0c91_0' to true")
            assertion_operand_97a5ffea80e1449eac6d1375a9db0c91_0 = "true"
            ui_action(driver = driver, operation_index = str(27))
            assertion_result = ui_action(driver=driver, operation_index=str(28))
            print("assertion_result: ", assertion_result)

            # Query 'Cancel' text visibility
            lambda_hooks(driver, "Query 'Cancel' text visibility")
            Cancel_visible = vision_query(driver = driver, operation_index = str(29))
            if isinstance(Cancel_visible, dict):
                Cancel_visible = Cancel_visible.get("vision_query")
            user_variables["Cancel_visible"] =  Cancel_visible
            print("Cancel_visible:", Cancel_visible)

            # set the value of variable 'assertion_operand_d078f6844cc54792b84ea421c16f97e1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d078f6844cc54792b84ea421c16f97e1_0' to true")
            assertion_operand_d078f6844cc54792b84ea421c16f97e1_0 = "true"
            ui_action(driver = driver, operation_index = str(30))
            assertion_result = ui_action(driver=driver, operation_index=str(31))
            print("assertion_result: ", assertion_result)

            # Query 'Save' text visibility
            lambda_hooks(driver, "Query 'Save' text visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(32))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_37eb1fbc4b3c4ea886f2eecb28c59d6b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_37eb1fbc4b3c4ea886f2eecb28c59d6b_0' to true")
            assertion_operand_37eb1fbc4b3c4ea886f2eecb28c59d6b_0 = "true"
            ui_action(driver = driver, operation_index = str(33))
            assertion_result = ui_action(driver=driver, operation_index=str(34))
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
