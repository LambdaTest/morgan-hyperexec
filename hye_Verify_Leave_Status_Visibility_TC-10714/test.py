
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

            # Click 'Leave' button
            lambda_hooks(driver, "Click 'Leave' button")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click 'Show Leave with Status' dropdown
            lambda_hooks(driver, "Click 'Show Leave with Status' dropdown")
            ui_action(driver = driver, operation_index = str(2))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Query 'viewport dropdown' visibility
            lambda_hooks(driver, "Query 'viewport dropdown' visibility")
            viewport_dropdown_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(viewport_dropdown_visible, dict):
                viewport_dropdown_visible = viewport_dropdown_visible.get("vision_query")
            user_variables["viewport_dropdown_visible"] =  viewport_dropdown_visible
            print("viewport_dropdown_visible:", viewport_dropdown_visible)

            # Query 'Rejected' text visibility in viewport dropdown
            lambda_hooks(driver, "Query 'Rejected' text visibility in viewport dropdown")
            rejected_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(rejected_visible, dict):
                rejected_visible = rejected_visible.get("vision_query")
            user_variables["rejected_visible"] =  rejected_visible
            print("rejected_visible:", rejected_visible)

            # set the value of variable 'assertion_operand_144d0d2944cc4651a2976ba21b1db9c7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_144d0d2944cc4651a2976ba21b1db9c7_0' to true")
            assertion_operand_144d0d2944cc4651a2976ba21b1db9c7_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query 'Cancelled' visibility
            lambda_hooks(driver, "Query 'Cancelled' visibility")
            Cancelled_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Cancelled_visible, dict):
                Cancelled_visible = Cancelled_visible.get("vision_query")
            user_variables["Cancelled_visible"] =  Cancelled_visible
            print("Cancelled_visible:", Cancelled_visible)

            # set the value of variable 'assertion_operand_c2b025b3239f45f0b7fc542076ab32ae_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c2b025b3239f45f0b7fc542076ab32ae_0' to true")
            assertion_operand_c2b025b3239f45f0b7fc542076ab32ae_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Taken' visibility
            lambda_hooks(driver, "Query 'Taken' visibility")
            Taken_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Taken_visible, dict):
                Taken_visible = Taken_visible.get("vision_query")
            user_variables["Taken_visible"] =  Taken_visible
            print("Taken_visible:", Taken_visible)

            # set the value of variable 'assertion_operand_7d14ffeb816840c8af884ee5f3faf28b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7d14ffeb816840c8af884ee5f3faf28b_0' to true")
            assertion_operand_7d14ffeb816840c8af884ee5f3faf28b_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Click 'Taken' from the dropdown
            lambda_hooks(driver, "Click 'Taken' from the dropdown")
            ui_action(driver = driver, operation_index = str(14))

            # Query visibility of 'Taken'
            lambda_hooks(driver, "Query visibility of 'Taken'")
            Taken_visible_a4cbbb = vision_query(driver = driver, operation_index = str(15))
            if isinstance(Taken_visible_a4cbbb, dict):
                Taken_visible_a4cbbb = Taken_visible_a4cbbb.get("vision_query")
            user_variables["Taken_visible_a4cbbb"] =  Taken_visible_a4cbbb
            print("Taken_visible_a4cbbb:", Taken_visible_a4cbbb)

            # set the value of variable 'assertion_operand_cfdb9d7f87364eb3b855e7ef6dbf8b1b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_cfdb9d7f87364eb3b855e7ef6dbf8b1b_0' to true")
            assertion_operand_cfdb9d7f87364eb3b855e7ef6dbf8b1b_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Click 'Reset' button
            lambda_hooks(driver, "Click 'Reset' button")
            ui_action(driver = driver, operation_index = str(18))

            # Query visibility of 'Taken'
            lambda_hooks(driver, "Query visibility of 'Taken'")
            Taken_visible_73b992 = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Taken_visible_73b992, dict):
                Taken_visible_73b992 = Taken_visible_73b992.get("vision_query")
            user_variables["Taken_visible_73b992"] =  Taken_visible_73b992
            print("Taken_visible_73b992:", Taken_visible_73b992)

            # set the value of variable 'assertion_operand_4644787ea45548ab9304e03cbc560d66_0' to false
            lambda_hooks(driver, "set the value of variable 'assertion_operand_4644787ea45548ab9304e03cbc560d66_0' to false")
            assertion_operand_4644787ea45548ab9304e03cbc560d66_0 = "false"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
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
