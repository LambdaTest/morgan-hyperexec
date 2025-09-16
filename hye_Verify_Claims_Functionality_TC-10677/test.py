
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

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(0))

            # Click on Claim menu item in left sidebar 
            lambda_hooks(driver, "Click on Claim menu item in left sidebar ")
            ui_action(driver = driver, operation_index = str(1))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(2))

            # Click on 'My Claims' tab in the top nav bar 
            lambda_hooks(driver, "Click on 'My Claims' tab in the top nav bar ")
            ui_action(driver = driver, operation_index = str(3))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(4))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            current_url = response = driver.current_url
            user_variables["current_url"] =  current_url
            print("current_url:", current_url)

            # set the value of variable 'assertion_operand_95677ca8e06b4e18a7e09c0c4588cc59_0' to viewClaim
            lambda_hooks(driver, "set the value of variable 'assertion_operand_95677ca8e06b4e18a7e09c0c4588cc59_0' to viewClaim")
            assertion_operand_95677ca8e06b4e18a7e09c0c4588cc59_0 = "viewClaim"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Click on the Search button in My Claims section 
            lambda_hooks(driver, "Click on the Search button in My Claims section ")
            ui_action(driver = driver, operation_index = str(8))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(9))

            # Query text '(1) Record Found' visibility
            lambda_hooks(driver, "Query text '(1) Record Found' visibility")
            record_found_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(record_found_visible, dict):
                record_found_visible = record_found_visible.get("vision_query")
            user_variables["record_found_visible"] =  record_found_visible
            print("record_found_visible:", record_found_visible)

            # set the value of variable 'assertion_operand_26852efcf5d841e9949c8c7ba1760f7d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_26852efcf5d841e9949c8c7ba1760f7d_0' to true")
            assertion_operand_26852efcf5d841e9949c8c7ba1760f7d_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Click on the event name dropdown arrow in My Claims filter 
            lambda_hooks(driver, "Click on the event name dropdown arrow in My Claims filter ")
            ui_action(driver = driver, operation_index = str(13))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(14))

            # Query 'Active Event' text visibility in dropdown
            lambda_hooks(driver, "Query 'Active Event' text visibility in dropdown")
            active_event_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(active_event_visible, dict):
                active_event_visible = active_event_visible.get("vision_query")
            user_variables["active_event_visible"] =  active_event_visible
            print("active_event_visible:", active_event_visible)

            # set the value of variable 'assertion_operand_5e07d88e5856477fa28cd03887b1950e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5e07d88e5856477fa28cd03887b1950e_0' to true")
            assertion_operand_5e07d88e5856477fa28cd03887b1950e_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Click on the event name dropdown arrow in My Claims filter 
            lambda_hooks(driver, "Click on the event name dropdown arrow in My Claims filter ")
            ui_action(driver = driver, operation_index = str(18))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(19))

            # Click on the status dropdown arrow in My Claims filter 
            lambda_hooks(driver, "Click on the status dropdown arrow in My Claims filter ")
            ui_action(driver = driver, operation_index = str(20))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(21))

            # Query 'Initiated' text visibility
            lambda_hooks(driver, "Query 'Initiated' text visibility")
            initiated_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(initiated_visible, dict):
                initiated_visible = initiated_visible.get("vision_query")
            user_variables["initiated_visible"] =  initiated_visible
            print("initiated_visible:", initiated_visible)

            # set the value of variable 'assertion_operand_65e4570f139e4b13a6bf5ae722558c72_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_65e4570f139e4b13a6bf5ae722558c72_0' to true")
            assertion_operand_65e4570f139e4b13a6bf5ae722558c72_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Query 'Submitted' text visibility
            lambda_hooks(driver, "Query 'Submitted' text visibility")
            Submitted_visible = vision_query(driver = driver, operation_index = str(25))
            if isinstance(Submitted_visible, dict):
                Submitted_visible = Submitted_visible.get("vision_query")
            user_variables["Submitted_visible"] =  Submitted_visible
            print("Submitted_visible:", Submitted_visible)

            # set the value of variable 'assertion_operand_cca3ec31d2744ed386e17d8d6813b632_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_cca3ec31d2744ed386e17d8d6813b632_0' to true")
            assertion_operand_cca3ec31d2744ed386e17d8d6813b632_0 = "true"
            ui_action(driver = driver, operation_index = str(26))
            assertion_result = ui_action(driver=driver, operation_index=str(27))
            print("assertion_result: ", assertion_result)

            # Query 'Approved' text visibility
            lambda_hooks(driver, "Query 'Approved' text visibility")
            Approved_visible = vision_query(driver = driver, operation_index = str(28))
            if isinstance(Approved_visible, dict):
                Approved_visible = Approved_visible.get("vision_query")
            user_variables["Approved_visible"] =  Approved_visible
            print("Approved_visible:", Approved_visible)

            # set the value of variable 'assertion_operand_de971f260e4f4be7848ed194ae3d7309_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_de971f260e4f4be7848ed194ae3d7309_0' to true")
            assertion_operand_de971f260e4f4be7848ed194ae3d7309_0 = "true"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
            print("assertion_result: ", assertion_result)

            # Query 'Rejetced' text visibility
            lambda_hooks(driver, "Query 'Rejetced' text visibility")
            Rejetced_visible = vision_query(driver = driver, operation_index = str(31))
            if isinstance(Rejetced_visible, dict):
                Rejetced_visible = Rejetced_visible.get("vision_query")
            user_variables["Rejetced_visible"] =  Rejetced_visible
            print("Rejetced_visible:", Rejetced_visible)

            # set the value of variable 'assertion_operand_bd07a02ae6c04aa1a8a14c55eea4d283_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_bd07a02ae6c04aa1a8a14c55eea4d283_0' to true")
            assertion_operand_bd07a02ae6c04aa1a8a14c55eea4d283_0 = "true"
            ui_action(driver = driver, operation_index = str(32))
            assertion_result = ui_action(driver=driver, operation_index=str(33))
            print("assertion_result: ", assertion_result)

            # Query 'Cancelled' text visibility
            lambda_hooks(driver, "Query 'Cancelled' text visibility")
            Cancelled_visible = vision_query(driver = driver, operation_index = str(34))
            if isinstance(Cancelled_visible, dict):
                Cancelled_visible = Cancelled_visible.get("vision_query")
            user_variables["Cancelled_visible"] =  Cancelled_visible
            print("Cancelled_visible:", Cancelled_visible)

            # set the value of variable 'assertion_operand_785353eb99fc4a8a9aa11d997b8eaa1d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_785353eb99fc4a8a9aa11d997b8eaa1d_0' to true")
            assertion_operand_785353eb99fc4a8a9aa11d997b8eaa1d_0 = "true"
            ui_action(driver = driver, operation_index = str(35))
            assertion_result = ui_action(driver=driver, operation_index=str(36))
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
