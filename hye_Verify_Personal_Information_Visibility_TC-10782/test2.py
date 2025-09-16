
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

    # Step - 3 : set the value of variable 'assertion_operand_564a0f91f0c64ab584a0b8ed1bdd1b80_0' to true
    assertion_operand_564a0f91f0c64ab584a0b8ed1bdd1b80_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_564a0f91f0c64ab584a0b8ed1bdd1b80_0 = "true"
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

    # Step - 9 : Click on 'My Info' menu item in left side menu 
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

    # Step - 11 : Query 'Personal Details' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Personal Details']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 12 : set the value of variable 'assertion_operand_82925fa50bb348508db8d042d5924ba6_0' to true
    assertion_operand_82925fa50bb348508db8d042d5924ba6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 13 : Assert 'Personal Details' text is visible
    assertion_operand_82925fa50bb348508db8d042d5924ba6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 14 : Query 'Contact Details' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]", "//a[text()='Contact Details']", "//a[contains(text(),'Contact Details')]", '[role="tablist"] > div:nth-child(2) > a:nth-child(1)', '[role="tablist"] > div:nth-child(2) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 15 : set the value of variable 'assertion_operand_0cb110adccb8464cb0f3b1ab295a1803_0' to true
    assertion_operand_0cb110adccb8464cb0f3b1ab295a1803_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Assert 'Contact Details' text is visible
    assertion_operand_0cb110adccb8464cb0f3b1ab295a1803_0 = "true"
    driver.implicitly_wait(6)

    # Step - 17 : Query 'Emergency Contacts' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/a[1]", "//a[text()='Emergency Contacts']", "//a[contains(text(),'Emergency Contacts')]", '[role="tablist"] > div:nth-child(3) > a:nth-child(1)', '[role="tablist"] > div:nth-child(3) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_cf2c4bdeb1a547c8819f43fc74f3c846_0' to true
    assertion_operand_cf2c4bdeb1a547c8819f43fc74f3c846_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'Emergency Contacts' text is visible
    assertion_operand_cf2c4bdeb1a547c8819f43fc74f3c846_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Query 'Dependents' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/a[1]", "//a[text()='Dependents']", "//a[contains(text(),'Dependents')]", '[role="tablist"] > div:nth-child(4) > a:nth-child(1)', '[role="tablist"] > div:nth-child(4) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 21 : set the value of variable 'assertion_operand_e69cb549b35441649b47a6c418185af6_0' to true
    assertion_operand_e69cb549b35441649b47a6c418185af6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Assert 'Dependents' text is visible
    assertion_operand_e69cb549b35441649b47a6c418185af6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Query 'Immigrations' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/a[1]", "//a[text()='Immigration']", "//a[contains(text(),'Immigration')]", '[role="tablist"] > div:nth-child(5) > a:nth-child(1)', '[role="tablist"] > div:nth-child(5) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 24 : set the value of variable 'assertion_operand_a3e809b7f84d4869b93e6d1b5227b48c_0' to true
    assertion_operand_a3e809b7f84d4869b93e6d1b5227b48c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Assert 'Immigrations' text is visible
    assertion_operand_a3e809b7f84d4869b93e6d1b5227b48c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Query 'Job' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 27 : set the value of variable 'assertion_operand_0f741ec3840b4cefb1ba32c3f53600d8_0' to true
    assertion_operand_0f741ec3840b4cefb1ba32c3f53600d8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Assert 'Job' text is visible
    assertion_operand_0f741ec3840b4cefb1ba32c3f53600d8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Query 'Salary' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 30 : set the value of variable 'assertion_operand_dacd84790a6840cfaff27bf8913857bd_0' to true
    assertion_operand_dacd84790a6840cfaff27bf8913857bd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Assert 'Salary' text is visible
    assertion_operand_dacd84790a6840cfaff27bf8913857bd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Query 'Report-to' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[8]/a[1]", "//a[text()='Report-to']", "//a[contains(text(),'Report-to')]", '[role="tablist"] > div:nth-child(8) > a:nth-child(1)', '[role="tablist"] > div:nth-child(8) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 33 : set the value of variable 'assertion_operand_4ecdf4aca8cc4c5fbc52b2d73e79f16e_0' to true
    assertion_operand_4ecdf4aca8cc4c5fbc52b2d73e79f16e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Assert 'Report-to' text is visible
    assertion_operand_4ecdf4aca8cc4c5fbc52b2d73e79f16e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Query 'Qualifications' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 36 : set the value of variable 'assertion_operand_0d3eb2f94c2e4338823c2331a1ace69d_0' to true
    assertion_operand_0d3eb2f94c2e4338823c2331a1ace69d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Assert 'Qualifications' text is visible
    assertion_operand_0d3eb2f94c2e4338823c2331a1ace69d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 38 : Query 'Memberships' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 39 : set the value of variable 'assertion_operand_69be28c4ed9c48358874cbc43cc769e4_0' to true
    assertion_operand_69be28c4ed9c48358874cbc43cc769e4_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Assert 'Memberships' text is visible
    assertion_operand_69be28c4ed9c48358874cbc43cc769e4_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
