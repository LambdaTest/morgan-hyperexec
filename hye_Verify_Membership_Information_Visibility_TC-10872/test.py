
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

            # Query 'Assigned Memberships' visibility
            lambda_hooks(driver, "Query 'Assigned Memberships' visibility")
            Assigned_Memberships_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(Assigned_Memberships_visible, dict):
                Assigned_Memberships_visible = Assigned_Memberships_visible.get("vision_query")
            user_variables["Assigned_Memberships_visible"] =  Assigned_Memberships_visible
            print("Assigned_Memberships_visible:", Assigned_Memberships_visible)

            # set the value of variable 'assertion_operand_39610b64299f4806b11c0f89930182fd_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_39610b64299f4806b11c0f89930182fd_0' to true")
            assertion_operand_39610b64299f4806b11c0f89930182fd_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'No Records Found' visibility
            lambda_hooks(driver, "Query 'No Records Found' visibility")
            no_records_found_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(no_records_found_visible, dict):
                no_records_found_visible = no_records_found_visible.get("vision_query")
            user_variables["no_records_found_visible"] =  no_records_found_visible
            print("no_records_found_visible:", no_records_found_visible)

            # set the value of variable 'assertion_operand_50b59ab72740469cae43abdf1983776d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_50b59ab72740469cae43abdf1983776d_0' to true")
            assertion_operand_50b59ab72740469cae43abdf1983776d_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Membership' text visibility
            lambda_hooks(driver, "Query 'Membership' text visibility")
            Membership_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Membership_visible, dict):
                Membership_visible = Membership_visible.get("vision_query")
            user_variables["Membership_visible"] =  Membership_visible
            print("Membership_visible:", Membership_visible)

            # set the value of variable 'assertion_operand_28c952077ae244fea2152179f0b56c40_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_28c952077ae244fea2152179f0b56c40_0' to true")
            assertion_operand_28c952077ae244fea2152179f0b56c40_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Subscription Paid by' text visibility
            lambda_hooks(driver, "Query 'Subscription Paid by' text visibility")
            subscription_paid_by_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(subscription_paid_by_visible, dict):
                subscription_paid_by_visible = subscription_paid_by_visible.get("vision_query")
            user_variables["subscription_paid_by_visible"] =  subscription_paid_by_visible
            print("subscription_paid_by_visible:", subscription_paid_by_visible)

            # set the value of variable 'assertion_operand_eacebd7a54194b31bed9f1c204b41bfb_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_eacebd7a54194b31bed9f1c204b41bfb_0' to true")
            assertion_operand_eacebd7a54194b31bed9f1c204b41bfb_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Subscription Amount' visibility
            lambda_hooks(driver, "Query 'Subscription Amount' visibility")
            Subscription_Amount_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Subscription_Amount_visible, dict):
                Subscription_Amount_visible = Subscription_Amount_visible.get("vision_query")
            user_variables["Subscription_Amount_visible"] =  Subscription_Amount_visible
            print("Subscription_Amount_visible:", Subscription_Amount_visible)

            # set the value of variable 'assertion_operand_2fdcc41ebd174514884f70dab288a102_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2fdcc41ebd174514884f70dab288a102_0' to true")
            assertion_operand_2fdcc41ebd174514884f70dab288a102_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Current' text visibility
            lambda_hooks(driver, "Query 'Current' text visibility")
            Current_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Current_visible, dict):
                Current_visible = Current_visible.get("vision_query")
            user_variables["Current_visible"] =  Current_visible
            print("Current_visible:", Current_visible)

            # set the value of variable 'assertion_operand_1d77dbf1fe6b4bfc8a0be8b26209ea5e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1d77dbf1fe6b4bfc8a0be8b26209ea5e_0' to true")
            assertion_operand_1d77dbf1fe6b4bfc8a0be8b26209ea5e_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'Subscription Commence Date' visibility
            lambda_hooks(driver, "Query 'Subscription Commence Date' visibility")
            Subscription_Commence_Date_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(Subscription_Commence_Date_visible, dict):
                Subscription_Commence_Date_visible = Subscription_Commence_Date_visible.get("vision_query")
            user_variables["Subscription_Commence_Date_visible"] =  Subscription_Commence_Date_visible
            print("Subscription_Commence_Date_visible:", Subscription_Commence_Date_visible)

            # set the value of variable 'assertion_operand_eb181784e41348119af2e09b7780afd2_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_eb181784e41348119af2e09b7780afd2_0' to true")
            assertion_operand_eb181784e41348119af2e09b7780afd2_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Query 'Subscription Renewal Date' visibility
            lambda_hooks(driver, "Query 'Subscription Renewal Date' visibility")
            Subscription_Renewal_Date_visible = vision_query(driver = driver, operation_index = str(25))
            if isinstance(Subscription_Renewal_Date_visible, dict):
                Subscription_Renewal_Date_visible = Subscription_Renewal_Date_visible.get("vision_query")
            user_variables["Subscription_Renewal_Date_visible"] =  Subscription_Renewal_Date_visible
            print("Subscription_Renewal_Date_visible:", Subscription_Renewal_Date_visible)

            # set the value of variable 'assertion_operand_0b25bbc4e8de4887b0ea4e4f01dc6ee0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0b25bbc4e8de4887b0ea4e4f01dc6ee0_0' to true")
            assertion_operand_0b25bbc4e8de4887b0ea4e4f01dc6ee0_0 = "true"
            ui_action(driver = driver, operation_index = str(26))
            assertion_result = ui_action(driver=driver, operation_index=str(27))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible = vision_query(driver = driver, operation_index = str(28))
            if isinstance(Actions_visible, dict):
                Actions_visible = Actions_visible.get("vision_query")
            user_variables["Actions_visible"] =  Actions_visible
            print("Actions_visible:", Actions_visible)

            # set the value of variable 'assertion_operand_958619d7852e4a86a23d5c043d9fcc5c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_958619d7852e4a86a23d5c043d9fcc5c_0' to true")
            assertion_operand_958619d7852e4a86a23d5c043d9fcc5c_0 = "true"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
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
