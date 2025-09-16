
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
    driver.implicitly_wait(6)

    # Step - 1 : navigate to 'https://orange-hrm.lambdatestinternal.com/orangehrm-5.7' website
    driver.get("https://orange-hrm.lambdatestinternal.com/orangehrm-5.7")
    driver.implicitly_wait(6)

    # Step - 2 : Query 'Username input box' visibility
    element_locators = ['[placeholder="Username"][name="username"]', '[placeholder="Username"]', '[name="username"]', "//input[@placeholder='Username' and @name='username']", '.oxd-input--focus', "//input[starts-with(@placeholder,'Usern')]", "//input[contains(@class,'oxd-input--focus')]", "//input[contains(@placeholder,'Username')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_80a4b7c6cc684f32bc46e3ba0cce7e11_0' to true
    assertion_operand_80a4b7c6cc684f32bc46e3ba0cce7e11_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_80a4b7c6cc684f32bc46e3ba0cce7e11_0 = "true"
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

    # Step - 9 : Click on 'My Info' menu item in left sidebar
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

    # Step - 11 : Click on 'Job' tab in the left side menu under 'My Info'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/a[1]", "//a[text()='Job']", "//a[contains(text(),'Job')]", '[role="tablist"] > div:nth-child(6) > a:nth-child(1)', '[role="tablist"] > div:nth-child(6) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Click on Include Employment Contract Details toggle switch
    element_locators = ['.--label-right', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/label[1]/span[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(3) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)', '[type="checkbox"] + span', "//span[contains(@class,'--label-right')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : Query 'Contact Start Date' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]", "//a[text()='Contact Details']", "//a[contains(text(),'Contact Details')]", '[role="tablist"] > div:nth-child(2) > a:nth-child(1)', '[role="tablist"] > div:nth-child(2) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 15 : set the value of variable 'assertion_operand_e6da098998fb4f48827efd7465758a1f_0' to true
    assertion_operand_e6da098998fb4f48827efd7465758a1f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Assert 'Contact Start Date' is visible
    assertion_operand_e6da098998fb4f48827efd7465758a1f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 17 : Query 'Contact End Date' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Contract End Date']", "//label[contains(text(),'Contract End Date')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_5210db313b5747058487a6c1fe362aec_0' to true
    assertion_operand_5210db313b5747058487a6c1fe362aec_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'Contact End Date' is visible
    assertion_operand_5210db313b5747058487a6c1fe362aec_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Query 'Contact Details' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]", "//a[text()='Contact Details']", "//a[contains(text(),'Contact Details')]", '[role="tablist"] > div:nth-child(2) > a:nth-child(1)', '[role="tablist"] > div:nth-child(2) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 21 : set the value of variable 'assertion_operand_8226014cb4a0410ca05356eb73a64f3c_0' to true
    assertion_operand_8226014cb4a0410ca05356eb73a64f3c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Assert 'Contact Details' is visible
    assertion_operand_8226014cb4a0410ca05356eb73a64f3c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Query 'Include Employment Contact Details' toggle visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 24 : set the value of variable 'assertion_operand_8bb34e533d2e4a9493b2df75f67cfef5_0' to true
    assertion_operand_8bb34e533d2e4a9493b2df75f67cfef5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Assert 'Include Employment Contact Details' toggle is enabled
    assertion_operand_8bb34e533d2e4a9493b2df75f67cfef5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Click on Include Employment Contract Details toggle switch
    element_locators = ['.--label-right', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/label[1]/span[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(3) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)', '[type="checkbox"] + span', "//span[contains(@class,'--label-right')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 27 : Query 'Include Employment Contact Details' toggle visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 28 : set the value of variable 'assertion_operand_1a115642336346a791ea1e1836e617d1_0' to true
    assertion_operand_1a115642336346a791ea1e1836e617d1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Assert 'Include Employment Contact Details' toggle is switched off
    assertion_operand_1a115642336346a791ea1e1836e617d1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Query 'Include Employment Contact Details' toggle selected state
    element_locators = ['[type="checkbox"]', 'input:has(+ .oxd-switch-input--focus)', 'input:has(+ .--label-right)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/label[1]/input[1]", 'input:has(+ .oxd-switch-input--focus.--label-right)', "//input[starts-with(@type,'check')]", "//input[contains(@type,'checkbox')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 31 : set the value of variable 'assertion_operand_1a115642336346a791ea1e1836e617d1_1' to false
    assertion_operand_1a115642336346a791ea1e1836e617d1_1 = "false"
    driver.implicitly_wait(6)

    # Step - 32 : Assert 'Include Employment Contact Details' toggle is switched off
    assertion_operand_1a115642336346a791ea1e1836e617d1_1 = "false"

    driver.quit()
except Exception as e:
    driver.quit()
