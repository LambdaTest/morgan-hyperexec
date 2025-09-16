
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

    # Step - 1 : navigate to 'https://orange-hrm.lambdatestinternal.com/orangehrm-5.7' website
    driver.get("https://orange-hrm.lambdatestinternal.com/orangehrm-5.7")
    driver.implicitly_wait(6)

    # Step - 2 : Query 'Username input box' visibility
    element_locators = ['[placeholder="Username"][name="username"]', '[placeholder="Username"]', '[name="username"]', "//input[@placeholder='Username' and @name='username']", '.oxd-input--focus', "//input[starts-with(@placeholder,'Usern')]", "//input[contains(@class,'oxd-input--focus')]", "//input[contains(@placeholder,'Username')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_3f54007c91d54fd681cc9af871577051_0' to true
    assertion_operand_3f54007c91d54fd681cc9af871577051_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible
    assertion_operand_3f54007c91d54fd681cc9af871577051_0 = "true"
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

    # Step - 14 : set the value of variable 'assertion_operand_6b7b361a3da743229426f54db1696bfe_0' to true
    assertion_operand_6b7b361a3da743229426f54db1696bfe_0 = "true"
    driver.implicitly_wait(6)

    # Step - 15 : Assert 'Assigned Emergency Contacts' text is visible
    assertion_operand_6b7b361a3da743229426f54db1696bfe_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Query 'No Records Found' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 17 : set the value of variable 'assertion_operand_0fd4f5571482419da83768c5dd50a6e5_0' to true
    assertion_operand_0fd4f5571482419da83768c5dd50a6e5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 18 : Assert 'No Records Found' text is visible
    assertion_operand_0fd4f5571482419da83768c5dd50a6e5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Query 'Name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 20 : set the value of variable 'assertion_operand_1937299a1fd9496fb873e66781800400_0' to true
    assertion_operand_1937299a1fd9496fb873e66781800400_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Assert 'Name' text is visible
    assertion_operand_1937299a1fd9496fb873e66781800400_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Query 'Relationship' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 23 : set the value of variable 'assertion_operand_fdf51ee359434abc81da413baed220cd_0' to true
    assertion_operand_fdf51ee359434abc81da413baed220cd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Assert 'Relationship' text is visible
    assertion_operand_fdf51ee359434abc81da413baed220cd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Query 'Home Telephone' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 26 : set the value of variable 'assertion_operand_52cded3e9d184d86ae923fe0c6eeaef4_0' to true
    assertion_operand_52cded3e9d184d86ae923fe0c6eeaef4_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Assert 'Home Telephone' is visible
    assertion_operand_52cded3e9d184d86ae923fe0c6eeaef4_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Query 'Mobile' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 29 : set the value of variable 'assertion_operand_c06633847df84e3a9cc6035bbb23765f_0' to true
    assertion_operand_c06633847df84e3a9cc6035bbb23765f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Assert 'Mobile' is visible on screen
    assertion_operand_c06633847df84e3a9cc6035bbb23765f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Query 'Work Telephone' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 32 : set the value of variable 'assertion_operand_c7896cdbe3d947ea84e9076556058a03_0' to true
    assertion_operand_c7896cdbe3d947ea84e9076556058a03_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Assert 'Work Telephone' is visible
    assertion_operand_c7896cdbe3d947ea84e9076556058a03_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 35 : set the value of variable 'assertion_operand_73e29da11ae249b4b4f3cf1cc9f0b939_0' to true
    assertion_operand_73e29da11ae249b4b4f3cf1cc9f0b939_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Assert 'Actions' text is visible
    assertion_operand_73e29da11ae249b4b4f3cf1cc9f0b939_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Query 'File Name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 38 : set the value of variable 'assertion_operand_74103f6f3e664277b258189906c2c8f6_0' to true
    assertion_operand_74103f6f3e664277b258189906c2c8f6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 39 : Assert 'File_Name_visible' equals 'true'
    assertion_operand_74103f6f3e664277b258189906c2c8f6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Query 'Description' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 41 : set the value of variable 'assertion_operand_0f840583910e433d974a0778e072402c_0' to true
    assertion_operand_0f840583910e433d974a0778e072402c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 42 : Assert 'Description' is visible
    assertion_operand_0f840583910e433d974a0778e072402c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Query visibility of text 'Size'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(3)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 44 : set the value of variable 'assertion_operand_f5e48d207cf54422a1a44f21295a9104_0' to true
    assertion_operand_f5e48d207cf54422a1a44f21295a9104_0 = "true"
    driver.implicitly_wait(6)

    # Step - 45 : Assert text 'Size' is visible
    assertion_operand_f5e48d207cf54422a1a44f21295a9104_0 = "true"
    driver.implicitly_wait(6)

    # Step - 46 : Query 'type' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 47 : set the value of variable 'assertion_operand_752b2469e0334154b709796cab51147e_0' to true
    assertion_operand_752b2469e0334154b709796cab51147e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 48 : Assert 'type' text is visible
    assertion_operand_752b2469e0334154b709796cab51147e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 49 : Query visibility of text 'Date Added'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 50 : set the value of variable 'assertion_operand_111cdcd5b8594d08ad95d58543d41379_0' to true
    assertion_operand_111cdcd5b8594d08ad95d58543d41379_0 = "true"
    driver.implicitly_wait(6)

    # Step - 51 : Assert text 'Date Added' is visible
    assertion_operand_111cdcd5b8594d08ad95d58543d41379_0 = "true"
    driver.implicitly_wait(6)

    # Step - 52 : Query visibility of text 'Added By'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 53 : set the value of variable 'assertion_operand_f3ef2e7946e34c5ba1958e6d9e517ff2_0' to true
    assertion_operand_f3ef2e7946e34c5ba1958e6d9e517ff2_0 = "true"
    driver.implicitly_wait(6)

    # Step - 54 : Assert text 'Added By' is visible
    assertion_operand_f3ef2e7946e34c5ba1958e6d9e517ff2_0 = "true"
    driver.implicitly_wait(6)

    # Step - 55 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 56 : set the value of variable 'assertion_operand_a29dafafd8154824a871d6f23e6d6ae9_0' to true
    assertion_operand_a29dafafd8154824a871d6f23e6d6ae9_0 = "true"
    driver.implicitly_wait(6)

    # Step - 57 : Assert 'Actions' text is visible
    assertion_operand_a29dafafd8154824a871d6f23e6d6ae9_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
