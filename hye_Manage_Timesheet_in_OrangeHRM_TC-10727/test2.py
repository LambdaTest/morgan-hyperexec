
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

    # Step - 3 : set the value of variable 'assertion_operand_21b1801172b14e9b8b4bd9ef102720e5_0' to true
    assertion_operand_21b1801172b14e9b8b4bd9ef102720e5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_21b1801172b14e9b8b4bd9ef102720e5_0 = "true"
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

    # Step - 9 : Click 'Time'
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[4]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[4]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 11 : Click 'Timesheet' dropdown
    element_locators = ['.--visited', '.oxd-topbar-body-nav-tab.--visited', '.--parent.--visited', "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[1]", "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[1]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(1)', "//li[contains(@class,'--visited')]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent') and contains(@class,'--visited')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : Click 'My Timesheet'
    element_locators = ["//a[text()='My Timesheets']", '[role="menu"] > li:nth-child(1) > a:nth-child(1)', '[role="menu"] > li:nth-child(1) > a:nth-child(1)', "//a[contains(text(),'My Timesheets')]", "//li[contains(@class,'--visited')]/ul[1]/li[1]/a[1]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent') and contains(@class,'--visited')]/ul[1]/li[1]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 13 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 14 : Query 'My Timesheet' text visibility
    element_locators = ['.orangehrm-timesheet-header--title', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]", 'div:has(+ .orangehrm-timesheet-header--options)', '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1)', "//div[contains(@class,'orangehrm-timesheet-header--title')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 15 : set the value of variable 'assertion_operand_6129ff6f1ed14cc498db210d3188a954_0' to true
    assertion_operand_6129ff6f1ed14cc498db210d3188a954_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Assert 'My Timesheet' text is displayed
    assertion_operand_6129ff6f1ed14cc498db210d3188a954_0 = "true"
    driver.implicitly_wait(6)

    # Step - 17 : Query if 'Status: Not Submitted' text is visible
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_e61fe4793c6946899c4f21f09eefbc15_0' to true
    assertion_operand_e61fe4793c6946899c4f21f09eefbc15_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'Status: Not Submitted' text is displayed
    assertion_operand_e61fe4793c6946899c4f21f09eefbc15_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Click 'Edit' button
    element_locators = ['.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ .oxd-button--secondary)', '.orangehrm-timesheet-footer--options > button:nth-child(1)', "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]", "//div[contains(@class,'orangehrm-timesheet-footer--options')]/button[1]", "//div[contains(@class,'orangehrm-timesheet-footer--options')]/button[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 21 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Edit Timesheet' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_77ad9875029f407e82f11e64363fe45b_0' to true
    assertion_operand_77ad9875029f407e82f11e64363fe45b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Edit Timesheet' text is displayed
    assertion_operand_77ad9875029f407e82f11e64363fe45b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Click 'Add Row' button
    element_locators = ['button:has(+ .oxd-text--subtitle-2)', 'button:has(+ .oxd-text--p.oxd-text--subtitle-2)', '.--editable > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1) > button:nth-child(1)', '.--editable > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1) > button:nth-child(1)', "//table[contains(@class,'--editable')]/tbody[1]/tr[2]/td[1]/button[1]", "//table[contains(@class,'--editable')]/tbody[1]/tr[2]/td[1]/button[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 26 : Click 'Delete' icon
    element_locators = ['.--editable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(10) > button:nth-child(1)', '.--editable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(10) > button:nth-child(1)', "//table[contains(@class,'--editable')]/tbody[1]/tr[1]/td[10]/button[1]", "//table[contains(@class,'--editable')]/tbody[1]/tr[1]/td[10]/button[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 27 : Click 'Delete' icon
    element_locators = ['.--editable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(10) > button:nth-child(1)', '.--editable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(10) > button:nth-child(1)', "//table[contains(@class,'--editable')]/tbody[1]/tr[1]/td[10]/button[1]", "//table[contains(@class,'--editable')]/tbody[1]/tr[1]/td[10]/button[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 28 : Click 'save' button
    element_locators = ['[type="submit"]', '.oxd-button--secondary', '.oxd-button--medium.oxd-button--secondary', '.orangehrm-timesheet-footer--options > button:nth-child(3)', "//button[starts-with(@type,'submi')]", "//button[contains(@class,'oxd-button--secondary')]", "//button[contains(@type,'submit')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--secondary')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 29 : Query 'Select a Project' text visibility
    element_locators = ["//span[text()='Select a Project']", '.--editable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > span:nth-child(3)', "//table[contains(@class,'--editable')]/tbody[1]/tr[1]/td[1]/div[1]/span[1]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 30 : set the value of variable 'assertion_operand_2f106e198c0c484aa92c37b21e7a7ee6_0' to true
    assertion_operand_2f106e198c0c484aa92c37b21e7a7ee6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Assert 'Select a Project' text is displayed
    assertion_operand_2f106e198c0c484aa92c37b21e7a7ee6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Query if 'Select an Activity' text is visible
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 33 : set the value of variable 'assertion_operand_b5bd38eb672f4e32859dcd37055fc2bc_0' to true
    assertion_operand_b5bd38eb672f4e32859dcd37055fc2bc_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Assert 'Select an Activity' text is displayed
    assertion_operand_b5bd38eb672f4e32859dcd37055fc2bc_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Click 'Reset' button
    element_locators = ['button:has(+ .oxd-button--secondary)', '.orangehrm-timesheet-footer--options > button:nth-child(2)', '.orangehrm-timesheet-footer--options > button:nth-child(2)', 'button:has(+ .oxd-button--medium.oxd-button--secondary)', "//div[contains(@class,'orangehrm-timesheet-footer--options')]/button[2]", "//div[contains(@class,'orangehrm-timesheet-footer--options')]/button[2]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()

    driver.quit()
except Exception as e:
    driver.quit()
