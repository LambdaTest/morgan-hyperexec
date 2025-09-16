
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

            # Click 'PIM'
            lambda_hooks(driver, "Click 'PIM'")
            ui_action(driver = driver, operation_index = str(0))

            # wait 3 seconds
            lambda_hooks(driver, "wait 3 seconds")
            ui_action(driver = driver, operation_index = str(1))

            # Click 'Configuration'
            lambda_hooks(driver, "Click 'Configuration'")
            ui_action(driver = driver, operation_index = str(2))

            # Click 'Optional Fields' dropdown
            lambda_hooks(driver, "Click 'Optional Fields' dropdown")
            ui_action(driver = driver, operation_index = str(3))

            # wait 5 seconds
            lambda_hooks(driver, "wait 5 seconds")
            ui_action(driver = driver, operation_index = str(4))

            # Query visibility of 'Show Deprecated Fields' text
            lambda_hooks(driver, "Query visibility of 'Show Deprecated Fields' text")
            show_deprecated_fields_visible_0d32c4 = vision_query(driver = driver, operation_index = str(5))
            if isinstance(show_deprecated_fields_visible_0d32c4, dict):
                show_deprecated_fields_visible_0d32c4 = show_deprecated_fields_visible_0d32c4.get("vision_query")
            user_variables["show_deprecated_fields_visible_0d32c4"] =  show_deprecated_fields_visible_0d32c4
            print("show_deprecated_fields_visible_0d32c4:", show_deprecated_fields_visible_0d32c4)

            # set the value of variable 'assertion_operand_1c54324ddcfa4af7be53867cdff6dade_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_1c54324ddcfa4af7be53867cdff6dade_0' to true")
            assertion_operand_1c54324ddcfa4af7be53867cdff6dade_0 = "true"
            ui_action(driver = driver, operation_index = str(6))
            assertion_result = ui_action(driver=driver, operation_index=str(7))
            print("assertion_result: ", assertion_result)

            # Query visibility of 'Show Nick Name, Smoker and Military Service in Personal Details' text
            lambda_hooks(driver, "Query visibility of 'Show Nick Name, Smoker and Military Service in Personal Details' text")
            show_nick_name_text_visible = vision_query(driver = driver, operation_index = str(8))
            if isinstance(show_nick_name_text_visible, dict):
                show_nick_name_text_visible = show_nick_name_text_visible.get("vision_query")
            user_variables["show_nick_name_text_visible"] =  show_nick_name_text_visible
            print("show_nick_name_text_visible:", show_nick_name_text_visible)

            # set the value of variable 'assertion_operand_5895c14364004f25a0e0c7adbdcc8fb7_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_5895c14364004f25a0e0c7adbdcc8fb7_0' to true")
            assertion_operand_5895c14364004f25a0e0c7adbdcc8fb7_0 = "true"
            ui_action(driver = driver, operation_index = str(9))
            assertion_result = ui_action(driver=driver, operation_index=str(10))
            print("assertion_result: ", assertion_result)

            # Query 'Country Specific Information' text visibility
            lambda_hooks(driver, "Query 'Country Specific Information' text visibility")
            Country_Specific_Information_visible = vision_query(driver = driver, operation_index = str(11))
            if isinstance(Country_Specific_Information_visible, dict):
                Country_Specific_Information_visible = Country_Specific_Information_visible.get("vision_query")
            user_variables["Country_Specific_Information_visible"] =  Country_Specific_Information_visible
            print("Country_Specific_Information_visible:", Country_Specific_Information_visible)

            # set the value of variable 'assertion_operand_f4d97834effd4d9798c9502c7cc19b96_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f4d97834effd4d9798c9502c7cc19b96_0' to true")
            assertion_operand_f4d97834effd4d9798c9502c7cc19b96_0 = "true"
            ui_action(driver = driver, operation_index = str(12))
            assertion_result = ui_action(driver=driver, operation_index=str(13))
            print("assertion_result: ", assertion_result)

            # Query if 'Show SSN field in Personal Details' text is displayed
            lambda_hooks(driver, "Query if 'Show SSN field in Personal Details' text is displayed")
            show_ssn_field_in_personal_details_visible = vision_query(driver = driver, operation_index = str(14))
            if isinstance(show_ssn_field_in_personal_details_visible, dict):
                show_ssn_field_in_personal_details_visible = show_ssn_field_in_personal_details_visible.get("vision_query")
            user_variables["show_ssn_field_in_personal_details_visible"] =  show_ssn_field_in_personal_details_visible
            print("show_ssn_field_in_personal_details_visible:", show_ssn_field_in_personal_details_visible)

            # set the value of variable 'assertion_operand_4f3122338ef8434b8ae68645d832ef4e_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_4f3122338ef8434b8ae68645d832ef4e_0' to true")
            assertion_operand_4f3122338ef8434b8ae68645d832ef4e_0 = "true"
            ui_action(driver = driver, operation_index = str(15))
            assertion_result = ui_action(driver=driver, operation_index=str(16))
            print("assertion_result: ", assertion_result)

            # Query 'Show SIN field in Personal Details' text visibility
            lambda_hooks(driver, "Query 'Show SIN field in Personal Details' text visibility")
            show_sin_field_in_personal_details_visible = vision_query(driver = driver, operation_index = str(17))
            if isinstance(show_sin_field_in_personal_details_visible, dict):
                show_sin_field_in_personal_details_visible = show_sin_field_in_personal_details_visible.get("vision_query")
            user_variables["show_sin_field_in_personal_details_visible"] =  show_sin_field_in_personal_details_visible
            print("show_sin_field_in_personal_details_visible:", show_sin_field_in_personal_details_visible)

            # set the value of variable 'assertion_operand_14863a0281fc464982cf36df52b73c27_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_14863a0281fc464982cf36df52b73c27_0' to true")
            assertion_operand_14863a0281fc464982cf36df52b73c27_0 = "true"
            ui_action(driver = driver, operation_index = str(18))
            assertion_result = ui_action(driver=driver, operation_index=str(19))
            print("assertion_result: ", assertion_result)

            # Query 'Show US Tax Exemptions menu' text visibility
            lambda_hooks(driver, "Query 'Show US Tax Exemptions menu' text visibility")
            show_us_tax_exemptions_menu_visible_d1edeb = vision_query(driver = driver, operation_index = str(20))
            if isinstance(show_us_tax_exemptions_menu_visible_d1edeb, dict):
                show_us_tax_exemptions_menu_visible_d1edeb = show_us_tax_exemptions_menu_visible_d1edeb.get("vision_query")
            user_variables["show_us_tax_exemptions_menu_visible_d1edeb"] =  show_us_tax_exemptions_menu_visible_d1edeb
            print("show_us_tax_exemptions_menu_visible_d1edeb:", show_us_tax_exemptions_menu_visible_d1edeb)

            # set the value of variable 'assertion_operand_f63d5a6614d0410ebe951016e15a9bad_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_f63d5a6614d0410ebe951016e15a9bad_0' to true")
            assertion_operand_f63d5a6614d0410ebe951016e15a9bad_0 = "true"
            ui_action(driver = driver, operation_index = str(21))
            assertion_result = ui_action(driver=driver, operation_index=str(22))
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
