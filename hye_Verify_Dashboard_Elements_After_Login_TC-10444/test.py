
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

            # Query 'Admin' text visibility
            lambda_hooks(driver, "Query 'Admin' text visibility")
            Admin_visible = vision_query(driver = driver, operation_index = str(0))
            if isinstance(Admin_visible, dict):
                Admin_visible = Admin_visible.get("vision_query")
            user_variables["Admin_visible"] =  Admin_visible
            print("Admin_visible:", Admin_visible)

            # set the value of variable 'assertion_operand_fe2d8e66d8c14c53898d1a0f241095a8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_fe2d8e66d8c14c53898d1a0f241095a8_0' to true")
            assertion_operand_fe2d8e66d8c14c53898d1a0f241095a8_0 = "true"
            ui_action(driver = driver, operation_index = str(1))
            assertion_result = ui_action(driver=driver, operation_index=str(2))
            print("assertion_result: ", assertion_result)

            # Query 'PIM' text visibility
            lambda_hooks(driver, "Query 'PIM' text visibility")
            PIM_visible = vision_query(driver = driver, operation_index = str(3))
            if isinstance(PIM_visible, dict):
                PIM_visible = PIM_visible.get("vision_query")
            user_variables["PIM_visible"] =  PIM_visible
            print("PIM_visible:", PIM_visible)

            # set the value of variable 'assertion_operand_599801e1f65d4e13b5b8bc00219c0461_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_599801e1f65d4e13b5b8bc00219c0461_0' to true")
            assertion_operand_599801e1f65d4e13b5b8bc00219c0461_0 = "true"
            ui_action(driver = driver, operation_index = str(4))
            assertion_result = ui_action(driver=driver, operation_index=str(5))
            print("assertion_result: ", assertion_result)

            # Query 'Leave' text visibility
            lambda_hooks(driver, "Query 'Leave' text visibility")
            Leave_visible = vision_query(driver = driver, operation_index = str(6))
            if isinstance(Leave_visible, dict):
                Leave_visible = Leave_visible.get("vision_query")
            user_variables["Leave_visible"] =  Leave_visible
            print("Leave_visible:", Leave_visible)

            # set the value of variable 'assertion_operand_b4f4d0d5af7c49e4898a7024b78c1e33_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_b4f4d0d5af7c49e4898a7024b78c1e33_0' to true")
            assertion_operand_b4f4d0d5af7c49e4898a7024b78c1e33_0 = "true"
            ui_action(driver = driver, operation_index = str(7))
            assertion_result = ui_action(driver=driver, operation_index=str(8))
            print("assertion_result: ", assertion_result)

            # Query 'Time' text visibility
            lambda_hooks(driver, "Query 'Time' text visibility")
            Time_visible = vision_query(driver = driver, operation_index = str(9))
            if isinstance(Time_visible, dict):
                Time_visible = Time_visible.get("vision_query")
            user_variables["Time_visible"] =  Time_visible
            print("Time_visible:", Time_visible)

            # set the value of variable 'assertion_operand_d26311ee41c3490ba313a460986bcbdb_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d26311ee41c3490ba313a460986bcbdb_0' to true")
            assertion_operand_d26311ee41c3490ba313a460986bcbdb_0 = "true"
            ui_action(driver = driver, operation_index = str(10))
            assertion_result = ui_action(driver=driver, operation_index=str(11))
            print("assertion_result: ", assertion_result)

            # Query 'Recruitment' text visibility
            lambda_hooks(driver, "Query 'Recruitment' text visibility")
            Recruitment_visible = vision_query(driver = driver, operation_index = str(12))
            if isinstance(Recruitment_visible, dict):
                Recruitment_visible = Recruitment_visible.get("vision_query")
            user_variables["Recruitment_visible"] =  Recruitment_visible
            print("Recruitment_visible:", Recruitment_visible)

            # set the value of variable 'assertion_operand_96de9ed7292a431291127cec3db2d6e9_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_96de9ed7292a431291127cec3db2d6e9_0' to true")
            assertion_operand_96de9ed7292a431291127cec3db2d6e9_0 = "true"
            ui_action(driver = driver, operation_index = str(13))
            assertion_result = ui_action(driver=driver, operation_index=str(14))
            print("assertion_result: ", assertion_result)

            # Query 'My Info' text visibility
            lambda_hooks(driver, "Query 'My Info' text visibility")
            my_info_visible = vision_query(driver = driver, operation_index = str(15))
            if isinstance(my_info_visible, dict):
                my_info_visible = my_info_visible.get("vision_query")
            user_variables["my_info_visible"] =  my_info_visible
            print("my_info_visible:", my_info_visible)

            # set the value of variable 'assertion_operand_99ed0d51b29a4955a27297b568b568e0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_99ed0d51b29a4955a27297b568b568e0_0' to true")
            assertion_operand_99ed0d51b29a4955a27297b568b568e0_0 = "true"
            ui_action(driver = driver, operation_index = str(16))
            assertion_result = ui_action(driver=driver, operation_index=str(17))
            print("assertion_result: ", assertion_result)

            # Query 'Dashboard' text visibility
            lambda_hooks(driver, "Query 'Dashboard' text visibility")
            Dashboard_visible = vision_query(driver = driver, operation_index = str(18))
            if isinstance(Dashboard_visible, dict):
                Dashboard_visible = Dashboard_visible.get("vision_query")
            user_variables["Dashboard_visible"] =  Dashboard_visible
            print("Dashboard_visible:", Dashboard_visible)

            # set the value of variable 'assertion_operand_2de35aa08cd24a19be0b876c5a707170_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2de35aa08cd24a19be0b876c5a707170_0' to true")
            assertion_operand_2de35aa08cd24a19be0b876c5a707170_0 = "true"
            ui_action(driver = driver, operation_index = str(19))
            assertion_result = ui_action(driver=driver, operation_index=str(20))
            print("assertion_result: ", assertion_result)

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            url = response = driver.current_url
            user_variables["url"] =  url
            print("url:", url)

            # set the value of variable 'assertion_operand_15f67e4cc33a47a1b2ea64ea42274796_0' to dashboard
            lambda_hooks(driver, "set the value of variable 'assertion_operand_15f67e4cc33a47a1b2ea64ea42274796_0' to dashboard")
            assertion_operand_15f67e4cc33a47a1b2ea64ea42274796_0 = "dashboard"
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
