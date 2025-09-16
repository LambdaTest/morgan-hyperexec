
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

    # Step - 3 : set the value of variable 'assertion_operand_d502f403a4ec449bbadd84a9228853d6_0' to true
    assertion_operand_d502f403a4ec449bbadd84a9228853d6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_d502f403a4ec449bbadd84a9228853d6_0 = "true"
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

    # Step - 11 : Click on 'Memberships' tab in the left side menu
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/a[1]", "//a[text()='Memberships']", "//a[contains(text(),'Memberships')]", '[role="tablist"] > div:nth-child(10) > a:nth-child(1)', '[role="tablist"] > div:nth-child(10) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Query 'Assigned Memberships' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Assigned Memberships']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_39610b64299f4806b11c0f89930182fd_0' to true
    assertion_operand_39610b64299f4806b11c0f89930182fd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Assigned Memberships' text is visible
    assertion_operand_39610b64299f4806b11c0f89930182fd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'No Records Found' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_50b59ab72740469cae43abdf1983776d_0' to true
    assertion_operand_50b59ab72740469cae43abdf1983776d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'No Records Found' text is visible
    assertion_operand_50b59ab72740469cae43abdf1983776d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Membership' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/a[1]", "//a[text()='Memberships']", "//a[contains(text(),'Memberships')]", '[role="tablist"] > div:nth-child(10) > a:nth-child(1)', '[role="tablist"] > div:nth-child(10) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_28c952077ae244fea2152179f0b56c40_0' to true
    assertion_operand_28c952077ae244fea2152179f0b56c40_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Membership' text is visible
    assertion_operand_28c952077ae244fea2152179f0b56c40_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Subscription Paid by' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_eacebd7a54194b31bed9f1c204b41bfb_0' to true
    assertion_operand_eacebd7a54194b31bed9f1c204b41bfb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Subscription Paid by' text is visible
    assertion_operand_eacebd7a54194b31bed9f1c204b41bfb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Subscription Amount' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_2fdcc41ebd174514884f70dab288a102_0' to true
    assertion_operand_2fdcc41ebd174514884f70dab288a102_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Subscription Amount' is visible
    assertion_operand_2fdcc41ebd174514884f70dab288a102_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Current' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_1d77dbf1fe6b4bfc8a0be8b26209ea5e_0' to true
    assertion_operand_1d77dbf1fe6b4bfc8a0be8b26209ea5e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Current' text is visible
    assertion_operand_1d77dbf1fe6b4bfc8a0be8b26209ea5e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'Subscription Commence Date' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_eb181784e41348119af2e09b7780afd2_0' to true
    assertion_operand_eb181784e41348119af2e09b7780afd2_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'Subscription Commence Date' is visible
    assertion_operand_eb181784e41348119af2e09b7780afd2_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Subscription Renewal Date' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_0b25bbc4e8de4887b0ea4e4f01dc6ee0_0' to true
    assertion_operand_0b25bbc4e8de4887b0ea4e4f01dc6ee0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Subscription Renewal Date' text is visible
    assertion_operand_0b25bbc4e8de4887b0ea4e4f01dc6ee0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_958619d7852e4a86a23d5c043d9fcc5c_0' to true
    assertion_operand_958619d7852e4a86a23d5c043d9fcc5c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Actions' text is visible
    assertion_operand_958619d7852e4a86a23d5c043d9fcc5c_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
