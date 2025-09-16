
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
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_1c7b5d49bbaa4fcf9a10964493cf9cc7_0' to true
    assertion_operand_1c7b5d49bbaa4fcf9a10964493cf9cc7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_1c7b5d49bbaa4fcf9a10964493cf9cc7_0 = "true"
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

    # Step - 11 : Click on Immigration tab in left side menu
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/a[1]", "//a[text()='Immigration']", "//a[contains(text(),'Immigration')]", '[role="tablist"] > div:nth-child(5) > a:nth-child(1)', '[role="tablist"] > div:nth-child(5) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Click on Add button in Assigned Immigration Records section
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : Query 'Passport radio button' selection state
    element_locators = ['.--gender-grouped-field > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)', "//div[contains(@class,'--gender-grouped-field')]/div[1]/div[2]/div[1]/label[1]/input[1]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 15 : set the value of variable 'assertion_operand_9bac195a6c0f47df9f4c54f86f0761a0_0' to true
    assertion_operand_9bac195a6c0f47df9f4c54f86f0761a0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Assert 'Passport radio button' is selected
    assertion_operand_9bac195a6c0f47df9f4c54f86f0761a0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 17 : Query 'Number' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Number']", "//label[contains(text(),'Number')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_e3974eebe75547c78cee269b95f61518_0' to true
    assertion_operand_e3974eebe75547c78cee269b95f61518_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'Number' text is visible
    assertion_operand_e3974eebe75547c78cee269b95f61518_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Query 'Issued Date' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 21 : set the value of variable 'assertion_operand_b8f59bca568544dcb640c494c7afcb9b_0' to true
    assertion_operand_b8f59bca568544dcb640c494c7afcb9b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Assert 'Issued Date' text is visible
    assertion_operand_b8f59bca568544dcb640c494c7afcb9b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Query 'Expiry Date' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Expiry Date']", "//label[contains(text(),'Expiry Date')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 24 : set the value of variable 'assertion_operand_d7a70e2ee21246fea6b2e4bf7e0e739e_0' to true
    assertion_operand_d7a70e2ee21246fea6b2e4bf7e0e739e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Assert 'Expiry Date' text is visible
    assertion_operand_d7a70e2ee21246fea6b2e4bf7e0e739e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Query 'Eligible Status' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 27 : set the value of variable 'assertion_operand_a811e6428c2144a59bc15d1420fecccf_0' to true
    assertion_operand_a811e6428c2144a59bc15d1420fecccf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Assert 'Eligible Status' is visible
    assertion_operand_a811e6428c2144a59bc15d1420fecccf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Query 'Issued By' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[5]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Issued By']", "//label[contains(text(),'Issued By')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 30 : set the value of variable 'assertion_operand_9f41bfa2971e4bd9a3595db191fcac15_0' to true
    assertion_operand_9f41bfa2971e4bd9a3595db191fcac15_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Assert 'Issued_By_visible' equals 'true'
    assertion_operand_9f41bfa2971e4bd9a3595db191fcac15_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Query 'Eligible Review Date' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[6]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Eligible Review Date']", "//label[contains(text(),'Eligible Review Date')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 33 : set the value of variable 'assertion_operand_7e935de22f01404c83ccfac5f6e568f6_0' to true
    assertion_operand_7e935de22f01404c83ccfac5f6e568f6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Assert 'Eligible Review Date' is visible
    assertion_operand_7e935de22f01404c83ccfac5f6e568f6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Query 'Comments' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[7]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Comments']", "//label[contains(text(),'Comments')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 36 : set the value of variable 'assertion_operand_97a5ffea80e1449eac6d1375a9db0c91_0' to true
    assertion_operand_97a5ffea80e1449eac6d1375a9db0c91_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Assert 'Comments' text is visible
    assertion_operand_97a5ffea80e1449eac6d1375a9db0c91_0 = "true"
    driver.implicitly_wait(6)

    # Step - 38 : Query 'Cancel' text visibility
    element_locators = ['.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ .oxd-button--secondary)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/button[1]", 'button:has(+ .oxd-button--medium.oxd-button--secondary)', "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 39 : set the value of variable 'assertion_operand_d078f6844cc54792b84ea421c16f97e1_0' to true
    assertion_operand_d078f6844cc54792b84ea421c16f97e1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Assert 'Cancel' text is visible
    assertion_operand_d078f6844cc54792b84ea421c16f97e1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 41 : Query 'Save' text visibility
    element_locators = ['[type="submit"]', '.oxd-button--secondary', '.oxd-button--medium.oxd-button--secondary', '.oxd-button--ghost + button', "//button[starts-with(@type,'submi')]", "//button[contains(@class,'oxd-button--secondary')]", "//button[contains(@type,'submit')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--secondary')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 42 : set the value of variable 'assertion_operand_37eb1fbc4b3c4ea886f2eecb28c59d6b_0' to true
    assertion_operand_37eb1fbc4b3c4ea886f2eecb28c59d6b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Assert 'Save' text is visible
    assertion_operand_37eb1fbc4b3c4ea886f2eecb28c59d6b_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
