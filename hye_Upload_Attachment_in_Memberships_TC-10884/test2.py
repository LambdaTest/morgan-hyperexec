
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

    # Step - 3 : set the value of variable 'assertion_operand_4f2fe1d3fd664e159bab9b68912cb91d_0' to true
    assertion_operand_4f2fe1d3fd664e159bab9b68912cb91d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_4f2fe1d3fd664e159bab9b68912cb91d_0 = "true"
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

    # Step - 11 : Click on 'Memberships' tab in the left side menu
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

    # Step - 13 : Click on Add button in Attachments section
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/button[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : Query 'Add Attachment' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > h6:nth-child(1)', "//h6[text()='Add Attachment']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 15 : set the value of variable 'assertion_operand_bca2da26428b45cbb65bfc85902d452e_0' to true
    assertion_operand_bca2da26428b45cbb65bfc85902d452e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Assert 'Add Attachment' text is visible
    assertion_operand_bca2da26428b45cbb65bfc85902d452e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 17 : Query 'Select File' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Select File']", "//label[contains(text(),'Select File')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_1e5c0c4f1ce44e37b91cf63406a22ab9_0' to true
    assertion_operand_1e5c0c4f1ce44e37b91cf63406a22ab9_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'Select File' text is visible
    assertion_operand_1e5c0c4f1ce44e37b91cf63406a22ab9_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Query 'Browse' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 21 : set the value of variable 'assertion_operand_8704191c30074d72bff5e0dc95912bd7_0' to true
    assertion_operand_8704191c30074d72bff5e0dc95912bd7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Assert 'Browse' text is visible
    assertion_operand_8704191c30074d72bff5e0dc95912bd7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Query 'No File Selected' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)', "//div[text()='No file selected']", "//div[contains(text(),'No file selected')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 24 : set the value of variable 'assertion_operand_544f64db6d614d87b5aead14c2d0457b_0' to true
    assertion_operand_544f64db6d614d87b5aead14c2d0457b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Assert 'No File Selected' text is visible
    assertion_operand_544f64db6d614d87b5aead14c2d0457b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Query visibility of text 'Accepts up to 1 MB'
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/form[1]/div[1]/div[1]/div[1]/p[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(2)', "//p[text()='Accepts up to 1MB']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 27 : set the value of variable 'assertion_operand_c97a7ec1c3b24b9e9a0f9635d3db7360_0' to true
    assertion_operand_c97a7ec1c3b24b9e9a0f9635d3db7360_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Assert text 'Accepts up to 1 MB' is visible
    assertion_operand_c97a7ec1c3b24b9e9a0f9635d3db7360_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Query 'Comment' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > form:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Comment']", "//label[contains(text(),'Comment')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 30 : set the value of variable 'assertion_operand_23880d51692b4ede99afcec8ac6b0b2d_0' to true
    assertion_operand_23880d51692b4ede99afcec8ac6b0b2d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Assert 'Comment' text is visible
    assertion_operand_23880d51692b4ede99afcec8ac6b0b2d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Query 'Type comment here' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 33 : set the value of variable 'assertion_operand_042cb93b89b64e24b7bff0d0be2f2af5_0' to true
    assertion_operand_042cb93b89b64e24b7bff0d0be2f2af5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Assert 'Type comment here' is visible
    assertion_operand_042cb93b89b64e24b7bff0d0be2f2af5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Query 'Cancel' text visibility
    element_locators = ['.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ .oxd-button--secondary)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/form[1]/div[3]/button[1]", 'button:has(+ .oxd-button--medium.oxd-button--secondary)', "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 36 : set the value of variable 'assertion_operand_cded5f4aef40489cae8ec4a91fd567e0_0' to true
    assertion_operand_cded5f4aef40489cae8ec4a91fd567e0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Assert 'Cancel' text is visible
    assertion_operand_cded5f4aef40489cae8ec4a91fd567e0_0 = "true"
    driver.implicitly_wait(6)

    # Step - 38 : Query 'Save' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 39 : set the value of variable 'assertion_operand_2ed50cc894234316be818751ecf89db6_0' to true
    assertion_operand_2ed50cc894234316be818751ecf89db6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Assert 'Save' text is visible
    assertion_operand_2ed50cc894234316be818751ecf89db6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 41 : Upload file from variable 'FILE_Screenshot_2025_09_12_at_7_19_03_E2_80_AFPM_png'
    element_locators = ['/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]']
    element = get_element(driver,element_locators)

    file_name = "Screenshot+2025-09-12+at+7.19.03%E2%80%AFPM.png"
    element.send_keys(str(Path(os.path.join(os.environ["USERPROFILE"], "Downloads") if os.name == "nt" else os.path.expanduser("~/Downloads")) / file_name))
    driver.implicitly_wait(6)

    # Step - 42 : Click 'Cancel' button
    element_locators = ['.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ .oxd-button--secondary)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/form[1]/div[3]/button[1]", 'button:has(+ .oxd-button--medium.oxd-button--secondary)', "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 43 : Query 'No Records Found' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 44 : set the value of variable 'assertion_operand_c49ebc80402d4af5861ee89071fa34e6_0' to true
    assertion_operand_c49ebc80402d4af5861ee89071fa34e6_0 = "true"
    driver.implicitly_wait(6)

    # Step - 45 : Assert 'No Records Found' text is visible
    assertion_operand_c49ebc80402d4af5861ee89071fa34e6_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
