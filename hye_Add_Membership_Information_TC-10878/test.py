
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

            # Click on 'Memberships' tab in the left side menu under 'Qualifications'
            lambda_hooks(driver, "Click on 'Memberships' tab in the left side menu under 'Qualifications'")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on 'Add' button in Assigned Memberships section
            lambda_hooks(driver, "Click on 'Add' button in Assigned Memberships section")
            ui_action(driver = driver, operation_index = str(4))

            # Query 'Membership' text visibility
            lambda_hooks(driver, "Query 'Membership' text visibility")
            Membership_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(Membership_visible, dict):
                Membership_visible = Membership_visible.get("vision_query")
            user_variables["Membership_visible"] =  Membership_visible
            print("Membership_visible:", Membership_visible)

            # set the value of variable 'assertion_operand_d152368299ad4134b827149af54d1d76_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d152368299ad4134b827149af54d1d76_0' to true")
            assertion_operand_d152368299ad4134b827149af54d1d76_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query 'Subscription Paid By' text visibility
            lambda_hooks(driver, "Query 'Subscription Paid By' text visibility")
            subscription_paid_by_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(subscription_paid_by_visible, dict):
                subscription_paid_by_visible = subscription_paid_by_visible.get("vision_query")
            user_variables["subscription_paid_by_visible"] =  subscription_paid_by_visible
            print("subscription_paid_by_visible:", subscription_paid_by_visible)

            # set the value of variable 'assertion_operand_91d4ab010bde4710a1ccf545fb6e1ca1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_91d4ab010bde4710a1ccf545fb6e1ca1_0' to true")
            assertion_operand_91d4ab010bde4710a1ccf545fb6e1ca1_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Subscription Amount' visibility
            lambda_hooks(driver, "Query 'Subscription Amount' visibility")
            Subscription_Amount_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Subscription_Amount_visible, dict):
                Subscription_Amount_visible = Subscription_Amount_visible.get("vision_query")
            user_variables["Subscription_Amount_visible"] =  Subscription_Amount_visible
            print("Subscription_Amount_visible:", Subscription_Amount_visible)

            # set the value of variable 'assertion_operand_f25f4702ca19479a831da444607710a7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f25f4702ca19479a831da444607710a7_0' to true")
            assertion_operand_f25f4702ca19479a831da444607710a7_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query 'Currency' text visibility
            lambda_hooks(driver, "Query 'Currency' text visibility")
            Currency_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(Currency_visible, dict):
                Currency_visible = Currency_visible.get("vision_query")
            user_variables["Currency_visible"] =  Currency_visible
            print("Currency_visible:", Currency_visible)

            # set the value of variable 'assertion_operand_84ed887d187b4c5ebb0c1a9ede3b02da_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_84ed887d187b4c5ebb0c1a9ede3b02da_0' to true")
            assertion_operand_84ed887d187b4c5ebb0c1a9ede3b02da_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'Subscription Commence Date' visibility
            lambda_hooks(driver, "Query 'Subscription Commence Date' visibility")
            subscription_commence_date_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(subscription_commence_date_visible, dict):
                subscription_commence_date_visible = subscription_commence_date_visible.get("vision_query")
            user_variables["subscription_commence_date_visible"] =  subscription_commence_date_visible
            print("subscription_commence_date_visible:", subscription_commence_date_visible)

            # set the value of variable 'assertion_operand_6eddb214528d4de788c5d58e64370d0f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6eddb214528d4de788c5d58e64370d0f_0' to true")
            assertion_operand_6eddb214528d4de788c5d58e64370d0f_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'Subscription Renewal Date' visibility
            lambda_hooks(driver, "Query 'Subscription Renewal Date' visibility")
            Subscription_Renewal_Date_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(Subscription_Renewal_Date_visible, dict):
                Subscription_Renewal_Date_visible = Subscription_Renewal_Date_visible.get("vision_query")
            user_variables["Subscription_Renewal_Date_visible"] =  Subscription_Renewal_Date_visible
            print("Subscription_Renewal_Date_visible:", Subscription_Renewal_Date_visible)

            # set the value of variable 'assertion_operand_a42b181067114d8f9e6b5e62429e6184_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a42b181067114d8f9e6b5e62429e6184_0' to true")
            assertion_operand_a42b181067114d8f9e6b5e62429e6184_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Query 'Cancel' text visibility
            lambda_hooks(driver, "Query 'Cancel' text visibility")
            Cancel_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(Cancel_visible, dict):
                Cancel_visible = Cancel_visible.get("vision_query")
            user_variables["Cancel_visible"] =  Cancel_visible
            print("Cancel_visible:", Cancel_visible)

            # set the value of variable 'assertion_operand_e8180e02ab684ea785662f4d436b07c4_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e8180e02ab684ea785662f4d436b07c4_0' to true")
            assertion_operand_e8180e02ab684ea785662f4d436b07c4_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
            print("assertion_result: ", assertion_result)

            # Query 'Save' text visibility
            lambda_hooks(driver, "Query 'Save' text visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(26))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_02a0afb650b3480387acb228716c37f1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_02a0afb650b3480387acb228716c37f1_0' to true")
            assertion_operand_02a0afb650b3480387acb228716c37f1_0 = "true"
            ui_action(driver = driver, operation_index = str(27))
            assertion_result = ui_action(driver=driver, operation_index=str(28))
            print("assertion_result: ", assertion_result)

            # Click 'Save' button
            lambda_hooks(driver, "Click 'Save' button")
            ui_action(driver = driver, operation_index = str(29))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(30))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_e255cf986cac471aa63f4f560d375123_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e255cf986cac471aa63f4f560d375123_0' to true")
            assertion_operand_e255cf986cac471aa63f4f560d375123_0 = "true"
            ui_action(driver = driver, operation_index = str(31))
            assertion_result = ui_action(driver=driver, operation_index=str(32))
            print("assertion_result: ", assertion_result)

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(33))

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
