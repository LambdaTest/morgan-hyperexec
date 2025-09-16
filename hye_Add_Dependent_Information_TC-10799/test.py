
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

            # Click on 'Dependents' tab in the left side menu under Emergency Contacts
            lambda_hooks(driver, "Click on 'Dependents' tab in the left side menu under Emergency Contacts")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on Add button in Assigned Dependents section
            lambda_hooks(driver, "Click on Add button in Assigned Dependents section")
            ui_action(driver = driver, operation_index = str(4))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(5))

            # Query 'Name' visibility
            lambda_hooks(driver, "Query 'Name' visibility")
            Name_visible = vision_query(driver = driver, operation_index = str(6))
            if isinstance(Name_visible, dict):
                Name_visible = Name_visible.get("vision_query")
            user_variables["Name_visible"] =  Name_visible
            print("Name_visible:", Name_visible)

            # set the value of variable 'assertion_operand_ff639d5fb8f04eeaa2c2b6632fd35534_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ff639d5fb8f04eeaa2c2b6632fd35534_0' to true")
            assertion_operand_ff639d5fb8f04eeaa2c2b6632fd35534_0 = "true"
            ui_action(driver = driver, operation_index = str(7))
            assertion_result = ui_action(driver=driver, operation_index=str(8))
            print("assertion_result: ", assertion_result)

            # Query 'Relationship' text visibility
            lambda_hooks(driver, "Query 'Relationship' text visibility")
            Relationship_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(Relationship_visible, dict):
                Relationship_visible = Relationship_visible.get("vision_query")
            user_variables["Relationship_visible"] =  Relationship_visible
            print("Relationship_visible:", Relationship_visible)

            # set the value of variable 'assertion_operand_3347248915b64cebb3aa178c26fb5658_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3347248915b64cebb3aa178c26fb5658_0' to true")
            assertion_operand_3347248915b64cebb3aa178c26fb5658_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Query 'Date of Birth' visibility
            lambda_hooks(driver, "Query 'Date of Birth' visibility")
            Date_of_Birth_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Date_of_Birth_visible, dict):
                Date_of_Birth_visible = Date_of_Birth_visible.get("vision_query")
            user_variables["Date_of_Birth_visible"] =  Date_of_Birth_visible
            print("Date_of_Birth_visible:", Date_of_Birth_visible)

            # set the value of variable 'assertion_operand_adf1901d767c48b4b6d2ca1fa52565e6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_adf1901d767c48b4b6d2ca1fa52565e6_0' to true")
            assertion_operand_adf1901d767c48b4b6d2ca1fa52565e6_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query 'Save' text visibility
            lambda_hooks(driver, "Query 'Save' text visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_c1a7a176216641be92a9bafbd6a8c54b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c1a7a176216641be92a9bafbd6a8c54b_0' to true")
            assertion_operand_c1a7a176216641be92a9bafbd6a8c54b_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Query 'Cancel' text visibility
            lambda_hooks(driver, "Query 'Cancel' text visibility")
            Cancel_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(Cancel_visible, dict):
                Cancel_visible = Cancel_visible.get("vision_query")
            user_variables["Cancel_visible"] =  Cancel_visible
            print("Cancel_visible:", Cancel_visible)

            # set the value of variable 'assertion_operand_1d354c570e9043f38c10f7e43ffb397e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1d354c570e9043f38c10f7e43ffb397e_0' to true")
            assertion_operand_1d354c570e9043f38c10f7e43ffb397e_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
            print("assertion_result: ", assertion_result)

            # Click 'Save' button
            lambda_hooks(driver, "Click 'Save' button")
            ui_action(driver = driver, operation_index = str(21))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_99508e2f540048249b1ae6bd8721b6d7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_99508e2f540048249b1ae6bd8721b6d7_0' to true")
            assertion_operand_99508e2f540048249b1ae6bd8721b6d7_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(25))

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
