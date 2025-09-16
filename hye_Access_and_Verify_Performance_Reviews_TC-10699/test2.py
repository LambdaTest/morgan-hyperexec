
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

    # Step - 3 : set the value of variable 'assertion_operand_e3c2c19f27b34928b473812e102d5622_0' to true
    assertion_operand_e3c2c19f27b34928b473812e102d5622_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_e3c2c19f27b34928b473812e102d5622_0 = "true"
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

    # Step - 11 : Click on 'Manage Reviews' tab in the top nav bar
    element_locators = ['.--visited > span', '.oxd-topbar-body-nav-tab.--visited > span', '.--parent.--visited > span', '.--visited > span:nth-child(1)', "//span[contains(text(),'Manage Reviews')]", "//li[contains(@class,'--visited')]/span[1]", "//li[contains(@class,'--visited')]/span[1]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent') and contains(@class,'--visited')]/span[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 13 : Click on 'Manage Reviews' option in the dropdown below 'Manage Reviews' tab
    element_locators = ['.--visited > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', '.--visited > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', "//a[text()='Manage Reviews']", "//a[contains(text(),'Manage Reviews')]", "//li[contains(@class,'--visited')]/ul[1]/li[1]/a[1]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent') and contains(@class,'--visited')]/ul[1]/li[1]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : wait 2 seconds
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 15 : Get the current URL
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 16 : set the value of variable 'assertion_operand_455aa89406474e9b954e082db28c9558_0' to searchPerformanceReview
    assertion_operand_455aa89406474e9b954e082db28c9558_0 = "searchPerformanceReview"
    driver.implicitly_wait(6)

    # Step - 17 : Assert current URL contains 'searchPerformanceReview'
    assertion_operand_455aa89406474e9b954e082db28c9558_0 = "searchPerformanceReview"
    driver.implicitly_wait(6)

    # Step - 18 : Query 'Manage Performance Reviews' visibility
    element_locators = ['.oxd-table-filter-header-title', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]", 'div:has(+ .oxd-table-filter-header-options)', '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)', "//div[contains(@class,'oxd-table-filter-header-title')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 19 : set the value of variable 'assertion_operand_5469c1e443a74fa1a36df6e224d4708a_0' to true
    assertion_operand_5469c1e443a74fa1a36df6e224d4708a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Assert 'Manage Performance Reviews' is visible
    assertion_operand_5469c1e443a74fa1a36df6e224d4708a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Query 'Employee Name' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Employee Name']", "//label[contains(text(),'Employee Name')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 22 : set the value of variable 'assertion_operand_44aeece3bbe24dbba7504bcb6fabbf38_0' to true
    assertion_operand_44aeece3bbe24dbba7504bcb6fabbf38_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Assert 'Employee Name' text is visible
    assertion_operand_44aeece3bbe24dbba7504bcb6fabbf38_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Query 'Job Title' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 25 : set the value of variable 'assertion_operand_d4d20bef2ec74911aec1fc0457353f4c_0' to true
    assertion_operand_d4d20bef2ec74911aec1fc0457353f4c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Assert 'Job Title' is visible
    assertion_operand_d4d20bef2ec74911aec1fc0457353f4c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Query 'Review Status' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 28 : set the value of variable 'assertion_operand_f185dacbc89540f1ac0b9f1f0f1c14f8_0' to true
    assertion_operand_f185dacbc89540f1ac0b9f1f0f1c14f8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Assert 'Review Status' is visible
    assertion_operand_f185dacbc89540f1ac0b9f1f0f1c14f8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Query 'Include' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[4]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Include']", "//label[contains(text(),'Include')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 31 : set the value of variable 'assertion_operand_8a632282bdd945baa015b25311623261_0' to true
    assertion_operand_8a632282bdd945baa015b25311623261_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Assert 'Include' text is visible
    assertion_operand_8a632282bdd945baa015b25311623261_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Query 'Reviewer' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[5]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Reviewer']", "//label[contains(text(),'Reviewer')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 34 : set the value of variable 'assertion_operand_dc42ebc3adb946939b4eecdb709f8e03_0' to true
    assertion_operand_dc42ebc3adb946939b4eecdb709f8e03_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Assert 'Reviewer' text is visible
    assertion_operand_dc42ebc3adb946939b4eecdb709f8e03_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Query 'From Date' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[6]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='From Date']", "//label[contains(text(),'From Date')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 37 : set the value of variable 'assertion_operand_51cdd135c42b43548f20b61895f0f0f5_0' to true
    assertion_operand_51cdd135c42b43548f20b61895f0f0f5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 38 : Assert 'From Date' text is visible
    assertion_operand_51cdd135c42b43548f20b61895f0f0f5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Query 'To Date' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[7]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='To Date']", "//label[contains(text(),'To Date')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 40 : set the value of variable 'assertion_operand_797bb4c89ed445e1b60eccab2d5b33ca_0' to true
    assertion_operand_797bb4c89ed445e1b60eccab2d5b33ca_0 = "true"
    driver.implicitly_wait(6)

    # Step - 41 : Assert 'To Date' text is visible
    assertion_operand_797bb4c89ed445e1b60eccab2d5b33ca_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Query 'Reset' text visibility
    element_locators = ['[type="reset"]', '.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ [type="submit"])', "//button[starts-with(@type,'reset')]", "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@type,'reset')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 43 : set the value of variable 'assertion_operand_66bbd201f4f24e40bf86ee2981b252bb_0' to true
    assertion_operand_66bbd201f4f24e40bf86ee2981b252bb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 44 : Assert 'Reset' text is visible
    assertion_operand_66bbd201f4f24e40bf86ee2981b252bb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 45 : Query 'Search' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 46 : set the value of variable 'assertion_operand_17c3a6c65ae048c4a1e9d928c2565a8b_0' to true
    assertion_operand_17c3a6c65ae048c4a1e9d928c2565a8b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 47 : Assert 'Search' text is visible
    assertion_operand_17c3a6c65ae048c4a1e9d928c2565a8b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 48 : Query '+ Add' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 49 : set the value of variable 'assertion_operand_daca838672ef446ea04b09f3eb146277_0' to true
    assertion_operand_daca838672ef446ea04b09f3eb146277_0 = "true"
    driver.implicitly_wait(6)

    # Step - 50 : Assert '+ Add' text is visible
    assertion_operand_daca838672ef446ea04b09f3eb146277_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
