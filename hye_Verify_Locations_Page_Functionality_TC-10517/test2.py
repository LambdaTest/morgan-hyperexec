
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

    # Step - 3 : set the value of variable 'assertion_operand_8f057c783a5448c29555837516e8471b_0' to true
    assertion_operand_8f057c783a5448c29555837516e8471b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_8f057c783a5448c29555837516e8471b_0 = "true"
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

    # Step - 9 : Click 'Admin'
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[1]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[1]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 11 : Click 'Organization' dropdown
    element_locators = ["//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[3]", "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[3]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(3)', '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(3)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : Click 'Location'
    element_locators = ["//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[3]/ul[1]/li[2]/a[1]", "//a[text()='Locations']", "//a[contains(text(),'Locations')]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(3) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 13 : Get the current URL
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_5e55420a21b64aa09ddc002bb34c824b_0' to viewLocations
    assertion_operand_5e55420a21b64aa09ddc002bb34c824b_0 = "viewLocations"
    driver.implicitly_wait(6)

    # Step - 15 : Assert '{{current_url}}' contains 'viewLocations'
    assertion_operand_5e55420a21b64aa09ddc002bb34c824b_0 = "viewLocations"
    driver.implicitly_wait(6)

    # Step - 16 : Query if 'Locations' text is visible
    element_locators = ['.oxd-table-filter-header-title', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]", 'div:has(+ .oxd-table-filter-header-options)', '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)', "//div[contains(@class,'oxd-table-filter-header-title')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_6c7a956f171347eeb2a9054966341dcb_0' to true
    assertion_operand_6c7a956f171347eeb2a9054966341dcb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'Locations' text is displayed on viewport
    assertion_operand_6c7a956f171347eeb2a9054966341dcb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Search' icon visibility
    element_locators = ['[placeholder="Search"]', '.--fixed > div:nth-child(1) > input:nth-child(2)', 'input:has(+ [role="none"])', 'input:has(+ [type="button"][role="none"])', "//input[starts-with(@placeholder,'Searc')]", "//input[contains(@placeholder,'Search')]", "//div[contains(@class,'--fixed')]/div[1]/input[1]", "//div[contains(@class,'--fixed')]/div[1]/input[1]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_e56f0a68064140ed966722dd1d994e84_0' to true
    assertion_operand_e56f0a68064140ed966722dd1d994e84_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Search_icon_visible' equals 'true'
    assertion_operand_e56f0a68064140ed966722dd1d994e84_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query if 'No Records Found' is displayed
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_ff1e02bf0be5424a85d7294725354849_0' to true
    assertion_operand_ff1e02bf0be5424a85d7294725354849_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'No Records Found' is displayed on the viewport
    assertion_operand_ff1e02bf0be5424a85d7294725354849_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
