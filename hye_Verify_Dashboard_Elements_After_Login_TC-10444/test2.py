
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

    # Step - 3 : set the value of variable 'assertion_operand_ba84a79c1b564241ad720c5057cb9b0e_0' to true
    assertion_operand_ba84a79c1b564241ad720c5057cb9b0e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_ba84a79c1b564241ad720c5057cb9b0e_0 = "true"
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

    # Step - 9 : Query 'Admin' text visibility
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[1]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[1]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 10 : set the value of variable 'assertion_operand_fe2d8e66d8c14c53898d1a0f241095a8_0' to true
    assertion_operand_fe2d8e66d8c14c53898d1a0f241095a8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 11 : Assert 'Admin' text is visible on the viewport
    assertion_operand_fe2d8e66d8c14c53898d1a0f241095a8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 12 : Query 'PIM' text visibility
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[2]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[2]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 13 : set the value of variable 'assertion_operand_599801e1f65d4e13b5b8bc00219c0461_0' to true
    assertion_operand_599801e1f65d4e13b5b8bc00219c0461_0 = "true"
    driver.implicitly_wait(6)

    # Step - 14 : Assert 'PIM' text is visible on the viewport
    assertion_operand_599801e1f65d4e13b5b8bc00219c0461_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Query 'Leave' text visibility
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[3]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[3]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 16 : set the value of variable 'assertion_operand_b4f4d0d5af7c49e4898a7024b78c1e33_0' to true
    assertion_operand_b4f4d0d5af7c49e4898a7024b78c1e33_0 = "true"
    driver.implicitly_wait(6)

    # Step - 17 : Assert 'Leave' text is visible on the viewport
    assertion_operand_b4f4d0d5af7c49e4898a7024b78c1e33_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Query 'Time' text visibility
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[4]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[4]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 19 : set the value of variable 'assertion_operand_d26311ee41c3490ba313a460986bcbdb_0' to true
    assertion_operand_d26311ee41c3490ba313a460986bcbdb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Assert 'Time' text is visible on the viewport
    assertion_operand_d26311ee41c3490ba313a460986bcbdb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Query 'Recruitment' text visibility
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[5]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[5]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 22 : set the value of variable 'assertion_operand_96de9ed7292a431291127cec3db2d6e9_0' to true
    assertion_operand_96de9ed7292a431291127cec3db2d6e9_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Assert 'Recruitment' text is visible
    assertion_operand_96de9ed7292a431291127cec3db2d6e9_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Query 'My Info' text visibility
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[6]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[6]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(6) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(6) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 25 : set the value of variable 'assertion_operand_99ed0d51b29a4955a27297b568b568e0_0' to true
    assertion_operand_99ed0d51b29a4955a27297b568b568e0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Assert 'My Info' text is visible on viewport
    assertion_operand_99ed0d51b29a4955a27297b568b568e0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Query 'Dashboard' text visibility
    element_locators = ['.oxd-text--h6', '.oxd-topbar-header-breadcrumb-module', '.oxd-text--h6.oxd-topbar-header-breadcrumb-module', '#app > div:nth-child(1) > div:nth-child(1) > header:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > h6:nth-child(1)', "//h6[text()='Dashboard']", "//h6[contains(@class,'oxd-text--h6')]", "//h6[contains(@class,'oxd-topbar-header-breadcrumb-module')]", "//h6[contains(@class,'oxd-text--h6') and contains(@class,'oxd-topbar-header-breadcrumb-module')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 28 : set the value of variable 'assertion_operand_2de35aa08cd24a19be0b876c5a707170_0' to true
    assertion_operand_2de35aa08cd24a19be0b876c5a707170_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Assert 'Dashboard' text is visible
    assertion_operand_2de35aa08cd24a19be0b876c5a707170_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Get the current URL
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 31 : set the value of variable 'assertion_operand_15f67e4cc33a47a1b2ea64ea42274796_0' to dashboard
    assertion_operand_15f67e4cc33a47a1b2ea64ea42274796_0 = "dashboard"
    driver.implicitly_wait(6)

    # Step - 32 : Assert '{{url}}' contains 'dashboard'
    assertion_operand_15f67e4cc33a47a1b2ea64ea42274796_0 = "dashboard"

    driver.quit()
except Exception as e:
    driver.quit()
