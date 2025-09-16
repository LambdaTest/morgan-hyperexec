
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

    # Step - 3 : set the value of variable 'assertion_operand_63e51da8abcd453f84830f8336aef030_0' to true
    assertion_operand_63e51da8abcd453f84830f8336aef030_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on viewport
    assertion_operand_63e51da8abcd453f84830f8336aef030_0 = "true"
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

    # Step - 11 : Click on 'Qualifications' tab in the left side menu
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[9]/a[1]", "//a[text()='Qualifications']", "//a[contains(text(),'Qualifications')]", '[role="tablist"] > div:nth-child(9) > a:nth-child(1)', '[role="tablist"] > div:nth-child(9) > a:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 12 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 13 : scroll down once
    driver.execute_script(f"scroll_height = 1*window.innerHeight; window.scrollBy(0, scroll_height)")
    time.sleep(1)
    driver.implicitly_wait(6)

    # Step - 14 : Query 'Languages' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 15 : set the value of variable 'assertion_operand_4edcbda4f141471c8f0ef479ae76ca93_0' to true
    assertion_operand_4edcbda4f141471c8f0ef479ae76ca93_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Assert 'Languages' text is visible
    assertion_operand_4edcbda4f141471c8f0ef479ae76ca93_0 = "true"
    driver.implicitly_wait(6)

    # Step - 17 : Query 'No Records Found' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_c7b3c6d165c64fcabba1cc87caa66b37_0' to true
    assertion_operand_c7b3c6d165c64fcabba1cc87caa66b37_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'No Records Found' text is visible
    assertion_operand_c7b3c6d165c64fcabba1cc87caa66b37_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Query 'Language' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 21 : set the value of variable 'assertion_operand_b7e2f87745424b42ae1682b0779d3679_0' to true
    assertion_operand_b7e2f87745424b42ae1682b0779d3679_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Assert 'Language' text is visible
    assertion_operand_b7e2f87745424b42ae1682b0779d3679_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Query 'Fluency' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 24 : set the value of variable 'assertion_operand_f0f062b1dd8b40bc81557f8bb147470d_0' to true
    assertion_operand_f0f062b1dd8b40bc81557f8bb147470d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Assert 'Fluency' text is visible
    assertion_operand_f0f062b1dd8b40bc81557f8bb147470d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Query 'Competency' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 27 : set the value of variable 'assertion_operand_f4bdc0ab83cd49d0846d46bed51ea1ef_0' to true
    assertion_operand_f4bdc0ab83cd49d0846d46bed51ea1ef_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Assert 'Competency' text is visible
    assertion_operand_f4bdc0ab83cd49d0846d46bed51ea1ef_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Query 'Comments' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 30 : set the value of variable 'assertion_operand_d3c25d604f334f0492cac110e2459297_0' to true
    assertion_operand_d3c25d604f334f0492cac110e2459297_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Assert 'Comments' text is visible
    assertion_operand_d3c25d604f334f0492cac110e2459297_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 33 : set the value of variable 'assertion_operand_1399974bdf6d4531b25c3d942ece00a8_0' to true
    assertion_operand_1399974bdf6d4531b25c3d942ece00a8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Assert 'Actions' text is visible
    assertion_operand_1399974bdf6d4531b25c3d942ece00a8_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Query 'License' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='License']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 36 : set the value of variable 'assertion_operand_28507f793f5b4c46af3a97538a2c3f6e_0' to true
    assertion_operand_28507f793f5b4c46af3a97538a2c3f6e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Assert 'License' text is visible
    assertion_operand_28507f793f5b4c46af3a97538a2c3f6e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 38 : Query 'License Type' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 39 : set the value of variable 'assertion_operand_43b7ca82e4b948d6849abbe6e2950daa_0' to true
    assertion_operand_43b7ca82e4b948d6849abbe6e2950daa_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Assert 'License Type' text is visible
    assertion_operand_43b7ca82e4b948d6849abbe6e2950daa_0 = "true"
    driver.implicitly_wait(6)

    # Step - 41 : Query 'Issued Date' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[6]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(6) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 42 : set the value of variable 'assertion_operand_10ab440a85df45e499735eca6e9987fb_0' to true
    assertion_operand_10ab440a85df45e499735eca6e9987fb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Assert 'Issued Date' text is visible
    assertion_operand_10ab440a85df45e499735eca6e9987fb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 44 : Query 'Expiry Date' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[6]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(6) > div:nth-child(2)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 45 : set the value of variable 'assertion_operand_829595c4a91f4c6489740846666a4ff5_0' to true
    assertion_operand_829595c4a91f4c6489740846666a4ff5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 46 : Assert 'Expiry Date' text is visible
    assertion_operand_829595c4a91f4c6489740846666a4ff5_0 = "true"
    driver.implicitly_wait(6)

    # Step - 47 : Query 'Attachments' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 48 : set the value of variable 'assertion_operand_fdee930deb1e4f69901f234828dc2920_0' to true
    assertion_operand_fdee930deb1e4f69901f234828dc2920_0 = "true"
    driver.implicitly_wait(6)

    # Step - 49 : Assert 'Attachments' text is visible
    assertion_operand_fdee930deb1e4f69901f234828dc2920_0 = "true"
    driver.implicitly_wait(6)

    # Step - 50 : Query 'File Name' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 51 : set the value of variable 'assertion_operand_797cdfc7eda64f0386b26d75d7a4cafd_0' to true
    assertion_operand_797cdfc7eda64f0386b26d75d7a4cafd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 52 : Assert 'File Name' is visible
    assertion_operand_797cdfc7eda64f0386b26d75d7a4cafd_0 = "true"
    driver.implicitly_wait(6)

    # Step - 53 : Query 'Description' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 54 : set the value of variable 'assertion_operand_d7b08f2e7f354fa7933365213cfd3e6f_0' to true
    assertion_operand_d7b08f2e7f354fa7933365213cfd3e6f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 55 : Assert 'Description' text is visible
    assertion_operand_d7b08f2e7f354fa7933365213cfd3e6f_0 = "true"
    driver.implicitly_wait(6)

    # Step - 56 : Query 'Size' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 57 : set the value of variable 'assertion_operand_e8b578652e3b4fef9b384a3cef7da6c2_0' to true
    assertion_operand_e8b578652e3b4fef9b384a3cef7da6c2_0 = "true"
    driver.implicitly_wait(6)

    # Step - 58 : Assert 'Size' text is visible
    assertion_operand_e8b578652e3b4fef9b384a3cef7da6c2_0 = "true"
    driver.implicitly_wait(6)

    # Step - 59 : Query 'Type' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 60 : set the value of variable 'assertion_operand_861dbd9f0ecd45fc8f77ce4e4094027e_0' to true
    assertion_operand_861dbd9f0ecd45fc8f77ce4e4094027e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 61 : Assert 'Type' text is visible
    assertion_operand_861dbd9f0ecd45fc8f77ce4e4094027e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 62 : Query 'Date Added' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[7]/div[2]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(7) > div:nth-child(3)']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 63 : set the value of variable 'assertion_operand_ca22ae1382154a8d998907cd341dfa6b_0' to true
    assertion_operand_ca22ae1382154a8d998907cd341dfa6b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 64 : Assert 'Date Added' text is visible
    assertion_operand_ca22ae1382154a8d998907cd341dfa6b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 65 : Query visibility of text 'Added By'
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 66 : set the value of variable 'assertion_operand_b27376decb0640c7b185d91fede953d3_0' to true
    assertion_operand_b27376decb0640c7b185d91fede953d3_0 = "true"
    driver.implicitly_wait(6)

    # Step - 67 : Assert text 'Added By' is visible
    assertion_operand_b27376decb0640c7b185d91fede953d3_0 = "true"
    driver.implicitly_wait(6)

    # Step - 68 : Query 'Actions' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 69 : set the value of variable 'assertion_operand_5c98eb13c38e427d972672e424c54ef7_0' to true
    assertion_operand_5c98eb13c38e427d972672e424c54ef7_0 = "true"
    driver.implicitly_wait(6)

    # Step - 70 : Assert 'Actions' text is visible
    assertion_operand_5c98eb13c38e427d972672e424c54ef7_0 = "true"

    driver.quit()
except Exception as e:
    driver.quit()
