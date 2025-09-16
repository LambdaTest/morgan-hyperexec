
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
            lambda_hooks(driver, "Click on 'My Info' menu item in left side menu")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Salary' tab in the left side menu under 'My Info'
            lambda_hooks(driver, "Click on 'Salary' tab in the left side menu under 'My Info'")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Query visibility of text 'Assigned Salary Components'
            lambda_hooks(driver, "Query visibility of text 'Assigned Salary Components'")
            assigned_salary_components_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(assigned_salary_components_visible, dict):
                assigned_salary_components_visible = assigned_salary_components_visible.get("vision_query")
            user_variables["assigned_salary_components_visible"] =  assigned_salary_components_visible
            print("assigned_salary_components_visible:", assigned_salary_components_visible)

            # set the value of variable 'assertion_operand_e4ea99540a3e4a9e91591114c4189b60_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e4ea99540a3e4a9e91591114c4189b60_0' to true")
            assertion_operand_e4ea99540a3e4a9e91591114c4189b60_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'No Records Found' visibility
            lambda_hooks(driver, "Query 'No Records Found' visibility")
            no_records_found_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(no_records_found_visible, dict):
                no_records_found_visible = no_records_found_visible.get("vision_query")
            user_variables["no_records_found_visible"] =  no_records_found_visible
            print("no_records_found_visible:", no_records_found_visible)

            # set the value of variable 'assertion_operand_d3d038cc9d2f4cb9845f8681a0e76ae1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d3d038cc9d2f4cb9845f8681a0e76ae1_0' to true")
            assertion_operand_d3d038cc9d2f4cb9845f8681a0e76ae1_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Salary Component' visibility
            lambda_hooks(driver, "Query 'Salary Component' visibility")
            Salary_Component_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Salary_Component_visible, dict):
                Salary_Component_visible = Salary_Component_visible.get("vision_query")
            user_variables["Salary_Component_visible"] =  Salary_Component_visible
            print("Salary_Component_visible:", Salary_Component_visible)

            # set the value of variable 'assertion_operand_222b05dec33e4579841270445a7bc8bb_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_222b05dec33e4579841270445a7bc8bb_0' to true")
            assertion_operand_222b05dec33e4579841270445a7bc8bb_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Amount' visibility
            lambda_hooks(driver, "Query 'Amount' visibility")
            Amount_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Amount_visible, dict):
                Amount_visible = Amount_visible.get("vision_query")
            user_variables["Amount_visible"] =  Amount_visible
            print("Amount_visible:", Amount_visible)

            # set the value of variable 'assertion_operand_8b3df06c7fec457586b69298de5b87df_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8b3df06c7fec457586b69298de5b87df_0' to true")
            assertion_operand_8b3df06c7fec457586b69298de5b87df_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Currency' text visibility
            lambda_hooks(driver, "Query 'Currency' text visibility")
            Currency_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Currency_visible, dict):
                Currency_visible = Currency_visible.get("vision_query")
            user_variables["Currency_visible"] =  Currency_visible
            print("Currency_visible:", Currency_visible)

            # set the value of variable 'assertion_operand_02716d1205574e47a8d540ff55d88e3c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_02716d1205574e47a8d540ff55d88e3c_0' to true")
            assertion_operand_02716d1205574e47a8d540ff55d88e3c_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'Pay Frequency' text visibility
            lambda_hooks(driver, "Query 'Pay Frequency' text visibility")
            pay_frequency_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(pay_frequency_visible, dict):
                pay_frequency_visible = pay_frequency_visible.get("vision_query")
            user_variables["pay_frequency_visible"] =  pay_frequency_visible
            print("pay_frequency_visible:", pay_frequency_visible)

            # set the value of variable 'assertion_operand_63d036ba305f4709bd137b6ef8f46831_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_63d036ba305f4709bd137b6ef8f46831_0' to true")
            assertion_operand_63d036ba305f4709bd137b6ef8f46831_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query 'Direct Deposit Amount' visibility
            lambda_hooks(driver, "Query 'Direct Deposit Amount' visibility")
            Direct_Deposit_Amount_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(Direct_Deposit_Amount_visible, dict):
                Direct_Deposit_Amount_visible = Direct_Deposit_Amount_visible.get("vision_query")
            user_variables["Direct_Deposit_Amount_visible"] =  Direct_Deposit_Amount_visible
            print("Direct_Deposit_Amount_visible:", Direct_Deposit_Amount_visible)

            # set the value of variable 'assertion_operand_0106528d80024abd8ddd963ed477e36f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0106528d80024abd8ddd963ed477e36f_0' to true")
            assertion_operand_0106528d80024abd8ddd963ed477e36f_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Query 'File Name' visibility
            lambda_hooks(driver, "Query 'File Name' visibility")
            File_Name_visible = vision_query(driver = driver, operation_index = str(25))
            if isinstance(File_Name_visible, dict):
                File_Name_visible = File_Name_visible.get("vision_query")
            user_variables["File_Name_visible"] =  File_Name_visible
            print("File_Name_visible:", File_Name_visible)

            # set the value of variable 'assertion_operand_2891213769c64230a7c9ec3709cf3f42_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_2891213769c64230a7c9ec3709cf3f42_0' to true")
            assertion_operand_2891213769c64230a7c9ec3709cf3f42_0 = "true"
            ui_action(driver = driver, operation_index = str(26))
            assertion_result = ui_action(driver=driver, operation_index=str(27))
            print("assertion_result: ", assertion_result)

            # Query 'Description' visibility
            lambda_hooks(driver, "Query 'Description' visibility")
            Description_visible = vision_query(driver = driver, operation_index = str(28))
            if isinstance(Description_visible, dict):
                Description_visible = Description_visible.get("vision_query")
            user_variables["Description_visible"] =  Description_visible
            print("Description_visible:", Description_visible)

            # set the value of variable 'assertion_operand_e05680b572d64c6680e245456f280f73_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e05680b572d64c6680e245456f280f73_0' to true")
            assertion_operand_e05680b572d64c6680e245456f280f73_0 = "true"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Size'
            lambda_hooks(driver, "Query visibility of text 'Size'")
            Size_visible = vision_query(driver = driver, operation_index = str(31))
            if isinstance(Size_visible, dict):
                Size_visible = Size_visible.get("vision_query")
            user_variables["Size_visible"] =  Size_visible
            print("Size_visible:", Size_visible)

            # set the value of variable 'assertion_operand_63ff5f9ae0124b9e8b9c4ed76a3bccd0_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_63ff5f9ae0124b9e8b9c4ed76a3bccd0_0' to true")
            assertion_operand_63ff5f9ae0124b9e8b9c4ed76a3bccd0_0 = "true"
            ui_action(driver = driver, operation_index = str(32))
            assertion_result = ui_action(driver=driver, operation_index=str(33))
            print("assertion_result: ", assertion_result)

            # Query 'Type' text visibility
            lambda_hooks(driver, "Query 'Type' text visibility")
            Type_visible = vision_query(driver = driver, operation_index = str(34))
            if isinstance(Type_visible, dict):
                Type_visible = Type_visible.get("vision_query")
            user_variables["Type_visible"] =  Type_visible
            print("Type_visible:", Type_visible)

            # set the value of variable 'assertion_operand_d3182eb1e684440bbd47f7afc4225188_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d3182eb1e684440bbd47f7afc4225188_0' to true")
            assertion_operand_d3182eb1e684440bbd47f7afc4225188_0 = "true"
            ui_action(driver = driver, operation_index = str(35))
            assertion_result = ui_action(driver=driver, operation_index=str(36))
            print("assertion_result: ", assertion_result)

            # Query 'Date Added' text visibility
            lambda_hooks(driver, "Query 'Date Added' text visibility")
            Date_Added_visible = vision_query(driver = driver, operation_index = str(37))
            if isinstance(Date_Added_visible, dict):
                Date_Added_visible = Date_Added_visible.get("vision_query")
            user_variables["Date_Added_visible"] =  Date_Added_visible
            print("Date_Added_visible:", Date_Added_visible)

            # set the value of variable 'assertion_operand_fbbe1f6862ea4c7cb8d6fa7663861a1a_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_fbbe1f6862ea4c7cb8d6fa7663861a1a_0' to true")
            assertion_operand_fbbe1f6862ea4c7cb8d6fa7663861a1a_0 = "true"
            ui_action(driver = driver, operation_index = str(38))
            assertion_result = ui_action(driver=driver, operation_index=str(39))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Added by'
            lambda_hooks(driver, "Query visibility of text 'Added by'")
            added_by_visible = vision_query(driver = driver, operation_index = str(40))
            if isinstance(added_by_visible, dict):
                added_by_visible = added_by_visible.get("vision_query")
            user_variables["added_by_visible"] =  added_by_visible
            print("added_by_visible:", added_by_visible)

            # set the value of variable 'assertion_operand_c22a29a6c5d949af9d22254398f4f16d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c22a29a6c5d949af9d22254398f4f16d_0' to true")
            assertion_operand_c22a29a6c5d949af9d22254398f4f16d_0 = "true"
            ui_action(driver = driver, operation_index = str(41))
            assertion_result = ui_action(driver=driver, operation_index=str(42))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible = vision_query(driver = driver, operation_index = str(43))
            if isinstance(Actions_visible, dict):
                Actions_visible = Actions_visible.get("vision_query")
            user_variables["Actions_visible"] =  Actions_visible
            print("Actions_visible:", Actions_visible)

            # set the value of variable 'assertion_operand_3bc6bd8f72bd4d24a2f5950af0462f3c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3bc6bd8f72bd4d24a2f5950af0462f3c_0' to true")
            assertion_operand_3bc6bd8f72bd4d24a2f5950af0462f3c_0 = "true"
            ui_action(driver = driver, operation_index = str(44))
            assertion_result = ui_action(driver=driver, operation_index=str(45))
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
