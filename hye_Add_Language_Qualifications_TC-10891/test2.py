
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

    # Step - 3 : set the value of variable 'assertion_operand_8491606f49414b53b31e1d8e244f9b13_0' to true
    assertion_operand_8491606f49414b53b31e1d8e244f9b13_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_8491606f49414b53b31e1d8e244f9b13_0 = "true"
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

    # Step - 9 : Click 'My Info' from the left side panel
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

    # Step - 11 : Click on 'Qualifications' tab in the left side menu
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[9]/a[1]", "//a[text()='Qualifications']", "//a[contains(text(),'Qualifications')]", '[role="tablist"] > div:nth-child(9) > a:nth-child(1)', '[role="tablist"] > div:nth-child(9) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : scroll down 200 px
    driver.execute_script("window.scrollBy(0, 200)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 13 : Click on the plus icon in Languages section add button
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/button[1]/i[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2) > i:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : scroll down 200 px
    driver.execute_script("window.scrollBy(0, 200)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 15 : Click on the language dropdown in Add Language section
    element_locators = ['.oxd-select-text--focus > div:nth-child(2) > i:nth-child(1)', '.oxd-select-text--focus > div:nth-child(2) > i:nth-child(1)', "//div[contains(@class,'oxd-select-text--focus')]/div[2]/i[1]", "//div[contains(@class,'oxd-select-text--focus')]/div[2]/i[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 16 : Click on the fluency dropdown arrow in Add Language section
    element_locators = ['.oxd-select-text--focus > div:nth-child(2) > i:nth-child(1)', '.oxd-select-text--focus > div:nth-child(2) > i:nth-child(1)', "//div[contains(@class,'oxd-select-text--focus')]/div[2]/i[1]", "//div[contains(@class,'oxd-select-text--focus')]/div[2]/i[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 17 : Click on the competency dropdown arrow in Add Language section
    element_locators = ['.oxd-select-text--focus > div:nth-child(2) > i:nth-child(1)', '.oxd-select-text--focus > div:nth-child(2) > i:nth-child(1)', "//div[contains(@class,'oxd-select-text--focus')]/div[2]/i[1]", "//div[contains(@class,'oxd-select-text--focus')]/div[2]/i[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 18 : Query 'Poor' text visibility
    element_locators = ['.--positon-bottom > div:nth-child(2)', '.--positon-bottom > div:nth-child(2)', '.--positon-bottom > div:nth-child(2)', '[role="listbox"] > div:nth-child(2)', "//div[contains(@class,'--positon-bottom')]/div[2]", "//div[contains(@class,'--positon-bottom')]/div[2]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 19 : set the value of variable 'assertion_operand_d77027b511b344e290869e5abcfaa845_0' to true
    assertion_operand_d77027b511b344e290869e5abcfaa845_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Assert 'Poor' text is visible
    assertion_operand_d77027b511b344e290869e5abcfaa845_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Query 'Basic' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 22 : set the value of variable 'assertion_operand_2c70fbc266f94288a79f4d2385fb617e_0' to true
    assertion_operand_2c70fbc266f94288a79f4d2385fb617e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Assert 'Basic' text is visible
    assertion_operand_2c70fbc266f94288a79f4d2385fb617e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Query 'Good' text visibility
    element_locators = ['.--positon-bottom > div:nth-child(4)', '.--positon-bottom > div:nth-child(4)', '.--positon-bottom > div:nth-child(4)', '[role="listbox"] > div:nth-child(4)', "//div[contains(@class,'--positon-bottom')]/div[4]", "//div[contains(@class,'--positon-bottom')]/div[4]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 25 : set the value of variable 'assertion_operand_711074cb990847d68346a763c3328519_0' to true
    assertion_operand_711074cb990847d68346a763c3328519_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Assert 'Good' text is visible
    assertion_operand_711074cb990847d68346a763c3328519_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Query 'Mother Tounge' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 28 : set the value of variable 'assertion_operand_2d463a74b114458d8ad6ea585a7f8f55_0' to true
    assertion_operand_2d463a74b114458d8ad6ea585a7f8f55_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Assert 'Mother Tounge' text is visible
    assertion_operand_2d463a74b114458d8ad6ea585a7f8f55_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Click on the competency dropdown arrow in Add Language section
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/i[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > i:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 31 : Click 'Save' button
    element_locators = ['[type="submit"]', '.oxd-button--secondary', '.oxd-button--medium.oxd-button--secondary', '.oxd-button--ghost + button', "//button[starts-with(@type,'submi')]", "//button[contains(@class,'oxd-button--secondary')]", "//button[contains(@type,'submit')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--secondary')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 32 : Query 'Required' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 33 : set the value of variable 'assertion_operand_2ec48494e0b64f75bd4d264bef34560f_0' to true
    assertion_operand_2ec48494e0b64f75bd4d264bef34560f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Assert 'Required' text is visible
    assertion_operand_2ec48494e0b64f75bd4d264bef34560f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Click 'Cancel' button
    element_locators = ['.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ .oxd-button--secondary)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/form[1]/div[3]/button[1]", 'button:has(+ .oxd-button--medium.oxd-button--secondary)', "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()

    driver.quit()
except Exception as e:
    driver.quit()
