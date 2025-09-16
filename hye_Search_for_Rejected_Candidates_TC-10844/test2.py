
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

    # Step - 3 : set the value of variable 'assertion_operand_d2172d19a6004076a20920b0a9dfedf4_0' to true
    assertion_operand_d2172d19a6004076a20920b0a9dfedf4_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_d2172d19a6004076a20920b0a9dfedf4_0 = "true"
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

    # Step - 9 : Click 'Recruitment'
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[5]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[5]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 11 : Click 'Search'
    element_locators = ['[type="submit"]', '.oxd-button--ghost + button', '.oxd-button--medium.oxd-button--ghost + button', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[4]/button[2]", '[type="reset"] + button', "//button[starts-with(@type,'submi')]", "//button[contains(@type,'submit')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : Click 'status' dropdown
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 13 : Query 'Rejected' text visibility
    element_locators = ['.--positon-bottom > div:nth-child(4)', '.--positon-bottom > div:nth-child(4)', '.--positon-bottom > div:nth-child(4)', '[role="listbox"] > div:nth-child(4)', "//div[contains(@class,'--positon-bottom')]/div[4]", "//div[contains(@class,'--positon-bottom')]/div[4]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_887312804b804e56b831c38b40eebbaf_0' to true
    assertion_operand_887312804b804e56b831c38b40eebbaf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Rejected' text is displayed on viewport
    assertion_operand_887312804b804e56b831c38b40eebbaf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : type 'abc' in candidate name
    element_locators = ['[placeholder="Type for hints..."]', '.oxd-autocomplete-text-input--before + input', 'input:has(+ .oxd-autocomplete-text-input--after)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)', "//input[starts-with(@placeholder,'Type ')]", "//input[contains(@placeholder,'Type for hints...')]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'abc':
            element.send_keys(char)
    else:
        element.send_keys('abc')
    driver.implicitly_wait(6)

    # Step - 17 : type 'abc' in keywords
    element_locators = ['[placeholder="Enter comma seperated words..."]', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)', "//input[starts-with(@placeholder,'Enter')]", "//input[contains(@placeholder,'Enter comma seperated words...')]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'abc':
            element.send_keys(char)
    else:
        element.send_keys('abc')
    driver.implicitly_wait(6)

    # Step - 18 : Click 'Search'
    element_locators = ['[type="submit"]', '.oxd-button--ghost + button', '.oxd-button--medium.oxd-button--ghost + button', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[4]/button[2]", '[type="reset"] + button', "//button[starts-with(@type,'submi')]", "//button[contains(@type,'submit')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Invalid' text visibility
    element_locators = ['.oxd-input-field-error-message', '.oxd-text--span.oxd-input-field-error-message', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/span[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)', "//span[text()='Invalid']", "//span[contains(@class,'oxd-input-field-error-message')]", "//span[contains(@class,'oxd-text--span') and contains(@class,'oxd-input-field-error-message')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_91a9117b1c28496cbfa957f650bb8b4b_0' to true
    assertion_operand_91a9117b1c28496cbfa957f650bb8b4b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Invalid' text is displayed on viewport
    assertion_operand_91a9117b1c28496cbfa957f650bb8b4b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Click 'Reset'
    element_locators = ['[type="reset"]', '.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ [type="submit"])', "//button[starts-with(@type,'reset')]", "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@type,'reset')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 23 : wait 5 seconds
    time.sleep(int(5))

    driver.quit()
except Exception as e:
    driver.quit()
