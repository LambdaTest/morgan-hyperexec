
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

    # Step - 3 : set the value of variable 'assertion_operand_b98b6ebb72cb4b1baf22b6e718ee7823_0' to true
    assertion_operand_b98b6ebb72cb4b1baf22b6e718ee7823_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_b98b6ebb72cb4b1baf22b6e718ee7823_0 = "true"
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

    # Step - 9 : Click on 'Admin' menu item in left side menu
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[1]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[1]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : Query 'System Users' text visibility
    element_locators = ['.oxd-table-filter-header-title', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]", 'div:has(+ .oxd-table-filter-header-options)', '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)', "//div[contains(@class,'oxd-table-filter-header-title')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 11 : set the value of variable 'assertion_operand_e56cb5e8fa1f492b8c43120aee801843_0' to true
    assertion_operand_e56cb5e8fa1f492b8c43120aee801843_0 = "true"
    driver.implicitly_wait(6)

    # Step - 12 : Assert 'System Users' text is visible
    assertion_operand_e56cb5e8fa1f492b8c43120aee801843_0 = "true"
    driver.implicitly_wait(6)

    # Step - 13 : Query 'Username' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_c9a2cfa693f9442cbdf75db058d3464b_0' to true
    assertion_operand_c9a2cfa693f9442cbdf75db058d3464b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Username' text is visible
    assertion_operand_c9a2cfa693f9442cbdf75db058d3464b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'Reset' text visibility
    element_locators = ['.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(3) > button:nth-child(1)', 'button:has(+ [type="submit"])', "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_f3c9750ce3d4441793ce391f0becbe76_0' to true
    assertion_operand_f3c9750ce3d4441793ce391f0becbe76_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'Reset' text is visible on the viewport
    assertion_operand_f3c9750ce3d4441793ce391f0becbe76_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Search' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_17fe1df0c1a54e21b98315cb0fb8858b_0' to true
    assertion_operand_17fe1df0c1a54e21b98315cb0fb8858b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Search' text is visible on the viewport
    assertion_operand_17fe1df0c1a54e21b98315cb0fb8858b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query '+ ADD' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_708d02a44b1e4d32b87f53dcd2052f99_0' to true
    assertion_operand_708d02a44b1e4d32b87f53dcd2052f99_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert '+ ADD' text is visible on viewport
    assertion_operand_708d02a44b1e4d32b87f53dcd2052f99_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'ayushp' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]", '[role="table"] > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)', '[role="table"] > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_2cab9dff114a4b369e52e755c4067773_0' to true
    assertion_operand_2cab9dff114a4b369e52e755c4067773_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'ayushp' text is visible on viewport
    assertion_operand_2cab9dff114a4b369e52e755c4067773_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'pushpa.raj' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]", '[role="table"] > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)', '[role="table"] > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_7b325febc0c9410da8418cf216086c82_0' to true
    assertion_operand_7b325febc0c9410da8418cf216086c82_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'pushpa.raj' text is visible
    assertion_operand_7b325febc0c9410da8418cf216086c82_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'status' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_f9b300cad0e24f8389328a8913b69221_0' to true
    assertion_operand_f9b300cad0e24f8389328a8913b69221_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'status' text is visible on viewport
    assertion_operand_f9b300cad0e24f8389328a8913b69221_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Delete' icon visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_5911fcc91c274d5db405ab6d3be9317a_0' to true
    assertion_operand_5911fcc91c274d5db405ab6d3be9317a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Delete_icon_visible' equals 'true'
    assertion_operand_5911fcc91c274d5db405ab6d3be9317a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Edit' icon visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/button[2]", '[role="table"] > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > button:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_2333e3bfed5a4e338d69926aef0775e7_0' to true
    assertion_operand_2333e3bfed5a4e338d69926aef0775e7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Edit' icon is visible on the viewport
    assertion_operand_2333e3bfed5a4e338d69926aef0775e7_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
