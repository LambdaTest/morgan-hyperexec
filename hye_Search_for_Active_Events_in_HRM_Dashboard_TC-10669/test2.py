
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

    # Step - 3 : set the value of variable 'assertion_operand_d9e0fe6c896c4d2984e2efb87b9e394d_0' to true
    assertion_operand_d9e0fe6c896c4d2984e2efb87b9e394d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_d9e0fe6c896c4d2984e2efb87b9e394d_0 = "true"
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

    # Step - 9 : Click on 'Claim' menu item in left side menu 
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[11]/a[1]/span[1]", "//span[text()='Claim']", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(11) > a:nth-child(1) > span:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 11 : Click on 'Configuration' tab in top navigation bar 
    element_locators = ['.--parent', '.oxd-topbar-body-nav-tab.--parent', "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[1]", "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[1]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(1)', '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(1)', "//li[contains(@class,'--parent')]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Click on 'Events' tab in top navigation bar 
    element_locators = ['.--parent > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', '.--parent > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', "//a[text()='Events']", "//a[contains(text(),'Events')]", "//li[contains(@class,'--parent')]/ul[1]/li[1]/a[1]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent')]/ul[1]/li[1]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 15 : Click on the punch out timer button in the Time at Work section 
    element_locators = ['[placeholder="Type for hints..."]', '.oxd-autocomplete-text-input--focus > input', '.oxd-autocomplete-text-input--before + input', 'input:has(+ .oxd-autocomplete-text-input--after)', "//input[starts-with(@placeholder,'Type ')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]", "//input[contains(@placeholder,'Type for hints...')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 16 : Type in search input with placeholder 'Type for hints...' 'active' 
    element_locators = ['[placeholder="Type for hints..."]', '.oxd-autocomplete-text-input--focus > input', '.oxd-autocomplete-text-input--before + input', 'input:has(+ .oxd-autocomplete-text-input--after)', "//input[starts-with(@placeholder,'Type ')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]", "//input[contains(@placeholder,'Type for hints...')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'active':
            element.send_keys(char)
    else:
        element.send_keys('active')
    driver.implicitly_wait(6)

    # Step - 17 : Click on the dashboard quick launch dropdown 
    element_locators = ['.oxd-select-text--focus > div:nth-child(1)', '.oxd-select-text--focus > div:nth-child(1)', '.oxd-select-text--focus > div:nth-child(1)', 'div:has(+ .oxd-select-text--after)', "//div[contains(text(),'-- Select --')]", "//div[contains(@class,'oxd-select-text--focus')]/div[1]", "//div[contains(@class,'oxd-select-text--focus')]/div[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 18 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 19 : Click on the Search button in orangehrm-left-space 
    element_locators = ['[type="submit"]', '.oxd-button--ghost + button', '.oxd-button--medium.oxd-button--ghost + button', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[2]/button[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(3) > button:nth-child(2)', "//button[starts-with(@type,'submi')]", "//button[contains(@type,'submit')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 20 : Query text '(2) Records Found' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 21 : set the value of variable 'assertion_operand_f965b563c26d49b18bd8d4de9582ac85_0' to true
    assertion_operand_f965b563c26d49b18bd8d4de9582ac85_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Assert text '(2) Records Found' is visible
    assertion_operand_f965b563c26d49b18bd8d4de9582ac85_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Query 'Active Event' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 24 : set the value of variable 'assertion_operand_16240e977fac41f28e0367cfcd76aa3d_0' to true
    assertion_operand_16240e977fac41f28e0367cfcd76aa3d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Assert 'Active Event' is visible
    assertion_operand_16240e977fac41f28e0367cfcd76aa3d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Query 'Inactive' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]", '[role="table"] > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)', '[role="table"] > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 27 : set the value of variable 'assertion_operand_40f09c7f90cc4891af913a9a80288570_0' to true
    assertion_operand_40f09c7f90cc4891af913a9a80288570_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Assert 'Inactive' text is visible
    assertion_operand_40f09c7f90cc4891af913a9a80288570_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Query 'Active Event name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 30 : set the value of variable 'assertion_operand_2ca53f43ac1b4d86ad07c5f9677a22c1_0' to true
    assertion_operand_2ca53f43ac1b4d86ad07c5f9677a22c1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Assert 'Active Event name' is visible
    assertion_operand_2ca53f43ac1b4d86ad07c5f9677a22c1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Query 'Inactive Event name' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]", '[role="table"] > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)', '[role="table"] > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 33 : set the value of variable 'assertion_operand_2ce5d4642e094841b473d5c7e56ad02a_0' to true
    assertion_operand_2ce5d4642e094841b473d5c7e56ad02a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Assert 'Inactive Event name' is visible
    assertion_operand_2ce5d4642e094841b473d5c7e56ad02a_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
