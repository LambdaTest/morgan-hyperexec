
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

            # set the value of variable 'assertion_operand_6b7b361a3da743229426f54db1696bfe_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6b7b361a3da743229426f54db1696bfe_0' to true")
            assertion_operand_6b7b361a3da743229426f54db1696bfe_0 = "true"
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

            # set the value of variable 'assertion_operand_0fd4f5571482419da83768c5dd50a6e5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0fd4f5571482419da83768c5dd50a6e5_0' to true")
            assertion_operand_0fd4f5571482419da83768c5dd50a6e5_0 = "true"
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

            # set the value of variable 'assertion_operand_1937299a1fd9496fb873e66781800400_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1937299a1fd9496fb873e66781800400_0' to true")
            assertion_operand_1937299a1fd9496fb873e66781800400_0 = "true"
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

            # set the value of variable 'assertion_operand_fdf51ee359434abc81da413baed220cd_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_fdf51ee359434abc81da413baed220cd_0' to true")
            assertion_operand_fdf51ee359434abc81da413baed220cd_0 = "true"
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

            # set the value of variable 'assertion_operand_52cded3e9d184d86ae923fe0c6eeaef4_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_52cded3e9d184d86ae923fe0c6eeaef4_0' to true")
            assertion_operand_52cded3e9d184d86ae923fe0c6eeaef4_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Mobile' visibility
            lambda_hooks(driver, "Query 'Mobile' visibility")
            Mobile_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Mobile_visible, dict):
                Mobile_visible = Mobile_visible.get("vision_query")
            user_variables["Mobile_visible"] =  Mobile_visible
            print("Mobile_visible:", Mobile_visible)

            # set the value of variable 'assertion_operand_c06633847df84e3a9cc6035bbb23765f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c06633847df84e3a9cc6035bbb23765f_0' to true")
            assertion_operand_c06633847df84e3a9cc6035bbb23765f_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'Work Telephone' visibility
            lambda_hooks(driver, "Query 'Work Telephone' visibility")
            Work_Telephone_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(Work_Telephone_visible, dict):
                Work_Telephone_visible = Work_Telephone_visible.get("vision_query")
            user_variables["Work_Telephone_visible"] =  Work_Telephone_visible
            print("Work_Telephone_visible:", Work_Telephone_visible)

            # set the value of variable 'assertion_operand_c7896cdbe3d947ea84e9076556058a03_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c7896cdbe3d947ea84e9076556058a03_0' to true")
            assertion_operand_c7896cdbe3d947ea84e9076556058a03_0 = "true"
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

            # set the value of variable 'assertion_operand_73e29da11ae249b4b4f3cf1cc9f0b939_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_73e29da11ae249b4b4f3cf1cc9f0b939_0' to true")
            assertion_operand_73e29da11ae249b4b4f3cf1cc9f0b939_0 = "true"
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

            # set the value of variable 'assertion_operand_74103f6f3e664277b258189906c2c8f6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_74103f6f3e664277b258189906c2c8f6_0' to true")
            assertion_operand_74103f6f3e664277b258189906c2c8f6_0 = "true"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
            print("assertion_result: ", assertion_result)

            # Query 'Description' visibility
            lambda_hooks(driver, "Query 'Description' visibility")
            Description_visible = vision_query(driver = driver, operation_index = str(31))
            if isinstance(Description_visible, dict):
                Description_visible = Description_visible.get("vision_query")
            user_variables["Description_visible"] =  Description_visible
            print("Description_visible:", Description_visible)

            # set the value of variable 'assertion_operand_0f840583910e433d974a0778e072402c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0f840583910e433d974a0778e072402c_0' to true")
            assertion_operand_0f840583910e433d974a0778e072402c_0 = "true"
            ui_action(driver = driver, operation_index = str(32))
            assertion_result = ui_action(driver=driver, operation_index=str(33))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Size'
            lambda_hooks(driver, "Query visibility of text 'Size'")
            Size_visible = vision_query(driver = driver, operation_index = str(34))
            if isinstance(Size_visible, dict):
                Size_visible = Size_visible.get("vision_query")
            user_variables["Size_visible"] =  Size_visible
            print("Size_visible:", Size_visible)

            # set the value of variable 'assertion_operand_f5e48d207cf54422a1a44f21295a9104_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f5e48d207cf54422a1a44f21295a9104_0' to true")
            assertion_operand_f5e48d207cf54422a1a44f21295a9104_0 = "true"
            ui_action(driver = driver, operation_index = str(35))
            assertion_result = ui_action(driver=driver, operation_index=str(36))
            print("assertion_result: ", assertion_result)

            # Query 'type' text visibility
            lambda_hooks(driver, "Query 'type' text visibility")
            type_visible = vision_query(driver = driver, operation_index = str(37))
            if isinstance(type_visible, dict):
                type_visible = type_visible.get("vision_query")
            user_variables["type_visible"] =  type_visible
            print("type_visible:", type_visible)

            # set the value of variable 'assertion_operand_752b2469e0334154b709796cab51147e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_752b2469e0334154b709796cab51147e_0' to true")
            assertion_operand_752b2469e0334154b709796cab51147e_0 = "true"
            ui_action(driver = driver, operation_index = str(38))
            assertion_result = ui_action(driver=driver, operation_index=str(39))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Date Added'
            lambda_hooks(driver, "Query visibility of text 'Date Added'")
            date_added_visible = vision_query(driver = driver, operation_index = str(40))
            if isinstance(date_added_visible, dict):
                date_added_visible = date_added_visible.get("vision_query")
            user_variables["date_added_visible"] =  date_added_visible
            print("date_added_visible:", date_added_visible)

            # set the value of variable 'assertion_operand_111cdcd5b8594d08ad95d58543d41379_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_111cdcd5b8594d08ad95d58543d41379_0' to true")
            assertion_operand_111cdcd5b8594d08ad95d58543d41379_0 = "true"
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

            # set the value of variable 'assertion_operand_f3ef2e7946e34c5ba1958e6d9e517ff2_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f3ef2e7946e34c5ba1958e6d9e517ff2_0' to true")
            assertion_operand_f3ef2e7946e34c5ba1958e6d9e517ff2_0 = "true"
            ui_action(driver = driver, operation_index = str(44))
            assertion_result = ui_action(driver=driver, operation_index=str(45))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible_f7a7b2 = vision_query(driver = driver, operation_index = str(46))
            if isinstance(Actions_visible_f7a7b2, dict):
                Actions_visible_f7a7b2 = Actions_visible_f7a7b2.get("vision_query")
            user_variables["Actions_visible_f7a7b2"] =  Actions_visible_f7a7b2
            print("Actions_visible_f7a7b2:", Actions_visible_f7a7b2)

            # set the value of variable 'assertion_operand_a29dafafd8154824a871d6f23e6d6ae9_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a29dafafd8154824a871d6f23e6d6ae9_0' to true")
            assertion_operand_a29dafafd8154824a871d6f23e6d6ae9_0 = "true"
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
