
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

    # Step - 3 : set the value of variable 'assertion_operand_bc128001b67745779942ca5b2d736966_0' to true
    assertion_operand_bc128001b67745779942ca5b2d736966_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_bc128001b67745779942ca5b2d736966_0 = "true"
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

    # Step - 10 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 11 : Click 'Configuration'
    element_locators = ["//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[7]", "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[7]", 'li:has(+ .oxd-topbar-body-nav-slot)', '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(7)', '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(7)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : Click 'Language Packages' dropdown
    element_locators = ["//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[7]/ul[1]/li[4]/a[1]", "//a[text()='Language Packages']", "//a[contains(text(),'Language Packages')]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(7) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)']
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

    # Step - 14 : set the value of variable 'assertion_operand_3e878116fa074eba8537732e66e9d491_0' to languagePackage
    assertion_operand_3e878116fa074eba8537732e66e9d491_0 = "languagePackage"
    driver.implicitly_wait(6)

    # Step - 15 : Assert '{{url}}' contains 'languagePackage'
    assertion_operand_3e878116fa074eba8537732e66e9d491_0 = "languagePackage"
    driver.implicitly_wait(6)

    # Step - 16 : Query if '(8) Record Found' text is visible
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_5b5475168f7b41bc9a24b063d522be5c_0' to true
    assertion_operand_5b5475168f7b41bc9a24b063d522be5c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert '(8) Record Found' text is visible
    assertion_operand_5b5475168f7b41bc9a24b063d522be5c_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
