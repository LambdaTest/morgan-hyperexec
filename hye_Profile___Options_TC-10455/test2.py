
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
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_35a87590487643c7a8711957950a3310_0' to true
    assertion_operand_35a87590487643c7a8711957950a3310_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_35a87590487643c7a8711957950a3310_0 = "true"
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

    # Step - 9 : Click on the user dropdown with name Pushpa Raj in the top right corner
    element_locators = ["//div[@id='app']/div[1]/div[1]/header[1]/div[1]/div[3]/ul[1]/li[1]/span[1]/p[1]", '#app > div:nth-child(1) > div:nth-child(1) > header:nth-child(2) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1) > p:nth-child(2)', "//p[text()='Pushpa Raj']", "//p[contains(text(),'Pushpa Raj')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : Click on the help icon in the top right corner
    element_locators = ["//div[@id='app']/div[1]/div[1]/header[1]/div[1]/div[3]/ul[1]/li[1]/ul[1]/li[1]/a[1]", "//a[text()='About']", '[role="menu"] > li:nth-child(1) > a:nth-child(1)', '[role="menu"] > li:nth-child(1) > a:nth-child(1)', "//a[contains(text(),'About')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 11 : Query if 'Company Name: NetFunda' is displayed
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 12 : set the value of variable 'assertion_operand_c063c2f887d64d2591aee4154dada115_0' to true
    assertion_operand_c063c2f887d64d2591aee4154dada115_0 = "true"
    driver.implicitly_wait(6)

    # Step - 13 : Assert 'Company Name: NetFunda' is displayed on viewport
    assertion_operand_c063c2f887d64d2591aee4154dada115_0 = "true"
    driver.implicitly_wait(6)

    # Step - 14 : Click 'x' icon
    element_locators = ['.oxd-dialog-close-button-position', '.oxd-dialog-sheet--shadow > button', '.oxd-dialog-sheet--gutters > button', "//button[text()='×']", '[role="document"] > button', "//button[contains(text(),'×')]", "//div[contains(@class,'oxd-sheet--rounded') and contains(@class,'oxd-sheet--white') and contains(@class,'oxd-dialog-sheet--shadow') and contains(@class,'oxd-dialog-sheet--gutters')]/button[1]", "//button[contains(@class,'oxd-dialog-close-button-position')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 15 : Click on user dropdown with name Pushpa Raj in top right corner
    element_locators = ["//div[@id='app']/div[1]/div[1]/header[1]/div[1]/div[3]/ul[1]/li[1]/span[1]/p[1]", '#app > div:nth-child(1) > div:nth-child(1) > header:nth-child(2) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1) > p:nth-child(2)', "//p[text()='Pushpa Raj']", "//p[contains(text(),'Pushpa Raj')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 16 : Click on 'Support' link in user dropdown menu
    element_locators = ["//div[@id='app']/div[1]/div[1]/header[1]/div[1]/div[3]/ul[1]/li[1]/ul[1]/li[2]/a[1]", "//a[text()='Support']", '[role="menu"] > li:nth-child(2) > a:nth-child(1)', '[role="menu"] > li:nth-child(2) > a:nth-child(1)', "//a[contains(text(),'Support')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 17 : Query 'Customer Support' text visibility
    element_locators = ['.--mail > div:nth-child(2) > p:nth-child(1)', '.--mail > div:nth-child(2) > p:nth-child(1)', "//p[text()='Customer Support']", "//div[contains(@class,'--mail')]/div[2]/p[1]", "//div[contains(@class,'--mail')]/div[2]/p[1]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_10a6457de5764a5f82c4e57e4c0ebc18_0' to true
    assertion_operand_10a6457de5764a5f82c4e57e4c0ebc18_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'Customer Support' text is visible
    assertion_operand_10a6457de5764a5f82c4e57e4c0ebc18_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Click on user dropdown with name Pushpa Raj in top right corner
    element_locators = ["//div[@id='app']/div[1]/div[1]/header[1]/div[1]/div[3]/ul[1]/li[1]/span[1]/p[1]", '#app > div:nth-child(1) > div:nth-child(1) > header:nth-child(2) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1) > p:nth-child(2)', "//p[text()='Pushpa Raj']", '[alt="profile picture"] + p', "//p[contains(text(),'Pushpa Raj')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 21 : Click on 'Change Password' link in user dropdown menu
    element_locators = ["//div[@id='app']/div[1]/div[1]/header[1]/div[1]/div[3]/ul[1]/li[1]/ul[1]/li[3]/a[1]", "//a[text()='Change Password']", '[role="menu"] > li:nth-child(3) > a:nth-child(1)', '[role="menu"] > li:nth-child(3) > a:nth-child(1)', "//a[contains(text(),'Change Password')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Update Password' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Update Password']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_2e5b39338b1b47b0aa3e2cab69198ad2_0' to true
    assertion_operand_2e5b39338b1b47b0aa3e2cab69198ad2_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Update Password' text is visible
    assertion_operand_2e5b39338b1b47b0aa3e2cab69198ad2_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
