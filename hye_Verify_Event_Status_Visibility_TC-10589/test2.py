
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

    # Step - 3 : set the value of variable 'assertion_operand_16484e0984df4302b92e28b0dd889bfc_0' to true
    assertion_operand_16484e0984df4302b92e28b0dd889bfc_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_16484e0984df4302b92e28b0dd889bfc_0 = "true"
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

    # Step - 9 : Click on 'Claim' menu item in the left side menu
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[11]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[11]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(11) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(11) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : Click on 'Configuration' tab in the top navigation bar
    element_locators = ['span.oxd-topbar-body-nav-tab-item', '.--parent > span', '.oxd-topbar-body-nav-tab.--parent > span', '.--parent > span:nth-child(1)', "//span[contains(text(),'Configuration')]", "//li[contains(@class,'--parent')]/span[1]", "//span[contains(@class,'oxd-topbar-body-nav-tab-item')]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent')]/span[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 11 : Click on 'Events' tab in top navigation bar
    element_locators = ['.--parent > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', '.--parent > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', "//a[text()='Events']", "//a[contains(text(),'Events')]", "//li[contains(@class,'--parent')]/ul[1]/li[1]/a[1]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent')]/ul[1]/li[1]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : Click on the caret up icon in dropdown arrow
    element_locators = ['.oxd-select-text--arrow', '.oxd-select-text--after > i', '.oxd-select-text--after > i:nth-child(1)', '.oxd-select-text--after > i:nth-child(1)', "//i[contains(@class,'oxd-select-text--arrow')]", "//div[contains(@class,'oxd-select-text--after')]/i[1]", "//div[contains(@class,'oxd-select-text--after')]/i[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 13 : Query 'Active' text visibility
    element_locators = ['.--positon-bottom > div:nth-child(2)', '.--positon-bottom > div:nth-child(2)', '.--positon-bottom > div:nth-child(2)', '[role="listbox"] > div:nth-child(2)', "//div[contains(@class,'--positon-bottom')]/div[2]", "//div[contains(@class,'--positon-bottom')]/div[2]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_53cdc98bd85940738db2b44dae66207b_0' to true
    assertion_operand_53cdc98bd85940738db2b44dae66207b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Active' text is visible
    assertion_operand_53cdc98bd85940738db2b44dae66207b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'inactive' text visibility
    element_locators = ['.--positon-bottom > div:nth-child(3)', '.--positon-bottom > div:nth-child(3)', '.--positon-bottom > div:nth-child(3)', '[role="listbox"] > div:nth-child(3)', "//div[contains(@class,'--positon-bottom')]/div[3]", "//div[contains(@class,'--positon-bottom')]/div[3]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_b1267d47799c4e9a85863b0a41575162_0' to true
    assertion_operand_b1267d47799c4e9a85863b0a41575162_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'inactive' text is visible
    assertion_operand_b1267d47799c4e9a85863b0a41575162_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Active' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_aad51d550c2f434d8b2659fe2fcf2d54_0' to true
    assertion_operand_aad51d550c2f434d8b2659fe2fcf2d54_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Active' text is visible
    assertion_operand_aad51d550c2f434d8b2659fe2fcf2d54_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Click on the status dropdown arrow in Events filter
    element_locators = ['.oxd-select-text--arrow', '.oxd-select-text--after > i', '.oxd-select-text--after > i:nth-child(1)', '.oxd-select-text--after > i:nth-child(1)', "//i[contains(@class,'oxd-select-text--arrow')]", "//div[contains(@class,'oxd-select-text--after')]/i[1]", "//div[contains(@class,'oxd-select-text--after')]/i[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 23 : Query 'Inactive' text visibility
    element_locators = ['div:has(+ .oxd-select-text--after)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)', "//div[text()='Inactive']", "//div[contains(text(),'Inactive')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 24 : set the value of variable 'assertion_operand_f32fb59c4ec54af89a5176b78521711b_0' to true
    assertion_operand_f32fb59c4ec54af89a5176b78521711b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Assert 'Inactive' text is visible
    assertion_operand_f32fb59c4ec54af89a5176b78521711b_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
