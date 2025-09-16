
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

            # Click on 'My Info' menu item in the left side menu
            lambda_hooks(driver, "Click on 'My Info' menu item in the left side menu")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Qualifications' tab in the left side menu
            lambda_hooks(driver, "Click on 'Qualifications' tab in the left side menu")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # scroll down once
            lambda_hooks(driver, "scroll down once")
            ui_action(driver = driver, operation_index = str(4))

            # Query 'Languages' visibility
            lambda_hooks(driver, "Query 'Languages' visibility")
            Languages_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(Languages_visible, dict):
                Languages_visible = Languages_visible.get("vision_query")
            user_variables["Languages_visible"] =  Languages_visible
            print("Languages_visible:", Languages_visible)

            # set the value of variable 'assertion_operand_4edcbda4f141471c8f0ef479ae76ca93_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_4edcbda4f141471c8f0ef479ae76ca93_0' to true")
            assertion_operand_4edcbda4f141471c8f0ef479ae76ca93_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query 'No Records Found' text visibility
            lambda_hooks(driver, "Query 'No Records Found' text visibility")
            no_records_found_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(no_records_found_visible, dict):
                no_records_found_visible = no_records_found_visible.get("vision_query")
            user_variables["no_records_found_visible"] =  no_records_found_visible
            print("no_records_found_visible:", no_records_found_visible)

            # set the value of variable 'assertion_operand_c7b3c6d165c64fcabba1cc87caa66b37_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c7b3c6d165c64fcabba1cc87caa66b37_0' to true")
            assertion_operand_c7b3c6d165c64fcabba1cc87caa66b37_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Language' text visibility
            lambda_hooks(driver, "Query 'Language' text visibility")
            Language_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Language_visible, dict):
                Language_visible = Language_visible.get("vision_query")
            user_variables["Language_visible"] =  Language_visible
            print("Language_visible:", Language_visible)

            # set the value of variable 'assertion_operand_b7e2f87745424b42ae1682b0779d3679_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b7e2f87745424b42ae1682b0779d3679_0' to true")
            assertion_operand_b7e2f87745424b42ae1682b0779d3679_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query 'Fluency' text visibility
            lambda_hooks(driver, "Query 'Fluency' text visibility")
            Fluency_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(Fluency_visible, dict):
                Fluency_visible = Fluency_visible.get("vision_query")
            user_variables["Fluency_visible"] =  Fluency_visible
            print("Fluency_visible:", Fluency_visible)

            # set the value of variable 'assertion_operand_f0f062b1dd8b40bc81557f8bb147470d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f0f062b1dd8b40bc81557f8bb147470d_0' to true")
            assertion_operand_f0f062b1dd8b40bc81557f8bb147470d_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'Competency' text visibility
            lambda_hooks(driver, "Query 'Competency' text visibility")
            Competency_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(Competency_visible, dict):
                Competency_visible = Competency_visible.get("vision_query")
            user_variables["Competency_visible"] =  Competency_visible
            print("Competency_visible:", Competency_visible)

            # set the value of variable 'assertion_operand_f4bdc0ab83cd49d0846d46bed51ea1ef_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f4bdc0ab83cd49d0846d46bed51ea1ef_0' to true")
            assertion_operand_f4bdc0ab83cd49d0846d46bed51ea1ef_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'Comments' text visibility
            lambda_hooks(driver, "Query 'Comments' text visibility")
            Comments_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(Comments_visible, dict):
                Comments_visible = Comments_visible.get("vision_query")
            user_variables["Comments_visible"] =  Comments_visible
            print("Comments_visible:", Comments_visible)

            # set the value of variable 'assertion_operand_d3c25d604f334f0492cac110e2459297_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d3c25d604f334f0492cac110e2459297_0' to true")
            assertion_operand_d3c25d604f334f0492cac110e2459297_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(Actions_visible, dict):
                Actions_visible = Actions_visible.get("vision_query")
            user_variables["Actions_visible"] =  Actions_visible
            print("Actions_visible:", Actions_visible)

            # set the value of variable 'assertion_operand_1399974bdf6d4531b25c3d942ece00a8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1399974bdf6d4531b25c3d942ece00a8_0' to true")
            assertion_operand_1399974bdf6d4531b25c3d942ece00a8_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
            print("assertion_result: ", assertion_result)

            # Query 'License' text visibility
            lambda_hooks(driver, "Query 'License' text visibility")
            License_visible = vision_query(driver = driver, operation_index = str(26))
            if isinstance(License_visible, dict):
                License_visible = License_visible.get("vision_query")
            user_variables["License_visible"] =  License_visible
            print("License_visible:", License_visible)

            # set the value of variable 'assertion_operand_28507f793f5b4c46af3a97538a2c3f6e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_28507f793f5b4c46af3a97538a2c3f6e_0' to true")
            assertion_operand_28507f793f5b4c46af3a97538a2c3f6e_0 = "true"
            ui_action(driver = driver, operation_index = str(27))
            assertion_result = ui_action(driver=driver, operation_index=str(28))
            print("assertion_result: ", assertion_result)

            # Query 'License Type' visibility
            lambda_hooks(driver, "Query 'License Type' visibility")
            License_Type_visible = vision_query(driver = driver, operation_index = str(29))
            if isinstance(License_Type_visible, dict):
                License_Type_visible = License_Type_visible.get("vision_query")
            user_variables["License_Type_visible"] =  License_Type_visible
            print("License_Type_visible:", License_Type_visible)

            # set the value of variable 'assertion_operand_43b7ca82e4b948d6849abbe6e2950daa_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_43b7ca82e4b948d6849abbe6e2950daa_0' to true")
            assertion_operand_43b7ca82e4b948d6849abbe6e2950daa_0 = "true"
            ui_action(driver = driver, operation_index = str(30))
            assertion_result = ui_action(driver=driver, operation_index=str(31))
            print("assertion_result: ", assertion_result)

            # Query 'Issued Date' text visibility
            lambda_hooks(driver, "Query 'Issued Date' text visibility")
            issued_date_visible = vision_query(driver = driver, operation_index = str(32))
            if isinstance(issued_date_visible, dict):
                issued_date_visible = issued_date_visible.get("vision_query")
            user_variables["issued_date_visible"] =  issued_date_visible
            print("issued_date_visible:", issued_date_visible)

            # set the value of variable 'assertion_operand_10ab440a85df45e499735eca6e9987fb_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_10ab440a85df45e499735eca6e9987fb_0' to true")
            assertion_operand_10ab440a85df45e499735eca6e9987fb_0 = "true"
            ui_action(driver = driver, operation_index = str(33))
            assertion_result = ui_action(driver=driver, operation_index=str(34))
            print("assertion_result: ", assertion_result)

            # Query 'Expiry Date' text visibility
            lambda_hooks(driver, "Query 'Expiry Date' text visibility")
            Expiry_Date_visible = vision_query(driver = driver, operation_index = str(35))
            if isinstance(Expiry_Date_visible, dict):
                Expiry_Date_visible = Expiry_Date_visible.get("vision_query")
            user_variables["Expiry_Date_visible"] =  Expiry_Date_visible
            print("Expiry_Date_visible:", Expiry_Date_visible)

            # set the value of variable 'assertion_operand_829595c4a91f4c6489740846666a4ff5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_829595c4a91f4c6489740846666a4ff5_0' to true")
            assertion_operand_829595c4a91f4c6489740846666a4ff5_0 = "true"
            ui_action(driver = driver, operation_index = str(36))
            assertion_result = ui_action(driver=driver, operation_index=str(37))
            print("assertion_result: ", assertion_result)

            # Query 'Attachments' text visibility
            lambda_hooks(driver, "Query 'Attachments' text visibility")
            Attachments_visible = vision_query(driver = driver, operation_index = str(38))
            if isinstance(Attachments_visible, dict):
                Attachments_visible = Attachments_visible.get("vision_query")
            user_variables["Attachments_visible"] =  Attachments_visible
            print("Attachments_visible:", Attachments_visible)

            # set the value of variable 'assertion_operand_fdee930deb1e4f69901f234828dc2920_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_fdee930deb1e4f69901f234828dc2920_0' to true")
            assertion_operand_fdee930deb1e4f69901f234828dc2920_0 = "true"
            ui_action(driver = driver, operation_index = str(39))
            assertion_result = ui_action(driver=driver, operation_index=str(40))
            print("assertion_result: ", assertion_result)

            # Query 'File Name' visibility
            lambda_hooks(driver, "Query 'File Name' visibility")
            File_Name_visible = vision_query(driver = driver, operation_index = str(41))
            if isinstance(File_Name_visible, dict):
                File_Name_visible = File_Name_visible.get("vision_query")
            user_variables["File_Name_visible"] =  File_Name_visible
            print("File_Name_visible:", File_Name_visible)

            # set the value of variable 'assertion_operand_797cdfc7eda64f0386b26d75d7a4cafd_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_797cdfc7eda64f0386b26d75d7a4cafd_0' to true")
            assertion_operand_797cdfc7eda64f0386b26d75d7a4cafd_0 = "true"
            ui_action(driver = driver, operation_index = str(42))
            assertion_result = ui_action(driver=driver, operation_index=str(43))
            print("assertion_result: ", assertion_result)

            # Query 'Description' visibility
            lambda_hooks(driver, "Query 'Description' visibility")
            Description_visible = vision_query(driver = driver, operation_index = str(44))
            if isinstance(Description_visible, dict):
                Description_visible = Description_visible.get("vision_query")
            user_variables["Description_visible"] =  Description_visible
            print("Description_visible:", Description_visible)

            # set the value of variable 'assertion_operand_d7b08f2e7f354fa7933365213cfd3e6f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d7b08f2e7f354fa7933365213cfd3e6f_0' to true")
            assertion_operand_d7b08f2e7f354fa7933365213cfd3e6f_0 = "true"
            ui_action(driver = driver, operation_index = str(45))
            assertion_result = ui_action(driver=driver, operation_index=str(46))
            print("assertion_result: ", assertion_result)

            # Query 'Size' text visibility
            lambda_hooks(driver, "Query 'Size' text visibility")
            Size_visible = vision_query(driver = driver, operation_index = str(47))
            if isinstance(Size_visible, dict):
                Size_visible = Size_visible.get("vision_query")
            user_variables["Size_visible"] =  Size_visible
            print("Size_visible:", Size_visible)

            # set the value of variable 'assertion_operand_e8b578652e3b4fef9b384a3cef7da6c2_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e8b578652e3b4fef9b384a3cef7da6c2_0' to true")
            assertion_operand_e8b578652e3b4fef9b384a3cef7da6c2_0 = "true"
            ui_action(driver = driver, operation_index = str(48))
            assertion_result = ui_action(driver=driver, operation_index=str(49))
            print("assertion_result: ", assertion_result)

            # Query 'Type' text visibility
            lambda_hooks(driver, "Query 'Type' text visibility")
            Type_visible = vision_query(driver = driver, operation_index = str(50))
            if isinstance(Type_visible, dict):
                Type_visible = Type_visible.get("vision_query")
            user_variables["Type_visible"] =  Type_visible
            print("Type_visible:", Type_visible)

            # set the value of variable 'assertion_operand_861dbd9f0ecd45fc8f77ce4e4094027e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_861dbd9f0ecd45fc8f77ce4e4094027e_0' to true")
            assertion_operand_861dbd9f0ecd45fc8f77ce4e4094027e_0 = "true"
            ui_action(driver = driver, operation_index = str(51))
            assertion_result = ui_action(driver=driver, operation_index=str(52))
            print("assertion_result: ", assertion_result)

            # Query 'Date Added' text visibility
            lambda_hooks(driver, "Query 'Date Added' text visibility")
            date_added_visible = vision_query(driver = driver, operation_index = str(53))
            if isinstance(date_added_visible, dict):
                date_added_visible = date_added_visible.get("vision_query")
            user_variables["date_added_visible"] =  date_added_visible
            print("date_added_visible:", date_added_visible)

            # set the value of variable 'assertion_operand_ca22ae1382154a8d998907cd341dfa6b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ca22ae1382154a8d998907cd341dfa6b_0' to true")
            assertion_operand_ca22ae1382154a8d998907cd341dfa6b_0 = "true"
            ui_action(driver = driver, operation_index = str(54))
            assertion_result = ui_action(driver=driver, operation_index=str(55))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Added By'
            lambda_hooks(driver, "Query visibility of text 'Added By'")
            added_by_visible = vision_query(driver = driver, operation_index = str(56))
            if isinstance(added_by_visible, dict):
                added_by_visible = added_by_visible.get("vision_query")
            user_variables["added_by_visible"] =  added_by_visible
            print("added_by_visible:", added_by_visible)

            # set the value of variable 'assertion_operand_b27376decb0640c7b185d91fede953d3_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b27376decb0640c7b185d91fede953d3_0' to true")
            assertion_operand_b27376decb0640c7b185d91fede953d3_0 = "true"
            ui_action(driver = driver, operation_index = str(57))
            assertion_result = ui_action(driver=driver, operation_index=str(58))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible_6a8e46 = vision_query(driver = driver, operation_index = str(59))
            if isinstance(Actions_visible_6a8e46, dict):
                Actions_visible_6a8e46 = Actions_visible_6a8e46.get("vision_query")
            user_variables["Actions_visible_6a8e46"] =  Actions_visible_6a8e46
            print("Actions_visible_6a8e46:", Actions_visible_6a8e46)

            # set the value of variable 'assertion_operand_5c98eb13c38e427d972672e424c54ef7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5c98eb13c38e427d972672e424c54ef7_0' to true")
            assertion_operand_5c98eb13c38e427d972672e424c54ef7_0 = "true"
            ui_action(driver = driver, operation_index = str(60))
            assertion_result = ui_action(driver=driver, operation_index=str(61))
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
