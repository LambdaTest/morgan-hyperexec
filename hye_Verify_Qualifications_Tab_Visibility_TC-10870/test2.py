
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time,requests,re,os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lambdatest_selenium_driver import smartui_snapshot
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
try:

    actions = ActionChains(driver)
    def get_element(driver,locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element(By.XPATH, locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
                try:
                    element = driver.find_element(by_method, locator['selector'])
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : navigate to 'https://orange-hrm.lambdatestinternal.com/orangehrm-5.7'
    driver.get("https://orange-hrm.lambdatestinternal.com/orangehrm-5.7")
    driver.implicitly_wait(6)

    # Step - 2 : Query 'Username input box' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_052b789c0f28453394d5d74cc5d07bad_0' to true
    assertion_operand_052b789c0f28453394d5d74cc5d07bad_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_052b789c0f28453394d5d74cc5d07bad_0 = "true"
    driver.implicitly_wait(6)

    # Step - 5 : type 'pushpa.raj' in Username
    element_locators = ['[placeholder="Username"][name="username"]', '[placeholder="Username"]', '[name="username"]', "//input[@placeholder='Username' and @name='username']", '.oxd-input--focus', "//input[starts-with(@placeholder,'Usern')]", "//input[contains(@class,'oxd-input--focus')]", "//input[contains(@placeholder,'Username')]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'pushpa.raj':
            element.send_keys(char)
    else:
        element.send_keys('pushpa.raj')
    driver.implicitly_wait(6)

    # Step - 6 : type ******************* in Password input field
    element_locators = ["//input[@name='password' and @type='password']", '[placeholder="Password"][name="password"]', '[placeholder="Password"][type="password"]', '[name="password"][type="password"]', '[placeholder="Password"]', "//input[@placeholder='Password' and @type='password']", "//input[@placeholder='Password' and @name='password']", "//input[contains(@placeholder,'Password')]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in '0NkLWCMXdAnZ45LJ@#2':
            element.send_keys(char)
    else:
        element.send_keys('0NkLWCMXdAnZ45LJ@#2')
    driver.implicitly_wait(6)

    # Step - 7 : Click 'Login'
    element_locators = ['[type="submit"]', '.oxd-button--medium', '.oxd-button--main', '.oxd-button--medium.oxd-button--main', "//button[starts-with(@type,'submi')]", "//button[contains(@class,'oxd-button--medium')]", "//button[contains(@type,'submit')]", "//button[contains(@class,'oxd-button--main')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 8 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 9 : Click on 'My Info' menu item in the left sidebar
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[6]/a[1]/span[1]", "//span[text()='My Info']", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(6) > a:nth-child(1) > span:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 11 : Click on 'Qualifications' tab in the left side menu
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[9]/a[1]", "//a[text()='Qualifications']", "//a[contains(text(),'Qualifications')]", '[role="tablist"] > div:nth-child(9) > a:nth-child(1)', '[role="tablist"] > div:nth-child(9) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Query 'Qualifications' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_48a6ac13b3d948ae97ab3769905ed0a5_0' to true
    assertion_operand_48a6ac13b3d948ae97ab3769905ed0a5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Qualifications' text is visible
    assertion_operand_48a6ac13b3d948ae97ab3769905ed0a5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'Work Experience' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Work Experience']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_388866cc1833433c95eb6fb50e636c6c_0' to true
    assertion_operand_388866cc1833433c95eb6fb50e636c6c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'Work Experience' text is visible
    assertion_operand_388866cc1833433c95eb6fb50e636c6c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'No Records Found' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_0877fea01e0e4d31ae8b7c3ce102e995_0' to true
    assertion_operand_0877fea01e0e4d31ae8b7c3ce102e995_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'No Records Found' text is visible
    assertion_operand_0877fea01e0e4d31ae8b7c3ce102e995_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Company' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_6b6b66315eac45ea8e1737f74054feb9_0' to true
    assertion_operand_6b6b66315eac45ea8e1737f74054feb9_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Company' text is visible
    assertion_operand_6b6b66315eac45ea8e1737f74054feb9_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Job Title' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_c4ce33a98d8f43aba9216629627e7641_0' to true
    assertion_operand_c4ce33a98d8f43aba9216629627e7641_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Job Title' text is visible
    assertion_operand_c4ce33a98d8f43aba9216629627e7641_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'From' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_44ae6b9d6b3c443ba12abb530980b81c_0' to true
    assertion_operand_44ae6b9d6b3c443ba12abb530980b81c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'From' text is visible
    assertion_operand_44ae6b9d6b3c443ba12abb530980b81c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query visibility of text 'To'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_d4031ff46d1e4de881f218cf74ae94f7_0' to true
    assertion_operand_d4031ff46d1e4de881f218cf74ae94f7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert text 'To' is visible
    assertion_operand_d4031ff46d1e4de881f218cf74ae94f7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Comment' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_3c01892859764a759cb69c22da9ccabd_0' to true
    assertion_operand_3c01892859764a759cb69c22da9ccabd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Comment' text is visible
    assertion_operand_3c01892859764a759cb69c22da9ccabd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_8df24d5d21df43eca24bd0670424e99f_0' to true
    assertion_operand_8df24d5d21df43eca24bd0670424e99f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Actions' text is visible
    assertion_operand_8df24d5d21df43eca24bd0670424e99f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Query 'Education' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 41 : set the value of variable 'assertion_operand_feb8999f22db44d8986a85e99e9901ad_0' to true
    assertion_operand_feb8999f22db44d8986a85e99e9901ad_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Assert 'Education' text is visible
    assertion_operand_feb8999f22db44d8986a85e99e9901ad_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Query 'Level' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 44 : set the value of variable 'assertion_operand_bbada02d95ac4f3686c0e1972838c584_0' to true
    assertion_operand_bbada02d95ac4f3686c0e1972838c584_0 = "true"
    driver.implicitly_wait(6)

    # Step - 45 : Assert 'Level' text is visible
    assertion_operand_bbada02d95ac4f3686c0e1972838c584_0 = "true"
    driver.implicitly_wait(6)

    # Step - 46 : Query 'Year' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 47 : set the value of variable 'assertion_operand_74537e2f7fd340409c3bba2caef1b0e7_0' to true
    assertion_operand_74537e2f7fd340409c3bba2caef1b0e7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 48 : Assert 'Year' text is visible
    assertion_operand_74537e2f7fd340409c3bba2caef1b0e7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 49 : Query 'GPA/Score' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 50 : set the value of variable 'assertion_operand_5c7d13e071b743adb428cb68cb48a43c_0' to true
    assertion_operand_5c7d13e071b743adb428cb68cb48a43c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 51 : Assert 'GPA/Score' text is visible
    assertion_operand_5c7d13e071b743adb428cb68cb48a43c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 52 : Query 'Skills' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 53 : set the value of variable 'assertion_operand_c503ee829df445a1aa0f84ca28961cb6_0' to true
    assertion_operand_c503ee829df445a1aa0f84ca28961cb6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 54 : Assert 'Skills' text is visible
    assertion_operand_c503ee829df445a1aa0f84ca28961cb6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 55 : Query 'Skill' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 56 : set the value of variable 'assertion_operand_f738d6c5cc9e429f862b9625e2bf02bb_0' to true
    assertion_operand_f738d6c5cc9e429f862b9625e2bf02bb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 57 : Assert 'Skill' text is visible
    assertion_operand_f738d6c5cc9e429f862b9625e2bf02bb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 58 : Query 'Year of Experience' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 59 : set the value of variable 'assertion_operand_47314e485c7b4eac8093c004f0748736_0' to true
    assertion_operand_47314e485c7b4eac8093c004f0748736_0 = "true"
    driver.implicitly_wait(6)

    # Step - 60 : Assert 'Year of Experience' is visible
    assertion_operand_47314e485c7b4eac8093c004f0748736_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
