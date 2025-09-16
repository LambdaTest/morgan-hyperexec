
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

            # Click on 'Configure' dropdown in top left next to 'Manage Reviews'
            lambda_hooks(driver, "Click on 'Configure' dropdown in top left next to 'Manage Reviews'")
            ui_action(driver = driver, operation_index = str(2))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on 'KPIs' option in Manage Reviews dropdown
            lambda_hooks(driver, "Click on 'KPIs' option in Manage Reviews dropdown")
            ui_action(driver = driver, operation_index = str(4))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(5))

            # Click on the plus icon in Add button
            lambda_hooks(driver, "Click on the plus icon in Add button")
            ui_action(driver = driver, operation_index = str(6))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(7))

            # Query 'Add Key Performance Indicator' text visibility
            lambda_hooks(driver, "Query 'Add Key Performance Indicator' text visibility")
            Add_Key_Performance_Indicator_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Add_Key_Performance_Indicator_visible, dict):
                Add_Key_Performance_Indicator_visible = Add_Key_Performance_Indicator_visible.get("vision_query")
            user_variables["Add_Key_Performance_Indicator_visible"] =  Add_Key_Performance_Indicator_visible
            print("Add_Key_Performance_Indicator_visible:", Add_Key_Performance_Indicator_visible)

            # set the value of variable 'assertion_operand_3ef476295a0d4779b3b7aa7ab9d8467e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3ef476295a0d4779b3b7aa7ab9d8467e_0' to true")
            assertion_operand_3ef476295a0d4779b3b7aa7ab9d8467e_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Key Performance Indicator' visibility
            lambda_hooks(driver, "Query 'Key Performance Indicator' visibility")
            Key_Performance_Indicator_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Key_Performance_Indicator_visible, dict):
                Key_Performance_Indicator_visible = Key_Performance_Indicator_visible.get("vision_query")
            user_variables["Key_Performance_Indicator_visible"] =  Key_Performance_Indicator_visible
            print("Key_Performance_Indicator_visible:", Key_Performance_Indicator_visible)

            # set the value of variable 'assertion_operand_a4c9cb27d7a249d5a1d0c9ba74e7edd8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a4c9cb27d7a249d5a1d0c9ba74e7edd8_0' to true")
            assertion_operand_a4c9cb27d7a249d5a1d0c9ba74e7edd8_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query 'Job Title' visibility
            lambda_hooks(driver, "Query 'Job Title' visibility")
            Job_Title_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(Job_Title_visible, dict):
                Job_Title_visible = Job_Title_visible.get("vision_query")
            user_variables["Job_Title_visible"] =  Job_Title_visible
            print("Job_Title_visible:", Job_Title_visible)

            # set the value of variable 'assertion_operand_f591073d2a51494bb3c7896d8dad33b9_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f591073d2a51494bb3c7896d8dad33b9_0' to true")
            assertion_operand_f591073d2a51494bb3c7896d8dad33b9_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'Minimum Rating' visibility
            lambda_hooks(driver, "Query 'Minimum Rating' visibility")
            Minimum_Rating_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(Minimum_Rating_visible, dict):
                Minimum_Rating_visible = Minimum_Rating_visible.get("vision_query")
            user_variables["Minimum_Rating_visible"] =  Minimum_Rating_visible
            print("Minimum_Rating_visible:", Minimum_Rating_visible)

            # set the value of variable 'assertion_operand_9984f9710f904f91b9aa316bb2569164_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_9984f9710f904f91b9aa316bb2569164_0' to true")
            assertion_operand_9984f9710f904f91b9aa316bb2569164_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'Maximum Rating' visibility
            lambda_hooks(driver, "Query 'Maximum Rating' visibility")
            Maximum_Rating_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(Maximum_Rating_visible, dict):
                Maximum_Rating_visible = Maximum_Rating_visible.get("vision_query")
            user_variables["Maximum_Rating_visible"] =  Maximum_Rating_visible
            print("Maximum_Rating_visible:", Maximum_Rating_visible)

            # set the value of variable 'assertion_operand_7276c5b5afd44e4c8b0cd7a2d413f17b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7276c5b5afd44e4c8b0cd7a2d413f17b_0' to true")
            assertion_operand_7276c5b5afd44e4c8b0cd7a2d413f17b_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Make Default Scale'
            lambda_hooks(driver, "Query visibility of text 'Make Default Scale'")
            make_default_scale_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(make_default_scale_visible, dict):
                make_default_scale_visible = make_default_scale_visible.get("vision_query")
            user_variables["make_default_scale_visible"] =  make_default_scale_visible
            print("make_default_scale_visible:", make_default_scale_visible)

            # set the value of variable 'assertion_operand_6e2dee7251494379ba7e64d6002a9f5c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6e2dee7251494379ba7e64d6002a9f5c_0' to true")
            assertion_operand_6e2dee7251494379ba7e64d6002a9f5c_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
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
