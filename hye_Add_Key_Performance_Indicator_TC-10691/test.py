
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

            # Click on 'Performance' menu item in left sidebar
            lambda_hooks(driver, "Click on 'Performance' menu item in left sidebar")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on Configure dropdown in top left
            lambda_hooks(driver, "Click on Configure dropdown in top left")
            ui_action(driver = driver, operation_index = str(2))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on 'KPIs' option in Manage Reviews dropdown
            lambda_hooks(driver, "Click on 'KPIs' option in Manage Reviews dropdown")
            ui_action(driver = driver, operation_index = str(4))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            current_url = response = driver.current_url
            user_variables["current_url"] =  current_url
            print("current_url:", current_url)

            # set the value of variable 'assertion_operand_d62db769a0134975a2cc210c6cfc290b_0' to searchKpi
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d62db769a0134975a2cc210c6cfc290b_0' to searchKpi")
            assertion_operand_d62db769a0134975a2cc210c6cfc290b_0 = "searchKpi"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Click on the Search button in Key Performance Indicators section
            lambda_hooks(driver, "Click on the Search button in Key Performance Indicators section")
            ui_action(driver = driver, operation_index = str(8))

            # Query 'No Records Found' visibility
            lambda_hooks(driver, "Query 'No Records Found' visibility")
            no_records_found_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(no_records_found_visible, dict):
                no_records_found_visible = no_records_found_visible.get("vision_query")
            user_variables["no_records_found_visible"] =  no_records_found_visible
            print("no_records_found_visible:", no_records_found_visible)

            # set the value of variable 'assertion_operand_3edc876bf29c45de8ea71fb65f6620b3_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3edc876bf29c45de8ea71fb65f6620b3_0' to true")
            assertion_operand_3edc876bf29c45de8ea71fb65f6620b3_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Click on the job title dropdown arrow
            lambda_hooks(driver, "Click on the job title dropdown arrow")
            ui_action(driver = driver, operation_index = str(12))

            # Click on the green Add button below Key Performance Indicators table
            lambda_hooks(driver, "Click on the green Add button below Key Performance Indicators table")
            ui_action(driver = driver, operation_index = str(13))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            current_url_a65fba = response = driver.current_url
            user_variables["current_url_a65fba"] =  current_url_a65fba
            print("current_url_a65fba:", current_url_a65fba)

            # set the value of variable 'assertion_operand_55ca4736731c4202bdd26166f2575957_0' to saveKpi
            lambda_hooks(driver, "set the value of variable 'assertion_operand_55ca4736731c4202bdd26166f2575957_0' to saveKpi")
            assertion_operand_55ca4736731c4202bdd26166f2575957_0 = "saveKpi"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Click on Save button in Add Key Performance Indicator form
            lambda_hooks(driver, "Click on Save button in Add Key Performance Indicator form")
            ui_action(driver = driver, operation_index = str(17))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_2b17610b2879402f991a6b4d073e4694_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2b17610b2879402f991a6b4d073e4694_0' to true")
            assertion_operand_2b17610b2879402f991a6b4d073e4694_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
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
