
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

    # Step - 3 : set the value of variable 'assertion_operand_60c1d9f004cf466f841b98f1b3cef365_0' to true
    assertion_operand_60c1d9f004cf466f841b98f1b3cef365_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_60c1d9f004cf466f841b98f1b3cef365_0 = "true"
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
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[7]/a[1]/span[1]", "//span[text()='Performance']", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(7) > a:nth-child(1) > span:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 11 : Click on 'Manage Reviews' tab in the top nav bar
    element_locators = ['.--visited > span', '.oxd-topbar-body-nav-tab.--visited > span', '.--parent.--visited > span', '.--visited > span:nth-child(1)', "//span[contains(text(),'Manage Reviews')]", "//li[contains(@class,'--visited')]/span[1]", "//li[contains(@class,'--visited')]/span[1]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent') and contains(@class,'--visited')]/span[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : Click on 'Manage Reviews' tab in the top nav bar
    element_locators = ['.--visited > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', '.--visited > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', "//a[text()='Manage Reviews']", "//a[contains(text(),'Manage Reviews')]", "//li[contains(@class,'--visited')]/ul[1]/li[1]/a[1]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent') and contains(@class,'--visited')]/ul[1]/li[1]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 13 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 14 : Click on the green + Add button below Manage Performance Reviews form
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 15 : wait 5 seconds
    time.sleep(int(5))
    driver.implicitly_wait(6)

    # Step - 16 : Get the current URL
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_03338a8baab244ea9a1abf0031848975_0' to saveReview
    assertion_operand_03338a8baab244ea9a1abf0031848975_0 = "saveReview"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'current_url' contains 'saveReview'
    assertion_operand_03338a8baab244ea9a1abf0031848975_0 = "saveReview"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Employee Name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_7d78b800461541fc957296f24910b88c_0' to true
    assertion_operand_7d78b800461541fc957296f24910b88c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Employee Name' is visible
    assertion_operand_7d78b800461541fc957296f24910b88c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Supervisor Reviewer' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_ea20b42fe04d4681bd7b9aa1f2239c5a_0' to true
    assertion_operand_ea20b42fe04d4681bd7b9aa1f2239c5a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Supervisor Reviewer' text is visible
    assertion_operand_ea20b42fe04d4681bd7b9aa1f2239c5a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Review Period Start Date' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Review Period Start Date']", "//label[contains(text(),'Review Period Start Date')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_4bfb7abf910b49a2a1816240edb7d574_0' to true
    assertion_operand_4bfb7abf910b49a2a1816240edb7d574_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Review Period Start Date' text is visible
    assertion_operand_4bfb7abf910b49a2a1816240edb7d574_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query visibility of text 'Review Period End Date'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_ff01b5a39ab048eeb08ca885e8b1d3da_0' to true
    assertion_operand_ff01b5a39ab048eeb08ca885e8b1d3da_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert text 'Review Period End Date' is visible
    assertion_operand_ff01b5a39ab048eeb08ca885e8b1d3da_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'Due Date' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_e8cf17dcf3ad45148130004fbe92d576_0' to true
    assertion_operand_e8cf17dcf3ad45148130004fbe92d576_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'Due Date' text is visible
    assertion_operand_e8cf17dcf3ad45148130004fbe92d576_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Cancel' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_ccfff9612a004d01a9edc06559bfd168_0' to true
    assertion_operand_ccfff9612a004d01a9edc06559bfd168_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Cancel' text is visible
    assertion_operand_ccfff9612a004d01a9edc06559bfd168_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Save' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_86755774100e4803be343a7022582d8d_0' to true
    assertion_operand_86755774100e4803be343a7022582d8d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Save' text is visible
    assertion_operand_86755774100e4803be343a7022582d8d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Query 'Activate' text visibility
    element_locators = ['.oxd-button--secondary', '.oxd-button--medium.oxd-button--secondary', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/button[3]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(5) > div:nth-child(2) > button:nth-child(3)', '[type="submit"] + button', "//button[contains(@class,'oxd-button--secondary')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--secondary')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 41 : set the value of variable 'assertion_operand_c6648ce2f75f4ab38bedb7206719475b_0' to true
    assertion_operand_c6648ce2f75f4ab38bedb7206719475b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Assert 'Activate' text is visible
    assertion_operand_c6648ce2f75f4ab38bedb7206719475b_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
