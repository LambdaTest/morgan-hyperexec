
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

            # Click on 'Report-to' tab in the left side menu under My Info
            lambda_hooks(driver, "Click on 'Report-to' tab in the left side menu under My Info")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Query visibility of text 'report to'
            lambda_hooks(driver, "Query visibility of text 'report to'")
            report_to_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(report_to_visible, dict):
                report_to_visible = report_to_visible.get("vision_query")
            user_variables["report_to_visible"] =  report_to_visible
            print("report_to_visible:", report_to_visible)

            # set the value of variable 'assertion_operand_94c06a560e83486c84e4a6339cb493d1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_94c06a560e83486c84e4a6339cb493d1_0' to true")
            assertion_operand_94c06a560e83486c84e4a6339cb493d1_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'Assigned Supervisors' visibility
            lambda_hooks(driver, "Query 'Assigned Supervisors' visibility")
            Assigned_Supervisors_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(Assigned_Supervisors_visible, dict):
                Assigned_Supervisors_visible = Assigned_Supervisors_visible.get("vision_query")
            user_variables["Assigned_Supervisors_visible"] =  Assigned_Supervisors_visible
            print("Assigned_Supervisors_visible:", Assigned_Supervisors_visible)

            # set the value of variable 'assertion_operand_d470765c45eb4868b9a1f6e0b0a914bf_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d470765c45eb4868b9a1f6e0b0a914bf_0' to true")
            assertion_operand_d470765c45eb4868b9a1f6e0b0a914bf_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'No Records Found' visibility
            lambda_hooks(driver, "Query 'No Records Found' visibility")
            No_Records_Found_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(No_Records_Found_visible, dict):
                No_Records_Found_visible = No_Records_Found_visible.get("vision_query")
            user_variables["No_Records_Found_visible"] =  No_Records_Found_visible
            print("No_Records_Found_visible:", No_Records_Found_visible)

            # set the value of variable 'assertion_operand_c8b3f60f6e3341f2b9551b5df2e90078_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c8b3f60f6e3341f2b9551b5df2e90078_0' to true")
            assertion_operand_c8b3f60f6e3341f2b9551b5df2e90078_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Name' visibility
            lambda_hooks(driver, "Query 'Name' visibility")
            Name_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Name_visible, dict):
                Name_visible = Name_visible.get("vision_query")
            user_variables["Name_visible"] =  Name_visible
            print("Name_visible:", Name_visible)

            # set the value of variable 'assertion_operand_3af1e136da1b4044a7c36bc2e44837d8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3af1e136da1b4044a7c36bc2e44837d8_0' to true")
            assertion_operand_3af1e136da1b4044a7c36bc2e44837d8_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Reporting Method' visibility
            lambda_hooks(driver, "Query 'Reporting Method' visibility")
            Reporting_Method_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Reporting_Method_visible, dict):
                Reporting_Method_visible = Reporting_Method_visible.get("vision_query")
            user_variables["Reporting_Method_visible"] =  Reporting_Method_visible
            print("Reporting_Method_visible:", Reporting_Method_visible)

            # set the value of variable 'assertion_operand_f86c8d44652b457caf4832feff274cc0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f86c8d44652b457caf4832feff274cc0_0' to true")
            assertion_operand_f86c8d44652b457caf4832feff274cc0_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Assigned Subordinates' text visibility
            lambda_hooks(driver, "Query 'Assigned Subordinates' text visibility")
            assigned_subordinates_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(assigned_subordinates_visible, dict):
                assigned_subordinates_visible = assigned_subordinates_visible.get("vision_query")
            user_variables["assigned_subordinates_visible"] =  assigned_subordinates_visible
            print("assigned_subordinates_visible:", assigned_subordinates_visible)

            # set the value of variable 'assertion_operand_3cd69cbcacf94d8da308d82cf4539aac_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3cd69cbcacf94d8da308d82cf4539aac_0' to true")
            assertion_operand_3cd69cbcacf94d8da308d82cf4539aac_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'File Name' visibility
            lambda_hooks(driver, "Query 'File Name' visibility")
            File_Name_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(File_Name_visible, dict):
                File_Name_visible = File_Name_visible.get("vision_query")
            user_variables["File_Name_visible"] =  File_Name_visible
            print("File_Name_visible:", File_Name_visible)

            # set the value of variable 'assertion_operand_ef2873c369f54f21b9f52397873e4911_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ef2873c369f54f21b9f52397873e4911_0' to true")
            assertion_operand_ef2873c369f54f21b9f52397873e4911_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Query 'Description' visibility
            lambda_hooks(driver, "Query 'Description' visibility")
            Description_visible = vision_query(driver = driver, operation_index = str(25))
            if isinstance(Description_visible, dict):
                Description_visible = Description_visible.get("vision_query")
            user_variables["Description_visible"] =  Description_visible
            print("Description_visible:", Description_visible)

            # set the value of variable 'assertion_operand_f6b1166f81e740c3a636b6b4b9d3a872_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f6b1166f81e740c3a636b6b4b9d3a872_0' to true")
            assertion_operand_f6b1166f81e740c3a636b6b4b9d3a872_0 = "true"
            ui_action(driver = driver, operation_index = str(26))
            assertion_result = ui_action(driver=driver, operation_index=str(27))
            print("assertion_result: ", assertion_result)

            # Query 'Size' text visibility
            lambda_hooks(driver, "Query 'Size' text visibility")
            Size_visible = vision_query(driver = driver, operation_index = str(28))
            if isinstance(Size_visible, dict):
                Size_visible = Size_visible.get("vision_query")
            user_variables["Size_visible"] =  Size_visible
            print("Size_visible:", Size_visible)

            # set the value of variable 'assertion_operand_4726f80b0baa40dcbb6274eb5d64bc9b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_4726f80b0baa40dcbb6274eb5d64bc9b_0' to true")
            assertion_operand_4726f80b0baa40dcbb6274eb5d64bc9b_0 = "true"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
            print("assertion_result: ", assertion_result)

            # Query 'Type' text visibility
            lambda_hooks(driver, "Query 'Type' text visibility")
            Type_visible = vision_query(driver = driver, operation_index = str(31))
            if isinstance(Type_visible, dict):
                Type_visible = Type_visible.get("vision_query")
            user_variables["Type_visible"] =  Type_visible
            print("Type_visible:", Type_visible)

            # set the value of variable 'assertion_operand_5df4276fd62d42ae87341cf5ad47d714_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5df4276fd62d42ae87341cf5ad47d714_0' to true")
            assertion_operand_5df4276fd62d42ae87341cf5ad47d714_0 = "true"
            ui_action(driver = driver, operation_index = str(32))
            assertion_result = ui_action(driver=driver, operation_index=str(33))
            print("assertion_result: ", assertion_result)

            # Query 'Date Added' text visibility
            lambda_hooks(driver, "Query 'Date Added' text visibility")
            Date_Added_visible = vision_query(driver = driver, operation_index = str(34))
            if isinstance(Date_Added_visible, dict):
                Date_Added_visible = Date_Added_visible.get("vision_query")
            user_variables["Date_Added_visible"] =  Date_Added_visible
            print("Date_Added_visible:", Date_Added_visible)

            # set the value of variable 'assertion_operand_f8fc3215c2d04e92899d4731e2beaa18_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f8fc3215c2d04e92899d4731e2beaa18_0' to true")
            assertion_operand_f8fc3215c2d04e92899d4731e2beaa18_0 = "true"
            ui_action(driver = driver, operation_index = str(35))
            assertion_result = ui_action(driver=driver, operation_index=str(36))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Added By'
            lambda_hooks(driver, "Query visibility of text 'Added By'")
            added_by_visible = vision_query(driver = driver, operation_index = str(37))
            if isinstance(added_by_visible, dict):
                added_by_visible = added_by_visible.get("vision_query")
            user_variables["added_by_visible"] =  added_by_visible
            print("added_by_visible:", added_by_visible)

            # set the value of variable 'assertion_operand_1adf6784d2c94df29c22ec6ee21d94ec_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1adf6784d2c94df29c22ec6ee21d94ec_0' to true")
            assertion_operand_1adf6784d2c94df29c22ec6ee21d94ec_0 = "true"
            ui_action(driver = driver, operation_index = str(38))
            assertion_result = ui_action(driver=driver, operation_index=str(39))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible = vision_query(driver = driver, operation_index = str(40))
            if isinstance(Actions_visible, dict):
                Actions_visible = Actions_visible.get("vision_query")
            user_variables["Actions_visible"] =  Actions_visible
            print("Actions_visible:", Actions_visible)

            # set the value of variable 'assertion_operand_2c28be2388d64879a31250a89cccb8ab_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2c28be2388d64879a31250a89cccb8ab_0' to true")
            assertion_operand_2c28be2388d64879a31250a89cccb8ab_0 = "true"
            ui_action(driver = driver, operation_index = str(41))
            assertion_result = ui_action(driver=driver, operation_index=str(42))
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
