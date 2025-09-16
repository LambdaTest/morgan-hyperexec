
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

            # Click on 'My Info' menu item in the left sidebar
            lambda_hooks(driver, "Click on 'My Info' menu item in the left sidebar")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click on 'Qualifications' tab in the left side menu
            lambda_hooks(driver, "Click on 'Qualifications' tab in the left side menu")
            ui_action(driver = driver, operation_index = str(2))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(3))

            # Query 'Qualifications' text visibility
            lambda_hooks(driver, "Query 'Qualifications' text visibility")
            Qualifications_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(Qualifications_visible, dict):
                Qualifications_visible = Qualifications_visible.get("vision_query")
            user_variables["Qualifications_visible"] =  Qualifications_visible
            print("Qualifications_visible:", Qualifications_visible)

            # set the value of variable 'assertion_operand_48a6ac13b3d948ae97ab3769905ed0a5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_48a6ac13b3d948ae97ab3769905ed0a5_0' to true")
            assertion_operand_48a6ac13b3d948ae97ab3769905ed0a5_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'Work Experience' visibility
            lambda_hooks(driver, "Query 'Work Experience' visibility")
            Work_Experience_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(Work_Experience_visible, dict):
                Work_Experience_visible = Work_Experience_visible.get("vision_query")
            user_variables["Work_Experience_visible"] =  Work_Experience_visible
            print("Work_Experience_visible:", Work_Experience_visible)

            # set the value of variable 'assertion_operand_388866cc1833433c95eb6fb50e636c6c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_388866cc1833433c95eb6fb50e636c6c_0' to true")
            assertion_operand_388866cc1833433c95eb6fb50e636c6c_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'No Records Found' visibility
            lambda_hooks(driver, "Query 'No Records Found' visibility")
            no_records_found_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(no_records_found_visible, dict):
                no_records_found_visible = no_records_found_visible.get("vision_query")
            user_variables["no_records_found_visible"] =  no_records_found_visible
            print("no_records_found_visible:", no_records_found_visible)

            # set the value of variable 'assertion_operand_0877fea01e0e4d31ae8b7c3ce102e995_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_0877fea01e0e4d31ae8b7c3ce102e995_0' to true")
            assertion_operand_0877fea01e0e4d31ae8b7c3ce102e995_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query 'Company' text visibility
            lambda_hooks(driver, "Query 'Company' text visibility")
            Company_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(Company_visible, dict):
                Company_visible = Company_visible.get("vision_query")
            user_variables["Company_visible"] =  Company_visible
            print("Company_visible:", Company_visible)

            # set the value of variable 'assertion_operand_6b6b66315eac45ea8e1737f74054feb9_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_6b6b66315eac45ea8e1737f74054feb9_0' to true")
            assertion_operand_6b6b66315eac45ea8e1737f74054feb9_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query 'Job Title' visibility
            lambda_hooks(driver, "Query 'Job Title' visibility")
            Job_Title_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(Job_Title_visible, dict):
                Job_Title_visible = Job_Title_visible.get("vision_query")
            user_variables["Job_Title_visible"] =  Job_Title_visible
            print("Job_Title_visible:", Job_Title_visible)

            # set the value of variable 'assertion_operand_c4ce33a98d8f43aba9216629627e7641_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c4ce33a98d8f43aba9216629627e7641_0' to true")
            assertion_operand_c4ce33a98d8f43aba9216629627e7641_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
            print("assertion_result: ", assertion_result)

            # Query 'From' text visibility
            lambda_hooks(driver, "Query 'From' text visibility")
            From_visible = vision_query(driver = driver, operation_index = str(19))
            if isinstance(From_visible, dict):
                From_visible = From_visible.get("vision_query")
            user_variables["From_visible"] =  From_visible
            print("From_visible:", From_visible)

            # set the value of variable 'assertion_operand_44ae6b9d6b3c443ba12abb530980b81c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_44ae6b9d6b3c443ba12abb530980b81c_0' to true")
            assertion_operand_44ae6b9d6b3c443ba12abb530980b81c_0 = "true"
            ui_action(driver = driver, operation_index = str(20))
            assertion_result = ui_action(driver=driver, operation_index=str(21))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'To'
            lambda_hooks(driver, "Query visibility of text 'To'")
            To_visible = vision_query(driver = driver, operation_index = str(22))
            if isinstance(To_visible, dict):
                To_visible = To_visible.get("vision_query")
            user_variables["To_visible"] =  To_visible
            print("To_visible:", To_visible)

            # set the value of variable 'assertion_operand_d4031ff46d1e4de881f218cf74ae94f7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_d4031ff46d1e4de881f218cf74ae94f7_0' to true")
            assertion_operand_d4031ff46d1e4de881f218cf74ae94f7_0 = "true"
            ui_action(driver = driver, operation_index = str(23))
            assertion_result = ui_action(driver=driver, operation_index=str(24))
            print("assertion_result: ", assertion_result)

            # Query 'Comment' text visibility
            lambda_hooks(driver, "Query 'Comment' text visibility")
            Comment_visible = vision_query(driver = driver, operation_index = str(25))
            if isinstance(Comment_visible, dict):
                Comment_visible = Comment_visible.get("vision_query")
            user_variables["Comment_visible"] =  Comment_visible
            print("Comment_visible:", Comment_visible)

            # set the value of variable 'assertion_operand_3c01892859764a759cb69c22da9ccabd_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_3c01892859764a759cb69c22da9ccabd_0' to true")
            assertion_operand_3c01892859764a759cb69c22da9ccabd_0 = "true"
            ui_action(driver = driver, operation_index = str(26))
            assertion_result = ui_action(driver=driver, operation_index=str(27))
            print("assertion_result: ", assertion_result)

            # Query 'Actions' text visibility
            lambda_hooks(driver, "Query 'Actions' text visibility")
            Actions_visible = vision_query(driver = driver, operation_index = str(28))
            if isinstance(Actions_visible, dict):
                Actions_visible = Actions_visible.get("vision_query")
            user_variables["Actions_visible"] =  Actions_visible
            print("Actions_visible:", Actions_visible)

            # set the value of variable 'assertion_operand_8df24d5d21df43eca24bd0670424e99f_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_8df24d5d21df43eca24bd0670424e99f_0' to true")
            assertion_operand_8df24d5d21df43eca24bd0670424e99f_0 = "true"
            ui_action(driver = driver, operation_index = str(29))
            assertion_result = ui_action(driver=driver, operation_index=str(30))
            print("assertion_result: ", assertion_result)

            # Query 'Education' text visibility
            lambda_hooks(driver, "Query 'Education' text visibility")
            Education_visible = vision_query(driver = driver, operation_index = str(31))
            if isinstance(Education_visible, dict):
                Education_visible = Education_visible.get("vision_query")
            user_variables["Education_visible"] =  Education_visible
            print("Education_visible:", Education_visible)

            # set the value of variable 'assertion_operand_feb8999f22db44d8986a85e99e9901ad_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_feb8999f22db44d8986a85e99e9901ad_0' to true")
            assertion_operand_feb8999f22db44d8986a85e99e9901ad_0 = "true"
            ui_action(driver = driver, operation_index = str(32))
            assertion_result = ui_action(driver=driver, operation_index=str(33))
            print("assertion_result: ", assertion_result)

            # Query 'Level' text visibility
            lambda_hooks(driver, "Query 'Level' text visibility")
            Level_visible = vision_query(driver = driver, operation_index = str(34))
            if isinstance(Level_visible, dict):
                Level_visible = Level_visible.get("vision_query")
            user_variables["Level_visible"] =  Level_visible
            print("Level_visible:", Level_visible)

            # set the value of variable 'assertion_operand_bbada02d95ac4f3686c0e1972838c584_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_bbada02d95ac4f3686c0e1972838c584_0' to true")
            assertion_operand_bbada02d95ac4f3686c0e1972838c584_0 = "true"
            ui_action(driver = driver, operation_index = str(35))
            assertion_result = ui_action(driver=driver, operation_index=str(36))
            print("assertion_result: ", assertion_result)

            # Query 'Year' text visibility
            lambda_hooks(driver, "Query 'Year' text visibility")
            Year_visible = vision_query(driver = driver, operation_index = str(37))
            if isinstance(Year_visible, dict):
                Year_visible = Year_visible.get("vision_query")
            user_variables["Year_visible"] =  Year_visible
            print("Year_visible:", Year_visible)

            # set the value of variable 'assertion_operand_74537e2f7fd340409c3bba2caef1b0e7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_74537e2f7fd340409c3bba2caef1b0e7_0' to true")
            assertion_operand_74537e2f7fd340409c3bba2caef1b0e7_0 = "true"
            ui_action(driver = driver, operation_index = str(38))
            assertion_result = ui_action(driver=driver, operation_index=str(39))
            print("assertion_result: ", assertion_result)

            # Query 'GPA/Score' text visibility
            lambda_hooks(driver, "Query 'GPA/Score' text visibility")
            GPA_Score_visible = vision_query(driver = driver, operation_index = str(40))
            if isinstance(GPA_Score_visible, dict):
                GPA_Score_visible = GPA_Score_visible.get("vision_query")
            user_variables["GPA_Score_visible"] =  GPA_Score_visible
            print("GPA_Score_visible:", GPA_Score_visible)

            # set the value of variable 'assertion_operand_5c7d13e071b743adb428cb68cb48a43c_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5c7d13e071b743adb428cb68cb48a43c_0' to true")
            assertion_operand_5c7d13e071b743adb428cb68cb48a43c_0 = "true"
            ui_action(driver = driver, operation_index = str(41))
            assertion_result = ui_action(driver=driver, operation_index=str(42))
            print("assertion_result: ", assertion_result)

            # Query 'Skills' text visibility
            lambda_hooks(driver, "Query 'Skills' text visibility")
            Skills_visible = vision_query(driver = driver, operation_index = str(43))
            if isinstance(Skills_visible, dict):
                Skills_visible = Skills_visible.get("vision_query")
            user_variables["Skills_visible"] =  Skills_visible
            print("Skills_visible:", Skills_visible)

            # set the value of variable 'assertion_operand_c503ee829df445a1aa0f84ca28961cb6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_c503ee829df445a1aa0f84ca28961cb6_0' to true")
            assertion_operand_c503ee829df445a1aa0f84ca28961cb6_0 = "true"
            ui_action(driver = driver, operation_index = str(44))
            assertion_result = ui_action(driver=driver, operation_index=str(45))
            print("assertion_result: ", assertion_result)

            # Query 'Skill' text visibility
            lambda_hooks(driver, "Query 'Skill' text visibility")
            Skill_visible = vision_query(driver = driver, operation_index = str(46))
            if isinstance(Skill_visible, dict):
                Skill_visible = Skill_visible.get("vision_query")
            user_variables["Skill_visible"] =  Skill_visible
            print("Skill_visible:", Skill_visible)

            # set the value of variable 'assertion_operand_f738d6c5cc9e429f862b9625e2bf02bb_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f738d6c5cc9e429f862b9625e2bf02bb_0' to true")
            assertion_operand_f738d6c5cc9e429f862b9625e2bf02bb_0 = "true"
            ui_action(driver = driver, operation_index = str(47))
            assertion_result = ui_action(driver=driver, operation_index=str(48))
            print("assertion_result: ", assertion_result)

            # Query 'Year of Experience' visibility
            lambda_hooks(driver, "Query 'Year of Experience' visibility")
            Year_of_Experience_visible = vision_query(driver = driver, operation_index = str(49))
            if isinstance(Year_of_Experience_visible, dict):
                Year_of_Experience_visible = Year_of_Experience_visible.get("vision_query")
            user_variables["Year_of_Experience_visible"] =  Year_of_Experience_visible
            print("Year_of_Experience_visible:", Year_of_Experience_visible)

            # set the value of variable 'assertion_operand_47314e485c7b4eac8093c004f0748736_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_47314e485c7b4eac8093c004f0748736_0' to true")
            assertion_operand_47314e485c7b4eac8093c004f0748736_0 = "true"
            ui_action(driver = driver, operation_index = str(50))
            assertion_result = ui_action(driver=driver, operation_index=str(51))
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
