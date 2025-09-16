
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

            # Click 'My Info' from the left side panel
            lambda_hooks(driver, "Click 'My Info' from the left side panel")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on <a>
            lambda_hooks(driver, "Click on <a>")
            ui_action(driver = driver, operation_index = str(2))

            # scroll down 100 px
            lambda_hooks(driver, "scroll down 100 px")
            ui_action(driver = driver, operation_index = str(3))

            # Click on the Add button in the Languages section
            lambda_hooks(driver, "Click on the Add button in the Languages section")
            ui_action(driver = driver, operation_index = str(4))

            # scroll down 200 px
            lambda_hooks(driver, "scroll down 200 px")
            ui_action(driver = driver, operation_index = str(5))

            # Query 'Add Language' visibility
            lambda_hooks(driver, "Query 'Add Language' visibility")
            Add_Language_visible = vision_query(driver = driver, operation_index = str(6))
            if isinstance(Add_Language_visible, dict):
                Add_Language_visible = Add_Language_visible.get("vision_query")
            user_variables["Add_Language_visible"] =  Add_Language_visible
            print("Add_Language_visible:", Add_Language_visible)

            # set the value of variable 'assertion_operand_ac0d1f518b854bc6bd53f9229678c4b1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ac0d1f518b854bc6bd53f9229678c4b1_0' to true")
            assertion_operand_ac0d1f518b854bc6bd53f9229678c4b1_0 = "true"
            ui_action(driver = driver, operation_index = str(7))
            assertion_result = ui_action(driver=driver, operation_index=str(8))
            print("assertion_result: ", assertion_result)

            # Query 'Language' text visibility
            lambda_hooks(driver, "Query 'Language' text visibility")
            Language_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(Language_visible, dict):
                Language_visible = Language_visible.get("vision_query")
            user_variables["Language_visible"] =  Language_visible
            print("Language_visible:", Language_visible)

            # set the value of variable 'assertion_operand_8ba26f8d8706452f87e1f4940eb692a5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8ba26f8d8706452f87e1f4940eb692a5_0' to true")
            assertion_operand_8ba26f8d8706452f87e1f4940eb692a5_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Query 'Fluency' text visibility
            lambda_hooks(driver, "Query 'Fluency' text visibility")
            Fluency_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Fluency_visible, dict):
                Fluency_visible = Fluency_visible.get("vision_query")
            user_variables["Fluency_visible"] =  Fluency_visible
            print("Fluency_visible:", Fluency_visible)

            # set the value of variable 'assertion_operand_0d70a13e40964015b8877363e8a9164c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0d70a13e40964015b8877363e8a9164c_0' to true")
            assertion_operand_0d70a13e40964015b8877363e8a9164c_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query 'Competency' text visibility
            lambda_hooks(driver, "Query 'Competency' text visibility")
            Competency_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(Competency_visible, dict):
                Competency_visible = Competency_visible.get("vision_query")
            user_variables["Competency_visible"] =  Competency_visible
            print("Competency_visible:", Competency_visible)

            # set the value of variable 'assertion_operand_0f6461581cfb4719935db88a93a674b6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0f6461581cfb4719935db88a93a674b6_0' to true")
            assertion_operand_0f6461581cfb4719935db88a93a674b6_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Query 'Comments' text visibility
            lambda_hooks(driver, "Query 'Comments' text visibility")
            Comments_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(Comments_visible, dict):
                Comments_visible = Comments_visible.get("vision_query")
            user_variables["Comments_visible"] =  Comments_visible
            print("Comments_visible:", Comments_visible)

            # set the value of variable 'assertion_operand_95be45d1f8ed4ac0bc1e000c4311b2d7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_95be45d1f8ed4ac0bc1e000c4311b2d7_0' to true")
            assertion_operand_95be45d1f8ed4ac0bc1e000c4311b2d7_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
            print("assertion_result: ", assertion_result)

            # Query 'Cancel' text visibility
            lambda_hooks(driver, "Query 'Cancel' text visibility")
            Cancel_visible = vision_query(driver = driver, operation_index = str(21))
            if isinstance(Cancel_visible, dict):
                Cancel_visible = Cancel_visible.get("vision_query")
            user_variables["Cancel_visible"] =  Cancel_visible
            print("Cancel_visible:", Cancel_visible)

            # set the value of variable 'assertion_operand_a297c1f8885c4ec49ab26b73c6cea246_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a297c1f8885c4ec49ab26b73c6cea246_0' to true")
            assertion_operand_a297c1f8885c4ec49ab26b73c6cea246_0 = "true"
            ui_action(driver = driver, operation_index = str(22))
            assertion_result = ui_action(driver=driver, operation_index=str(23))
            print("assertion_result: ", assertion_result)

            # Query 'Save' text visibility
            lambda_hooks(driver, "Query 'Save' text visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(24))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_65a03598ae7c443596232f86880db413_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_65a03598ae7c443596232f86880db413_0' to true")
            assertion_operand_65a03598ae7c443596232f86880db413_0 = "true"
            ui_action(driver = driver, operation_index = str(25))
            assertion_result = ui_action(driver=driver, operation_index=str(26))
            print("assertion_result: ", assertion_result)

            # scroll down 100 px
            lambda_hooks(driver, "scroll down 100 px")
            ui_action(driver = driver, operation_index = str(27))

            # Click 'Save' button
            lambda_hooks(driver, "Click 'Save' button")
            ui_action(driver = driver, operation_index = str(28))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(29))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_31e765cb20b04f5bb889846507e9024d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_31e765cb20b04f5bb889846507e9024d_0' to true")
            assertion_operand_31e765cb20b04f5bb889846507e9024d_0 = "true"
            ui_action(driver = driver, operation_index = str(30))
            assertion_result = ui_action(driver=driver, operation_index=str(31))
            print("assertion_result: ", assertion_result)

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(32))

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
