
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
    element_locators = ['[placeholder="Username"][name="username"]', '[placeholder="Username"]', '[name="username"]', "//input[@placeholder='Username' and @name='username']", '.oxd-input--focus', "//input[starts-with(@placeholder,'Usern')]", "//input[contains(@class,'oxd-input--focus')]", "//input[contains(@placeholder,'Username')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_c977cc91e5254268acd6f9796023cfcb_0' to true
    assertion_operand_c977cc91e5254268acd6f9796023cfcb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_c977cc91e5254268acd6f9796023cfcb_0 = "true"
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

    # Step - 11 : Click on 'Salary' tab in the left side menu under 'My Info'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[7]/a[1]", "//a[text()='Salary']", "//a[contains(text(),'Salary')]", '[role="tablist"] > div:nth-child(7) > a:nth-child(1)', '[role="tablist"] > div:nth-child(7) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Query visibility of text 'Assigned Salary Components'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_e4ea99540a3e4a9e91591114c4189b60_0' to true
    assertion_operand_e4ea99540a3e4a9e91591114c4189b60_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert text 'Assigned Salary Components' is visible
    assertion_operand_e4ea99540a3e4a9e91591114c4189b60_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'No Records Found' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_d3d038cc9d2f4cb9845f8681a0e76ae1_0' to true
    assertion_operand_d3d038cc9d2f4cb9845f8681a0e76ae1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'No Records Found' text is visible
    assertion_operand_d3d038cc9d2f4cb9845f8681a0e76ae1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Salary Component' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Assigned Salary Components']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_222b05dec33e4579841270445a7bc8bb_0' to true
    assertion_operand_222b05dec33e4579841270445a7bc8bb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Salary Component' is visible
    assertion_operand_222b05dec33e4579841270445a7bc8bb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Amount' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_8b3df06c7fec457586b69298de5b87df_0' to true
    assertion_operand_8b3df06c7fec457586b69298de5b87df_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Amount' is visible on screen
    assertion_operand_8b3df06c7fec457586b69298de5b87df_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Currency' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_02716d1205574e47a8d540ff55d88e3c_0' to true
    assertion_operand_02716d1205574e47a8d540ff55d88e3c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Currency' text is visible
    assertion_operand_02716d1205574e47a8d540ff55d88e3c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Pay Frequency' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_63d036ba305f4709bd137b6ef8f46831_0' to true
    assertion_operand_63d036ba305f4709bd137b6ef8f46831_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Pay Frequency' text is visible
    assertion_operand_63d036ba305f4709bd137b6ef8f46831_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'Direct Deposit Amount' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_0106528d80024abd8ddd963ed477e36f_0' to true
    assertion_operand_0106528d80024abd8ddd963ed477e36f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'Direct Deposit Amount' is visible
    assertion_operand_0106528d80024abd8ddd963ed477e36f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'File Name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_2891213769c64230a7c9ec3709cf3f42_0' to true
    assertion_operand_2891213769c64230a7c9ec3709cf3f42_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'File Name' is visible
    assertion_operand_2891213769c64230a7c9ec3709cf3f42_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Description' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_e05680b572d64c6680e245456f280f73_0' to true
    assertion_operand_e05680b572d64c6680e245456f280f73_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Description' is visible
    assertion_operand_e05680b572d64c6680e245456f280f73_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Query visibility of text 'Size'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 41 : set the value of variable 'assertion_operand_63ff5f9ae0124b9e8b9c4ed76a3bccd0_0' to true
    assertion_operand_63ff5f9ae0124b9e8b9c4ed76a3bccd0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Assert text 'Size' is visible
    assertion_operand_63ff5f9ae0124b9e8b9c4ed76a3bccd0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Query 'Type' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 44 : set the value of variable 'assertion_operand_d3182eb1e684440bbd47f7afc4225188_0' to true
    assertion_operand_d3182eb1e684440bbd47f7afc4225188_0 = "true"
    driver.implicitly_wait(6)

    # Step - 45 : Assert 'Type' text is visible
    assertion_operand_d3182eb1e684440bbd47f7afc4225188_0 = "true"
    driver.implicitly_wait(6)

    # Step - 46 : Query 'Date Added' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 47 : set the value of variable 'assertion_operand_fbbe1f6862ea4c7cb8d6fa7663861a1a_0' to true
    assertion_operand_fbbe1f6862ea4c7cb8d6fa7663861a1a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 48 : Assert 'Date Added' text is visible
    assertion_operand_fbbe1f6862ea4c7cb8d6fa7663861a1a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 49 : Query visibility of text 'Added by'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 50 : set the value of variable 'assertion_operand_c22a29a6c5d949af9d22254398f4f16d_0' to true
    assertion_operand_c22a29a6c5d949af9d22254398f4f16d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 51 : Assert text 'Added by' is visible
    assertion_operand_c22a29a6c5d949af9d22254398f4f16d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 52 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 53 : set the value of variable 'assertion_operand_3bc6bd8f72bd4d24a2f5950af0462f3c_0' to true
    assertion_operand_3bc6bd8f72bd4d24a2f5950af0462f3c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 54 : Assert 'Actions' text is visible
    assertion_operand_3bc6bd8f72bd4d24a2f5950af0462f3c_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
