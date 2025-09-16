
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
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_ceaa6dee98de4cfa91d8b24302afd942_0' to true
    assertion_operand_ceaa6dee98de4cfa91d8b24302afd942_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_ceaa6dee98de4cfa91d8b24302afd942_0 = "true"
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

    # Step - 9 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 10 : Click on Claim menu item in left sidebar
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[11]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[11]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(11) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(11) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 11 : Click on 'Submit Claim' tab in the top nav bar
    element_locators = ["//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[2]/a[1]", "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[2]/a[1]", "//a[text()='Submit Claim']", "//a[contains(text(),'Submit Claim')]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)', '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : Click on the 'Create' button in the bottom right corner of Create Claim Request form
    element_locators = ['[type="submit"]', '.oxd-button--secondary', '.oxd-button--medium.oxd-button--secondary', '.oxd-button--ghost + button', "//button[starts-with(@type,'submi')]", "//button[contains(@class,'oxd-button--secondary')]", "//button[contains(@type,'submit')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--secondary')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 13 : Get the current page URL
    currentPageUrl = driver.current_url

    print("currentPageUrl:", currentPageUrl)
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_9de94b97b19f4c9a84286c587d7afa50_0' to submitClaim
    assertion_operand_9de94b97b19f4c9a84286c587d7afa50_0 = "submitClaim"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'current_url' contains 'submitClaim'
    assertion_operand_9de94b97b19f4c9a84286c587d7afa50_0 = "submitClaim"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'Required' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_5e40fcc7e64243c8a71ecbfea5a1e558_0' to true
    assertion_operand_5e40fcc7e64243c8a71ecbfea5a1e558_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'Required' text is visible
    assertion_operand_5e40fcc7e64243c8a71ecbfea5a1e558_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Click on the event dropdown arrow in create claim request form
    element_locators = ['#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 20 : Click on the currency dropdown up arrow
    element_locators = ['.oxd-select-text--focus > div:nth-child(2) > i:nth-child(1)', '.oxd-select-text--focus > div:nth-child(2) > i:nth-child(1)', "//div[contains(@class,'oxd-select-text--focus')]/div[2]/i[1]", "//div[contains(@class,'oxd-select-text--error')]/div[2]/i[1]", "//div[contains(@class,'oxd-select-text--focus')]/div[2]/i[1]", "//div[contains(@class,'oxd-select-text--focus') and contains(@class,'oxd-select-text--error')]/div[2]/i[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 21 : Click on the Cancel button in create claim request form
    element_locators = ['.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ .oxd-button--secondary)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[1]", 'button:has(+ .oxd-button--medium.oxd-button--secondary)', "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 22 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 23 : Click on 'Submit Claim' tab in the top nav bar
    element_locators = ["//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[2]/a[1]", "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[2]/a[1]", "//a[text()='Submit Claim']", "//a[contains(text(),'Submit Claim')]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)', '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()

    driver.quit()
except Exception as e:
    driver.quit()
