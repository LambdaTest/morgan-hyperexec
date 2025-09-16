
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

    # Step - 3 : set the value of variable 'assertion_operand_f6d100767b5746cf97ba35f8f098e18e_0' to true
    assertion_operand_f6d100767b5746cf97ba35f8f098e18e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on viewport
    assertion_operand_f6d100767b5746cf97ba35f8f098e18e_0 = "true"
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

    # Step - 9 : Click on 'Buzz' menu item in the left side menu
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[12]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[12]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(12) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(12) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : Click on Share Photos button in Buzz Newsfeed
    element_locators = ['.orangehrm-buzz-create-post-actions > button:nth-child(1)', '.orangehrm-buzz-create-post-actions > button:nth-child(1)', '.orangehrm-buzz-create-post-actions > button:nth-child(1)', "//button[contains(text(),'Share Photos')]", "//div[contains(@class,'orangehrm-buzz-create-post-actions')]/button[1]", "//div[contains(@class,'orangehrm-buzz-create-post-actions')]/button[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 11 : Upload file from variable 'FILE_Screenshot_2025_09_12_at_7_19_03_E2_80_AFPM_png'
    element_locators = ['/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/input[1]']
    element = get_element(driver,element_locators)

    file_name = "Screenshot+2025-09-12+at+7.19.03%E2%80%AFPM.png"
    element.send_keys(str(Path(os.path.join(os.environ["USERPROFILE"], "Downloads") if os.name == "nt" else os.path.expanduser("~/Downloads")) / file_name))
    driver.implicitly_wait(6)

    # Step - 12 : Click on the Share button in Share Photos popup
    element_locators = ['.orangehrm-buzz-post-modal-actions > button', '.orangehrm-buzz-post-modal-actions > button:nth-child(1)', '.orangehrm-buzz-post-modal-actions > button:nth-child(1)', "//div[contains(@class,'orangehrm-buzz-post-modal-actions')]/button[1]", "//div[contains(@class,'orangehrm-buzz-post-modal-actions')]/button[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 13 : Click on the three dots menu icon on post by Pushpa Raj
    element_locators = ['.orangehrm-buzz-post-header-config > li:nth-child(1) > button:nth-child(1) > i:nth-child(1)', '.orangehrm-buzz-post-header-config > li:nth-child(1) > button:nth-child(1) > i:nth-child(1)', "//div[contains(@class,'orangehrm-buzz-post-header-config')]/li[1]/button[1]/i[1]", "//div[contains(@class,'orangehrm-buzz-post-header-config')]/li[1]/button[1]/i[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : Click on 'Delete Post' option in post menu
    element_locators = ["//p[text()='Delete Post']", '[role="menu"] > li:nth-child(1) > p:nth-child(2)', '[role="menu"] > li:nth-child(1) > p:nth-child(2)', "//div[contains(@class,'orangehrm-buzz-post-header-config')]/li[1]/ul[1]/li[1]/p[1]", "//div[contains(@class,'orangehrm-buzz-post-header-config')]/li[1]/ul[1]/li[1]/p[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 15 : Click on 'Yes, Delete' button in confirmation popup
    element_locators = ['.oxd-button--label-danger', '.oxd-button--medium.oxd-button--label-danger', '.oxd-button--ghost + button', '.oxd-button--medium.oxd-button--ghost + button', "//button[contains(@class,'oxd-button--label-danger')]", "//div[contains(@class,'oxd-sheet--rounded') and contains(@class,'oxd-sheet--white') and contains(@class,'oxd-dialog-sheet--shadow') and contains(@class,'oxd-dialog-sheet--gutters')]/div[3]/button[2]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--label-danger')]", "//div[contains(@class,'oxd-dialog-sheet--shadow')]/div[3]/button[2]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()

    driver.quit()
except Exception as e:
    driver.quit()
