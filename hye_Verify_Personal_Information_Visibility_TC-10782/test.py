
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

            # Click on 'My Info' menu item in left side menu 
            lambda_hooks(driver, "Click on 'My Info' menu item in left side menu ")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Query 'Personal Details' visibility
            lambda_hooks(driver, "Query 'Personal Details' visibility")
            Personal_Details_visible = vision_query(driver = driver, operation_index = str(2))
            if isinstance(Personal_Details_visible, dict):
                Personal_Details_visible = Personal_Details_visible.get("vision_query")
            user_variables["Personal_Details_visible"] =  Personal_Details_visible
            print("Personal_Details_visible:", Personal_Details_visible)

            # set the value of variable 'assertion_operand_82925fa50bb348508db8d042d5924ba6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_82925fa50bb348508db8d042d5924ba6_0' to true")
            assertion_operand_82925fa50bb348508db8d042d5924ba6_0 = "true"
            ui_action(driver = driver, operation_index = str(3))
            assertion_result = ui_action(driver=driver, operation_index=str(4))
            print("assertion_result: ", assertion_result)

            # Query 'Contact Details' visibility
            lambda_hooks(driver, "Query 'Contact Details' visibility")
            contact_details_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(contact_details_visible, dict):
                contact_details_visible = contact_details_visible.get("vision_query")
            user_variables["contact_details_visible"] =  contact_details_visible
            print("contact_details_visible:", contact_details_visible)

            # set the value of variable 'assertion_operand_0cb110adccb8464cb0f3b1ab295a1803_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0cb110adccb8464cb0f3b1ab295a1803_0' to true")
            assertion_operand_0cb110adccb8464cb0f3b1ab295a1803_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query 'Emergency Contacts' visibility
            lambda_hooks(driver, "Query 'Emergency Contacts' visibility")
            Emergency_Contacts_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Emergency_Contacts_visible, dict):
                Emergency_Contacts_visible = Emergency_Contacts_visible.get("vision_query")
            user_variables["Emergency_Contacts_visible"] =  Emergency_Contacts_visible
            print("Emergency_Contacts_visible:", Emergency_Contacts_visible)

            # set the value of variable 'assertion_operand_cf2c4bdeb1a547c8819f43fc74f3c846_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_cf2c4bdeb1a547c8819f43fc74f3c846_0' to true")
            assertion_operand_cf2c4bdeb1a547c8819f43fc74f3c846_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Dependents' visibility
            lambda_hooks(driver, "Query 'Dependents' visibility")
            Dependents_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Dependents_visible, dict):
                Dependents_visible = Dependents_visible.get("vision_query")
            user_variables["Dependents_visible"] =  Dependents_visible
            print("Dependents_visible:", Dependents_visible)

            # set the value of variable 'assertion_operand_e69cb549b35441649b47a6c418185af6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e69cb549b35441649b47a6c418185af6_0' to true")
            assertion_operand_e69cb549b35441649b47a6c418185af6_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query 'Immigrations' text visibility
            lambda_hooks(driver, "Query 'Immigrations' text visibility")
            Immigrations_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(Immigrations_visible, dict):
                Immigrations_visible = Immigrations_visible.get("vision_query")
            user_variables["Immigrations_visible"] =  Immigrations_visible
            print("Immigrations_visible:", Immigrations_visible)

            # set the value of variable 'assertion_operand_a3e809b7f84d4869b93e6d1b5227b48c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a3e809b7f84d4869b93e6d1b5227b48c_0' to true")
            assertion_operand_a3e809b7f84d4869b93e6d1b5227b48c_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'Job' text visibility
            lambda_hooks(driver, "Query 'Job' text visibility")
            Job_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(Job_visible, dict):
                Job_visible = Job_visible.get("vision_query")
            user_variables["Job_visible"] =  Job_visible
            print("Job_visible:", Job_visible)

            # set the value of variable 'assertion_operand_0f741ec3840b4cefb1ba32c3f53600d8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0f741ec3840b4cefb1ba32c3f53600d8_0' to true")
            assertion_operand_0f741ec3840b4cefb1ba32c3f53600d8_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'Salary' text visibility
            lambda_hooks(driver, "Query 'Salary' text visibility")
            Salary_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(Salary_visible, dict):
                Salary_visible = Salary_visible.get("vision_query")
            user_variables["Salary_visible"] =  Salary_visible
            print("Salary_visible:", Salary_visible)

            # set the value of variable 'assertion_operand_dacd84790a6840cfaff27bf8913857bd_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_dacd84790a6840cfaff27bf8913857bd_0' to true")
            assertion_operand_dacd84790a6840cfaff27bf8913857bd_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Query 'Report-to' visibility
            lambda_hooks(driver, "Query 'Report-to' visibility")
            Report_to_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(Report_to_visible, dict):
                Report_to_visible = Report_to_visible.get("vision_query")
            user_variables["Report_to_visible"] =  Report_to_visible
            print("Report_to_visible:", Report_to_visible)

            # set the value of variable 'assertion_operand_4ecdf4aca8cc4c5fbc52b2d73e79f16e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_4ecdf4aca8cc4c5fbc52b2d73e79f16e_0' to true")
            assertion_operand_4ecdf4aca8cc4c5fbc52b2d73e79f16e_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
            print("assertion_result: ", assertion_result)

            # Query 'Qualifications' text visibility
            lambda_hooks(driver, "Query 'Qualifications' text visibility")
            Qualifications_visible = vision_query(driver = driver, operation_index = str(26))
            if isinstance(Qualifications_visible, dict):
                Qualifications_visible = Qualifications_visible.get("vision_query")
            user_variables["Qualifications_visible"] =  Qualifications_visible
            print("Qualifications_visible:", Qualifications_visible)

            # set the value of variable 'assertion_operand_0d3eb2f94c2e4338823c2331a1ace69d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0d3eb2f94c2e4338823c2331a1ace69d_0' to true")
            assertion_operand_0d3eb2f94c2e4338823c2331a1ace69d_0 = "true"
            ui_action(driver = driver, operation_index = str(27))
            assertion_result = ui_action(driver=driver, operation_index=str(28))
            print("assertion_result: ", assertion_result)

            # Query 'Memberships' visibility
            lambda_hooks(driver, "Query 'Memberships' visibility")
            Memberships_visible = vision_query(driver = driver, operation_index = str(29))
            if isinstance(Memberships_visible, dict):
                Memberships_visible = Memberships_visible.get("vision_query")
            user_variables["Memberships_visible"] =  Memberships_visible
            print("Memberships_visible:", Memberships_visible)

            # set the value of variable 'assertion_operand_69be28c4ed9c48358874cbc43cc769e4_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_69be28c4ed9c48358874cbc43cc769e4_0' to true")
            assertion_operand_69be28c4ed9c48358874cbc43cc769e4_0 = "true"
            ui_action(driver = driver, operation_index = str(30))
            assertion_result = ui_action(driver=driver, operation_index=str(31))
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
