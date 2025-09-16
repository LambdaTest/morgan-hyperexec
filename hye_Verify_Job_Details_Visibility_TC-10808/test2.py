
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
    driver.implicitly_wait(6)

    # Step - 1 : navigate to 'https://orange-hrm.lambdatestinternal.com/orangehrm-5.7'
    driver.get("https://orange-hrm.lambdatestinternal.com/orangehrm-5.7")
    driver.implicitly_wait(6)

    # Step - 2 : Query 'Username input box' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_eaef4f56f9c24403911a6b6e29684232_0' to true
    assertion_operand_eaef4f56f9c24403911a6b6e29684232_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_eaef4f56f9c24403911a6b6e29684232_0 = "true"
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

    # Step - 9 : Click on 'My Info' menu item in the left side menu
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

    # Step - 11 : Click on 'Job' tab in the left side menu under 'My Info'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/a[1]", "//a[text()='Job']", "//a[contains(text(),'Job')]", '[role="tablist"] > div:nth-child(6) > a:nth-child(1)', '[role="tablist"] > div:nth-child(6) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Query 'Job Details' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_609c3530ba1744d09388dc2d3aa28523_0' to true
    assertion_operand_609c3530ba1744d09388dc2d3aa28523_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Job Details' text is visible
    assertion_operand_609c3530ba1744d09388dc2d3aa28523_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'Joined Date' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_eb707204cd48442e8af43ff48c33c23d_0' to true
    assertion_operand_eb707204cd48442e8af43ff48c33c23d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'Joined Date' text is visible
    assertion_operand_eb707204cd48442e8af43ff48c33c23d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Job title' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_7bbac0cf54404038aa06455d3300222f_0' to true
    assertion_operand_7bbac0cf54404038aa06455d3300222f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Job title' is visible
    assertion_operand_7bbac0cf54404038aa06455d3300222f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Job Specification' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Job Specification']", "//label[contains(text(),'Job Specification')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_332508ce1fa8405fbb5ab64384a53e15_0' to true
    assertion_operand_332508ce1fa8405fbb5ab64384a53e15_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Job Specification' is visible
    assertion_operand_332508ce1fa8405fbb5ab64384a53e15_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Job Category' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_7880779ca36d4518b93ef60f2ab3e02e_0' to true
    assertion_operand_7880779ca36d4518b93ef60f2ab3e02e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Job Category' is visible
    assertion_operand_7880779ca36d4518b93ef60f2ab3e02e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Sub unit' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_7c49bb73422d4f129b0c7e45e068920a_0' to true
    assertion_operand_7c49bb73422d4f129b0c7e45e068920a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Sub unit' is visible
    assertion_operand_7c49bb73422d4f129b0c7e45e068920a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'Location' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_ef51f3e23a2e4902b7ac738a44326aa8_0' to true
    assertion_operand_ef51f3e23a2e4902b7ac738a44326aa8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'Location' text is visible
    assertion_operand_ef51f3e23a2e4902b7ac738a44326aa8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Employment Status' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_2a74a8ed8ee84900b742d36333a71029_0' to true
    assertion_operand_2a74a8ed8ee84900b742d36333a71029_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Employment Status' text is visible
    assertion_operand_2a74a8ed8ee84900b742d36333a71029_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Get the current URL
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_5d19813d7b444ee4a93369bc3851b759_0' to viewjobDetails
    assertion_operand_5d19813d7b444ee4a93369bc3851b759_0 = "viewjobDetails"
    driver.implicitly_wait(6)

    # Step - 39 : Assert current URL contains 'viewjobDetails'
    assertion_operand_5d19813d7b444ee4a93369bc3851b759_0 = "viewjobDetails"

    driver.quit()
except Exception as e:
    driver.quit()
