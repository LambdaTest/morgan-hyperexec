
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

    # Step - 1 : navigate to 'https://orange-hrm.lambdatestinternal.com/orangehrm-5.7' website
    driver.get("https://orange-hrm.lambdatestinternal.com/orangehrm-5.7")
    driver.implicitly_wait(6)

    # Step - 2 : Query 'Username input box' visibility
    element_locators = ['[placeholder="Username"][name="username"]', '[placeholder="Username"]', '[name="username"]', "//input[@placeholder='Username' and @name='username']", '.oxd-input--focus', "//input[starts-with(@placeholder,'Usern')]", "//input[contains(@class,'oxd-input--focus')]", "//input[contains(@placeholder,'Username')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_7fd1c58ffef64aaf831c6e7821474a0f_0' to true
    assertion_operand_7fd1c58ffef64aaf831c6e7821474a0f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on viewport
    assertion_operand_7fd1c58ffef64aaf831c6e7821474a0f_0 = "true"
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

    # Step - 9 : Click on 'My Info' menu item in left side menu
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[6]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[6]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(6) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(6) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 11 : Query 'Personal Deatils' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]", "//a[text()='Personal Details']", "//a[contains(text(),'Personal Details')]", '[role="tablist"] > div:nth-child(1) > a:nth-child(1)', '[role="tablist"] > div:nth-child(1) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 12 : set the value of variable 'assertion_operand_7189c7bd71d34c71b61cf11b06864b04_0' to true
    assertion_operand_7189c7bd71d34c71b61cf11b06864b04_0 = "true"
    driver.implicitly_wait(6)

    # Step - 13 : Assert 'Personal Deatils' text is visible
    assertion_operand_7189c7bd71d34c71b61cf11b06864b04_0 = "true"
    driver.implicitly_wait(6)

    # Step - 14 : Query 'Employee Full name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 15 : set the value of variable 'assertion_operand_31e23952fd6e4acd9f9f9ebc7e39f15c_0' to true
    assertion_operand_31e23952fd6e4acd9f9f9ebc7e39f15c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Assert 'Employee Full name' is visible
    assertion_operand_31e23952fd6e4acd9f9f9ebc7e39f15c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 17 : Query 'Employee Id' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_e91b4bdda7804bec9f6193e35e796cb1_0' to true
    assertion_operand_e91b4bdda7804bec9f6193e35e796cb1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'Employee Id' is visible
    assertion_operand_e91b4bdda7804bec9f6193e35e796cb1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Query 'Other Id' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 21 : set the value of variable 'assertion_operand_966b0f4c714b4a7eb03a65462ac8f674_0' to true
    assertion_operand_966b0f4c714b4a7eb03a65462ac8f674_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Assert 'Other_Id_visible' equals 'true'
    assertion_operand_966b0f4c714b4a7eb03a65462ac8f674_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Query visibility of text 'Driver's License Number'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 24 : set the value of variable 'assertion_operand_a7357ee570894f90acf7a4f5b68a3fa1_0' to true
    assertion_operand_a7357ee570894f90acf7a4f5b68a3fa1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Assert text 'Driver's License Number' is visible
    assertion_operand_a7357ee570894f90acf7a4f5b68a3fa1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Query 'License Expiry Date' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 27 : set the value of variable 'assertion_operand_1319fe9744104a54a2aca3ea4e8c7dc3_0' to true
    assertion_operand_1319fe9744104a54a2aca3ea4e8c7dc3_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Assert 'License Expiry Date' text is visible
    assertion_operand_1319fe9744104a54a2aca3ea4e8c7dc3_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Query 'Nationality' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 30 : set the value of variable 'assertion_operand_49d8f23feff344c2b503256cda86b0c8_0' to true
    assertion_operand_49d8f23feff344c2b503256cda86b0c8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Assert 'Nationality' text is visible
    assertion_operand_49d8f23feff344c2b503256cda86b0c8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Query 'Marital Status' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 33 : set the value of variable 'assertion_operand_fd981ba7b9a04ae8ba29bd406ee35025_0' to true
    assertion_operand_fd981ba7b9a04ae8ba29bd406ee35025_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Assert 'Marital Status' text is visible
    assertion_operand_fd981ba7b9a04ae8ba29bd406ee35025_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Query 'Date of Birth' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 36 : set the value of variable 'assertion_operand_333eb8db96fc43dc8e791cedbacde1d8_0' to true
    assertion_operand_333eb8db96fc43dc8e791cedbacde1d8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Assert 'Date of Birth' is visible
    assertion_operand_333eb8db96fc43dc8e791cedbacde1d8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 38 : Query 'Gender' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 39 : set the value of variable 'assertion_operand_7d88a181655a43c785c18e16f04c079c_0' to true
    assertion_operand_7d88a181655a43c785c18e16f04c079c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Assert 'Gender' text is visible
    assertion_operand_7d88a181655a43c785c18e16f04c079c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 41 : Query 'Save' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 42 : set the value of variable 'assertion_operand_ad0c5d00a28044f09b536e640204e3f3_0' to true
    assertion_operand_ad0c5d00a28044f09b536e640204e3f3_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Assert 'Save' text is visible
    assertion_operand_ad0c5d00a28044f09b536e640204e3f3_0 = "true"
    driver.implicitly_wait(6)

    # Step - 44 : Get the current URL
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 45 : set the value of variable 'assertion_operand_836298e06d5a4d5bac979dad6bb7fb2b_0' to empNumber/1
    assertion_operand_836298e06d5a4d5bac979dad6bb7fb2b_0 = "empNumber/1"
    driver.implicitly_wait(6)

    # Step - 46 : Assert current URL contains 'empNumber/1'
    assertion_operand_836298e06d5a4d5bac979dad6bb7fb2b_0 = "empNumber/1"

    driver.quit()
except Exception as e:
    driver.quit()
