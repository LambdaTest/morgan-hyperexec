
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

            # Click on 'Job' tab in the left side menu under 'My Info'
            lambda_hooks(driver, "Click on 'Job' tab in the left side menu under 'My Info'")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on Include Employment Contract Details toggle switch
            lambda_hooks(driver, "Click on Include Employment Contract Details toggle switch")
            ui_action(driver = driver, operation_index = str(4))

            # Query 'Contact Start Date' visibility
            lambda_hooks(driver, "Query 'Contact Start Date' visibility")
            Contact_Start_Date_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(Contact_Start_Date_visible, dict):
                Contact_Start_Date_visible = Contact_Start_Date_visible.get("vision_query")
            user_variables["Contact_Start_Date_visible"] =  Contact_Start_Date_visible
            print("Contact_Start_Date_visible:", Contact_Start_Date_visible)

            # set the value of variable 'assertion_operand_e6da098998fb4f48827efd7465758a1f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e6da098998fb4f48827efd7465758a1f_0' to true")
            assertion_operand_e6da098998fb4f48827efd7465758a1f_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query 'Contact End Date' visibility
            lambda_hooks(driver, "Query 'Contact End Date' visibility")
            Contact_End_Date_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Contact_End_Date_visible, dict):
                Contact_End_Date_visible = Contact_End_Date_visible.get("vision_query")
            user_variables["Contact_End_Date_visible"] =  Contact_End_Date_visible
            print("Contact_End_Date_visible:", Contact_End_Date_visible)

            # set the value of variable 'assertion_operand_5210db313b5747058487a6c1fe362aec_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5210db313b5747058487a6c1fe362aec_0' to true")
            assertion_operand_5210db313b5747058487a6c1fe362aec_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Contact Details' visibility
            lambda_hooks(driver, "Query 'Contact Details' visibility")
            Contact_Details_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Contact_Details_visible, dict):
                Contact_Details_visible = Contact_Details_visible.get("vision_query")
            user_variables["Contact_Details_visible"] =  Contact_Details_visible
            print("Contact_Details_visible:", Contact_Details_visible)

            # set the value of variable 'assertion_operand_8226014cb4a0410ca05356eb73a64f3c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8226014cb4a0410ca05356eb73a64f3c_0' to true")
            assertion_operand_8226014cb4a0410ca05356eb73a64f3c_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query 'Include Employment Contact Details' toggle visibility
            lambda_hooks(driver, "Query 'Include Employment Contact Details' toggle visibility")
            include_employment_contact_details_toggle_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(include_employment_contact_details_toggle_visible, dict):
                include_employment_contact_details_toggle_visible = include_employment_contact_details_toggle_visible.get("vision_query")
            user_variables["include_employment_contact_details_toggle_visible"] =  include_employment_contact_details_toggle_visible
            print("include_employment_contact_details_toggle_visible:", include_employment_contact_details_toggle_visible)

            # set the value of variable 'assertion_operand_8bb34e533d2e4a9493b2df75f67cfef5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8bb34e533d2e4a9493b2df75f67cfef5_0' to true")
            assertion_operand_8bb34e533d2e4a9493b2df75f67cfef5_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Click on Include Employment Contract Details toggle switch
            lambda_hooks(driver, "Click on Include Employment Contract Details toggle switch")
            ui_action(driver = driver, operation_index = str(17))

            # Query 'Include Employment Contact Details' toggle visibility
            lambda_hooks(driver, "Query 'Include Employment Contact Details' toggle visibility")
            include_employment_contact_details_toggle_visible_604c92 = vision_query(driver = driver, operation_index = str(18))
            if isinstance(include_employment_contact_details_toggle_visible_604c92, dict):
                include_employment_contact_details_toggle_visible_604c92 = include_employment_contact_details_toggle_visible_604c92.get("vision_query")
            user_variables["include_employment_contact_details_toggle_visible_604c92"] =  include_employment_contact_details_toggle_visible_604c92
            print("include_employment_contact_details_toggle_visible_604c92:", include_employment_contact_details_toggle_visible_604c92)

            # set the value of variable 'assertion_operand_1a115642336346a791ea1e1836e617d1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1a115642336346a791ea1e1836e617d1_0' to true")
            assertion_operand_1a115642336346a791ea1e1836e617d1_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
            print("assertion_result: ", assertion_result)

            # Query 'Include Employment Contact Details' toggle selected state
            lambda_hooks(driver, "Query 'Include Employment Contact Details' toggle selected state")
            include_employment_contact_details_toggle_selected = vision_query(driver = driver, operation_index = str(21))
            if isinstance(include_employment_contact_details_toggle_selected, dict):
                include_employment_contact_details_toggle_selected = include_employment_contact_details_toggle_selected.get("vision_query")
            user_variables["include_employment_contact_details_toggle_selected"] =  include_employment_contact_details_toggle_selected
            print("include_employment_contact_details_toggle_selected:", include_employment_contact_details_toggle_selected)

            # set the value of variable 'assertion_operand_1a115642336346a791ea1e1836e617d1_1' to false
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1a115642336346a791ea1e1836e617d1_1' to false")
            assertion_operand_1a115642336346a791ea1e1836e617d1_1 = "false"
            ui_action(driver = driver, operation_index = str(22))
            assertion_result = ui_action(driver=driver, operation_index=str(23))
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
