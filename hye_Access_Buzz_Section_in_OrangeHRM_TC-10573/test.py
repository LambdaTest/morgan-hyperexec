
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

            # Click on 'Buzz' menu item in left side menu
            lambda_hooks(driver, "Click on 'Buzz' menu item in left side menu")
            ui_action(driver = driver, operation_index = str(0))

            # Query 'Buzz Newsfeed' visibility
            lambda_hooks(driver, "Query 'Buzz Newsfeed' visibility")
            Buzz_Newsfeed_visible = vision_query(driver = driver, operation_index = str(1))
            if isinstance(Buzz_Newsfeed_visible, dict):
                Buzz_Newsfeed_visible = Buzz_Newsfeed_visible.get("vision_query")
            user_variables["Buzz_Newsfeed_visible"] =  Buzz_Newsfeed_visible
            print("Buzz_Newsfeed_visible:", Buzz_Newsfeed_visible)

            # set the value of variable 'assertion_operand_cdead39a7cf442bf90d19bc1818eb9b1_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_cdead39a7cf442bf90d19bc1818eb9b1_0' to true")
            assertion_operand_cdead39a7cf442bf90d19bc1818eb9b1_0 = "true"
            ui_action(driver = driver, operation_index = str(2))
            assertion_result = ui_action(driver=driver, operation_index=str(3))
            print("assertion_result: ", assertion_result)

            # Query 'Share Photos' visibility
            lambda_hooks(driver, "Query 'Share Photos' visibility")
            Share_Photos_visible = vision_query(driver = driver, operation_index = str(4))
            if isinstance(Share_Photos_visible, dict):
                Share_Photos_visible = Share_Photos_visible.get("vision_query")
            user_variables["Share_Photos_visible"] =  Share_Photos_visible
            print("Share_Photos_visible:", Share_Photos_visible)

            # set the value of variable 'assertion_operand_cbe12da34e2e464eb60fbb5921e15c62_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_cbe12da34e2e464eb60fbb5921e15c62_0' to true")
            assertion_operand_cbe12da34e2e464eb60fbb5921e15c62_0 = "true"
            ui_action(driver = driver, operation_index = str(5))
            assertion_result = ui_action(driver=driver, operation_index=str(6))
            print("assertion_result: ", assertion_result)

            # Query 'Share Video' visibility
            lambda_hooks(driver, "Query 'Share Video' visibility")
            Share_Video_visible = vision_query(driver = driver, operation_index = str(7))
            if isinstance(Share_Video_visible, dict):
                Share_Video_visible = Share_Video_visible.get("vision_query")
            user_variables["Share_Video_visible"] =  Share_Video_visible
            print("Share_Video_visible:", Share_Video_visible)

            # set the value of variable 'assertion_operand_ab1fbf8c762b44119cf0c5a85d5f7cd5_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_ab1fbf8c762b44119cf0c5a85d5f7cd5_0' to true")
            assertion_operand_ab1fbf8c762b44119cf0c5a85d5f7cd5_0 = "true"
            ui_action(driver = driver, operation_index = str(8))
            assertion_result = ui_action(driver=driver, operation_index=str(9))
            print("assertion_result: ", assertion_result)

            # Query 'Most Recent Posts' visibility
            lambda_hooks(driver, "Query 'Most Recent Posts' visibility")
            Most_Recent_Posts_visible = vision_query(driver = driver, operation_index = str(10))
            if isinstance(Most_Recent_Posts_visible, dict):
                Most_Recent_Posts_visible = Most_Recent_Posts_visible.get("vision_query")
            user_variables["Most_Recent_Posts_visible"] =  Most_Recent_Posts_visible
            print("Most_Recent_Posts_visible:", Most_Recent_Posts_visible)

            # set the value of variable 'assertion_operand_92c743b19bc6412e922889fca11b161b_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_92c743b19bc6412e922889fca11b161b_0' to true")
            assertion_operand_92c743b19bc6412e922889fca11b161b_0 = "true"
            ui_action(driver = driver, operation_index = str(11))
            assertion_result = ui_action(driver=driver, operation_index=str(12))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Most Liked Posts'
            lambda_hooks(driver, "Query visibility of text 'Most Liked Posts'")
            most_liked_posts_visible = vision_query(driver = driver, operation_index = str(13))
            if isinstance(most_liked_posts_visible, dict):
                most_liked_posts_visible = most_liked_posts_visible.get("vision_query")
            user_variables["most_liked_posts_visible"] =  most_liked_posts_visible
            print("most_liked_posts_visible:", most_liked_posts_visible)

            # set the value of variable 'assertion_operand_a4501028b61043cab4228222a26bfc47_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_a4501028b61043cab4228222a26bfc47_0' to true")
            assertion_operand_a4501028b61043cab4228222a26bfc47_0 = "true"
            ui_action(driver = driver, operation_index = str(14))
            assertion_result = ui_action(driver=driver, operation_index=str(15))
            print("assertion_result: ", assertion_result)

            # Query visibility of text 'Most commented posts'
            lambda_hooks(driver, "Query visibility of text 'Most commented posts'")
            most_commented_posts_visible = vision_query(driver = driver, operation_index = str(16))
            if isinstance(most_commented_posts_visible, dict):
                most_commented_posts_visible = most_commented_posts_visible.get("vision_query")
            user_variables["most_commented_posts_visible"] =  most_commented_posts_visible
            print("most_commented_posts_visible:", most_commented_posts_visible)

            # set the value of variable 'assertion_operand_59b22f0014a84483bd898ecca3f97fa6_0' to true
            lambda_hooks(driver, "set the value of variable 'assertion_operand_59b22f0014a84483bd898ecca3f97fa6_0' to true")
            assertion_operand_59b22f0014a84483bd898ecca3f97fa6_0 = "true"
            ui_action(driver = driver, operation_index = str(17))
            assertion_result = ui_action(driver=driver, operation_index=str(18))
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
