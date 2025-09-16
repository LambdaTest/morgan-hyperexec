
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

            # Click on 'Admin' menu item in the left sidebar  
            lambda_hooks(driver, "Click on 'Admin' menu item in the left sidebar  ")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on the input field with class oxd-input oxd-input--focus  
            lambda_hooks(driver, "Click on the input field with class oxd-input oxd-input--focus  ")
            ui_action(driver = driver, operation_index = str(2))

            # Type in dashboard search input field 'ayush'  
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['3']['value']}")
            ui_action(driver = driver, operation_index = str(3))

            # Click on the Search button with orangehrm-left-space class  
            lambda_hooks(driver, "Click on the Search button with orangehrm-left-space class  ")
            ui_action(driver = driver, operation_index = str(4))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(5))

            # Click on the empty bar in Time at Work chart for Wednesday  
            lambda_hooks(driver, "Click on the empty bar in Time at Work chart for Wednesday  ")
            ui_action(driver = driver, operation_index = str(6))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(7))

            # Click on the Save button  
            lambda_hooks(driver, "Click on the Save button  ")
            ui_action(driver = driver, operation_index = str(8))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(9))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_21cd4b021d184ac3b6b7e90693bee80f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_21cd4b021d184ac3b6b7e90693bee80f_0' to true")
            assertion_operand_21cd4b021d184ac3b6b7e90693bee80f_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'User Role*' text visibility
            lambda_hooks(driver, "Query 'User Role*' text visibility")
            User_Role_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(User_Role_visible, dict):
                User_Role_visible = User_Role_visible.get("vision_query")
            user_variables["User_Role_visible"] =  User_Role_visible
            print("User_Role_visible:", User_Role_visible)

            # set the value of variable 'assertion_operand_16ba9d88fcba46caac2a0714f8ed0cb6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_16ba9d88fcba46caac2a0714f8ed0cb6_0' to true")
            assertion_operand_16ba9d88fcba46caac2a0714f8ed0cb6_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Status*' text visibility
            lambda_hooks(driver, "Query 'Status*' text visibility")
            Status_star_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Status_star_visible, dict):
                Status_star_visible = Status_star_visible.get("vision_query")
            user_variables["Status_star_visible"] =  Status_star_visible
            print("Status_star_visible:", Status_star_visible)

            # set the value of variable 'assertion_operand_d7dc2847923543ba86597eccdd8c5f1a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d7dc2847923543ba86597eccdd8c5f1a_0' to true")
            assertion_operand_d7dc2847923543ba86597eccdd8c5f1a_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Password' text visibility
            lambda_hooks(driver, "Query 'Password' text visibility")
            Password_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Password_visible, dict):
                Password_visible = Password_visible.get("vision_query")
            user_variables["Password_visible"] =  Password_visible
            print("Password_visible:", Password_visible)

            # set the value of variable 'assertion_operand_4fef7700112e4ad3b5aac724c0baa1ef_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_4fef7700112e4ad3b5aac724c0baa1ef_0' to true")
            assertion_operand_4fef7700112e4ad3b5aac724c0baa1ef_0 = "true"
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
