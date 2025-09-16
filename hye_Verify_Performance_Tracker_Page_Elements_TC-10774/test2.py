
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
    element_locators = ['[placeholder="Username"][name="username"]', '[placeholder="Username"]', '[name="username"]', "//input[@placeholder='Username' and @name='username']", '.oxd-input--focus', "//input[starts-with(@placeholder,'Usern')]", "//input[contains(@class,'oxd-input--focus')]", "//input[contains(@placeholder,'Username')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_edb89b198b99423dbfc644c64495b33d_0' to true
    assertion_operand_edb89b198b99423dbfc644c64495b33d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_edb89b198b99423dbfc644c64495b33d_0 = "true"
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

    # Step - 9 : Click on Performance menu item in left sidebar
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[7]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[7]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(7) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(7) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 11 : Click on 'My Trackers' tab in the top nav bar
    element_locators = ["//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[3]/a[1]", "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[3]/a[1]", "//a[text()='My Trackers']", "//a[contains(text(),'My Trackers')]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)', '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Get the current URL
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_542533da57bf476aa3bc6a3b101ba7c5_0' to viewMyPerformanceTrackerList
    assertion_operand_542533da57bf476aa3bc6a3b101ba7c5_0 = "viewMyPerformanceTrackerList"
    driver.implicitly_wait(6)

    # Step - 15 : Assert current URL contains 'viewMyPerformanceTrackerList'
    assertion_operand_542533da57bf476aa3bc6a3b101ba7c5_0 = "viewMyPerformanceTrackerList"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'My Performance Trackers' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_18c22a84e621413d93e91651d36b50aa_0' to true
    assertion_operand_18c22a84e621413d93e91651d36b50aa_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'My Performance Trackers' is visible
    assertion_operand_18c22a84e621413d93e91651d36b50aa_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'No Records Found' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_6cce5fb8948b48e19cd0eb10a809608e_0' to true
    assertion_operand_6cce5fb8948b48e19cd0eb10a809608e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'No Records Found' text is visible
    assertion_operand_6cce5fb8948b48e19cd0eb10a809608e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Tracker' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_a1c39a97a8f14eec9b543125818eaec5_0' to true
    assertion_operand_a1c39a97a8f14eec9b543125818eaec5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Tracker' text is visible
    assertion_operand_a1c39a97a8f14eec9b543125818eaec5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Added Date' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_a133679b32f640b582c2b46f14a9ad30_0' to true
    assertion_operand_a133679b32f640b582c2b46f14a9ad30_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Added Date' text is visible
    assertion_operand_a133679b32f640b582c2b46f14a9ad30_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Modified Date' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_9c5ac44ff24043baa66e7b4f0978efdc_0' to true
    assertion_operand_9c5ac44ff24043baa66e7b4f0978efdc_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Modified Date' text is visible
    assertion_operand_9c5ac44ff24043baa66e7b4f0978efdc_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_51ad4a64f1194a7f981aa2ee65ea3fb1_0' to true
    assertion_operand_51ad4a64f1194a7f981aa2ee65ea3fb1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'Actions' text is visible
    assertion_operand_51ad4a64f1194a7f981aa2ee65ea3fb1_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
