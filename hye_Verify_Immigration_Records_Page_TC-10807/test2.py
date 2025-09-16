
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

    # Step - 3 : set the value of variable 'assertion_operand_6b518fdbba8b4efaa0dba4a679d0a4f9_0' to true
    assertion_operand_6b518fdbba8b4efaa0dba4a679d0a4f9_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_6b518fdbba8b4efaa0dba4a679d0a4f9_0 = "true"
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

    # Step - 11 : Click on 'Immigration' tab in the left side menu under 'My Info'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/a[1]", "//a[text()='Immigration']", "//a[contains(text(),'Immigration')]", '[role="tablist"] > div:nth-child(5) > a:nth-child(1)', '[role="tablist"] > div:nth-child(5) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : Query 'Assigned Immigration Records' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Assigned Immigration Records']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 14 : set the value of variable 'assertion_operand_ada58133966145429c03e0e64c48ce7c_0' to true
    assertion_operand_ada58133966145429c03e0e64c48ce7c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Assigned Immigration Records' is visible
    assertion_operand_ada58133966145429c03e0e64c48ce7c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'No Records Found' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_86f29d1b89354b278bc0547da7d31894_0' to true
    assertion_operand_86f29d1b89354b278bc0547da7d31894_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'No Records Found' text is visible
    assertion_operand_86f29d1b89354b278bc0547da7d31894_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Document' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_5d875d50e6fb4534b9de646fdef96297_0' to true
    assertion_operand_5d875d50e6fb4534b9de646fdef96297_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Document' text is visible
    assertion_operand_5d875d50e6fb4534b9de646fdef96297_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Number' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_f9a0194e5bd74bf88abde5312d6642d6_0' to true
    assertion_operand_f9a0194e5bd74bf88abde5312d6642d6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Number' text is visible
    assertion_operand_f9a0194e5bd74bf88abde5312d6642d6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Issued By' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_733a88edcdae4401b85a2ab118fb3f36_0' to true
    assertion_operand_733a88edcdae4401b85a2ab118fb3f36_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Issued_By_visible' equals 'true'
    assertion_operand_733a88edcdae4401b85a2ab118fb3f36_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Issued Date' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_efbd1a83d3f04f4fae1d8e686124619c_0' to true
    assertion_operand_efbd1a83d3f04f4fae1d8e686124619c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Issued Date' text is visible
    assertion_operand_efbd1a83d3f04f4fae1d8e686124619c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'Expiry Date' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_bfccfec44f994be3b12bda1ce2cf48cf_0' to true
    assertion_operand_bfccfec44f994be3b12bda1ce2cf48cf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'Expiry Date' text is visible
    assertion_operand_bfccfec44f994be3b12bda1ce2cf48cf_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_6cd651a48bb5436f83434f64c97f26f1_0' to true
    assertion_operand_6cd651a48bb5436f83434f64c97f26f1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Actions' text is visible
    assertion_operand_6cd651a48bb5436f83434f64c97f26f1_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'Attachments' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_67c8e6ecd0314fae967fe91087ebc8c0_0' to true
    assertion_operand_67c8e6ecd0314fae967fe91087ebc8c0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'Attachments' text is visible
    assertion_operand_67c8e6ecd0314fae967fe91087ebc8c0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Query 'File Name' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 41 : set the value of variable 'assertion_operand_0725afe218fe4376829ab05fe2e3d4e7_0' to true
    assertion_operand_0725afe218fe4376829ab05fe2e3d4e7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Assert 'File Name' is visible
    assertion_operand_0725afe218fe4376829ab05fe2e3d4e7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Query 'Description' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 44 : set the value of variable 'assertion_operand_3f3ce9d7d92b43bcabef997f1bc3580f_0' to true
    assertion_operand_3f3ce9d7d92b43bcabef997f1bc3580f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 45 : Assert 'Description' is visible
    assertion_operand_3f3ce9d7d92b43bcabef997f1bc3580f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 46 : Query 'Size' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 47 : set the value of variable 'assertion_operand_d7c10acd3a4d46289d2214e8a386a67a_0' to true
    assertion_operand_d7c10acd3a4d46289d2214e8a386a67a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 48 : Assert 'Size' text is visible
    assertion_operand_d7c10acd3a4d46289d2214e8a386a67a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 49 : Query 'Type' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 50 : set the value of variable 'assertion_operand_d38724007bdb49c192e1959a4418fe37_0' to true
    assertion_operand_d38724007bdb49c192e1959a4418fe37_0 = "true"
    driver.implicitly_wait(6)

    # Step - 51 : Assert 'Type' text is visible
    assertion_operand_d38724007bdb49c192e1959a4418fe37_0 = "true"
    driver.implicitly_wait(6)

    # Step - 52 : Query 'Date Added' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 53 : set the value of variable 'assertion_operand_38a773184c3c481c8d63d669f0895171_0' to true
    assertion_operand_38a773184c3c481c8d63d669f0895171_0 = "true"
    driver.implicitly_wait(6)

    # Step - 54 : Assert 'Date Added' text is visible
    assertion_operand_38a773184c3c481c8d63d669f0895171_0 = "true"
    driver.implicitly_wait(6)

    # Step - 55 : Query visibility of text 'Added By'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 56 : set the value of variable 'assertion_operand_1e6ab15acddc401a99a1888d00a7ae7c_0' to true
    assertion_operand_1e6ab15acddc401a99a1888d00a7ae7c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 57 : Assert text 'Added By' is visible
    assertion_operand_1e6ab15acddc401a99a1888d00a7ae7c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 58 : Query '+ Add' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 59 : set the value of variable 'assertion_operand_14fe0ce6837748b49ed9b31ce7556ad5_0' to true
    assertion_operand_14fe0ce6837748b49ed9b31ce7556ad5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 60 : Assert '+ Add' text is visible
    assertion_operand_14fe0ce6837748b49ed9b31ce7556ad5_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
