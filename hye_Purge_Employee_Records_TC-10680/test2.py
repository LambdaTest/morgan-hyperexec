
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

    # Step - 3 : set the value of variable 'assertion_operand_5f6517099928493ea52f0bb7e0f567bf_0' to true
    assertion_operand_5f6517099928493ea52f0bb7e0f567bf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_5f6517099928493ea52f0bb7e0f567bf_0 = "true"
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

    # Step - 11 : type ******************* in password input field
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

    # Step - 12 : Click 'Confirm' button
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

    # Step - 14 : Click on Past Employee input field with placeholder 'Type for hints...'
    element_locators = ['[placeholder="Type for hints..."]', '.oxd-autocomplete-text-input--focus > input', '.oxd-autocomplete-text-input--before + input', 'input:has(+ .oxd-autocomplete-text-input--after)', "//input[starts-with(@placeholder,'Type ')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]", "//input[contains(@placeholder,'Type for hints...')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 15 : Type in past employee input field with placeholder 'Type for hints...' 'ayush'
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

    # Step - 16 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 17 : Query 'Invalid' text visibility
    element_locators = ['.oxd-input-field-error-message', '.oxd-text--span.oxd-input-field-error-message', '.oxd-input-field-bottom-space > span', '.oxd-input-field-bottom-space > span:nth-child(3)', "//span[text()='Invalid']", "//span[contains(@class,'oxd-input-field-error-message')]", "//div[contains(@class,'oxd-input-field-bottom-space')]/span[1]", "//span[contains(@class,'oxd-text--span') and contains(@class,'oxd-input-field-error-message')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_854b809c5ff742fba349a67a2602643e_0' to true
    assertion_operand_854b809c5ff742fba349a67a2602643e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'Invalid' text is visible
    assertion_operand_854b809c5ff742fba349a67a2602643e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Click on the Search button in Purge Employee Records section
    element_locators = ['[type="submit"]', '.oxd-button--medium', '.oxd-button--secondary', '.oxd-button--medium.oxd-button--secondary', "//button[starts-with(@type,'submi')]", "//button[contains(@class,'oxd-button--medium')]", "//button[contains(@type,'submit')]", "//button[contains(@class,'oxd-button--secondary')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 21 : Get the current URL
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 22 : set the value of variable 'assertion_operand_63387db6cdcd4a94868d3369d420edc2_0' to purgeEmployee
    assertion_operand_63387db6cdcd4a94868d3369d420edc2_0 = "purgeEmployee"
    driver.implicitly_wait(6)

    # Step - 23 : Assert current URL contains 'purgeEmployee'
    assertion_operand_63387db6cdcd4a94868d3369d420edc2_0 = "purgeEmployee"

    driver.quit()
except Exception as e:
    driver.quit()
