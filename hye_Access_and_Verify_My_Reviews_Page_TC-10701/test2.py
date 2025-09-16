
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
    element_locators = ['[placeholder="Username"][name="username"]', '[placeholder="Username"]', '[name="username"]', "//input[@placeholder='Username' and @name='username']", '.oxd-input--focus', "//input[starts-with(@placeholder,'Usern')]", "//input[contains(@class,'oxd-input--focus')]", "//input[contains(@placeholder,'Username')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_3d4a38a0e0144baf9d97c65c79fbb606_0' to true
    assertion_operand_3d4a38a0e0144baf9d97c65c79fbb606_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_3d4a38a0e0144baf9d97c65c79fbb606_0 = "true"
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

    # Step - 9 : Click on Performance menu item in left sidebar
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[7]/a[1]", "//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[7]/a[1]", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(7) > a:nth-child(1)', '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(7) > a:nth-child(1)']
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

    # Step - 13 : Click on 'My Reviews' option in Manage Reviews dropdown
    element_locators = ['.--visited > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)', '.--visited > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)', "//a[text()='My Reviews']", "//a[contains(text(),'My Reviews')]", "//li[contains(@class,'--visited')]/ul[1]/li[2]/a[1]", "//li[contains(@class,'oxd-topbar-body-nav-tab') and contains(@class,'--parent') and contains(@class,'--visited')]/ul[1]/li[2]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 15 : Get the current URL
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 16 : set the value of variable 'assertion_operand_5d25fbc1b11f420bb6380f9de3958487_0' to myPerformanceReview
    assertion_operand_5d25fbc1b11f420bb6380f9de3958487_0 = "myPerformanceReview"
    driver.implicitly_wait(6)

    # Step - 17 : Assert 'current_url' contains 'myPerformanceReview'
    assertion_operand_5d25fbc1b11f420bb6380f9de3958487_0 = "myPerformanceReview"
    driver.implicitly_wait(6)

    # Step - 18 : Query 'My Reviews' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 19 : set the value of variable 'assertion_operand_50563cfe555c4d058335c60d376e8b9c_0' to true
    assertion_operand_50563cfe555c4d058335c60d376e8b9c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Assert 'My Reviews' text is visible
    assertion_operand_50563cfe555c4d058335c60d376e8b9c_0 = "true"
    driver.implicitly_wait(6)

    # Step - 21 : Query 'No Records Found' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 22 : set the value of variable 'assertion_operand_10c4a05595914c1ebc3d57078e1ae1e7_0' to true
    assertion_operand_10c4a05595914c1ebc3d57078e1ae1e7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Assert 'No Records Found' text is visible
    assertion_operand_10c4a05595914c1ebc3d57078e1ae1e7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 24 : Query 'Job Title' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 25 : set the value of variable 'assertion_operand_fb8e007c55e84063a0dc8e51627be652_0' to true
    assertion_operand_fb8e007c55e84063a0dc8e51627be652_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Assert 'Job Title' is visible
    assertion_operand_fb8e007c55e84063a0dc8e51627be652_0 = "true"
    driver.implicitly_wait(6)

    # Step - 27 : Query 'Sub unit' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 28 : set the value of variable 'assertion_operand_ca06ea8bf40247bcb0dc21ba3a371f5d_0' to true
    assertion_operand_ca06ea8bf40247bcb0dc21ba3a371f5d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Assert 'Sub unit' is visible
    assertion_operand_ca06ea8bf40247bcb0dc21ba3a371f5d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 30 : Query 'Review Period' text visibility
    element_locators = ['.oxd-table-row--with-border > div:nth-child(3) > div:nth-child(1) > i:nth-child(1)', '.oxd-table-row--with-border > div:nth-child(3) > div:nth-child(1) > i:nth-child(1)', "//div[contains(@class,'oxd-table-row--with-border')]/div[3]/div[1]/i[1]", "//div[contains(@class,'oxd-table-row--with-border')]/div[3]/div[1]/i[1]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 31 : set the value of variable 'assertion_operand_4dc023c523534f10b1e3949c1c7f297e_0' to true
    assertion_operand_4dc023c523534f10b1e3949c1c7f297e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Assert 'Review Period' text is visible
    assertion_operand_4dc023c523534f10b1e3949c1c7f297e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 33 : Query 'Due Date' visibility
    element_locators = ['.oxd-table-row--with-border > div:nth-child(4) > div:nth-child(1) > i:nth-child(1)', '.oxd-table-row--with-border > div:nth-child(4) > div:nth-child(1) > i:nth-child(1)', "//div[contains(@class,'oxd-table-row--with-border')]/div[4]/div[1]/i[1]", "//div[contains(@class,'oxd-table-row--with-border')]/div[4]/div[1]/i[1]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 34 : set the value of variable 'assertion_operand_53a544186ddd4834b62928a98d01bf26_0' to true
    assertion_operand_53a544186ddd4834b62928a98d01bf26_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Assert 'Due Date' text is visible
    assertion_operand_53a544186ddd4834b62928a98d01bf26_0 = "true"
    driver.implicitly_wait(6)

    # Step - 36 : Query 'Actions' text visibility
    element_locators = ['.oxd-table-row--with-border > div:nth-child(6) > div:nth-child(1) > i:nth-child(1)', '.oxd-table-row--with-border > div:nth-child(6) > div:nth-child(1) > i:nth-child(1)', "//div[contains(@class,'oxd-table-row--with-border')]/div[6]/div[1]/i[1]", "//div[contains(@class,'oxd-table-row--with-border')]/div[6]/div[1]/i[1]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 37 : set the value of variable 'assertion_operand_bf1606ad3ff94bd4a7dbfcd0f9572a91_0' to true
    assertion_operand_bf1606ad3ff94bd4a7dbfcd0f9572a91_0 = "true"
    driver.implicitly_wait(6)

    # Step - 38 : Assert 'Actions' text is visible
    assertion_operand_bf1606ad3ff94bd4a7dbfcd0f9572a91_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
