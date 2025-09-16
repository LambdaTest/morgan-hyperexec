
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

            # Click on 'Qualifications' tab in the left side menu
            lambda_hooks(driver, "Click on 'Qualifications' tab in the left side menu")
            ui_action(driver = driver, operation_index = str(2))

            # scroll down 200 px
            lambda_hooks(driver, "scroll down 200 px")
            ui_action(driver = driver, operation_index = str(3))

            # Click on the plus icon in Languages section add button
            lambda_hooks(driver, "Click on the plus icon in Languages section add button")
            ui_action(driver = driver, operation_index = str(4))

            # scroll down 200 px
            lambda_hooks(driver, "scroll down 200 px")
            ui_action(driver = driver, operation_index = str(5))

            # Click on the language dropdown in Add Language section
            lambda_hooks(driver, "Click on the language dropdown in Add Language section")
            ui_action(driver = driver, operation_index = str(6))

            # Click on the fluency dropdown arrow in Add Language section
            lambda_hooks(driver, "Click on the fluency dropdown arrow in Add Language section")
            ui_action(driver = driver, operation_index = str(7))

            # Click on the competency dropdown arrow in Add Language section
            lambda_hooks(driver, "Click on the competency dropdown arrow in Add Language section")
            ui_action(driver = driver, operation_index = str(8))

            # Query 'Poor' text visibility
            lambda_hooks(driver, "Query 'Poor' text visibility")
            Poor_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(Poor_visible, dict):
                Poor_visible = Poor_visible.get("vision_query")
            user_variables["Poor_visible"] =  Poor_visible
            print("Poor_visible:", Poor_visible)

            # set the value of variable 'assertion_operand_d77027b511b344e290869e5abcfaa845_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d77027b511b344e290869e5abcfaa845_0' to true")
            assertion_operand_d77027b511b344e290869e5abcfaa845_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Query 'Basic' text visibility
            lambda_hooks(driver, "Query 'Basic' text visibility")
            Basic_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Basic_visible, dict):
                Basic_visible = Basic_visible.get("vision_query")
            user_variables["Basic_visible"] =  Basic_visible
            print("Basic_visible:", Basic_visible)

            # set the value of variable 'assertion_operand_2c70fbc266f94288a79f4d2385fb617e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2c70fbc266f94288a79f4d2385fb617e_0' to true")
            assertion_operand_2c70fbc266f94288a79f4d2385fb617e_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query 'Good' text visibility
            lambda_hooks(driver, "Query 'Good' text visibility")
            Good_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(Good_visible, dict):
                Good_visible = Good_visible.get("vision_query")
            user_variables["Good_visible"] =  Good_visible
            print("Good_visible:", Good_visible)

            # set the value of variable 'assertion_operand_711074cb990847d68346a763c3328519_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_711074cb990847d68346a763c3328519_0' to true")
            assertion_operand_711074cb990847d68346a763c3328519_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Query 'Mother Tounge' text visibility
            lambda_hooks(driver, "Query 'Mother Tounge' text visibility")
            Mother_Tounge_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(Mother_Tounge_visible, dict):
                Mother_Tounge_visible = Mother_Tounge_visible.get("vision_query")
            user_variables["Mother_Tounge_visible"] =  Mother_Tounge_visible
            print("Mother_Tounge_visible:", Mother_Tounge_visible)

            # set the value of variable 'assertion_operand_2d463a74b114458d8ad6ea585a7f8f55_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2d463a74b114458d8ad6ea585a7f8f55_0' to true")
            assertion_operand_2d463a74b114458d8ad6ea585a7f8f55_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
            print("assertion_result: ", assertion_result)

            # Click on the competency dropdown arrow in Add Language section
            lambda_hooks(driver, "Click on the competency dropdown arrow in Add Language section")
            ui_action(driver = driver, operation_index = str(21))

            # Click 'Save' button
            lambda_hooks(driver, "Click 'Save' button")
            ui_action(driver = driver, operation_index = str(22))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_2ec48494e0b64f75bd4d264bef34560f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2ec48494e0b64f75bd4d264bef34560f_0' to true")
            assertion_operand_2ec48494e0b64f75bd4d264bef34560f_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
            print("assertion_result: ", assertion_result)

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(26))

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
