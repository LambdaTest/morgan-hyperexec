
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

    # Step - 3 : set the value of variable 'assertion_operand_7729f3bc362d4bbcae9ae4c63784def0_0' to true
    assertion_operand_7729f3bc362d4bbcae9ae4c63784def0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_7729f3bc362d4bbcae9ae4c63784def0_0 = "true"
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

    # Step - 10 : Click on Configuration tab in the topbar 
    element_locators = ['span.oxd-topbar-body-nav-tab-item', '.--parent > span', '.oxd-topbar-body-nav-tab.--parent > span', '.--parent > span:nth-child(1)', "//span[contains(text(),'Configuration')]", "//li[contains(@class,'--parent')]/span[1]", "//span[contains(@class,'oxd-topbar-body-nav-tab-item')]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent')]/span[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 11 : Click 'Events' in dropdownlist
    element_locators = ['.--parent > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', '.--parent > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', "//a[text()='Events']", "//a[contains(text(),'Events')]", "//li[contains(@class,'--parent')]/ul[1]/li[1]/a[1]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent')]/ul[1]/li[1]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : Click on the time at work summary bar in the dashboard center 
    element_locators = ['[placeholder="Type for hints..."]', '.oxd-autocomplete-text-input--focus > input', '.oxd-autocomplete-text-input--before + input', 'input:has(+ .oxd-autocomplete-text-input--after)', "//input[starts-with(@placeholder,'Type ')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]", "//input[contains(@placeholder,'Type for hints...')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 13 : Type in time at work input with placeholder 'Type for hints...' 'active' 
    element_locators = ['[placeholder="Type for hints..."]', '.oxd-autocomplete-text-input--focus > input', '.oxd-autocomplete-text-input--before + input', 'input:has(+ .oxd-autocomplete-text-input--after)', "//input[starts-with(@placeholder,'Type ')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]", "//input[contains(@placeholder,'Type for hints...')]", "//div[contains(@class,'oxd-autocomplete-text-input--focus')]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'active':
            element.send_keys(char)
    else:
        element.send_keys('active')
    driver.implicitly_wait(6)

    # Step - 14 : Click on the caret up icon in dropdown arrow 
    element_locators = ['.oxd-select-text--arrow', '.oxd-select-text--after > i', '.oxd-select-text--after > i:nth-child(1)', '.oxd-select-text--after > i:nth-child(1)', "//i[contains(@class,'oxd-select-text--arrow')]", "//div[contains(@class,'oxd-select-text--after')]/i[1]", "//div[contains(@class,'oxd-select-text--after')]/i[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 15 : Click on the Search button 
    element_locators = ['[type="submit"]', '.oxd-button--ghost + button', '.oxd-button--medium.oxd-button--ghost + button', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[2]/button[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(3) > button:nth-child(2)', "//button[starts-with(@type,'submi')]", "//button[contains(@type,'submit')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 16 : wait 5 seconds
    time.sleep(int(5))
    driver.implicitly_wait(6)

    # Step - 17 : Query text '(2) Record Found' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[2]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_e7baf9814fa74a94804f1b6cb106e0b1_0' to true
    assertion_operand_e7baf9814fa74a94804f1b6cb106e0b1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert text '(2) Record Found' is visible
    assertion_operand_e7baf9814fa74a94804f1b6cb106e0b1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Click on the checkbox for Active Event in the claims list 
    element_locators = ['.oxd-table-card-cell-checkbox > div:nth-child(1) > label:nth-child(1) > span:nth-child(2) > i:nth-child(1)', '.oxd-table-card-cell-checkbox > div:nth-child(1) > label:nth-child(1) > span:nth-child(2) > i:nth-child(1)', "//div[contains(@class,'oxd-table-card-cell-checkbox')]/div[1]/label[1]/span[1]/i[1]", "//div[contains(@class,'oxd-table-card-cell-checkbox')]/div[1]/label[1]/span[1]/i[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 21 : Query 'Deleted Selected' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 22 : set the value of variable 'assertion_operand_ea10c33f363e4718844594bb7e3cb059_0' to true
    assertion_operand_ea10c33f363e4718844594bb7e3cb059_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Assert 'Deleted Selected' text is visible
    assertion_operand_ea10c33f363e4718844594bb7e3cb059_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Click on the Reset button in the Events filter section 
    element_locators = ['.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[2]/button[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(3) > button:nth-child(1)', 'button:has(+ [type="submit"])', "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 25 : wait 5 seconds
    time.sleep(int(5))

    driver.quit()
except Exception as e:
    driver.quit()
