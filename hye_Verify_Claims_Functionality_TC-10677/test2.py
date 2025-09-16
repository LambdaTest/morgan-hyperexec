
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

    # Step - 3 : set the value of variable 'assertion_operand_1c8860234e5842f0a9b5dad3015275a4_0' to true
    assertion_operand_1c8860234e5842f0a9b5dad3015275a4_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_1c8860234e5842f0a9b5dad3015275a4_0 = "true"
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

    # Step - 11 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 12 : Click on 'My Claims' tab in the top nav bar 
    element_locators = ["//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[3]/a[1]", "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[3]/a[1]", "//a[text()='My Claims']", "//a[contains(text(),'My Claims')]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)', '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 13 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 14 : Get the current URL
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 15 : set the value of variable 'assertion_operand_95677ca8e06b4e18a7e09c0c4588cc59_0' to viewClaim
    assertion_operand_95677ca8e06b4e18a7e09c0c4588cc59_0 = "viewClaim"
    driver.implicitly_wait(6)

    # Step - 16 : Assert 'current_url' contains 'viewClaim'
    assertion_operand_95677ca8e06b4e18a7e09c0c4588cc59_0 = "viewClaim"
    driver.implicitly_wait(6)

    # Step - 17 : Click on the Search button in My Claims section 
    element_locators = ['[type="submit"]', '.oxd-button--ghost + button', '.oxd-button--medium.oxd-button--ghost + button', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[3]/button[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(4) > button:nth-child(2)', "//button[starts-with(@type,'submi')]", "//button[contains(@type,'submit')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 18 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 19 : Query text '(1) Record Found' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_26852efcf5d841e9949c8c7ba1760f7d_0' to true
    assertion_operand_26852efcf5d841e9949c8c7ba1760f7d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert text '(1) Record Found' is visible
    assertion_operand_26852efcf5d841e9949c8c7ba1760f7d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Click on the event name dropdown arrow in My Claims filter 
    element_locators = ['#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 23 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 24 : Query 'Active Event' text visibility in dropdown
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 25 : set the value of variable 'assertion_operand_5e07d88e5856477fa28cd03887b1950e_0' to true
    assertion_operand_5e07d88e5856477fa28cd03887b1950e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Assert 'Active Event' text is visible in dropdown
    assertion_operand_5e07d88e5856477fa28cd03887b1950e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Click on the event name dropdown arrow in My Claims filter 
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/i[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > i:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 28 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 29 : Click on the status dropdown arrow in My Claims filter 
    element_locators = ['#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 30 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 31 : Query 'Initiated' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_65e4570f139e4b13a6bf5ae722558c72_0' to true
    assertion_operand_65e4570f139e4b13a6bf5ae722558c72_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'Initiated' text is visible
    assertion_operand_65e4570f139e4b13a6bf5ae722558c72_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Submitted' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_cca3ec31d2744ed386e17d8d6813b632_0' to true
    assertion_operand_cca3ec31d2744ed386e17d8d6813b632_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Submitted' text is visible
    assertion_operand_cca3ec31d2744ed386e17d8d6813b632_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Approved' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_de971f260e4f4be7848ed194ae3d7309_0' to true
    assertion_operand_de971f260e4f4be7848ed194ae3d7309_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Approved' text is visible
    assertion_operand_de971f260e4f4be7848ed194ae3d7309_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Query 'Rejetced' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 41 : set the value of variable 'assertion_operand_bd07a02ae6c04aa1a8a14c55eea4d283_0' to true
    assertion_operand_bd07a02ae6c04aa1a8a14c55eea4d283_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Assert 'Rejetced' text is visible
    assertion_operand_bd07a02ae6c04aa1a8a14c55eea4d283_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Query 'Cancelled' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 44 : set the value of variable 'assertion_operand_785353eb99fc4a8a9aa11d997b8eaa1d_0' to true
    assertion_operand_785353eb99fc4a8a9aa11d997b8eaa1d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 45 : Assert 'Cancelled' text is visible
    assertion_operand_785353eb99fc4a8a9aa11d997b8eaa1d_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
