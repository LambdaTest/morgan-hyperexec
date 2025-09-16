
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

            # Click on 'Claim' menu item in left side menu 
            lambda_hooks(driver, "Click on 'Claim' menu item in left side menu ")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on the Search button in employee claims section 
            lambda_hooks(driver, "Click on the Search button in employee claims section ")
            ui_action(driver = driver, operation_index = str(2))

            # Query '(2) Records Found' visibility
            lambda_hooks(driver, "Query '(2) Records Found' visibility")
            records_found_visible = vision_query(driver = driver, operation_index = str(3))
            if isinstance(records_found_visible, dict):
                records_found_visible = records_found_visible.get("vision_query")
            user_variables["records_found_visible"] =  records_found_visible
            print("records_found_visible:", records_found_visible)

            # set the value of variable 'assertion_operand_2e4f746b68c3458abcd61b594a51f6b8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2e4f746b68c3458abcd61b594a51f6b8_0' to true")
            assertion_operand_2e4f746b68c3458abcd61b594a51f6b8_0 = "true"
            ui_action(driver = driver, operation_index = str(4))
            assertion_result = ui_action(driver=driver, operation_index=str(5))
            print("assertion_result: ", assertion_result)

            # Query 'Ayush Pathania' visibility
            lambda_hooks(driver, "Query 'Ayush Pathania' visibility")
            Ayush_Pathania_visible = vision_query(driver = driver, operation_index = str(6))
            if isinstance(Ayush_Pathania_visible, dict):
                Ayush_Pathania_visible = Ayush_Pathania_visible.get("vision_query")
            user_variables["Ayush_Pathania_visible"] =  Ayush_Pathania_visible
            print("Ayush_Pathania_visible:", Ayush_Pathania_visible)

            # set the value of variable 'assertion_operand_a866f78f6a2e4e75be6f1a8f90bf15f3_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a866f78f6a2e4e75be6f1a8f90bf15f3_0' to true")
            assertion_operand_a866f78f6a2e4e75be6f1a8f90bf15f3_0 = "true"
            ui_action(driver = driver, operation_index = str(7))
            assertion_result = ui_action(driver=driver, operation_index=str(8))
            print("assertion_result: ", assertion_result)

            # Query 'Pushpa Raj' text visibility
            lambda_hooks(driver, "Query 'Pushpa Raj' text visibility")
            Pushpa_Raj_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(Pushpa_Raj_visible, dict):
                Pushpa_Raj_visible = Pushpa_Raj_visible.get("vision_query")
            user_variables["Pushpa_Raj_visible"] =  Pushpa_Raj_visible
            print("Pushpa_Raj_visible:", Pushpa_Raj_visible)

            # set the value of variable 'assertion_operand_157faa7020c74ab1bb34d0841c25df71_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_157faa7020c74ab1bb34d0841c25df71_0' to true")
            assertion_operand_157faa7020c74ab1bb34d0841c25df71_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Query 'Active Evenet' visibility
            lambda_hooks(driver, "Query 'Active Evenet' visibility")
            Active_Evenet_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Active_Evenet_visible, dict):
                Active_Evenet_visible = Active_Evenet_visible.get("vision_query")
            user_variables["Active_Evenet_visible"] =  Active_Evenet_visible
            print("Active_Evenet_visible:", Active_Evenet_visible)

            # set the value of variable 'assertion_operand_dfc483f649cc42cf89907f025a134e19_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_dfc483f649cc42cf89907f025a134e19_0' to true")
            assertion_operand_dfc483f649cc42cf89907f025a134e19_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query 'View Details' visibility
            lambda_hooks(driver, "Query 'View Details' visibility")
            View_Details_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(View_Details_visible, dict):
                View_Details_visible = View_Details_visible.get("vision_query")
            user_variables["View_Details_visible"] =  View_Details_visible
            print("View_Details_visible:", View_Details_visible)

            # set the value of variable 'assertion_operand_9dbd4a4c03f04af68eefb8ff66f52431_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_9dbd4a4c03f04af68eefb8ff66f52431_0' to true")
            assertion_operand_9dbd4a4c03f04af68eefb8ff66f52431_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Query 'Afghanistan' text visibility
            lambda_hooks(driver, "Query 'Afghanistan' text visibility")
            Afghanistan_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(Afghanistan_visible, dict):
                Afghanistan_visible = Afghanistan_visible.get("vision_query")
            user_variables["Afghanistan_visible"] =  Afghanistan_visible
            print("Afghanistan_visible:", Afghanistan_visible)

            # set the value of variable 'assertion_operand_28b4cb4c5e964cf1873fc33f1e6c2282_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_28b4cb4c5e964cf1873fc33f1e6c2282_0' to true")
            assertion_operand_28b4cb4c5e964cf1873fc33f1e6c2282_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
            print("assertion_result: ", assertion_result)

            # Query 'Afghani' text visibility
            lambda_hooks(driver, "Query 'Afghani' text visibility")
            Afghani_visible = vision_query(driver = driver, operation_index = str(21))
            if isinstance(Afghani_visible, dict):
                Afghani_visible = Afghani_visible.get("vision_query")
            user_variables["Afghani_visible"] =  Afghani_visible
            print("Afghani_visible:", Afghani_visible)

            # set the value of variable 'assertion_operand_7a95b8265c4a42ba8ee145219ee18de9_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7a95b8265c4a42ba8ee145219ee18de9_0' to true")
            assertion_operand_7a95b8265c4a42ba8ee145219ee18de9_0 = "true"
            ui_action(driver = driver, operation_index = str(22))
            assertion_result = ui_action(driver=driver, operation_index=str(23))
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
