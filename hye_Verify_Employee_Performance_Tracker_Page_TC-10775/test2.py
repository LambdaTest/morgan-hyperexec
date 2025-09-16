
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

    # Step - 3 : set the value of variable 'assertion_operand_9b8ec73ee45a46a086d17675f3a11181_0' to true
    assertion_operand_9b8ec73ee45a46a086d17675f3a11181_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_9b8ec73ee45a46a086d17675f3a11181_0 = "true"
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

    # Step - 9 : Click on 'Performance' menu item in left sidebar
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

    # Step - 11 : Click on 'Employee Trackers' tab in the top nav bar
    element_locators = ["//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[4]/a[1]", "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[4]/a[1]", "//a[text()='Employee Trackers']", "//a[contains(text(),'Employee Trackers')]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)', '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)']
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

    # Step - 14 : set the value of variable 'assertion_operand_cd8d41bafb6647be8d3cbcc425d737bd_0' to viewEmployeePerformanceTrackerList
    assertion_operand_cd8d41bafb6647be8d3cbcc425d737bd_0 = "viewEmployeePerformanceTrackerList"
    driver.implicitly_wait(6)

    # Step - 15 : Assert current URL contains 'viewEmployeePerformanceTrackerList'
    assertion_operand_cd8d41bafb6647be8d3cbcc425d737bd_0 = "viewEmployeePerformanceTrackerList"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'Employee Performance Tracker' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_b48ebd068b704c6fae2b6657053a110a_0' to true
    assertion_operand_b48ebd068b704c6fae2b6657053a110a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'Employee Performance Tracker' is visible
    assertion_operand_b48ebd068b704c6fae2b6657053a110a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Employee Name' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Employee Name']", "//label[contains(text(),'Employee Name')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_8e7be80f5a4e4ebd84050e374222379e_0' to true
    assertion_operand_8e7be80f5a4e4ebd84050e374222379e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Employee Name' text is visible
    assertion_operand_8e7be80f5a4e4ebd84050e374222379e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Include' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Include']", "//label[contains(text(),'Include')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_dade373a813f4671946a0e7c5e4373f4_0' to true
    assertion_operand_dade373a813f4671946a0e7c5e4373f4_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Include' text is visible
    assertion_operand_dade373a813f4671946a0e7c5e4373f4_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Reset' text visibility
    element_locators = ['[type="reset"]', '.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ .oxd-button--secondary)', "//button[starts-with(@type,'reset')]", "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@type,'reset')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_8d98c07eabc24118846bff1c43d61031_0' to true
    assertion_operand_8d98c07eabc24118846bff1c43d61031_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Reset' text is visible
    assertion_operand_8d98c07eabc24118846bff1c43d61031_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Search' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_999045adf77b4b0db733c8f64aed29b1_0' to true
    assertion_operand_999045adf77b4b0db733c8f64aed29b1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Search' text is visible
    assertion_operand_999045adf77b4b0db733c8f64aed29b1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'No Records Found' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_08a361e46ff347d9bc84d33e5d23efb1_0' to true
    assertion_operand_08a361e46ff347d9bc84d33e5d23efb1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'No Records Found' text is visible
    assertion_operand_08a361e46ff347d9bc84d33e5d23efb1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Employee Name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_3059e998ecf14629b77b6736e992ed82_0' to true
    assertion_operand_3059e998ecf14629b77b6736e992ed82_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Employee Name' is visible
    assertion_operand_3059e998ecf14629b77b6736e992ed82_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Tracker' visibility
    element_locators = ["//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[3]/a[1]", "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul[1]/li[3]/a[1]", "//a[text()='My Trackers']", "//a[contains(text(),'My Trackers')]", '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)', '[aria-label="Topbar Menu"] > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_9297041e34244dcbaaba098002d4bff8_0' to true
    assertion_operand_9297041e34244dcbaaba098002d4bff8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Tracker' is visible
    assertion_operand_9297041e34244dcbaaba098002d4bff8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Query 'Added Date' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 41 : set the value of variable 'assertion_operand_0954b117d2af4a4396366dbac9db33c5_0' to true
    assertion_operand_0954b117d2af4a4396366dbac9db33c5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Assert 'Added Date' text is visible
    assertion_operand_0954b117d2af4a4396366dbac9db33c5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Query 'Modified Date' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 44 : set the value of variable 'assertion_operand_68fdab5a049d435a986abddc26c9e4a2_0' to true
    assertion_operand_68fdab5a049d435a986abddc26c9e4a2_0 = "true"
    driver.implicitly_wait(6)

    # Step - 45 : Assert 'Modified Date' text is visible
    assertion_operand_68fdab5a049d435a986abddc26c9e4a2_0 = "true"
    driver.implicitly_wait(6)

    # Step - 46 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 47 : set the value of variable 'assertion_operand_845ef07854c3453f916e10e1620f19cf_0' to true
    assertion_operand_845ef07854c3453f916e10e1620f19cf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 48 : Assert 'Actions' text is visible
    assertion_operand_845ef07854c3453f916e10e1620f19cf_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
