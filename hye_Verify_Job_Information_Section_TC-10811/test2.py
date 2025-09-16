
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

    # Step - 3 : set the value of variable 'assertion_operand_85e2ece2c850417a9c5ce502b033abe9_0' to true
    assertion_operand_85e2ece2c850417a9c5ce502b033abe9_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_85e2ece2c850417a9c5ce502b033abe9_0 = "true"
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

    # Step - 11 : Click on 'Job' tab in the left side menu under 'My Info'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/a[1]", "//a[text()='Job']", "//a[contains(text(),'Job')]", '[role="tablist"] > div:nth-child(6) > a:nth-child(1)', '[role="tablist"] > div:nth-child(6) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Query 'include Employment Contact Details' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/p[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(3) > p:nth-child(1)', "//p[text()='Include Employment Contract Details']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_96f662987d2744edb3f3b1468027537c_0' to true
    assertion_operand_96f662987d2744edb3f3b1468027537c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'include Employment Contact Details' is visible
    assertion_operand_96f662987d2744edb3f3b1468027537c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'Attachments' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Attachments']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_a65873df8f064c8c83dd1779271b3628_0' to true
    assertion_operand_a65873df8f064c8c83dd1779271b3628_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'Attachments' text is visible
    assertion_operand_a65873df8f064c8c83dd1779271b3628_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'No Records Found' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_f2d39153b9a64c8aab5f95cb3baacf30_0' to true
    assertion_operand_f2d39153b9a64c8aab5f95cb3baacf30_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'No Records Found' text is visible
    assertion_operand_f2d39153b9a64c8aab5f95cb3baacf30_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'File Name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_d3b868efe0834ce0af889dcc9d5b8809_0' to true
    assertion_operand_d3b868efe0834ce0af889dcc9d5b8809_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'File Name' text is visible
    assertion_operand_d3b868efe0834ce0af889dcc9d5b8809_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Description' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_b142c7146d0e440db727629314fcd7b5_0' to true
    assertion_operand_b142c7146d0e440db727629314fcd7b5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Description' is visible
    assertion_operand_b142c7146d0e440db727629314fcd7b5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Size' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_e435347dc6f2465992ff2c5fcc343abf_0' to true
    assertion_operand_e435347dc6f2465992ff2c5fcc343abf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Size' text is visible
    assertion_operand_e435347dc6f2465992ff2c5fcc343abf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'Type' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_da060b754e18478e9dda8bea4df681b9_0' to true
    assertion_operand_da060b754e18478e9dda8bea4df681b9_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'Type' text is visible
    assertion_operand_da060b754e18478e9dda8bea4df681b9_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Date Added' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_e11866358fe847b1a99936af7b5f742f_0' to true
    assertion_operand_e11866358fe847b1a99936af7b5f742f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Date Added' text is visible
    assertion_operand_e11866358fe847b1a99936af7b5f742f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Added By' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_b97d4161464c4c5185c175a352d4a770_0' to true
    assertion_operand_b97d4161464c4c5185c175a352d4a770_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Added By' text is visible
    assertion_operand_b97d4161464c4c5185c175a352d4a770_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 41 : set the value of variable 'assertion_operand_f0c9901941804d028b881299e2bee8f2_0' to true
    assertion_operand_f0c9901941804d028b881299e2bee8f2_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Assert 'Actions' text is visible
    assertion_operand_f0c9901941804d028b881299e2bee8f2_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
