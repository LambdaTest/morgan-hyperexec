
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

            # Click 'PIM'
            lambda_hooks(driver, "Click 'PIM'")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            url = response = driver.current_url
            user_variables["url"] =  url
            print("url:", url)

            # set the value of variable 'assertion_operand_de9e27bd55d641c38a0f6accfccca076_0' to viewEmployeeList
            lambda_hooks(driver, "set the value of variable 'assertion_operand_de9e27bd55d641c38a0f6accfccca076_0' to viewEmployeeList")
            assertion_operand_de9e27bd55d641c38a0f6accfccca076_0 = "viewEmployeeList"
            ui_action(driver = driver, operation_index = str(3))
            assertion_result = ui_action(driver=driver, operation_index=str(4))
            print("assertion_result: ", assertion_result)

            # Query 'Employee Information' text visibility
            lambda_hooks(driver, "Query 'Employee Information' text visibility")
            employee_information_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(employee_information_visible, dict):
                employee_information_visible = employee_information_visible.get("vision_query")
            user_variables["employee_information_visible"] =  employee_information_visible
            print("employee_information_visible:", employee_information_visible)

            # set the value of variable 'assertion_operand_0e496a2e80da4023860cf14629d630dc_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0e496a2e80da4023860cf14629d630dc_0' to true")
            assertion_operand_0e496a2e80da4023860cf14629d630dc_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query if 'Reset' text is visible
            lambda_hooks(driver, "Query if 'Reset' text is visible")
            Reset_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Reset_visible, dict):
                Reset_visible = Reset_visible.get("vision_query")
            user_variables["Reset_visible"] =  Reset_visible
            print("Reset_visible:", Reset_visible)

            # set the value of variable 'assertion_operand_2d56923925df4e3688b7e992cdf86033_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2d56923925df4e3688b7e992cdf86033_0' to true")
            assertion_operand_2d56923925df4e3688b7e992cdf86033_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Search' text visibility
            lambda_hooks(driver, "Query 'Search' text visibility")
            Search_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Search_visible, dict):
                Search_visible = Search_visible.get("vision_query")
            user_variables["Search_visible"] =  Search_visible
            print("Search_visible:", Search_visible)

            # set the value of variable 'assertion_operand_f544fa40fca84192b6cb96275c589f25_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f544fa40fca84192b6cb96275c589f25_0' to true")
            assertion_operand_f544fa40fca84192b6cb96275c589f25_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query '(2) Records Found' text visibility
            lambda_hooks(driver, "Query '(2) Records Found' text visibility")
            records_found_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(records_found_visible, dict):
                records_found_visible = records_found_visible.get("vision_query")
            user_variables["records_found_visible"] =  records_found_visible
            print("records_found_visible:", records_found_visible)

            # set the value of variable 'assertion_operand_efa5d41de81947af9ba051a29f8c6ef6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_efa5d41de81947af9ba051a29f8c6ef6_0' to true")
            assertion_operand_efa5d41de81947af9ba051a29f8c6ef6_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
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
