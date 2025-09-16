
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

            # Click on the Qualifications tab in left side menu
            lambda_hooks(driver, "Click on the Qualifications tab in left side menu")
            ui_action(driver = driver, operation_index = str(2))

            # Click on the Add button with plus icon
            lambda_hooks(driver, "Click on the Add button with plus icon")
            ui_action(driver = driver, operation_index = str(3))

            # scroll down 100 px
            lambda_hooks(driver, "scroll down 100 px")
            ui_action(driver = driver, operation_index = str(4))

            # Query 'Add Skills' visibility
            lambda_hooks(driver, "Query 'Add Skills' visibility")
            Add_Skills_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(Add_Skills_visible, dict):
                Add_Skills_visible = Add_Skills_visible.get("vision_query")
            user_variables["Add_Skills_visible"] =  Add_Skills_visible
            print("Add_Skills_visible:", Add_Skills_visible)

            # set the value of variable 'assertion_operand_a4f5d8c2d8fe45ea92d58929a02e0a69_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a4f5d8c2d8fe45ea92d58929a02e0a69_0' to true")
            assertion_operand_a4f5d8c2d8fe45ea92d58929a02e0a69_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query 'Skill' text visibility
            lambda_hooks(driver, "Query 'Skill' text visibility")
            Skill_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Skill_visible, dict):
                Skill_visible = Skill_visible.get("vision_query")
            user_variables["Skill_visible"] =  Skill_visible
            print("Skill_visible:", Skill_visible)

            # set the value of variable 'assertion_operand_a4bc7efbef9f4d8fb249df8409f38e0d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a4bc7efbef9f4d8fb249df8409f38e0d_0' to true")
            assertion_operand_a4bc7efbef9f4d8fb249df8409f38e0d_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Year of Experience' visibility
            lambda_hooks(driver, "Query 'Year of Experience' visibility")
            Year_of_Experience_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Year_of_Experience_visible, dict):
                Year_of_Experience_visible = Year_of_Experience_visible.get("vision_query")
            user_variables["Year_of_Experience_visible"] =  Year_of_Experience_visible
            print("Year_of_Experience_visible:", Year_of_Experience_visible)

            # set the value of variable 'assertion_operand_d4816d158fe24f10a4a384d8102a844b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d4816d158fe24f10a4a384d8102a844b_0' to true")
            assertion_operand_d4816d158fe24f10a4a384d8102a844b_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query 'Comments' text visibility
            lambda_hooks(driver, "Query 'Comments' text visibility")
            Comments_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(Comments_visible, dict):
                Comments_visible = Comments_visible.get("vision_query")
            user_variables["Comments_visible"] =  Comments_visible
            print("Comments_visible:", Comments_visible)

            # set the value of variable 'assertion_operand_1a7bc61d37ee4756a0f72c7821ed2149_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1a7bc61d37ee4756a0f72c7821ed2149_0' to true")
            assertion_operand_1a7bc61d37ee4756a0f72c7821ed2149_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'Cancel' text visibility
            lambda_hooks(driver, "Query 'Cancel' text visibility")
            Cancel_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(Cancel_visible, dict):
                Cancel_visible = Cancel_visible.get("vision_query")
            user_variables["Cancel_visible"] =  Cancel_visible
            print("Cancel_visible:", Cancel_visible)

            # set the value of variable 'assertion_operand_401d6c5b7ddb48758d2afe69ea3fdde6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_401d6c5b7ddb48758d2afe69ea3fdde6_0' to true")
            assertion_operand_401d6c5b7ddb48758d2afe69ea3fdde6_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'Save' text visibility
            lambda_hooks(driver, "Query 'Save' text visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_29e399d195cc4f7daca7a11a74f24ad8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_29e399d195cc4f7daca7a11a74f24ad8_0' to true")
            assertion_operand_29e399d195cc4f7daca7a11a74f24ad8_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Click 'Save' button
            lambda_hooks(driver, "Click 'Save' button")
            ui_action(driver = driver, operation_index = str(23))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(24))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_b9c39f09124548d8885030d211386f10_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b9c39f09124548d8885030d211386f10_0' to true")
            assertion_operand_b9c39f09124548d8885030d211386f10_0 = "true"
            ui_action(driver = driver, operation_index = str(25))
            assertion_result = ui_action(driver=driver, operation_index=str(26))
            print("assertion_result: ", assertion_result)

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(27))

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
