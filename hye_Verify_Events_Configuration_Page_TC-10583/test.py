
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

            # Click on 'Claim' menu item in the left side menu
            lambda_hooks(driver, "Click on 'Claim' menu item in the left side menu")
            ui_action(driver = driver, operation_index = str(0))

            # Click on 'Configuration' dropdown in the top left navigation bar
            lambda_hooks(driver, "Click on 'Configuration' dropdown in the top left navigation bar")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Events' option in the Configuration dropdown
            lambda_hooks(driver, "Click on 'Events' option in the Configuration dropdown")
            ui_action(driver = driver, operation_index = str(2))

            # Query 'Events' text visibility
            lambda_hooks(driver, "Query 'Events' text visibility")
            Events_visible = vision_query(driver = driver, operation_index = str(3))
            if isinstance(Events_visible, dict):
                Events_visible = Events_visible.get("vision_query")
            user_variables["Events_visible"] =  Events_visible
            print("Events_visible:", Events_visible)

            # set the value of variable 'assertion_operand_6384017f03904527a774d674555ab912_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6384017f03904527a774d674555ab912_0' to true")
            assertion_operand_6384017f03904527a774d674555ab912_0 = "true"
            ui_action(driver = driver, operation_index = str(4))
            assertion_result = ui_action(driver=driver, operation_index=str(5))
            print("assertion_result: ", assertion_result)

            # Query 'Event Name' visibility
            lambda_hooks(driver, "Query 'Event Name' visibility")
            Event_Name_visible = vision_query(driver = driver, operation_index = str(6))
            if isinstance(Event_Name_visible, dict):
                Event_Name_visible = Event_Name_visible.get("vision_query")
            user_variables["Event_Name_visible"] =  Event_Name_visible
            print("Event_Name_visible:", Event_Name_visible)

            # set the value of variable 'assertion_operand_c8d2c1fe5adc463787def4d7e6ca3620_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c8d2c1fe5adc463787def4d7e6ca3620_0' to true")
            assertion_operand_c8d2c1fe5adc463787def4d7e6ca3620_0 = "true"
            ui_action(driver = driver, operation_index = str(7))
            assertion_result = ui_action(driver=driver, operation_index=str(8))
            print("assertion_result: ", assertion_result)

            # Query 'Reset' text visibility
            lambda_hooks(driver, "Query 'Reset' text visibility")
            Reset_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(Reset_visible, dict):
                Reset_visible = Reset_visible.get("vision_query")
            user_variables["Reset_visible"] =  Reset_visible
            print("Reset_visible:", Reset_visible)

            # set the value of variable 'assertion_operand_959681f1ee6641c2ae8f5e0158c95fbe_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_959681f1ee6641c2ae8f5e0158c95fbe_0' to true")
            assertion_operand_959681f1ee6641c2ae8f5e0158c95fbe_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Query 'Search' visibility
            lambda_hooks(driver, "Query 'Search' visibility")
            Search_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Search_visible, dict):
                Search_visible = Search_visible.get("vision_query")
            user_variables["Search_visible"] =  Search_visible
            print("Search_visible:", Search_visible)

            # set the value of variable 'assertion_operand_e24f9be6f0354ccbb1d717933cf43119_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e24f9be6f0354ccbb1d717933cf43119_0' to true")
            assertion_operand_e24f9be6f0354ccbb1d717933cf43119_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query 'Status' text visibility
            lambda_hooks(driver, "Query 'Status' text visibility")
            Status_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(Status_visible, dict):
                Status_visible = Status_visible.get("vision_query")
            user_variables["Status_visible"] =  Status_visible
            print("Status_visible:", Status_visible)

            # set the value of variable 'assertion_operand_d09b4054f5874117872f186544d43c94_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d09b4054f5874117872f186544d43c94_0' to true")
            assertion_operand_d09b4054f5874117872f186544d43c94_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Query '+ Add' visibility
            lambda_hooks(driver, "Query '+ Add' visibility")
            add_text_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(add_text_visible, dict):
                add_text_visible = add_text_visible.get("vision_query")
            user_variables["add_text_visible"] =  add_text_visible
            print("add_text_visible:", add_text_visible)

            # set the value of variable 'assertion_operand_7b214c3b6a9d45c581bcf09ca8586337_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7b214c3b6a9d45c581bcf09ca8586337_0' to true")
            assertion_operand_7b214c3b6a9d45c581bcf09ca8586337_0 = "true"
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
