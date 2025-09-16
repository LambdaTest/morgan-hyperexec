
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

    # Step - 3 : set the value of variable 'assertion_operand_b608476fc66846df9d0c6efb536adee5_0' to true
    assertion_operand_b608476fc66846df9d0c6efb536adee5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_b608476fc66846df9d0c6efb536adee5_0 = "true"
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

    # Step - 9 : Click on 'Buzz' menu item in left side menu
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[12]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[12]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(12) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(12) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : Query 'Buzz Newsfeed' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/p[1]", 'p:has(+ .oxd-sheet--rounded)', 'p:has(+ .oxd-sheet--gutters)', 'p:has(+ .oxd-sheet--white)', 'p:has(+ .oxd-sheet--rounded.oxd-sheet--gutters)', "//p[text()='Buzz Newsfeed']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 11 : set the value of variable 'assertion_operand_cdead39a7cf442bf90d19bc1818eb9b1_0' to true
    assertion_operand_cdead39a7cf442bf90d19bc1818eb9b1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 12 : Assert 'Buzz Newsfeed' text is visible
    assertion_operand_cdead39a7cf442bf90d19bc1818eb9b1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 13 : Query 'Share Photos' visibility
    element_locators = ['.orangehrm-buzz-create-post-actions > button:nth-child(1)', '.orangehrm-buzz-create-post-actions > button:nth-child(1)', '.orangehrm-buzz-create-post-actions > button:nth-child(1)', "//button[contains(text(),'Share Photos')]", "//div[contains(@class,'orangehrm-buzz-create-post-actions')]/button[1]", "//div[contains(@class,'orangehrm-buzz-create-post-actions')]/button[1]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_cbe12da34e2e464eb60fbb5921e15c62_0' to true
    assertion_operand_cbe12da34e2e464eb60fbb5921e15c62_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Share Photos' is visible
    assertion_operand_cbe12da34e2e464eb60fbb5921e15c62_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'Share Video' visibility
    element_locators = ['.orangehrm-buzz-create-post-actions > button:nth-child(2)', '.orangehrm-buzz-create-post-actions > button:nth-child(2)', '.orangehrm-buzz-create-post-actions > button:nth-child(2)', "//button[contains(text(),'Share Video')]", "//div[contains(@class,'orangehrm-buzz-create-post-actions')]/button[2]", "//div[contains(@class,'orangehrm-buzz-create-post-actions')]/button[2]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_ab1fbf8c762b44119cf0c5a85d5f7cd5_0' to true
    assertion_operand_ab1fbf8c762b44119cf0c5a85d5f7cd5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'Share Video' text is visible
    assertion_operand_ab1fbf8c762b44119cf0c5a85d5f7cd5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Most Recent Posts' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_92c743b19bc6412e922889fca11b161b_0' to true
    assertion_operand_92c743b19bc6412e922889fca11b161b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Most Recent Posts' is visible
    assertion_operand_92c743b19bc6412e922889fca11b161b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query visibility of text 'Most Liked Posts'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_a4501028b61043cab4228222a26bfc47_0' to true
    assertion_operand_a4501028b61043cab4228222a26bfc47_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Most Liked Posts' text is visible
    assertion_operand_a4501028b61043cab4228222a26bfc47_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query visibility of text 'Most commented posts'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/button[3]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_59b22f0014a84483bd898ecca3f97fa6_0' to true
    assertion_operand_59b22f0014a84483bd898ecca3f97fa6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert text 'Most commented posts' is visible
    assertion_operand_59b22f0014a84483bd898ecca3f97fa6_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
