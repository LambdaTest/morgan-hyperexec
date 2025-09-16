
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

            # Click 'LDAP Configuration' dropdown
            lambda_hooks(driver, "Click 'LDAP Configuration' dropdown")
            ui_action(driver = driver, operation_index = str(3))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(4))

            # Scroll to the bottom of the page
            lambda_hooks(driver, "Scroll to the bottom of the page")
            ui_action(driver = driver, operation_index = str(5))

            # Query 'Test Connection' visibility
            lambda_hooks(driver, "Query 'Test Connection' visibility")
            Test_Connection_visible = vision_query(driver = driver, operation_index = str(6))
            if isinstance(Test_Connection_visible, dict):
                Test_Connection_visible = Test_Connection_visible.get("vision_query")
            user_variables["Test_Connection_visible"] =  Test_Connection_visible
            print("Test_Connection_visible:", Test_Connection_visible)

            # set the value of variable 'assertion_operand_6e495eeaaaa2448793cb55b6d2226c2a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6e495eeaaaa2448793cb55b6d2226c2a_0' to true")
            assertion_operand_6e495eeaaaa2448793cb55b6d2226c2a_0 = "true"
            ui_action(driver = driver, operation_index = str(7))
            assertion_result = ui_action(driver=driver, operation_index=str(8))
            print("assertion_result: ", assertion_result)

            # Query 'Save' visibility
            lambda_hooks(driver, "Query 'Save' visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_c4cb8a8393b54270a829e42767a51143_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c4cb8a8393b54270a829e42767a51143_0' to true")
            assertion_operand_c4cb8a8393b54270a829e42767a51143_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Query visibility of the given LDAP service warning text
            lambda_hooks(driver, "Query visibility of the given LDAP service warning text")
            ldap_warning_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(ldap_warning_visible, dict):
                ldap_warning_visible = ldap_warning_visible.get("vision_query")
            user_variables["ldap_warning_visible"] =  ldap_warning_visible
            print("ldap_warning_visible:", ldap_warning_visible)

            # set the value of variable 'assertion_operand_e1584f71bd464c80b52c8407c7123c35_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e1584f71bd464c80b52c8407c7123c35_0' to true")
            assertion_operand_e1584f71bd464c80b52c8407c7123c35_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query 'Additional Settings' visibility
            lambda_hooks(driver, "Query 'Additional Settings' visibility")
            Additional_Settings_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(Additional_Settings_visible, dict):
                Additional_Settings_visible = Additional_Settings_visible.get("vision_query")
            user_variables["Additional_Settings_visible"] =  Additional_Settings_visible
            print("Additional_Settings_visible:", Additional_Settings_visible)

            # set the value of variable 'assertion_operand_6d1b62142229497d952bcf4fff7283c0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6d1b62142229497d952bcf4fff7283c0_0' to true")
            assertion_operand_6d1b62142229497d952bcf4fff7283c0_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
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
