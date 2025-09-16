
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

    # Step - 3 : set the value of variable 'assertion_operand_8669d1dc171241849800171d99872c42_0' to true
    assertion_operand_8669d1dc171241849800171d99872c42_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_8669d1dc171241849800171d99872c42_0 = "true"
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

    # Step - 11 : Click on 'Memberships' tab in the left side menu under 'Qualifications'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/a[1]", "//a[text()='Memberships']", "//a[contains(text(),'Memberships')]", '[role="tablist"] > div:nth-child(10) > a:nth-child(1)', '[role="tablist"] > div:nth-child(10) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Query 'Attachments' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_eb82950b36d140f5a005e085a0db5061_0' to true
    assertion_operand_eb82950b36d140f5a005e085a0db5061_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Attachments' text is visible
    assertion_operand_eb82950b36d140f5a005e085a0db5061_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'No Records Found' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_49b9b426968f4a909b5298aa83aaf12d_0' to true
    assertion_operand_49b9b426968f4a909b5298aa83aaf12d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'No Records Found' text is visible
    assertion_operand_49b9b426968f4a909b5298aa83aaf12d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'File Name' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_01b1ec9f15f74475b665eaad9dc7db0a_0' to true
    assertion_operand_01b1ec9f15f74475b665eaad9dc7db0a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'File_Name_visible' equals 'true'
    assertion_operand_01b1ec9f15f74475b665eaad9dc7db0a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Description' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_e3f22aabb89d42efb0bc41f8995ca87d_0' to true
    assertion_operand_e3f22aabb89d42efb0bc41f8995ca87d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Description' text is visible
    assertion_operand_e3f22aabb89d42efb0bc41f8995ca87d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Size' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_d2a0362ca1c84d64a509c75e49e58a80_0' to true
    assertion_operand_d2a0362ca1c84d64a509c75e49e58a80_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Size' text is visible
    assertion_operand_d2a0362ca1c84d64a509c75e49e58a80_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Type' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_94eacfd0105146f4a36baa425f39b16c_0' to true
    assertion_operand_94eacfd0105146f4a36baa425f39b16c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Type' text is visible
    assertion_operand_94eacfd0105146f4a36baa425f39b16c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'Date Added' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(3)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_b798dd2a2b7c4f2ca7abe4d216ae06d7_0' to true
    assertion_operand_b798dd2a2b7c4f2ca7abe4d216ae06d7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'Date Added' text is visible
    assertion_operand_b798dd2a2b7c4f2ca7abe4d216ae06d7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query visibility of text 'Added By'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_8376e5a6c9174d43a28f664d42d6c5dd_0' to true
    assertion_operand_8376e5a6c9174d43a28f664d42d6c5dd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert text 'Added By' is visible
    assertion_operand_8376e5a6c9174d43a28f664d42d6c5dd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_992266ba18e8442991cad309fe117e0e_0' to true
    assertion_operand_992266ba18e8442991cad309fe117e0e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Actions' text is visible
    assertion_operand_992266ba18e8442991cad309fe117e0e_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
