
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

            # Click on 'Admin' menu item in left side menu
            lambda_hooks(driver, "Click on 'Admin' menu item in left side menu")
            ui_action(driver = driver, operation_index = str(0))

            # Query 'System Users' text visibility
            lambda_hooks(driver, "Query 'System Users' text visibility")
            System_Users_visible = vision_query(driver = driver, operation_index = str(1))
            if isinstance(System_Users_visible, dict):
                System_Users_visible = System_Users_visible.get("vision_query")
            user_variables["System_Users_visible"] =  System_Users_visible
            print("System_Users_visible:", System_Users_visible)

            # set the value of variable 'assertion_operand_e56cb5e8fa1f492b8c43120aee801843_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e56cb5e8fa1f492b8c43120aee801843_0' to true")
            assertion_operand_e56cb5e8fa1f492b8c43120aee801843_0 = "true"
            ui_action(driver = driver, operation_index = str(2))
            assertion_result = ui_action(driver=driver, operation_index=str(3))
            print("assertion_result: ", assertion_result)

            # Query 'Username' text visibility
            lambda_hooks(driver, "Query 'Username' text visibility")
            Username_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(Username_visible, dict):
                Username_visible = Username_visible.get("vision_query")
            user_variables["Username_visible"] =  Username_visible
            print("Username_visible:", Username_visible)

            # set the value of variable 'assertion_operand_c9a2cfa693f9442cbdf75db058d3464b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c9a2cfa693f9442cbdf75db058d3464b_0' to true")
            assertion_operand_c9a2cfa693f9442cbdf75db058d3464b_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'Reset' text visibility
            lambda_hooks(driver, "Query 'Reset' text visibility")
            Reset_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(Reset_visible, dict):
                Reset_visible = Reset_visible.get("vision_query")
            user_variables["Reset_visible"] =  Reset_visible
            print("Reset_visible:", Reset_visible)

            # set the value of variable 'assertion_operand_f3c9750ce3d4441793ce391f0becbe76_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f3c9750ce3d4441793ce391f0becbe76_0' to true")
            assertion_operand_f3c9750ce3d4441793ce391f0becbe76_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Search' text visibility
            lambda_hooks(driver, "Query 'Search' text visibility")
            Search_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Search_visible, dict):
                Search_visible = Search_visible.get("vision_query")
            user_variables["Search_visible"] =  Search_visible
            print("Search_visible:", Search_visible)

            # set the value of variable 'assertion_operand_17fe1df0c1a54e21b98315cb0fb8858b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_17fe1df0c1a54e21b98315cb0fb8858b_0' to true")
            assertion_operand_17fe1df0c1a54e21b98315cb0fb8858b_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query '+ ADD' text visibility
            lambda_hooks(driver, "Query '+ ADD' text visibility")
            add_text_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(add_text_visible, dict):
                add_text_visible = add_text_visible.get("vision_query")
            user_variables["add_text_visible"] =  add_text_visible
            print("add_text_visible:", add_text_visible)

            # set the value of variable 'assertion_operand_708d02a44b1e4d32b87f53dcd2052f99_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_708d02a44b1e4d32b87f53dcd2052f99_0' to true")
            assertion_operand_708d02a44b1e4d32b87f53dcd2052f99_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'ayushp' text visibility
            lambda_hooks(driver, "Query 'ayushp' text visibility")
            ayushp_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(ayushp_visible, dict):
                ayushp_visible = ayushp_visible.get("vision_query")
            user_variables["ayushp_visible"] =  ayushp_visible
            print("ayushp_visible:", ayushp_visible)

            # set the value of variable 'assertion_operand_2cab9dff114a4b369e52e755c4067773_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2cab9dff114a4b369e52e755c4067773_0' to true")
            assertion_operand_2cab9dff114a4b369e52e755c4067773_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'pushpa.raj' text visibility
            lambda_hooks(driver, "Query 'pushpa.raj' text visibility")
            pushpa_raj_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(pushpa_raj_visible, dict):
                pushpa_raj_visible = pushpa_raj_visible.get("vision_query")
            user_variables["pushpa_raj_visible"] =  pushpa_raj_visible
            print("pushpa_raj_visible:", pushpa_raj_visible)

            # set the value of variable 'assertion_operand_7b325febc0c9410da8418cf216086c82_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7b325febc0c9410da8418cf216086c82_0' to true")
            assertion_operand_7b325febc0c9410da8418cf216086c82_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'status' text visibility
            lambda_hooks(driver, "Query 'status' text visibility")
            status_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(status_visible, dict):
                status_visible = status_visible.get("vision_query")
            user_variables["status_visible"] =  status_visible
            print("status_visible:", status_visible)

            # set the value of variable 'assertion_operand_f9b300cad0e24f8389328a8913b69221_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f9b300cad0e24f8389328a8913b69221_0' to true")
            assertion_operand_f9b300cad0e24f8389328a8913b69221_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Query 'Delete' icon visibility
            lambda_hooks(driver, "Query 'Delete' icon visibility")
            Delete_icon_visible = vision_query(driver = driver, operation_index = str(25))
            if isinstance(Delete_icon_visible, dict):
                Delete_icon_visible = Delete_icon_visible.get("vision_query")
            user_variables["Delete_icon_visible"] =  Delete_icon_visible
            print("Delete_icon_visible:", Delete_icon_visible)

            # set the value of variable 'assertion_operand_5911fcc91c274d5db405ab6d3be9317a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5911fcc91c274d5db405ab6d3be9317a_0' to true")
            assertion_operand_5911fcc91c274d5db405ab6d3be9317a_0 = "true"
            ui_action(driver = driver, operation_index = str(26))
            assertion_result = ui_action(driver=driver, operation_index=str(27))
            print("assertion_result: ", assertion_result)

            # Query 'Edit' icon visibility
            lambda_hooks(driver, "Query 'Edit' icon visibility")
            edit_icon_visible = vision_query(driver = driver, operation_index = str(28))
            if isinstance(edit_icon_visible, dict):
                edit_icon_visible = edit_icon_visible.get("vision_query")
            user_variables["edit_icon_visible"] =  edit_icon_visible
            print("edit_icon_visible:", edit_icon_visible)

            # set the value of variable 'assertion_operand_2333e3bfed5a4e338d69926aef0775e7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2333e3bfed5a4e338d69926aef0775e7_0' to true")
            assertion_operand_2333e3bfed5a4e338d69926aef0775e7_0 = "true"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
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
