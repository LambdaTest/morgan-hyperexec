
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

            # Click on 'My Info' menu item in left side menu
            lambda_hooks(driver, "Click on 'My Info' menu item in left side menu")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on Emergency Contacts tab in left side menu
            lambda_hooks(driver, "Click on Emergency Contacts tab in left side menu")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Query 'Assigned Emergency Contacts' visibility
            lambda_hooks(driver, "Query 'Assigned Emergency Contacts' visibility")
            assigned_emergency_contacts_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(assigned_emergency_contacts_visible, dict):
                assigned_emergency_contacts_visible = assigned_emergency_contacts_visible.get("vision_query")
            user_variables["assigned_emergency_contacts_visible"] =  assigned_emergency_contacts_visible
            print("assigned_emergency_contacts_visible:", assigned_emergency_contacts_visible)

            # set the value of variable 'assertion_operand_37839c7e70a94c5dab59d9687355ae7c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_37839c7e70a94c5dab59d9687355ae7c_0' to true")
            assertion_operand_37839c7e70a94c5dab59d9687355ae7c_0 = "true"
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

            # set the value of variable 'assertion_operand_fb1130adac9f448fa8d09074de2dcd21_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_fb1130adac9f448fa8d09074de2dcd21_0' to true")
            assertion_operand_fb1130adac9f448fa8d09074de2dcd21_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Name' visibility
            lambda_hooks(driver, "Query 'Name' visibility")
            Name_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Name_visible, dict):
                Name_visible = Name_visible.get("vision_query")
            user_variables["Name_visible"] =  Name_visible
            print("Name_visible:", Name_visible)

            # set the value of variable 'assertion_operand_bc35b6a22c9d4c91ae03024816f7e7f1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_bc35b6a22c9d4c91ae03024816f7e7f1_0' to true")
            assertion_operand_bc35b6a22c9d4c91ae03024816f7e7f1_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Relationship' text visibility
            lambda_hooks(driver, "Query 'Relationship' text visibility")
            Relationship_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Relationship_visible, dict):
                Relationship_visible = Relationship_visible.get("vision_query")
            user_variables["Relationship_visible"] =  Relationship_visible
            print("Relationship_visible:", Relationship_visible)

            # set the value of variable 'assertion_operand_86cf7fed6dc74786b833f8c6807bbd7d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_86cf7fed6dc74786b833f8c6807bbd7d_0' to true")
            assertion_operand_86cf7fed6dc74786b833f8c6807bbd7d_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Home Telephone' visibility
            lambda_hooks(driver, "Query 'Home Telephone' visibility")
            home_telephone_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(home_telephone_visible, dict):
                home_telephone_visible = home_telephone_visible.get("vision_query")
            user_variables["home_telephone_visible"] =  home_telephone_visible
            print("home_telephone_visible:", home_telephone_visible)

            # set the value of variable 'assertion_operand_b2c6078f984041dcba4571e6aeec2e04_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b2c6078f984041dcba4571e6aeec2e04_0' to true")
            assertion_operand_b2c6078f984041dcba4571e6aeec2e04_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Mobile' text visibility
            lambda_hooks(driver, "Query 'Mobile' text visibility")
            Mobile_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Mobile_visible, dict):
                Mobile_visible = Mobile_visible.get("vision_query")
            user_variables["Mobile_visible"] =  Mobile_visible
            print("Mobile_visible:", Mobile_visible)

            # set the value of variable 'assertion_operand_b0992323b0fc42c4a671d61a3b35cb16_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b0992323b0fc42c4a671d61a3b35cb16_0' to true")
            assertion_operand_b0992323b0fc42c4a671d61a3b35cb16_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'Work Telephone' visibility
            lambda_hooks(driver, "Query 'Work Telephone' visibility")
            work_telephone_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(work_telephone_visible, dict):
                work_telephone_visible = work_telephone_visible.get("vision_query")
            user_variables["work_telephone_visible"] =  work_telephone_visible
            print("work_telephone_visible:", work_telephone_visible)

            # set the value of variable 'assertion_operand_0101440bb4854b20a27205dc567f6c84_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0101440bb4854b20a27205dc567f6c84_0' to true")
            assertion_operand_0101440bb4854b20a27205dc567f6c84_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible = vision_query(driver = driver, operation_index = str(25))
            if isinstance(Actions_visible, dict):
                Actions_visible = Actions_visible.get("vision_query")
            user_variables["Actions_visible"] =  Actions_visible
            print("Actions_visible:", Actions_visible)

            # set the value of variable 'assertion_operand_850d67632fa14a7d98ef84dc968de6f6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_850d67632fa14a7d98ef84dc968de6f6_0' to true")
            assertion_operand_850d67632fa14a7d98ef84dc968de6f6_0 = "true"
            ui_action(driver = driver, operation_index = str(26))
            assertion_result = ui_action(driver=driver, operation_index=str(27))
            print("assertion_result: ", assertion_result)

            # Query 'File Name' visibility
            lambda_hooks(driver, "Query 'File Name' visibility")
            File_Name_visible = vision_query(driver = driver, operation_index = str(28))
            if isinstance(File_Name_visible, dict):
                File_Name_visible = File_Name_visible.get("vision_query")
            user_variables["File_Name_visible"] =  File_Name_visible
            print("File_Name_visible:", File_Name_visible)

            # set the value of variable 'assertion_operand_e3325c5e57fd432fbc75c35520d83d42_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e3325c5e57fd432fbc75c35520d83d42_0' to true")
            assertion_operand_e3325c5e57fd432fbc75c35520d83d42_0 = "true"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
            print("assertion_result: ", assertion_result)

            # Query 'Description' text visibility
            lambda_hooks(driver, "Query 'Description' text visibility")
            Description_visible = vision_query(driver = driver, operation_index = str(31))
            if isinstance(Description_visible, dict):
                Description_visible = Description_visible.get("vision_query")
            user_variables["Description_visible"] =  Description_visible
            print("Description_visible:", Description_visible)

            # set the value of variable 'assertion_operand_c7b6de9e416d40d99361f3f1e81077f7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c7b6de9e416d40d99361f3f1e81077f7_0' to true")
            assertion_operand_c7b6de9e416d40d99361f3f1e81077f7_0 = "true"
            ui_action(driver = driver, operation_index = str(32))
            assertion_result = ui_action(driver=driver, operation_index=str(33))
            print("assertion_result: ", assertion_result)

            # Query 'Size' text visibility
            lambda_hooks(driver, "Query 'Size' text visibility")
            Size_visible = vision_query(driver = driver, operation_index = str(34))
            if isinstance(Size_visible, dict):
                Size_visible = Size_visible.get("vision_query")
            user_variables["Size_visible"] =  Size_visible
            print("Size_visible:", Size_visible)

            # set the value of variable 'assertion_operand_806f5936333c4d99ad184196a9789325_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_806f5936333c4d99ad184196a9789325_0' to true")
            assertion_operand_806f5936333c4d99ad184196a9789325_0 = "true"
            ui_action(driver = driver, operation_index = str(35))
            assertion_result = ui_action(driver=driver, operation_index=str(36))
            print("assertion_result: ", assertion_result)

            # Query 'Type' text visibility
            lambda_hooks(driver, "Query 'Type' text visibility")
            Type_visible = vision_query(driver = driver, operation_index = str(37))
            if isinstance(Type_visible, dict):
                Type_visible = Type_visible.get("vision_query")
            user_variables["Type_visible"] =  Type_visible
            print("Type_visible:", Type_visible)

            # set the value of variable 'assertion_operand_db15920179664ad0968138ece759d8ce_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_db15920179664ad0968138ece759d8ce_0' to true")
            assertion_operand_db15920179664ad0968138ece759d8ce_0 = "true"
            ui_action(driver = driver, operation_index = str(38))
            assertion_result = ui_action(driver=driver, operation_index=str(39))
            print("assertion_result: ", assertion_result)

            # Query 'Date Added' text visibility
            lambda_hooks(driver, "Query 'Date Added' text visibility")
            Date_Added_visible = vision_query(driver = driver, operation_index = str(40))
            if isinstance(Date_Added_visible, dict):
                Date_Added_visible = Date_Added_visible.get("vision_query")
            user_variables["Date_Added_visible"] =  Date_Added_visible
            print("Date_Added_visible:", Date_Added_visible)

            # set the value of variable 'assertion_operand_09e12a918cbb4978bb70b7d21a2f5f3b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_09e12a918cbb4978bb70b7d21a2f5f3b_0' to true")
            assertion_operand_09e12a918cbb4978bb70b7d21a2f5f3b_0 = "true"
            ui_action(driver = driver, operation_index = str(41))
            assertion_result = ui_action(driver=driver, operation_index=str(42))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Added By'
            lambda_hooks(driver, "Query visibility of text 'Added By'")
            added_by_visible = vision_query(driver = driver, operation_index = str(43))
            if isinstance(added_by_visible, dict):
                added_by_visible = added_by_visible.get("vision_query")
            user_variables["added_by_visible"] =  added_by_visible
            print("added_by_visible:", added_by_visible)

            # set the value of variable 'assertion_operand_f328dd2b71514ba2a92e81629a2a4e64_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f328dd2b71514ba2a92e81629a2a4e64_0' to true")
            assertion_operand_f328dd2b71514ba2a92e81629a2a4e64_0 = "true"
            ui_action(driver = driver, operation_index = str(44))
            assertion_result = ui_action(driver=driver, operation_index=str(45))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible_0bdf38 = vision_query(driver = driver, operation_index = str(46))
            if isinstance(Actions_visible_0bdf38, dict):
                Actions_visible_0bdf38 = Actions_visible_0bdf38.get("vision_query")
            user_variables["Actions_visible_0bdf38"] =  Actions_visible_0bdf38
            print("Actions_visible_0bdf38:", Actions_visible_0bdf38)

            # set the value of variable 'assertion_operand_8f7732d19d334d2fb2b71a319ae786ef_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8f7732d19d334d2fb2b71a319ae786ef_0' to true")
            assertion_operand_8f7732d19d334d2fb2b71a319ae786ef_0 = "true"
            ui_action(driver = driver, operation_index = str(47))
            assertion_result = ui_action(driver=driver, operation_index=str(48))
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
