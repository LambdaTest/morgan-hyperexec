
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
    element_locators = ['[placeholder="Username"][name="username"]', '[placeholder="Username"]', '[name="username"]', "//input[@placeholder='Username' and @name='username']", '.oxd-input--focus', "//input[starts-with(@placeholder,'Usern')]", "//input[contains(@class,'oxd-input--focus')]", "//input[contains(@placeholder,'Username')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_9ea56bc26bed428886d0acfb8280adfc_0' to true
    assertion_operand_9ea56bc26bed428886d0acfb8280adfc_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_9ea56bc26bed428886d0acfb8280adfc_0 = "true"
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

    # Step - 11 : Click on 'Report-to' tab in the left side menu under My Info
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[8]/a[1]", "//a[text()='Report-to']", "//a[contains(text(),'Report-to')]", '[role="tablist"] > div:nth-child(8) > a:nth-child(1)', '[role="tablist"] > div:nth-child(8) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Query visibility of text 'report to'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_94c06a560e83486c84e4a6339cb493d1_0' to true
    assertion_operand_94c06a560e83486c84e4a6339cb493d1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert text 'report to' is visible
    assertion_operand_94c06a560e83486c84e4a6339cb493d1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'Assigned Supervisors' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Assigned Supervisors']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_d470765c45eb4868b9a1f6e0b0a914bf_0' to true
    assertion_operand_d470765c45eb4868b9a1f6e0b0a914bf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'Assigned Supervisors' text is visible
    assertion_operand_d470765c45eb4868b9a1f6e0b0a914bf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'No Records Found' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_c8b3f60f6e3341f2b9551b5df2e90078_0' to true
    assertion_operand_c8b3f60f6e3341f2b9551b5df2e90078_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'No Records Found' text is visible
    assertion_operand_c8b3f60f6e3341f2b9551b5df2e90078_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Name' visibility
    element_locators = ['.--strong', '.oxd-text--h6.--strong', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Pushpa Raj']", "//h6[contains(@class,'--strong')]", "//h6[contains(@class,'oxd-text--h6') and contains(@class,'--strong')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_3af1e136da1b4044a7c36bc2e44837d8_0' to true
    assertion_operand_3af1e136da1b4044a7c36bc2e44837d8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Name' text is visible
    assertion_operand_3af1e136da1b4044a7c36bc2e44837d8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Reporting Method' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_f86c8d44652b457caf4832feff274cc0_0' to true
    assertion_operand_f86c8d44652b457caf4832feff274cc0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Reporting Method' is visible
    assertion_operand_f86c8d44652b457caf4832feff274cc0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Assigned Subordinates' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_3cd69cbcacf94d8da308d82cf4539aac_0' to true
    assertion_operand_3cd69cbcacf94d8da308d82cf4539aac_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Assigned Subordinates' text is visible
    assertion_operand_3cd69cbcacf94d8da308d82cf4539aac_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'File Name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_ef2873c369f54f21b9f52397873e4911_0' to true
    assertion_operand_ef2873c369f54f21b9f52397873e4911_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'File Name' is visible
    assertion_operand_ef2873c369f54f21b9f52397873e4911_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Description' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_f6b1166f81e740c3a636b6b4b9d3a872_0' to true
    assertion_operand_f6b1166f81e740c3a636b6b4b9d3a872_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Description' is visible on screen
    assertion_operand_f6b1166f81e740c3a636b6b4b9d3a872_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Size' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_4726f80b0baa40dcbb6274eb5d64bc9b_0' to true
    assertion_operand_4726f80b0baa40dcbb6274eb5d64bc9b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Size' text is visible
    assertion_operand_4726f80b0baa40dcbb6274eb5d64bc9b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Query 'Type' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 41 : set the value of variable 'assertion_operand_5df4276fd62d42ae87341cf5ad47d714_0' to true
    assertion_operand_5df4276fd62d42ae87341cf5ad47d714_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Assert 'Type' text is visible
    assertion_operand_5df4276fd62d42ae87341cf5ad47d714_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Query 'Date Added' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 44 : set the value of variable 'assertion_operand_f8fc3215c2d04e92899d4731e2beaa18_0' to true
    assertion_operand_f8fc3215c2d04e92899d4731e2beaa18_0 = "true"
    driver.implicitly_wait(6)

    # Step - 45 : Assert 'Date Added' text is visible
    assertion_operand_f8fc3215c2d04e92899d4731e2beaa18_0 = "true"
    driver.implicitly_wait(6)

    # Step - 46 : Query visibility of text 'Added By'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 47 : set the value of variable 'assertion_operand_1adf6784d2c94df29c22ec6ee21d94ec_0' to true
    assertion_operand_1adf6784d2c94df29c22ec6ee21d94ec_0 = "true"
    driver.implicitly_wait(6)

    # Step - 48 : Assert text 'Added By' is visible
    assertion_operand_1adf6784d2c94df29c22ec6ee21d94ec_0 = "true"
    driver.implicitly_wait(6)

    # Step - 49 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 50 : set the value of variable 'assertion_operand_2c28be2388d64879a31250a89cccb8ab_0' to true
    assertion_operand_2c28be2388d64879a31250a89cccb8ab_0 = "true"
    driver.implicitly_wait(6)

    # Step - 51 : Assert 'Actions' text is visible
    assertion_operand_2c28be2388d64879a31250a89cccb8ab_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
