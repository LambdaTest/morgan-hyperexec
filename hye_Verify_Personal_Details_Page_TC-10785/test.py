
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

            # Click on 'My Info' menu item in left side menu
            lambda_hooks(driver, "Click on 'My Info' menu item in left side menu")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Query 'Personal Deatils' visibility
            lambda_hooks(driver, "Query 'Personal Deatils' visibility")
            Personal_Deatils_visible = vision_query(driver = driver, operation_index = str(2))
            if isinstance(Personal_Deatils_visible, dict):
                Personal_Deatils_visible = Personal_Deatils_visible.get("vision_query")
            user_variables["Personal_Deatils_visible"] =  Personal_Deatils_visible
            print("Personal_Deatils_visible:", Personal_Deatils_visible)

            # set the value of variable 'assertion_operand_7189c7bd71d34c71b61cf11b06864b04_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7189c7bd71d34c71b61cf11b06864b04_0' to true")
            assertion_operand_7189c7bd71d34c71b61cf11b06864b04_0 = "true"
            ui_action(driver = driver, operation_index = str(3))
            assertion_result = ui_action(driver=driver, operation_index=str(4))
            print("assertion_result: ", assertion_result)

            # Query 'Employee Full name' visibility
            lambda_hooks(driver, "Query 'Employee Full name' visibility")
            Employee_Full_name_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(Employee_Full_name_visible, dict):
                Employee_Full_name_visible = Employee_Full_name_visible.get("vision_query")
            user_variables["Employee_Full_name_visible"] =  Employee_Full_name_visible
            print("Employee_Full_name_visible:", Employee_Full_name_visible)

            # set the value of variable 'assertion_operand_31e23952fd6e4acd9f9f9ebc7e39f15c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_31e23952fd6e4acd9f9f9ebc7e39f15c_0' to true")
            assertion_operand_31e23952fd6e4acd9f9f9ebc7e39f15c_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query 'Employee Id' visibility
            lambda_hooks(driver, "Query 'Employee Id' visibility")
            Employee_Id_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Employee_Id_visible, dict):
                Employee_Id_visible = Employee_Id_visible.get("vision_query")
            user_variables["Employee_Id_visible"] =  Employee_Id_visible
            print("Employee_Id_visible:", Employee_Id_visible)

            # set the value of variable 'assertion_operand_e91b4bdda7804bec9f6193e35e796cb1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e91b4bdda7804bec9f6193e35e796cb1_0' to true")
            assertion_operand_e91b4bdda7804bec9f6193e35e796cb1_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Other Id' text visibility
            lambda_hooks(driver, "Query 'Other Id' text visibility")
            Other_Id_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Other_Id_visible, dict):
                Other_Id_visible = Other_Id_visible.get("vision_query")
            user_variables["Other_Id_visible"] =  Other_Id_visible
            print("Other_Id_visible:", Other_Id_visible)

            # set the value of variable 'assertion_operand_966b0f4c714b4a7eb03a65462ac8f674_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_966b0f4c714b4a7eb03a65462ac8f674_0' to true")
            assertion_operand_966b0f4c714b4a7eb03a65462ac8f674_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Driver's License Number'
            lambda_hooks(driver, "Query visibility of text 'Driver's License Number'")
            drivers_license_number_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(drivers_license_number_visible, dict):
                drivers_license_number_visible = drivers_license_number_visible.get("vision_query")
            user_variables["drivers_license_number_visible"] =  drivers_license_number_visible
            print("drivers_license_number_visible:", drivers_license_number_visible)

            # set the value of variable 'assertion_operand_a7357ee570894f90acf7a4f5b68a3fa1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a7357ee570894f90acf7a4f5b68a3fa1_0' to true")
            assertion_operand_a7357ee570894f90acf7a4f5b68a3fa1_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'License Expiry Date' visibility
            lambda_hooks(driver, "Query 'License Expiry Date' visibility")
            License_Expiry_Date_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(License_Expiry_Date_visible, dict):
                License_Expiry_Date_visible = License_Expiry_Date_visible.get("vision_query")
            user_variables["License_Expiry_Date_visible"] =  License_Expiry_Date_visible
            print("License_Expiry_Date_visible:", License_Expiry_Date_visible)

            # set the value of variable 'assertion_operand_1319fe9744104a54a2aca3ea4e8c7dc3_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1319fe9744104a54a2aca3ea4e8c7dc3_0' to true")
            assertion_operand_1319fe9744104a54a2aca3ea4e8c7dc3_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'Nationality' text visibility
            lambda_hooks(driver, "Query 'Nationality' text visibility")
            Nationality_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(Nationality_visible, dict):
                Nationality_visible = Nationality_visible.get("vision_query")
            user_variables["Nationality_visible"] =  Nationality_visible
            print("Nationality_visible:", Nationality_visible)

            # set the value of variable 'assertion_operand_49d8f23feff344c2b503256cda86b0c8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_49d8f23feff344c2b503256cda86b0c8_0' to true")
            assertion_operand_49d8f23feff344c2b503256cda86b0c8_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Query 'Marital Status' visibility
            lambda_hooks(driver, "Query 'Marital Status' visibility")
            Marital_Status_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(Marital_Status_visible, dict):
                Marital_Status_visible = Marital_Status_visible.get("vision_query")
            user_variables["Marital_Status_visible"] =  Marital_Status_visible
            print("Marital_Status_visible:", Marital_Status_visible)

            # set the value of variable 'assertion_operand_fd981ba7b9a04ae8ba29bd406ee35025_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_fd981ba7b9a04ae8ba29bd406ee35025_0' to true")
            assertion_operand_fd981ba7b9a04ae8ba29bd406ee35025_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
            print("assertion_result: ", assertion_result)

            # Query 'Date of Birth' visibility
            lambda_hooks(driver, "Query 'Date of Birth' visibility")
            Date_of_Birth_visible = vision_query(driver = driver, operation_index = str(26))
            if isinstance(Date_of_Birth_visible, dict):
                Date_of_Birth_visible = Date_of_Birth_visible.get("vision_query")
            user_variables["Date_of_Birth_visible"] =  Date_of_Birth_visible
            print("Date_of_Birth_visible:", Date_of_Birth_visible)

            # set the value of variable 'assertion_operand_333eb8db96fc43dc8e791cedbacde1d8_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_333eb8db96fc43dc8e791cedbacde1d8_0' to true")
            assertion_operand_333eb8db96fc43dc8e791cedbacde1d8_0 = "true"
            ui_action(driver = driver, operation_index = str(27))
            assertion_result = ui_action(driver=driver, operation_index=str(28))
            print("assertion_result: ", assertion_result)

            # Query 'Gender' visibility
            lambda_hooks(driver, "Query 'Gender' visibility")
            Gender_visible = vision_query(driver = driver, operation_index = str(29))
            if isinstance(Gender_visible, dict):
                Gender_visible = Gender_visible.get("vision_query")
            user_variables["Gender_visible"] =  Gender_visible
            print("Gender_visible:", Gender_visible)

            # set the value of variable 'assertion_operand_7d88a181655a43c785c18e16f04c079c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_7d88a181655a43c785c18e16f04c079c_0' to true")
            assertion_operand_7d88a181655a43c785c18e16f04c079c_0 = "true"
            ui_action(driver = driver, operation_index = str(30))
            assertion_result = ui_action(driver=driver, operation_index=str(31))
            print("assertion_result: ", assertion_result)

            # Query 'Save' text visibility
            lambda_hooks(driver, "Query 'Save' text visibility")
            Save_visible = vision_query(driver = driver, operation_index = str(32))
            if isinstance(Save_visible, dict):
                Save_visible = Save_visible.get("vision_query")
            user_variables["Save_visible"] =  Save_visible
            print("Save_visible:", Save_visible)

            # set the value of variable 'assertion_operand_ad0c5d00a28044f09b536e640204e3f3_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ad0c5d00a28044f09b536e640204e3f3_0' to true")
            assertion_operand_ad0c5d00a28044f09b536e640204e3f3_0 = "true"
            ui_action(driver = driver, operation_index = str(33))
            assertion_result = ui_action(driver=driver, operation_index=str(34))
            print("assertion_result: ", assertion_result)

            # Get the current URL
            lambda_hooks(driver, "Get the current URL")
            current_url = response = driver.current_url
            user_variables["current_url"] =  current_url
            print("current_url:", current_url)

            # set the value of variable 'assertion_operand_836298e06d5a4d5bac979dad6bb7fb2b_0' to empNumber/1
            lambda_hooks(driver, "set the value of variable 'assertion_operand_836298e06d5a4d5bac979dad6bb7fb2b_0' to empNumber/1")
            assertion_operand_836298e06d5a4d5bac979dad6bb7fb2b_0 = "empNumber/1"
            ui_action(driver = driver, operation_index = str(36))
            assertion_result = ui_action(driver=driver, operation_index=str(37))
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
