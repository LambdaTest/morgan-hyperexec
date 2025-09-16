
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
            lambda_hooks(driver, "Click on 'Admin' menu item in the left sidebar")
            ui_action(driver = driver, operation_index = str(0))

            # wait 2 seconds
            lambda_hooks(driver, "wait 2 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Job' tab in the top navigation bar
            lambda_hooks(driver, "Click on 'Job' tab in the top navigation bar")
            ui_action(driver = driver, operation_index = str(2))

            # Click on 'Job Titles' tab in top navigation bar
            lambda_hooks(driver, "Click on 'Job Titles' tab in top navigation bar")
            ui_action(driver = driver, operation_index = str(3))

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            url = response = driver.current_url
            user_variables["url"] =  url
            print("url:", url)

            # set the value of variable 'assertion_operand_cce531416034407cb4134cb47f27abaa_0' to Job
            lambda_hooks(driver, "set the value of variable 'assertion_operand_cce531416034407cb4134cb47f27abaa_0' to Job")
            assertion_operand_cce531416034407cb4134cb47f27abaa_0 = "Job"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'Job Titles' text visibility
            lambda_hooks(driver, "Query 'Job Titles' text visibility")
            job_titles_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(job_titles_visible, dict):
                job_titles_visible = job_titles_visible.get("vision_query")
            user_variables["job_titles_visible"] =  job_titles_visible
            print("job_titles_visible:", job_titles_visible)

            # set the value of variable 'assertion_operand_3e3a4ae6f4104cdd8db70313c78148ce_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3e3a4ae6f4104cdd8db70313c78148ce_0' to true")
            assertion_operand_3e3a4ae6f4104cdd8db70313c78148ce_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query '+ Add' text visibility
            lambda_hooks(driver, "Query '+ Add' text visibility")
            add_text_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(add_text_visible, dict):
                add_text_visible = add_text_visible.get("vision_query")
            user_variables["add_text_visible"] =  add_text_visible
            print("add_text_visible:", add_text_visible)

            # set the value of variable 'assertion_operand_dcd5caef334a4ffc8c88fa8a02ebfadb_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_dcd5caef334a4ffc8c88fa8a02ebfadb_0' to true")
            assertion_operand_dcd5caef334a4ffc8c88fa8a02ebfadb_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
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
