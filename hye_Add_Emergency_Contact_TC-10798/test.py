
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

            # Click on the plus icon next to Assigned Emergency Contacts
            lambda_hooks(driver, "Click on the plus icon next to Assigned Emergency Contacts")
            ui_action(driver = driver, operation_index = str(4))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(5))

            # Query 'Save Emergency Contact' visibility
            lambda_hooks(driver, "Query 'Save Emergency Contact' visibility")
            Save_Emergency_Contact_visible = vision_query(driver = driver, operation_index = str(6))
            if isinstance(Save_Emergency_Contact_visible, dict):
                Save_Emergency_Contact_visible = Save_Emergency_Contact_visible.get("vision_query")
            user_variables["Save_Emergency_Contact_visible"] =  Save_Emergency_Contact_visible
            print("Save_Emergency_Contact_visible:", Save_Emergency_Contact_visible)

            # set the value of variable 'assertion_operand_d994300a6264476b9020ee10217ce581_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d994300a6264476b9020ee10217ce581_0' to true")
            assertion_operand_d994300a6264476b9020ee10217ce581_0 = "true"
            ui_action(driver = driver, operation_index = str(7))
            assertion_result = ui_action(driver=driver, operation_index=str(8))
            print("assertion_result: ", assertion_result)

            # Query 'Name' visibility
            lambda_hooks(driver, "Query 'Name' visibility")
            Name_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(Name_visible, dict):
                Name_visible = Name_visible.get("vision_query")
            user_variables["Name_visible"] =  Name_visible
            print("Name_visible:", Name_visible)

            # set the value of variable 'assertion_operand_3b90e833d0044c7e909f53ceb0e6c25d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3b90e833d0044c7e909f53ceb0e6c25d_0' to true")
            assertion_operand_3b90e833d0044c7e909f53ceb0e6c25d_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Query 'Relationship' text visibility
            lambda_hooks(driver, "Query 'Relationship' text visibility")
            Relationship_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Relationship_visible, dict):
                Relationship_visible = Relationship_visible.get("vision_query")
            user_variables["Relationship_visible"] =  Relationship_visible
            print("Relationship_visible:", Relationship_visible)

            # set the value of variable 'assertion_operand_98e5c94a15914d15b462f1a4f9fac3b1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_98e5c94a15914d15b462f1a4f9fac3b1_0' to true")
            assertion_operand_98e5c94a15914d15b462f1a4f9fac3b1_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query 'Home Telephone' visibility
            lambda_hooks(driver, "Query 'Home Telephone' visibility")
            Home_Telephone_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(Home_Telephone_visible, dict):
                Home_Telephone_visible = Home_Telephone_visible.get("vision_query")
            user_variables["Home_Telephone_visible"] =  Home_Telephone_visible
            print("Home_Telephone_visible:", Home_Telephone_visible)

            # set the value of variable 'assertion_operand_2801a4cda330446c8ffbc16f183a688d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2801a4cda330446c8ffbc16f183a688d_0' to true")
            assertion_operand_2801a4cda330446c8ffbc16f183a688d_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Query 'Mobile' text visibility
            lambda_hooks(driver, "Query 'Mobile' text visibility")
            Mobile_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(Mobile_visible, dict):
                Mobile_visible = Mobile_visible.get("vision_query")
            user_variables["Mobile_visible"] =  Mobile_visible
            print("Mobile_visible:", Mobile_visible)

            # set the value of variable 'assertion_operand_f59da144cd7949a784ec4c108e9fce66_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f59da144cd7949a784ec4c108e9fce66_0' to true")
            assertion_operand_f59da144cd7949a784ec4c108e9fce66_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
            print("assertion_result: ", assertion_result)

            # Query 'Work Telephone' visibility
            lambda_hooks(driver, "Query 'Work Telephone' visibility")
            Work_Telephone_visible = vision_query(driver = driver, operation_index = str(21))
            if isinstance(Work_Telephone_visible, dict):
                Work_Telephone_visible = Work_Telephone_visible.get("vision_query")
            user_variables["Work_Telephone_visible"] =  Work_Telephone_visible
            print("Work_Telephone_visible:", Work_Telephone_visible)

            # set the value of variable 'assertion_operand_a301096585be4eb0aaf168cf76a804b1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a301096585be4eb0aaf168cf76a804b1_0' to true")
            assertion_operand_a301096585be4eb0aaf168cf76a804b1_0 = "true"
            ui_action(driver = driver, operation_index = str(22))
            assertion_result = ui_action(driver=driver, operation_index=str(23))
            print("assertion_result: ", assertion_result)

            # Query 'Cancel' text visibility
            lambda_hooks(driver, "Query 'Cancel' text visibility")
            Cancel_visible = vision_query(driver = driver, operation_index = str(24))
            if isinstance(Cancel_visible, dict):
                Cancel_visible = Cancel_visible.get("vision_query")
            user_variables["Cancel_visible"] =  Cancel_visible
            print("Cancel_visible:", Cancel_visible)

            # set the value of variable 'assertion_operand_8051940618044d2b94cf82f8f67c0b2e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8051940618044d2b94cf82f8f67c0b2e_0' to true")
            assertion_operand_8051940618044d2b94cf82f8f67c0b2e_0 = "true"
            ui_action(driver = driver, operation_index = str(25))
            assertion_result = ui_action(driver=driver, operation_index=str(26))
            print("assertion_result: ", assertion_result)

            # Query 'Save' text visibility
            lambda_hooks(driver, "Query 'Save' text visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(27))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_19140c6b949e4111ba92a8ef5099fcff_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_19140c6b949e4111ba92a8ef5099fcff_0' to true")
            assertion_operand_19140c6b949e4111ba92a8ef5099fcff_0 = "true"
            ui_action(driver = driver, operation_index = str(28))
            assertion_result = ui_action(driver=driver, operation_index=str(29))
            print("assertion_result: ", assertion_result)

            # Click 'Save' button
            lambda_hooks(driver, "Click 'Save' button")
            ui_action(driver = driver, operation_index = str(30))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(31))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_b47327b5bc2a4acb97bb91878587ffa3_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b47327b5bc2a4acb97bb91878587ffa3_0' to true")
            assertion_operand_b47327b5bc2a4acb97bb91878587ffa3_0 = "true"
            ui_action(driver = driver, operation_index = str(32))
            assertion_result = ui_action(driver=driver, operation_index=str(33))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'At least one phone number is required'
            lambda_hooks(driver, "Query visibility of text 'At least one phone number is required'")
            phone_number_error_visible = vision_query(driver = driver, operation_index = str(34))
            if isinstance(phone_number_error_visible, dict):
                phone_number_error_visible = phone_number_error_visible.get("vision_query")
            user_variables["phone_number_error_visible"] =  phone_number_error_visible
            print("phone_number_error_visible:", phone_number_error_visible)

            # set the value of variable 'assertion_operand_1a9dfc36910a428ca1528c14325406db_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1a9dfc36910a428ca1528c14325406db_0' to true")
            assertion_operand_1a9dfc36910a428ca1528c14325406db_0 = "true"
            ui_action(driver = driver, operation_index = str(35))
            assertion_result = ui_action(driver=driver, operation_index=str(36))
            print("assertion_result: ", assertion_result)

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(37))

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
