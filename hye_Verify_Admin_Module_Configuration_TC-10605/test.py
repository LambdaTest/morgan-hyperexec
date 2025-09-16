
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

            # Click 'Admin'
            lambda_hooks(driver, "Click 'Admin'")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click 'Configuration'
            lambda_hooks(driver, "Click 'Configuration'")
            ui_action(driver = driver, operation_index = str(2))

            # Click 'Modules' dropdown
            lambda_hooks(driver, "Click 'Modules' dropdown")
            ui_action(driver = driver, operation_index = str(3))

            # Query 'Admin Module' text visibility
            lambda_hooks(driver, "Query 'Admin Module' text visibility")
            admin_module_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(admin_module_visible, dict):
                admin_module_visible = admin_module_visible.get("vision_query")
            user_variables["admin_module_visible"] =  admin_module_visible
            print("admin_module_visible:", admin_module_visible)

            # set the value of variable 'assertion_operand_b38655d45f4740f6886dead7ad4e9c13_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b38655d45f4740f6886dead7ad4e9c13_0' to true")
            assertion_operand_b38655d45f4740f6886dead7ad4e9c13_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'Buzz' text visibility
            lambda_hooks(driver, "Query 'Buzz' text visibility")
            Buzz_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(Buzz_visible, dict):
                Buzz_visible = Buzz_visible.get("vision_query")
            user_variables["Buzz_visible"] =  Buzz_visible
            print("Buzz_visible:", Buzz_visible)

            # set the value of variable 'assertion_operand_88984c41dfd84df2a7bafab28fae89fa_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_88984c41dfd84df2a7bafab28fae89fa_0' to true")
            assertion_operand_88984c41dfd84df2a7bafab28fae89fa_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Time Module' visibility
            lambda_hooks(driver, "Query 'Time Module' visibility")
            Time_Module_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Time_Module_visible, dict):
                Time_Module_visible = Time_Module_visible.get("vision_query")
            user_variables["Time_Module_visible"] =  Time_Module_visible
            print("Time_Module_visible:", Time_Module_visible)

            # set the value of variable 'assertion_operand_16b7e46288fd4e538123e332685b86ed_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_16b7e46288fd4e538123e332685b86ed_0' to true")
            assertion_operand_16b7e46288fd4e538123e332685b86ed_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'save' button visibility
            lambda_hooks(driver, "Query 'save' button visibility")
            save_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(save_visible, dict):
                save_visible = save_visible.get("vision_query")
            user_variables["save_visible"] =  save_visible
            print("save_visible:", save_visible)

            # set the value of variable 'assertion_operand_f8f7f2c3c42145d1a5361c423357e6fe_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f8f7f2c3c42145d1a5361c423357e6fe_0' to true")
            assertion_operand_f8f7f2c3c42145d1a5361c423357e6fe_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
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
