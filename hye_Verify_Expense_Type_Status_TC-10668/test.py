
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

            # Click on 'Claim' menu item in left side menu 
            lambda_hooks(driver, "Click on 'Claim' menu item in left side menu ")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Configuration' dropdown in the top left navigation bar 
            lambda_hooks(driver, "Click on 'Configuration' dropdown in the top left navigation bar ")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on 'Expense Types' menu item in the left side vertical menu under Claim 
            lambda_hooks(driver, "Click on 'Expense Types' menu item in the left side vertical menu under Claim ")
            ui_action(driver = driver, operation_index = str(4))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(5))

            # Click on the expense name input field with placeholder 'Type for hints...' 
            lambda_hooks(driver, "Click on the expense name input field with placeholder 'Type for hints...' ")
            ui_action(driver = driver, operation_index = str(6))

            # Type in expense type name input field 'active' 
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['7']['value']}")
            ui_action(driver = driver, operation_index = str(7))

            # Click on the status dropdown in expense types section 
            lambda_hooks(driver, "Click on the status dropdown in expense types section ")
            ui_action(driver = driver, operation_index = str(8))

            # Click on the Search button in Expense Types section 
            lambda_hooks(driver, "Click on the Search button in Expense Types section ")
            ui_action(driver = driver, operation_index = str(9))

            # Query text '(2) Records Found' visibility
            lambda_hooks(driver, "Query text '(2) Records Found' visibility")
            records_found_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(records_found_visible, dict):
                records_found_visible = records_found_visible.get("vision_query")
            user_variables["records_found_visible"] =  records_found_visible
            print("records_found_visible:", records_found_visible)

            # set the value of variable 'assertion_operand_18cb45e57e8a470085f0ca3e2878fcaf_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_18cb45e57e8a470085f0ca3e2878fcaf_0' to true")
            assertion_operand_18cb45e57e8a470085f0ca3e2878fcaf_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Inactive' text visibility
            lambda_hooks(driver, "Query 'Inactive' text visibility")
            Inactive_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Inactive_visible, dict):
                Inactive_visible = Inactive_visible.get("vision_query")
            user_variables["Inactive_visible"] =  Inactive_visible
            print("Inactive_visible:", Inactive_visible)

            # set the value of variable 'assertion_operand_9768de8a62fd4969bdcfe00be20c01f5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_9768de8a62fd4969bdcfe00be20c01f5_0' to true")
            assertion_operand_9768de8a62fd4969bdcfe00be20c01f5_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Active Expense name' visibility
            lambda_hooks(driver, "Query 'Active Expense name' visibility")
            Active_Expense_name_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Active_Expense_name_visible, dict):
                Active_Expense_name_visible = Active_Expense_name_visible.get("vision_query")
            user_variables["Active_Expense_name_visible"] =  Active_Expense_name_visible
            print("Active_Expense_name_visible:", Active_Expense_name_visible)

            # set the value of variable 'assertion_operand_94582f5af2bf45e196471a7fecc15c6b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_94582f5af2bf45e196471a7fecc15c6b_0' to true")
            assertion_operand_94582f5af2bf45e196471a7fecc15c6b_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Active Expense name' visibility
            lambda_hooks(driver, "Query 'Active Expense name' visibility")
            Active_Expense_name_visible_452a4d = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Active_Expense_name_visible_452a4d, dict):
                Active_Expense_name_visible_452a4d = Active_Expense_name_visible_452a4d.get("vision_query")
            user_variables["Active_Expense_name_visible_452a4d"] =  Active_Expense_name_visible_452a4d
            print("Active_Expense_name_visible_452a4d:", Active_Expense_name_visible_452a4d)

            # set the value of variable 'assertion_operand_92e96bf1b6ad4b22a70e632477db8496_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_92e96bf1b6ad4b22a70e632477db8496_0' to true")
            assertion_operand_92e96bf1b6ad4b22a70e632477db8496_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'Inactive Expense name' visibility
            lambda_hooks(driver, "Query 'Inactive Expense name' visibility")
            inactive_expense_name_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(inactive_expense_name_visible, dict):
                inactive_expense_name_visible = inactive_expense_name_visible.get("vision_query")
            user_variables["inactive_expense_name_visible"] =  inactive_expense_name_visible
            print("inactive_expense_name_visible:", inactive_expense_name_visible)

            # set the value of variable 'assertion_operand_2ab7828726a84bc89c0c56bb48206c55_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2ab7828726a84bc89c0c56bb48206c55_0' to true")
            assertion_operand_2ab7828726a84bc89c0c56bb48206c55_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
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
