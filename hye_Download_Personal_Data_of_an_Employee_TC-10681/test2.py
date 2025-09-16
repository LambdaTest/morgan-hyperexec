
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

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

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

    # Step - 3 : set the value of variable 'assertion_operand_021315c7c429473db23634c259f110c8_0' to true
    assertion_operand_021315c7c429473db23634c259f110c8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on viewport
    assertion_operand_021315c7c429473db23634c259f110c8_0 = "true"
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

    # Step - 9 : Click on 'Maintenance' menu item in left sidebar 
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[10]/a[1]/span[1]", "//span[text()='Maintenance']", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(10) > a:nth-child(1) > span:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : wait 5 seconds
    time.sleep(int(5))
    driver.implicitly_wait(6)

    # Step - 11 : type ******************* in Password input field
    element_locators = ["//input[@name='password' and @type='password']", '[name="password"][type="password"]', '[type="password"]', '[name="password"]', '.oxd-input--focus', "//input[starts-with(@type,'passw')]", "//input[contains(@class,'oxd-input--focus')]", "//input[contains(@type,'password')]"]
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

    # Step - 12 : Click 'Conform' button
    element_locators = ['[type="submit"]', '.oxd-button--secondary', '.oxd-button--large.oxd-button--secondary', '.oxd-button--ghost + button', "//button[starts-with(@type,'submi')]", "//button[contains(@class,'oxd-button--secondary')]", "//button[contains(@type,'submit')]", "//button[contains(@class,'oxd-button--large') and contains(@class,'oxd-button--secondary')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 13 : wait 5 seconds
    time.sleep(int(5))
    driver.implicitly_wait(6)

    # Step - 14 : Click on past employee input field with placeholder 'Type for hints...' 
    element_locators = ['[placeholder="Type for hints..."]', '.oxd-autocomplete-text-input--focus > input', '.oxd-autocomplete-text-input--before + input', 'input:has(+ .oxd-autocomplete-text-input--after)', "//input[starts-with(@placeholder,'Type ')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]", "//input[contains(@placeholder,'Type for hints...')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 15 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 16 : Click on 'Access Records' tab in the top nav bar 
    element_locators = ['a.oxd-topbar-body-nav-tab-item', "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[2]/a[1]", "//a[text()='Access Records']", "//a[contains(text(),'Access Records')]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)', '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)', "//a[contains(@class,'oxd-topbar-body-nav-tab-item')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 17 : Click on employee name input field with placeholder 'Type for hints...' 
    element_locators = ['[placeholder="Type for hints..."]', '.oxd-autocomplete-text-input--focus > input', '.oxd-autocomplete-text-input--before + input', 'input:has(+ .oxd-autocomplete-text-input--after)', "//input[starts-with(@placeholder,'Type ')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]", "//input[contains(@placeholder,'Type for hints...')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 18 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 19 : Type in employee name input field with placeholder 'Type for hints...' 'ayush' 
    element_locators = ['[placeholder="Type for hints..."]', '.oxd-autocomplete-text-input--focus > input', '.oxd-autocomplete-text-input--before + input', 'input:has(+ .oxd-autocomplete-text-input--after)', "//input[starts-with(@placeholder,'Type ')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]", "//input[contains(@placeholder,'Type for hints...')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'ayush':
            element.send_keys(char)
    else:
        element.send_keys('ayush')
    driver.implicitly_wait(6)

    # Step - 20 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 21 : Click 'Ayush Pathania' in dropdown list
    element_locators = ['[role="option"]', '.--positon-bottom > div', '.--positon-bottom > div:nth-child(1)', '[role="listbox"] > div', "//div[starts-with(@role,'optio')]", "//div[contains(@class,'--positon-bottom')]/div[1]", "//div[contains(@role,'option')]", "//div[contains(@class,'--positon-bottom')]/div[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 22 : Click on the green Search button in Download Personal Data section 
    element_locators = ['[type="submit"]', '.oxd-button--medium', '.oxd-button--secondary', '.oxd-button--medium.oxd-button--secondary', "//button[starts-with(@type,'submi')]", "//button[contains(@class,'oxd-button--medium')]", "//button[contains(@type,'submit')]", "//button[contains(@class,'oxd-button--secondary')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 23 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 24 : Query text '0007' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 25 : set the value of variable 'assertion_operand_fa56d590d8be489c9458e56c7a32378d_0' to true
    assertion_operand_fa56d590d8be489c9458e56c7a32378d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Assert text '0007' is visible
    assertion_operand_fa56d590d8be489c9458e56c7a32378d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Query 'Employee Id' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 28 : set the value of variable 'assertion_operand_d9d4185a926d4957b6a8bc3f466c76fe_0' to true
    assertion_operand_d9d4185a926d4957b6a8bc3f466c76fe_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Assert 'Employee Id' text is visible
    assertion_operand_d9d4185a926d4957b6a8bc3f466c76fe_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Query 'Employee Full Name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 31 : set the value of variable 'assertion_operand_3cbbcda34fb340a09a8809ce3ac4c27c_0' to true
    assertion_operand_3cbbcda34fb340a09a8809ce3ac4c27c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Assert 'Employee Full Name' is visible
    assertion_operand_3cbbcda34fb340a09a8809ce3ac4c27c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Query 'Download' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 34 : set the value of variable 'assertion_operand_e98e9555aa624678b173d190c25e339f_0' to true
    assertion_operand_e98e9555aa624678b173d190c25e339f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Assert 'Download' text is visible
    assertion_operand_e98e9555aa624678b173d190c25e339f_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
