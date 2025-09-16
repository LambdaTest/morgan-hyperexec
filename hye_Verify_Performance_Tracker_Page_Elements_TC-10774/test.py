
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

            # Click on Performance menu item in left sidebar
            lambda_hooks(driver, "Click on Performance menu item in left sidebar")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'My Trackers' tab in the top nav bar
            lambda_hooks(driver, "Click on 'My Trackers' tab in the top nav bar")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            current_url = response = driver.current_url
            user_variables["current_url"] =  current_url
            print("current_url:", current_url)

            # set the value of variable 'assertion_operand_542533da57bf476aa3bc6a3b101ba7c5_0' to viewMyPerformanceTrackerList
            lambda_hooks(driver, "set the value of variable 'assertion_operand_542533da57bf476aa3bc6a3b101ba7c5_0' to viewMyPerformanceTrackerList")
            assertion_operand_542533da57bf476aa3bc6a3b101ba7c5_0 = "viewMyPerformanceTrackerList"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'My Performance Trackers' visibility
            lambda_hooks(driver, "Query 'My Performance Trackers' visibility")
            My_Performance_Trackers_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(My_Performance_Trackers_visible, dict):
                My_Performance_Trackers_visible = My_Performance_Trackers_visible.get("vision_query")
            user_variables["My_Performance_Trackers_visible"] =  My_Performance_Trackers_visible
            print("My_Performance_Trackers_visible:", My_Performance_Trackers_visible)

            # set the value of variable 'assertion_operand_18c22a84e621413d93e91651d36b50aa_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_18c22a84e621413d93e91651d36b50aa_0' to true")
            assertion_operand_18c22a84e621413d93e91651d36b50aa_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'No Records Found' visibility
            lambda_hooks(driver, "Query 'No Records Found' visibility")
            no_records_found_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(no_records_found_visible, dict):
                no_records_found_visible = no_records_found_visible.get("vision_query")
            user_variables["no_records_found_visible"] =  no_records_found_visible
            print("no_records_found_visible:", no_records_found_visible)

            # set the value of variable 'assertion_operand_6cce5fb8948b48e19cd0eb10a809608e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6cce5fb8948b48e19cd0eb10a809608e_0' to true")
            assertion_operand_6cce5fb8948b48e19cd0eb10a809608e_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Tracker' visibility
            lambda_hooks(driver, "Query 'Tracker' visibility")
            Tracker_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Tracker_visible, dict):
                Tracker_visible = Tracker_visible.get("vision_query")
            user_variables["Tracker_visible"] =  Tracker_visible
            print("Tracker_visible:", Tracker_visible)

            # set the value of variable 'assertion_operand_a1c39a97a8f14eec9b543125818eaec5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a1c39a97a8f14eec9b543125818eaec5_0' to true")
            assertion_operand_a1c39a97a8f14eec9b543125818eaec5_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Added Date' text visibility
            lambda_hooks(driver, "Query 'Added Date' text visibility")
            Added_Date_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Added_Date_visible, dict):
                Added_Date_visible = Added_Date_visible.get("vision_query")
            user_variables["Added_Date_visible"] =  Added_Date_visible
            print("Added_Date_visible:", Added_Date_visible)

            # set the value of variable 'assertion_operand_a133679b32f640b582c2b46f14a9ad30_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a133679b32f640b582c2b46f14a9ad30_0' to true")
            assertion_operand_a133679b32f640b582c2b46f14a9ad30_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Modified Date' text visibility
            lambda_hooks(driver, "Query 'Modified Date' text visibility")
            Modified_Date_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(Modified_Date_visible, dict):
                Modified_Date_visible = Modified_Date_visible.get("vision_query")
            user_variables["Modified_Date_visible"] =  Modified_Date_visible
            print("Modified_Date_visible:", Modified_Date_visible)

            # set the value of variable 'assertion_operand_9c5ac44ff24043baa66e7b4f0978efdc_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_9c5ac44ff24043baa66e7b4f0978efdc_0' to true")
            assertion_operand_9c5ac44ff24043baa66e7b4f0978efdc_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(Actions_visible, dict):
                Actions_visible = Actions_visible.get("vision_query")
            user_variables["Actions_visible"] =  Actions_visible
            print("Actions_visible:", Actions_visible)

            # set the value of variable 'assertion_operand_51ad4a64f1194a7f981aa2ee65ea3fb1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_51ad4a64f1194a7f981aa2ee65ea3fb1_0' to true")
            assertion_operand_51ad4a64f1194a7f981aa2ee65ea3fb1_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
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
