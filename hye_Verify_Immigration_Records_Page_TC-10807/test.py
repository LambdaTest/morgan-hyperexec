
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

            # Click on 'Immigration' tab in the left side menu under 'My Info'
            lambda_hooks(driver, "Click on 'Immigration' tab in the left side menu under 'My Info'")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Query 'Assigned Immigration Records' visibility
            lambda_hooks(driver, "Query 'Assigned Immigration Records' visibility")
            Assigned_Immigration_Records_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(Assigned_Immigration_Records_visible, dict):
                Assigned_Immigration_Records_visible = Assigned_Immigration_Records_visible.get("vision_query")
            user_variables["Assigned_Immigration_Records_visible"] =  Assigned_Immigration_Records_visible
            print("Assigned_Immigration_Records_visible:", Assigned_Immigration_Records_visible)

            # set the value of variable 'assertion_operand_ada58133966145429c03e0e64c48ce7c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ada58133966145429c03e0e64c48ce7c_0' to true")
            assertion_operand_ada58133966145429c03e0e64c48ce7c_0 = "true"
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

            # set the value of variable 'assertion_operand_86f29d1b89354b278bc0547da7d31894_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_86f29d1b89354b278bc0547da7d31894_0' to true")
            assertion_operand_86f29d1b89354b278bc0547da7d31894_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Document' text visibility
            lambda_hooks(driver, "Query 'Document' text visibility")
            Document_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Document_visible, dict):
                Document_visible = Document_visible.get("vision_query")
            user_variables["Document_visible"] =  Document_visible
            print("Document_visible:", Document_visible)

            # set the value of variable 'assertion_operand_5d875d50e6fb4534b9de646fdef96297_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5d875d50e6fb4534b9de646fdef96297_0' to true")
            assertion_operand_5d875d50e6fb4534b9de646fdef96297_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Number' text visibility
            lambda_hooks(driver, "Query 'Number' text visibility")
            Number_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Number_visible, dict):
                Number_visible = Number_visible.get("vision_query")
            user_variables["Number_visible"] =  Number_visible
            print("Number_visible:", Number_visible)

            # set the value of variable 'assertion_operand_f9a0194e5bd74bf88abde5312d6642d6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f9a0194e5bd74bf88abde5312d6642d6_0' to true")
            assertion_operand_f9a0194e5bd74bf88abde5312d6642d6_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Issued By' text visibility
            lambda_hooks(driver, "Query 'Issued By' text visibility")
            Issued_By_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Issued_By_visible, dict):
                Issued_By_visible = Issued_By_visible.get("vision_query")
            user_variables["Issued_By_visible"] =  Issued_By_visible
            print("Issued_By_visible:", Issued_By_visible)

            # set the value of variable 'assertion_operand_733a88edcdae4401b85a2ab118fb3f36_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_733a88edcdae4401b85a2ab118fb3f36_0' to true")
            assertion_operand_733a88edcdae4401b85a2ab118fb3f36_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Issued Date' visibility
            lambda_hooks(driver, "Query 'Issued Date' visibility")
            Issued_Date_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Issued_Date_visible, dict):
                Issued_Date_visible = Issued_Date_visible.get("vision_query")
            user_variables["Issued_Date_visible"] =  Issued_Date_visible
            print("Issued_Date_visible:", Issued_Date_visible)

            # set the value of variable 'assertion_operand_efbd1a83d3f04f4fae1d8e686124619c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_efbd1a83d3f04f4fae1d8e686124619c_0' to true")
            assertion_operand_efbd1a83d3f04f4fae1d8e686124619c_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'Expiry Date' visibility
            lambda_hooks(driver, "Query 'Expiry Date' visibility")
            Expiry_Date_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(Expiry_Date_visible, dict):
                Expiry_Date_visible = Expiry_Date_visible.get("vision_query")
            user_variables["Expiry_Date_visible"] =  Expiry_Date_visible
            print("Expiry_Date_visible:", Expiry_Date_visible)

            # set the value of variable 'assertion_operand_bfccfec44f994be3b12bda1ce2cf48cf_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_bfccfec44f994be3b12bda1ce2cf48cf_0' to true")
            assertion_operand_bfccfec44f994be3b12bda1ce2cf48cf_0 = "true"
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

            # set the value of variable 'assertion_operand_6cd651a48bb5436f83434f64c97f26f1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6cd651a48bb5436f83434f64c97f26f1_0' to true")
            assertion_operand_6cd651a48bb5436f83434f64c97f26f1_0 = "true"
            ui_action(driver = driver, operation_index = str(26))
            assertion_result = ui_action(driver=driver, operation_index=str(27))
            print("assertion_result: ", assertion_result)

            # Query 'Attachments' visibility
            lambda_hooks(driver, "Query 'Attachments' visibility")
            Attachments_visible = vision_query(driver = driver, operation_index = str(28))
            if isinstance(Attachments_visible, dict):
                Attachments_visible = Attachments_visible.get("vision_query")
            user_variables["Attachments_visible"] =  Attachments_visible
            print("Attachments_visible:", Attachments_visible)

            # set the value of variable 'assertion_operand_67c8e6ecd0314fae967fe91087ebc8c0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_67c8e6ecd0314fae967fe91087ebc8c0_0' to true")
            assertion_operand_67c8e6ecd0314fae967fe91087ebc8c0_0 = "true"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
            print("assertion_result: ", assertion_result)

            # Query 'File Name' visibility
            lambda_hooks(driver, "Query 'File Name' visibility")
            File_Name_visible = vision_query(driver = driver, operation_index = str(31))
            if isinstance(File_Name_visible, dict):
                File_Name_visible = File_Name_visible.get("vision_query")
            user_variables["File_Name_visible"] =  File_Name_visible
            print("File_Name_visible:", File_Name_visible)

            # set the value of variable 'assertion_operand_0725afe218fe4376829ab05fe2e3d4e7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0725afe218fe4376829ab05fe2e3d4e7_0' to true")
            assertion_operand_0725afe218fe4376829ab05fe2e3d4e7_0 = "true"
            ui_action(driver = driver, operation_index = str(32))
            assertion_result = ui_action(driver=driver, operation_index=str(33))
            print("assertion_result: ", assertion_result)

            # Query 'Description' visibility
            lambda_hooks(driver, "Query 'Description' visibility")
            Description_visible = vision_query(driver = driver, operation_index = str(34))
            if isinstance(Description_visible, dict):
                Description_visible = Description_visible.get("vision_query")
            user_variables["Description_visible"] =  Description_visible
            print("Description_visible:", Description_visible)

            # set the value of variable 'assertion_operand_3f3ce9d7d92b43bcabef997f1bc3580f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3f3ce9d7d92b43bcabef997f1bc3580f_0' to true")
            assertion_operand_3f3ce9d7d92b43bcabef997f1bc3580f_0 = "true"
            ui_action(driver = driver, operation_index = str(35))
            assertion_result = ui_action(driver=driver, operation_index=str(36))
            print("assertion_result: ", assertion_result)

            # Query 'Size' text visibility
            lambda_hooks(driver, "Query 'Size' text visibility")
            Size_visible = vision_query(driver = driver, operation_index = str(37))
            if isinstance(Size_visible, dict):
                Size_visible = Size_visible.get("vision_query")
            user_variables["Size_visible"] =  Size_visible
            print("Size_visible:", Size_visible)

            # set the value of variable 'assertion_operand_d7c10acd3a4d46289d2214e8a386a67a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d7c10acd3a4d46289d2214e8a386a67a_0' to true")
            assertion_operand_d7c10acd3a4d46289d2214e8a386a67a_0 = "true"
            ui_action(driver = driver, operation_index = str(38))
            assertion_result = ui_action(driver=driver, operation_index=str(39))
            print("assertion_result: ", assertion_result)

            # Query 'Type' text visibility
            lambda_hooks(driver, "Query 'Type' text visibility")
            Type_visible = vision_query(driver = driver, operation_index = str(40))
            if isinstance(Type_visible, dict):
                Type_visible = Type_visible.get("vision_query")
            user_variables["Type_visible"] =  Type_visible
            print("Type_visible:", Type_visible)

            # set the value of variable 'assertion_operand_d38724007bdb49c192e1959a4418fe37_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d38724007bdb49c192e1959a4418fe37_0' to true")
            assertion_operand_d38724007bdb49c192e1959a4418fe37_0 = "true"
            ui_action(driver = driver, operation_index = str(41))
            assertion_result = ui_action(driver=driver, operation_index=str(42))
            print("assertion_result: ", assertion_result)

            # Query 'Date Added' text visibility
            lambda_hooks(driver, "Query 'Date Added' text visibility")
            date_added_visible = vision_query(driver = driver, operation_index = str(43))
            if isinstance(date_added_visible, dict):
                date_added_visible = date_added_visible.get("vision_query")
            user_variables["date_added_visible"] =  date_added_visible
            print("date_added_visible:", date_added_visible)

            # set the value of variable 'assertion_operand_38a773184c3c481c8d63d669f0895171_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_38a773184c3c481c8d63d669f0895171_0' to true")
            assertion_operand_38a773184c3c481c8d63d669f0895171_0 = "true"
            ui_action(driver = driver, operation_index = str(44))
            assertion_result = ui_action(driver=driver, operation_index=str(45))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Added By'
            lambda_hooks(driver, "Query visibility of text 'Added By'")
            Added_By_visible = vision_query(driver = driver, operation_index = str(46))
            if isinstance(Added_By_visible, dict):
                Added_By_visible = Added_By_visible.get("vision_query")
            user_variables["Added_By_visible"] =  Added_By_visible
            print("Added_By_visible:", Added_By_visible)

            # set the value of variable 'assertion_operand_1e6ab15acddc401a99a1888d00a7ae7c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1e6ab15acddc401a99a1888d00a7ae7c_0' to true")
            assertion_operand_1e6ab15acddc401a99a1888d00a7ae7c_0 = "true"
            ui_action(driver = driver, operation_index = str(47))
            assertion_result = ui_action(driver=driver, operation_index=str(48))
            print("assertion_result: ", assertion_result)

            # Query '+ Add' text visibility
            lambda_hooks(driver, "Query '+ Add' text visibility")
            add_text_visible = vision_query(driver = driver, operation_index = str(49))
            if isinstance(add_text_visible, dict):
                add_text_visible = add_text_visible.get("vision_query")
            user_variables["add_text_visible"] =  add_text_visible
            print("add_text_visible:", add_text_visible)

            # set the value of variable 'assertion_operand_14fe0ce6837748b49ed9b31ce7556ad5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_14fe0ce6837748b49ed9b31ce7556ad5_0' to true")
            assertion_operand_14fe0ce6837748b49ed9b31ce7556ad5_0 = "true"
            ui_action(driver = driver, operation_index = str(50))
            assertion_result = ui_action(driver=driver, operation_index=str(51))
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
