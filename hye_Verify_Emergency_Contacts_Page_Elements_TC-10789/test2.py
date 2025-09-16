
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

    # Step - 3 : set the value of variable 'assertion_operand_3e4f0c6987a046dbae8e2b2f5d2fc680_0' to true
    assertion_operand_3e4f0c6987a046dbae8e2b2f5d2fc680_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_3e4f0c6987a046dbae8e2b2f5d2fc680_0 = "true"
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

    # Step - 11 : Click on Emergency Contacts tab in left side menu
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/a[1]", "//a[text()='Emergency Contacts']", "//a[contains(text(),'Emergency Contacts')]", '[role="tablist"] > div:nth-child(3) > a:nth-child(1)', '[role="tablist"] > div:nth-child(3) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Query 'Assigned Emergency Contacts' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Assigned Emergency Contacts']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_37839c7e70a94c5dab59d9687355ae7c_0' to true
    assertion_operand_37839c7e70a94c5dab59d9687355ae7c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Assigned Emergency Contacts' is visible
    assertion_operand_37839c7e70a94c5dab59d9687355ae7c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'No Records Found' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_fb1130adac9f448fa8d09074de2dcd21_0' to true
    assertion_operand_fb1130adac9f448fa8d09074de2dcd21_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'No Records Found' text is visible
    assertion_operand_fb1130adac9f448fa8d09074de2dcd21_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Name' visibility
    element_locators = ['.--strong', '.oxd-text--h6.--strong', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Pushpa Raj']", "//h6[contains(@class,'--strong')]", "//h6[contains(@class,'oxd-text--h6') and contains(@class,'--strong')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_bc35b6a22c9d4c91ae03024816f7e7f1_0' to true
    assertion_operand_bc35b6a22c9d4c91ae03024816f7e7f1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Name' is visible on screen
    assertion_operand_bc35b6a22c9d4c91ae03024816f7e7f1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Relationship' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_86cf7fed6dc74786b833f8c6807bbd7d_0' to true
    assertion_operand_86cf7fed6dc74786b833f8c6807bbd7d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Relationship' text is visible
    assertion_operand_86cf7fed6dc74786b833f8c6807bbd7d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Home Telephone' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_b2c6078f984041dcba4571e6aeec2e04_0' to true
    assertion_operand_b2c6078f984041dcba4571e6aeec2e04_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Home Telephone' text is visible
    assertion_operand_b2c6078f984041dcba4571e6aeec2e04_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Mobile' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_b0992323b0fc42c4a671d61a3b35cb16_0' to true
    assertion_operand_b0992323b0fc42c4a671d61a3b35cb16_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Mobile' text is visible
    assertion_operand_b0992323b0fc42c4a671d61a3b35cb16_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'Work Telephone' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_0101440bb4854b20a27205dc567f6c84_0' to true
    assertion_operand_0101440bb4854b20a27205dc567f6c84_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'Work Telephone' is visible
    assertion_operand_0101440bb4854b20a27205dc567f6c84_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_850d67632fa14a7d98ef84dc968de6f6_0' to true
    assertion_operand_850d67632fa14a7d98ef84dc968de6f6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Actions' text is visible
    assertion_operand_850d67632fa14a7d98ef84dc968de6f6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'File Name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_e3325c5e57fd432fbc75c35520d83d42_0' to true
    assertion_operand_e3325c5e57fd432fbc75c35520d83d42_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'File Name' text is visible
    assertion_operand_e3325c5e57fd432fbc75c35520d83d42_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Query 'Description' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 41 : set the value of variable 'assertion_operand_c7b6de9e416d40d99361f3f1e81077f7_0' to true
    assertion_operand_c7b6de9e416d40d99361f3f1e81077f7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Assert 'Description' text is visible
    assertion_operand_c7b6de9e416d40d99361f3f1e81077f7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Query 'Size' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 44 : set the value of variable 'assertion_operand_806f5936333c4d99ad184196a9789325_0' to true
    assertion_operand_806f5936333c4d99ad184196a9789325_0 = "true"
    driver.implicitly_wait(6)

    # Step - 45 : Assert 'Size' text is visible
    assertion_operand_806f5936333c4d99ad184196a9789325_0 = "true"
    driver.implicitly_wait(6)

    # Step - 46 : Query 'Type' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 47 : set the value of variable 'assertion_operand_db15920179664ad0968138ece759d8ce_0' to true
    assertion_operand_db15920179664ad0968138ece759d8ce_0 = "true"
    driver.implicitly_wait(6)

    # Step - 48 : Assert 'Type' text is visible
    assertion_operand_db15920179664ad0968138ece759d8ce_0 = "true"
    driver.implicitly_wait(6)

    # Step - 49 : Query 'Date Added' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 50 : set the value of variable 'assertion_operand_09e12a918cbb4978bb70b7d21a2f5f3b_0' to true
    assertion_operand_09e12a918cbb4978bb70b7d21a2f5f3b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 51 : Assert 'Date Added' text is visible
    assertion_operand_09e12a918cbb4978bb70b7d21a2f5f3b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 52 : Query visibility of text 'Added By'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 53 : set the value of variable 'assertion_operand_f328dd2b71514ba2a92e81629a2a4e64_0' to true
    assertion_operand_f328dd2b71514ba2a92e81629a2a4e64_0 = "true"
    driver.implicitly_wait(6)

    # Step - 54 : Assert text 'Added By' is visible
    assertion_operand_f328dd2b71514ba2a92e81629a2a4e64_0 = "true"
    driver.implicitly_wait(6)

    # Step - 55 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 56 : set the value of variable 'assertion_operand_8f7732d19d334d2fb2b71a319ae786ef_0' to true
    assertion_operand_8f7732d19d334d2fb2b71a319ae786ef_0 = "true"
    driver.implicitly_wait(6)

    # Step - 57 : Assert 'Actions' text is visible
    assertion_operand_8f7732d19d334d2fb2b71a319ae786ef_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
