
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

            # Click on 'Memberships' tab in the left side menu under 'Qualifications'
            lambda_hooks(driver, "Click on 'Memberships' tab in the left side menu under 'Qualifications'")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Query 'Attachments' text visibility
            lambda_hooks(driver, "Query 'Attachments' text visibility")
            Attachments_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(Attachments_visible, dict):
                Attachments_visible = Attachments_visible.get("vision_query")
            user_variables["Attachments_visible"] =  Attachments_visible
            print("Attachments_visible:", Attachments_visible)

            # set the value of variable 'assertion_operand_eb82950b36d140f5a005e085a0db5061_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_eb82950b36d140f5a005e085a0db5061_0' to true")
            assertion_operand_eb82950b36d140f5a005e085a0db5061_0 = "true"
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

            # set the value of variable 'assertion_operand_49b9b426968f4a909b5298aa83aaf12d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_49b9b426968f4a909b5298aa83aaf12d_0' to true")
            assertion_operand_49b9b426968f4a909b5298aa83aaf12d_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'File Name' visibility
            lambda_hooks(driver, "Query 'File Name' visibility")
            File_Name_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(File_Name_visible, dict):
                File_Name_visible = File_Name_visible.get("vision_query")
            user_variables["File_Name_visible"] =  File_Name_visible
            print("File_Name_visible:", File_Name_visible)

            # set the value of variable 'assertion_operand_01b1ec9f15f74475b665eaad9dc7db0a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_01b1ec9f15f74475b665eaad9dc7db0a_0' to true")
            assertion_operand_01b1ec9f15f74475b665eaad9dc7db0a_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Description' text visibility
            lambda_hooks(driver, "Query 'Description' text visibility")
            Description_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Description_visible, dict):
                Description_visible = Description_visible.get("vision_query")
            user_variables["Description_visible"] =  Description_visible
            print("Description_visible:", Description_visible)

            # set the value of variable 'assertion_operand_e3f22aabb89d42efb0bc41f8995ca87d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e3f22aabb89d42efb0bc41f8995ca87d_0' to true")
            assertion_operand_e3f22aabb89d42efb0bc41f8995ca87d_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Size' text visibility
            lambda_hooks(driver, "Query 'Size' text visibility")
            Size_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Size_visible, dict):
                Size_visible = Size_visible.get("vision_query")
            user_variables["Size_visible"] =  Size_visible
            print("Size_visible:", Size_visible)

            # set the value of variable 'assertion_operand_d2a0362ca1c84d64a509c75e49e58a80_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d2a0362ca1c84d64a509c75e49e58a80_0' to true")
            assertion_operand_d2a0362ca1c84d64a509c75e49e58a80_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Type' text visibility
            lambda_hooks(driver, "Query 'Type' text visibility")
            Type_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Type_visible, dict):
                Type_visible = Type_visible.get("vision_query")
            user_variables["Type_visible"] =  Type_visible
            print("Type_visible:", Type_visible)

            # set the value of variable 'assertion_operand_94eacfd0105146f4a36baa425f39b16c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_94eacfd0105146f4a36baa425f39b16c_0' to true")
            assertion_operand_94eacfd0105146f4a36baa425f39b16c_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'Date Added' text visibility
            lambda_hooks(driver, "Query 'Date Added' text visibility")
            Date_Added_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(Date_Added_visible, dict):
                Date_Added_visible = Date_Added_visible.get("vision_query")
            user_variables["Date_Added_visible"] =  Date_Added_visible
            print("Date_Added_visible:", Date_Added_visible)

            # set the value of variable 'assertion_operand_b798dd2a2b7c4f2ca7abe4d216ae06d7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b798dd2a2b7c4f2ca7abe4d216ae06d7_0' to true")
            assertion_operand_b798dd2a2b7c4f2ca7abe4d216ae06d7_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Added By'
            lambda_hooks(driver, "Query visibility of text 'Added By'")
            added_by_visible = vision_query(driver = driver, operation_index = str(25))
            if isinstance(added_by_visible, dict):
                added_by_visible = added_by_visible.get("vision_query")
            user_variables["added_by_visible"] =  added_by_visible
            print("added_by_visible:", added_by_visible)

            # set the value of variable 'assertion_operand_8376e5a6c9174d43a28f664d42d6c5dd_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8376e5a6c9174d43a28f664d42d6c5dd_0' to true")
            assertion_operand_8376e5a6c9174d43a28f664d42d6c5dd_0 = "true"
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

            # set the value of variable 'assertion_operand_992266ba18e8442991cad309fe117e0e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_992266ba18e8442991cad309fe117e0e_0' to true")
            assertion_operand_992266ba18e8442991cad309fe117e0e_0 = "true"
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
