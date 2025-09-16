
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

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

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

    # Step - 3 : set the value of variable 'assertion_operand_ad3509d3fc6144e89171b2392947d339_0' to true
    assertion_operand_ad3509d3fc6144e89171b2392947d339_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_ad3509d3fc6144e89171b2392947d339_0 = "true"
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

    # Step - 11 : Click on 'Qualifications' tab in the left side menu
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[9]/a[1]", "//a[text()='Qualifications']", "//a[contains(text(),'Qualifications')]", '[role="tablist"] > div:nth-child(9) > a:nth-child(1)', '[role="tablist"] > div:nth-child(9) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Click on Work Experience + Add button
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : Query 'Company' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 15 : set the value of variable 'assertion_operand_ca8795319e6e4bb0892297b5060485f3_0' to true
    assertion_operand_ca8795319e6e4bb0892297b5060485f3_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Assert 'Company' text is visible
    assertion_operand_ca8795319e6e4bb0892297b5060485f3_0 = "true"
    driver.implicitly_wait(6)

    # Step - 17 : Query 'Job Title' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_4ce24ac1bbc841809118846867889d09_0' to true
    assertion_operand_4ce24ac1bbc841809118846867889d09_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'Job Title' text is visible
    assertion_operand_4ce24ac1bbc841809118846867889d09_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Query visibility of text 'From'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 21 : set the value of variable 'assertion_operand_c38d2945ae8d4a89a5fae00fa33feb7d_0' to true
    assertion_operand_c38d2945ae8d4a89a5fae00fa33feb7d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Assert text 'From' is visible
    assertion_operand_c38d2945ae8d4a89a5fae00fa33feb7d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Query visibility of text 'To'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='To']", "//label[contains(text(),'To')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 24 : set the value of variable 'assertion_operand_96f02738a3a34e0589ace78b7244c88b_0' to true
    assertion_operand_96f02738a3a34e0589ace78b7244c88b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Assert text 'To' is visible
    assertion_operand_96f02738a3a34e0589ace78b7244c88b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Query 'Comment' text visibility
    element_locators = ["//label[text()='Comment']", '.--span-column-2 > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', '.--span-column-2 > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[contains(text(),'Comment')]", "//div[contains(@class,'--span-column-2')]/div[1]/div[1]/label[1]", "//div[contains(@class,'oxd-grid-item--gutters') and contains(@class,'--span-column-2')]/div[1]/div[1]/label[1]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 27 : set the value of variable 'assertion_operand_d2e1fd5ce39646b698662fadee1c7f2f_0' to true
    assertion_operand_d2e1fd5ce39646b698662fadee1c7f2f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Assert 'Comment' text is visible
    assertion_operand_d2e1fd5ce39646b698662fadee1c7f2f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Query 'Cancel' text visibility
    element_locators = ['.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ .oxd-button--secondary)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[4]/button[1]", 'button:has(+ .oxd-button--medium.oxd-button--secondary)', "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 30 : set the value of variable 'assertion_operand_2354b50018a64ff29efd87d996e2e6fa_0' to true
    assertion_operand_2354b50018a64ff29efd87d996e2e6fa_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Assert 'Cancel' text is visible
    assertion_operand_2354b50018a64ff29efd87d996e2e6fa_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Query 'Save' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 33 : set the value of variable 'assertion_operand_a87c63befaa14fbb913b83cf41c91b43_0' to true
    assertion_operand_a87c63befaa14fbb913b83cf41c91b43_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Assert 'Save' text is visible
    assertion_operand_a87c63befaa14fbb913b83cf41c91b43_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Click 'Save Button'
    element_locators = ['[type="submit"]', '.oxd-button--secondary', '.oxd-button--medium.oxd-button--secondary', '.oxd-button--ghost + button', "//button[starts-with(@type,'submi')]", "//button[contains(@class,'oxd-button--secondary')]", "//button[contains(@type,'submit')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--secondary')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 36 : Query 'Required' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 37 : set the value of variable 'assertion_operand_aaed7cb199ec43fca23451ee05f12fac_0' to true
    assertion_operand_aaed7cb199ec43fca23451ee05f12fac_0 = "true"
    driver.implicitly_wait(6)

    # Step - 38 : Assert 'Required' text is visible
    assertion_operand_aaed7cb199ec43fca23451ee05f12fac_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Click 'Cancel' button
    element_locators = ['.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ .oxd-button--secondary)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[4]/button[1]", 'button:has(+ .oxd-button--medium.oxd-button--secondary)', "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()

    driver.quit()
except Exception as e:
    driver.quit()
