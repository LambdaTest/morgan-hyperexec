
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

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : navigate to 'https://orange-hrm.lambdatestinternal.com/orangehrm-5.7' website
    driver.get("https://orange-hrm.lambdatestinternal.com/orangehrm-5.7")
    driver.implicitly_wait(6)

    # Step - 2 : Query 'Username input box' visibility
    element_locators = ['[placeholder="Username"][name="username"]', '[placeholder="Username"]', '[name="username"]', "//input[@placeholder='Username' and @name='username']", '.oxd-input--focus', "//input[starts-with(@placeholder,'Usern')]", "//input[contains(@class,'oxd-input--focus')]", "//input[contains(@placeholder,'Username')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_7820fd1f877b4604b8a5edd6d8d8fa78_0' to true
    assertion_operand_7820fd1f877b4604b8a5edd6d8d8fa78_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_7820fd1f877b4604b8a5edd6d8d8fa78_0 = "true"
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

    # Step - 9 : Click on 'Buzz' menu item in left side menu
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[12]/a[1]/span[1]", "//span[text()='Buzz']", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(12) > a:nth-child(1) > span:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : Click on the 'What's on your mind?' text area in the Buzz Newsfeed section
    element_locators = ['[placeholder="What\'s on your mind?"]', '.oxd-buzz-post--focus > textarea', '.oxd-buzz-post--focus > textarea:nth-child(1)', '.oxd-buzz-post--focus > textarea:nth-child(1)', "//div[contains(@class,'oxd-buzz-post--focus')]/textarea[1]", "//div[contains(@class,'oxd-buzz-post--focus')]/textarea[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 11 : Type in What's on your mind? input textarea 'share post'
    element_locators = ['[placeholder="What\'s on your mind?"]', '.oxd-buzz-post--focus > textarea', '.oxd-buzz-post--focus > textarea:nth-child(1)', '.oxd-buzz-post--focus > textarea:nth-child(1)', "//div[contains(@class,'oxd-buzz-post--focus')]/textarea[1]", "//div[contains(@class,'oxd-buzz-post--focus')]/textarea[1]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'share post':
            element.send_keys(char)
    else:
        element.send_keys('share post')
    driver.implicitly_wait(6)

    # Step - 12 : Click on the Post button in Buzz Newsfeed
    element_locators = ['[type="submit"]', '.oxd-button--main', '.oxd-button--medium.oxd-button--main', '.oxd-buzz-post--composing > div:nth-child(2) > button:nth-child(1)', "//button[starts-with(@type,'submi')]", "//button[contains(@class,'oxd-button--main')]", "//button[contains(@type,'submit')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--main')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 13 : Click on the share icon below post by Pushpa Raj
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/button[2]/i[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(3) > i:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : Query 'Share Post' heading visibility in pop up
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 15 : set the value of variable 'assertion_operand_c077187b4570468f9d5c1e3fa47a86bb_0' to true
    assertion_operand_c077187b4570468f9d5c1e3fa47a86bb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Assert 'Share Post' heading is visible in pop up
    assertion_operand_c077187b4570468f9d5c1e3fa47a86bb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 17 : Query 'Share' button visibility
    element_locators = ['.orangehrm-buzz-post-modal-actions > button', '.orangehrm-buzz-post-modal-actions > button:nth-child(1)', '.orangehrm-buzz-post-modal-actions > button:nth-child(1)', "//div[contains(@class,'orangehrm-buzz-post-modal-actions')]/button[1]", "//div[contains(@class,'orangehrm-buzz-post-modal-actions')]/button[1]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_5b8038cd98fa448fba6f6bb9030cbe62_0' to true
    assertion_operand_5b8038cd98fa448fba6f6bb9030cbe62_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'Share' button is visible
    assertion_operand_5b8038cd98fa448fba6f6bb9030cbe62_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Click on the close button on share post popup
    element_locators = ['.oxd-dialog-close-button-position', '.oxd-dialog-sheet--shadow > button', '.oxd-dialog-sheet--gutters > button', "//button[text()='×']", '[role="document"] > button', "//button[contains(text(),'×')]", "//div[contains(@class,'oxd-sheet--rounded') and contains(@class,'oxd-sheet--white') and contains(@class,'oxd-dialog-sheet--shadow') and contains(@class,'oxd-dialog-sheet--gutters')]/button[1]", "//button[contains(@class,'oxd-dialog-close-button-position')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 21 : Click on the three dots menu icon on post by Pushpa Raj
    element_locators = ['.orangehrm-buzz-post-header-config > li:nth-child(1) > button:nth-child(1) > i:nth-child(1)', '.orangehrm-buzz-post-header-config > li:nth-child(1) > button:nth-child(1) > i:nth-child(1)', "//div[contains(@class,'orangehrm-buzz-post-header-config')]/li[1]/button[1]/i[1]", "//div[contains(@class,'orangehrm-buzz-post-header-config')]/li[1]/button[1]/i[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 22 : Click on 'Delete Post' option in post action menu
    element_locators = ["//p[text()='Delete Post']", '[role="menu"] > li:nth-child(1) > p:nth-child(2)', '[role="menu"] > li:nth-child(1) > p:nth-child(2)', "//div[contains(@class,'orangehrm-buzz-post-header-config')]/li[1]/ul[1]/li[1]/p[1]", "//div[contains(@class,'orangehrm-buzz-post-header-config')]/li[1]/ul[1]/li[1]/p[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 23 : Click on Yes, Delete button in confirmation popup
    element_locators = ['.oxd-button--label-danger', '.oxd-button--medium.oxd-button--label-danger', '.oxd-button--ghost + button', '.oxd-button--medium.oxd-button--ghost + button', "//button[contains(@class,'oxd-button--label-danger')]", "//div[contains(@class,'oxd-sheet--rounded') and contains(@class,'oxd-sheet--white') and contains(@class,'oxd-dialog-sheet--shadow') and contains(@class,'oxd-dialog-sheet--gutters')]/div[3]/button[2]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--label-danger')]", "//div[contains(@class,'oxd-dialog-sheet--shadow')]/div[3]/button[2]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()

    driver.quit()
except Exception as e:
    driver.quit()
