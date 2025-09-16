
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

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click 'Organization' dropdown
            lambda_hooks(driver, "Click 'Organization' dropdown")
            ui_action(driver = driver, operation_index = str(2))

            # Click 'General Information'
            lambda_hooks(driver, "Click 'General Information'")
            ui_action(driver = driver, operation_index = str(3))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            url = response = driver.current_url
            user_variables["url"] =  url
            print("url:", url)

            # set the value of variable 'assertion_operand_41cc63be476542ebbb23f3e5bd92a916_0' to viewOrganizationGeneralInformation
            lambda_hooks(driver, "set the value of variable 'assertion_operand_41cc63be476542ebbb23f3e5bd92a916_0' to viewOrganizationGeneralInformation")
            assertion_operand_41cc63be476542ebbb23f3e5bd92a916_0 = "viewOrganizationGeneralInformation"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'General Information' text visibility
            lambda_hooks(driver, "Query 'General Information' text visibility")
            general_information_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(general_information_visible, dict):
                general_information_visible = general_information_visible.get("vision_query")
            user_variables["general_information_visible"] =  general_information_visible
            print("general_information_visible:", general_information_visible)

            # set the value of variable 'assertion_operand_4a39cba79ec54b398cfd77ba1e97d1d0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_4a39cba79ec54b398cfd77ba1e97d1d0_0' to true")
            assertion_operand_4a39cba79ec54b398cfd77ba1e97d1d0_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Click 'Edit' link
            lambda_hooks(driver, "Click 'Edit' link")
            ui_action(driver = driver, operation_index = str(10))

            # Query 'NetFunda' text visibility
            lambda_hooks(driver, "Query 'NetFunda' text visibility")
            NetFunda_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(NetFunda_visible, dict):
                NetFunda_visible = NetFunda_visible.get("vision_query")
            user_variables["NetFunda_visible"] =  NetFunda_visible
            print("NetFunda_visible:", NetFunda_visible)

            # set the value of variable 'assertion_operand_eece64715c2b4af78070993d4602fd55_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_eece64715c2b4af78070993d4602fd55_0' to true")
            assertion_operand_eece64715c2b4af78070993d4602fd55_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # type 'abc@gmail.com' in email field
            lambda_hooks(driver, f"type {UIActions.operations_meta_data['14']['value']}")
            ui_action(driver = driver, operation_index = str(14))

            # Query visibility of 'abc@gmail.com' on viewport
            lambda_hooks(driver, "Query visibility of 'abc@gmail.com' on viewport")
            abc_gmail_com_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(abc_gmail_com_visible, dict):
                abc_gmail_com_visible = abc_gmail_com_visible.get("vision_query")
            user_variables["abc_gmail_com_visible"] =  abc_gmail_com_visible
            print("abc_gmail_com_visible:", abc_gmail_com_visible)

            # set the value of variable 'assertion_operand_ef2b319ae2b540da8b7521fd55a2e386_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ef2b319ae2b540da8b7521fd55a2e386_0' to true")
            assertion_operand_ef2b319ae2b540da8b7521fd55a2e386_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Click 'Edit' link
            lambda_hooks(driver, "Click 'Edit' link")
            ui_action(driver = driver, operation_index = str(18))

            # wait 10 seconds
            lambda_hooks(driver, "wait 10 seconds")
            ui_action(driver = driver, operation_index = str(19))

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
