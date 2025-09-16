
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

    # Step - 3 : set the value of variable 'assertion_operand_6a7a550a92c745eb931f0fd7bc21898f_0' to true
    assertion_operand_6a7a550a92c745eb931f0fd7bc21898f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_6a7a550a92c745eb931f0fd7bc21898f_0 = "true"
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

    # Step - 9 : Click on 'My Info' menu item in left sidebar
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[6]/a[1]/span[1]", "//span[text()='My Info']", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(6) > a:nth-child(1) > span:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 11 : Click on 'Dependents' tab in the left side menu under 'My Info'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/a[1]", "//a[text()='Dependents']", "//a[contains(text(),'Dependents')]", '[role="tablist"] > div:nth-child(4) > a:nth-child(1)', '[role="tablist"] > div:nth-child(4) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Query 'Assigned Dependents' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Assigned Dependents']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_ee31374e480d4e46a1235a90b2fec62c_0' to true
    assertion_operand_ee31374e480d4e46a1235a90b2fec62c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Assigned Dependents' is visible
    assertion_operand_ee31374e480d4e46a1235a90b2fec62c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'No Record Found' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_457f2988d5394c6bbec69121157b67d3_0' to true
    assertion_operand_457f2988d5394c6bbec69121157b67d3_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'No Record Found' text is visible
    assertion_operand_457f2988d5394c6bbec69121157b67d3_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Name' visibility
    element_locators = ['.--strong', '.oxd-text--h6.--strong', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Pushpa Raj']", "//h6[contains(@class,'--strong')]", "//h6[contains(@class,'oxd-text--h6') and contains(@class,'--strong')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_a080dae9bfe04eebb9090111d2ed3773_0' to true
    assertion_operand_a080dae9bfe04eebb9090111d2ed3773_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Name' is visible on screen
    assertion_operand_a080dae9bfe04eebb9090111d2ed3773_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'relationship' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_945eeeab9d844e0ca07a726eef0e1761_0' to true
    assertion_operand_945eeeab9d844e0ca07a726eef0e1761_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'relationship' text is visible
    assertion_operand_945eeeab9d844e0ca07a726eef0e1761_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Date of Birth' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_41a4b9ca172b4ad9b4c08691c71fe5c1_0' to true
    assertion_operand_41a4b9ca172b4ad9b4c08691c71fe5c1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Date of Birth' text is visible
    assertion_operand_41a4b9ca172b4ad9b4c08691c71fe5c1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_5503011c104c433abf045ac6f70f9b8d_0' to true
    assertion_operand_5503011c104c433abf045ac6f70f9b8d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Actions' text is visible
    assertion_operand_5503011c104c433abf045ac6f70f9b8d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'File Name' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_ab4838a758c141d39b265f07023891d0_0' to true
    assertion_operand_ab4838a758c141d39b265f07023891d0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'File Name' is visible
    assertion_operand_ab4838a758c141d39b265f07023891d0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Description' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_e81798d378ed425f87dfe202d672ec5a_0' to true
    assertion_operand_e81798d378ed425f87dfe202d672ec5a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Description' text is visible
    assertion_operand_e81798d378ed425f87dfe202d672ec5a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Size' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_cd00e6f3dffe4ca6b6f14ce786c28f17_0' to true
    assertion_operand_cd00e6f3dffe4ca6b6f14ce786c28f17_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Size' text is visible
    assertion_operand_cd00e6f3dffe4ca6b6f14ce786c28f17_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Query 'Type' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 41 : set the value of variable 'assertion_operand_3767ccc650874ae1bc55f006994990ef_0' to true
    assertion_operand_3767ccc650874ae1bc55f006994990ef_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Assert 'Type' text is visible
    assertion_operand_3767ccc650874ae1bc55f006994990ef_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Query visibility of text 'Date Added'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 44 : set the value of variable 'assertion_operand_6fbc80227595405c9f38b70186326b18_0' to true
    assertion_operand_6fbc80227595405c9f38b70186326b18_0 = "true"
    driver.implicitly_wait(6)

    # Step - 45 : Assert text 'Date Added' is visible
    assertion_operand_6fbc80227595405c9f38b70186326b18_0 = "true"
    driver.implicitly_wait(6)

    # Step - 46 : Query 'Added By' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 47 : set the value of variable 'assertion_operand_77d6e17d39d94827990a2b42f50814b5_0' to true
    assertion_operand_77d6e17d39d94827990a2b42f50814b5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 48 : Assert 'Added By' text is visible
    assertion_operand_77d6e17d39d94827990a2b42f50814b5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 49 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 50 : set the value of variable 'assertion_operand_57431bd878344fd79f192ac1cf822523_0' to true
    assertion_operand_57431bd878344fd79f192ac1cf822523_0 = "true"
    driver.implicitly_wait(6)

    # Step - 51 : Assert 'Actions' text is visible
    assertion_operand_57431bd878344fd79f192ac1cf822523_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
