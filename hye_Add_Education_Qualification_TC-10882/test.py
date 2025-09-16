
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

            # Click on 'My Info' menu item in left sidebar
            lambda_hooks(driver, "Click on 'My Info' menu item in left sidebar")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on Qualifications tab in left side menu
            lambda_hooks(driver, "Click on Qualifications tab in left side menu")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Click on the Add button in the Education section under Qualifications
            lambda_hooks(driver, "Click on the Add button in the Education section under Qualifications")
            ui_action(driver = driver, operation_index = str(4))

            # Query 'Add Education' text visibility
            lambda_hooks(driver, "Query 'Add Education' text visibility")
            Add_Education_visible = vision_query(driver = driver, operation_index = str(5))
            if isinstance(Add_Education_visible, dict):
                Add_Education_visible = Add_Education_visible.get("vision_query")
            user_variables["Add_Education_visible"] =  Add_Education_visible
            print("Add_Education_visible:", Add_Education_visible)

            # set the value of variable 'assertion_operand_f21a79d28fca44afbf6c6c374842adea_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f21a79d28fca44afbf6c6c374842adea_0' to true")
            assertion_operand_f21a79d28fca44afbf6c6c374842adea_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query 'Level' text visibility
            lambda_hooks(driver, "Query 'Level' text visibility")
            Level_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(Level_visible, dict):
                Level_visible = Level_visible.get("vision_query")
            user_variables["Level_visible"] =  Level_visible
            print("Level_visible:", Level_visible)

            # set the value of variable 'assertion_operand_76b111a746a741f0a223fe2180bbea07_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_76b111a746a741f0a223fe2180bbea07_0' to true")
            assertion_operand_76b111a746a741f0a223fe2180bbea07_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Institute' text visibility
            lambda_hooks(driver, "Query 'Institute' text visibility")
            Institute_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Institute_visible, dict):
                Institute_visible = Institute_visible.get("vision_query")
            user_variables["Institute_visible"] =  Institute_visible
            print("Institute_visible:", Institute_visible)

            # set the value of variable 'assertion_operand_d9e607e976e84466b00bbb534892841d_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d9e607e976e84466b00bbb534892841d_0' to true")
            assertion_operand_d9e607e976e84466b00bbb534892841d_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query 'Major/Specialization' text visibility
            lambda_hooks(driver, "Query 'Major/Specialization' text visibility")
            Major_Specialization_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(Major_Specialization_visible, dict):
                Major_Specialization_visible = Major_Specialization_visible.get("vision_query")
            user_variables["Major_Specialization_visible"] =  Major_Specialization_visible
            print("Major_Specialization_visible:", Major_Specialization_visible)

            # set the value of variable 'assertion_operand_716c6fcce1a24dda99c94703ed3c8c05_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_716c6fcce1a24dda99c94703ed3c8c05_0' to true")
            assertion_operand_716c6fcce1a24dda99c94703ed3c8c05_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'Year' text visibility
            lambda_hooks(driver, "Query 'Year' text visibility")
            Year_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(Year_visible, dict):
                Year_visible = Year_visible.get("vision_query")
            user_variables["Year_visible"] =  Year_visible
            print("Year_visible:", Year_visible)

            # set the value of variable 'assertion_operand_466f403ed64a43318e03849b00a2649b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_466f403ed64a43318e03849b00a2649b_0' to true")
            assertion_operand_466f403ed64a43318e03849b00a2649b_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'GPA/Score' text visibility
            lambda_hooks(driver, "Query 'GPA/Score' text visibility")
            GPA_Score_visible = vision_query(driver = driver, operation_index = str(20))
            if isinstance(GPA_Score_visible, dict):
                GPA_Score_visible = GPA_Score_visible.get("vision_query")
            user_variables["GPA_Score_visible"] =  GPA_Score_visible
            print("GPA_Score_visible:", GPA_Score_visible)

            # set the value of variable 'assertion_operand_05f93f62796545a0913548907cec2c35_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_05f93f62796545a0913548907cec2c35_0' to true")
            assertion_operand_05f93f62796545a0913548907cec2c35_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
            print("assertion_result: ", assertion_result)

            # Query 'Start Date' visibility
            lambda_hooks(driver, "Query 'Start Date' visibility")
            Start_Date_visible = vision_query(driver = driver, operation_index = str(23))
            if isinstance(Start_Date_visible, dict):
                Start_Date_visible = Start_Date_visible.get("vision_query")
            user_variables["Start_Date_visible"] =  Start_Date_visible
            print("Start_Date_visible:", Start_Date_visible)

            # set the value of variable 'assertion_operand_12bffc59fa374e8584dc16b107462734_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_12bffc59fa374e8584dc16b107462734_0' to true")
            assertion_operand_12bffc59fa374e8584dc16b107462734_0 = "true"
            ui_action(driver = driver, operation_index = str(24))
            assertion_result = ui_action(driver=driver, operation_index=str(25))
            print("assertion_result: ", assertion_result)

            # Query 'End Date' visibility
            lambda_hooks(driver, "Query 'End Date' visibility")
            End_Date_visible = vision_query(driver = driver, operation_index = str(26))
            if isinstance(End_Date_visible, dict):
                End_Date_visible = End_Date_visible.get("vision_query")
            user_variables["End_Date_visible"] =  End_Date_visible
            print("End_Date_visible:", End_Date_visible)

            # set the value of variable 'assertion_operand_27e3f5143182469ba69eb2cbbd923d61_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_27e3f5143182469ba69eb2cbbd923d61_0' to true")
            assertion_operand_27e3f5143182469ba69eb2cbbd923d61_0 = "true"
            ui_action(driver = driver, operation_index = str(27))
            assertion_result = ui_action(driver=driver, operation_index=str(28))
            print("assertion_result: ", assertion_result)

            # Query 'Cancel' text visibility
            lambda_hooks(driver, "Query 'Cancel' text visibility")
            Cancel_visible = vision_query(driver = driver, operation_index = str(29))
            if isinstance(Cancel_visible, dict):
                Cancel_visible = Cancel_visible.get("vision_query")
            user_variables["Cancel_visible"] =  Cancel_visible
            print("Cancel_visible:", Cancel_visible)

            # set the value of variable 'assertion_operand_223cce6a231c496e8a1d66b8065ccbbb_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_223cce6a231c496e8a1d66b8065ccbbb_0' to true")
            assertion_operand_223cce6a231c496e8a1d66b8065ccbbb_0 = "true"
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

            # set the value of variable 'assertion_operand_e632a7792e144af2bd0c32f0584a992e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_e632a7792e144af2bd0c32f0584a992e_0' to true")
            assertion_operand_e632a7792e144af2bd0c32f0584a992e_0 = "true"
            ui_action(driver = driver, operation_index = str(33))
            assertion_result = ui_action(driver=driver, operation_index=str(34))
            print("assertion_result: ", assertion_result)

            # Click 'Save' button
            lambda_hooks(driver, "Click 'Save' button")
            ui_action(driver = driver, operation_index = str(35))

            # Query 'Required' text visibility
            lambda_hooks(driver, "Query 'Required' text visibility")
            Required_visible = vision_query(driver = driver, operation_index = str(36))
            if isinstance(Required_visible, dict):
                Required_visible = Required_visible.get("vision_query")
            user_variables["Required_visible"] =  Required_visible
            print("Required_visible:", Required_visible)

            # set the value of variable 'assertion_operand_cd84f60ca002487a842009b776e1bc27_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_cd84f60ca002487a842009b776e1bc27_0' to true")
            assertion_operand_cd84f60ca002487a842009b776e1bc27_0 = "true"
            ui_action(driver = driver, operation_index = str(37))
            assertion_result = ui_action(driver=driver, operation_index=str(38))
            print("assertion_result: ", assertion_result)

            # Click 'Cancel' button
            lambda_hooks(driver, "Click 'Cancel' button")
            ui_action(driver = driver, operation_index = str(39))

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
