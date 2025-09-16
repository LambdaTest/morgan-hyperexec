
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

            # Click on 'Dependents' tab in the left side menu under 'My Info'
            lambda_hooks(driver, "Click on 'Dependents' tab in the left side menu under 'My Info'")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Query 'Assigned Dependents' visibility
            lambda_hooks(driver, "Query 'Assigned Dependents' visibility")
            Assigned_Dependents_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(Assigned_Dependents_visible, dict):
                Assigned_Dependents_visible = Assigned_Dependents_visible.get("vision_query")
            user_variables["Assigned_Dependents_visible"] =  Assigned_Dependents_visible
            print("Assigned_Dependents_visible:", Assigned_Dependents_visible)

            # set the value of variable 'assertion_operand_ee31374e480d4e46a1235a90b2fec62c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ee31374e480d4e46a1235a90b2fec62c_0' to true")
            assertion_operand_ee31374e480d4e46a1235a90b2fec62c_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'No Record Found' visibility
            lambda_hooks(driver, "Query 'No Record Found' visibility")
            no_record_found_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(no_record_found_visible, dict):
                no_record_found_visible = no_record_found_visible.get("vision_query")
            user_variables["no_record_found_visible"] =  no_record_found_visible
            print("no_record_found_visible:", no_record_found_visible)

            # set the value of variable 'assertion_operand_457f2988d5394c6bbec69121157b67d3_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_457f2988d5394c6bbec69121157b67d3_0' to true")
            assertion_operand_457f2988d5394c6bbec69121157b67d3_0 = "true"
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

            # set the value of variable 'assertion_operand_a080dae9bfe04eebb9090111d2ed3773_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a080dae9bfe04eebb9090111d2ed3773_0' to true")
            assertion_operand_a080dae9bfe04eebb9090111d2ed3773_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'relationship' text visibility
            lambda_hooks(driver, "Query 'relationship' text visibility")
            relationship_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(relationship_visible, dict):
                relationship_visible = relationship_visible.get("vision_query")
            user_variables["relationship_visible"] =  relationship_visible
            print("relationship_visible:", relationship_visible)

            # set the value of variable 'assertion_operand_945eeeab9d844e0ca07a726eef0e1761_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_945eeeab9d844e0ca07a726eef0e1761_0' to true")
            assertion_operand_945eeeab9d844e0ca07a726eef0e1761_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Date of Birth' visibility
            lambda_hooks(driver, "Query 'Date of Birth' visibility")
            Date_of_Birth_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Date_of_Birth_visible, dict):
                Date_of_Birth_visible = Date_of_Birth_visible.get("vision_query")
            user_variables["Date_of_Birth_visible"] =  Date_of_Birth_visible
            print("Date_of_Birth_visible:", Date_of_Birth_visible)

            # set the value of variable 'assertion_operand_41a4b9ca172b4ad9b4c08691c71fe5c1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_41a4b9ca172b4ad9b4c08691c71fe5c1_0' to true")
            assertion_operand_41a4b9ca172b4ad9b4c08691c71fe5c1_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Actions_visible, dict):
                Actions_visible = Actions_visible.get("vision_query")
            user_variables["Actions_visible"] =  Actions_visible
            print("Actions_visible:", Actions_visible)

            # set the value of variable 'assertion_operand_5503011c104c433abf045ac6f70f9b8d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5503011c104c433abf045ac6f70f9b8d_0' to true")
            assertion_operand_5503011c104c433abf045ac6f70f9b8d_0 = "true"
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

            # set the value of variable 'assertion_operand_ab4838a758c141d39b265f07023891d0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ab4838a758c141d39b265f07023891d0_0' to true")
            assertion_operand_ab4838a758c141d39b265f07023891d0_0 = "true"
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

            # set the value of variable 'assertion_operand_e81798d378ed425f87dfe202d672ec5a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e81798d378ed425f87dfe202d672ec5a_0' to true")
            assertion_operand_e81798d378ed425f87dfe202d672ec5a_0 = "true"
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

            # set the value of variable 'assertion_operand_cd00e6f3dffe4ca6b6f14ce786c28f17_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_cd00e6f3dffe4ca6b6f14ce786c28f17_0' to true")
            assertion_operand_cd00e6f3dffe4ca6b6f14ce786c28f17_0 = "true"
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

            # set the value of variable 'assertion_operand_3767ccc650874ae1bc55f006994990ef_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3767ccc650874ae1bc55f006994990ef_0' to true")
            assertion_operand_3767ccc650874ae1bc55f006994990ef_0 = "true"
            ui_action(driver = driver, operation_index = str(32))
            assertion_result = ui_action(driver=driver, operation_index=str(33))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Date Added'
            lambda_hooks(driver, "Query visibility of text 'Date Added'")
            date_added_visible = vision_query(driver = driver, operation_index = str(34))
            if isinstance(date_added_visible, dict):
                date_added_visible = date_added_visible.get("vision_query")
            user_variables["date_added_visible"] =  date_added_visible
            print("date_added_visible:", date_added_visible)

            # set the value of variable 'assertion_operand_6fbc80227595405c9f38b70186326b18_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6fbc80227595405c9f38b70186326b18_0' to true")
            assertion_operand_6fbc80227595405c9f38b70186326b18_0 = "true"
            ui_action(driver = driver, operation_index = str(35))
            assertion_result = ui_action(driver=driver, operation_index=str(36))
            print("assertion_result: ", assertion_result)

            # Query 'Added By' text visibility
            lambda_hooks(driver, "Query 'Added By' text visibility")
            added_by_visible = vision_query(driver = driver, operation_index = str(37))
            if isinstance(added_by_visible, dict):
                added_by_visible = added_by_visible.get("vision_query")
            user_variables["added_by_visible"] =  added_by_visible
            print("added_by_visible:", added_by_visible)

            # set the value of variable 'assertion_operand_77d6e17d39d94827990a2b42f50814b5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_77d6e17d39d94827990a2b42f50814b5_0' to true")
            assertion_operand_77d6e17d39d94827990a2b42f50814b5_0 = "true"
            ui_action(driver = driver, operation_index = str(38))
            assertion_result = ui_action(driver=driver, operation_index=str(39))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible_f05bd7 = vision_query(driver = driver, operation_index = str(40))
            if isinstance(Actions_visible_f05bd7, dict):
                Actions_visible_f05bd7 = Actions_visible_f05bd7.get("vision_query")
            user_variables["Actions_visible_f05bd7"] =  Actions_visible_f05bd7
            print("Actions_visible_f05bd7:", Actions_visible_f05bd7)

            # set the value of variable 'assertion_operand_57431bd878344fd79f192ac1cf822523_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_57431bd878344fd79f192ac1cf822523_0' to true")
            assertion_operand_57431bd878344fd79f192ac1cf822523_0 = "true"
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
