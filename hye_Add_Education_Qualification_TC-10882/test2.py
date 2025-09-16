
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
    element_locators = ['[placeholder="Username"][name="username"]', '[placeholder="Username"]', '[name="username"]', "//input[@placeholder='Username' and @name='username']", '.oxd-input--focus', "//input[starts-with(@placeholder,'Usern')]", "//input[contains(@class,'oxd-input--focus')]", "//input[contains(@placeholder,'Username')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : set the value of variable 'assertion_operand_79c1b68239104e3eb354288d316e245a_0' to true
    assertion_operand_79c1b68239104e3eb354288d316e245a_0 = "true"
    driver.implicitly_wait(6)

    # Step - 4 : Assert 'Username input box' is visible on the viewport
    assertion_operand_79c1b68239104e3eb354288d316e245a_0 = "true"
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

    # Step - 9 : Click on 'My Info' menu item in left sidebar
    element_locators = ["//nav[@role='navigation' and @aria-label='Sidepanel']/div[2]/ul[1]/li[6]/a[1]/span[1]", "//span[text()='My Info']", '[aria-label="Sidepanel"] > div:nth-child(2) > ul:nth-child(2) > li:nth-child(6) > a:nth-child(1) > span:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : wait 3 seconds
    time.sleep(int(3))
    driver.implicitly_wait(6)

    # Step - 11 : Click on Qualifications tab in left side menu
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

    # Step - 13 : Click on the Add button in the Education section under Qualifications
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : Query 'Add Education' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/h6[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > h6:nth-child(1)', "//h6[text()='Add Education']"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 15 : set the value of variable 'assertion_operand_f21a79d28fca44afbf6c6c374842adea_0' to true
    assertion_operand_f21a79d28fca44afbf6c6c374842adea_0 = "true"
    driver.implicitly_wait(6)

    # Step - 16 : Assert 'Add Education' text is visible
    assertion_operand_f21a79d28fca44afbf6c6c374842adea_0 = "true"
    driver.implicitly_wait(6)

    # Step - 17 : Query 'Level' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 18 : set the value of variable 'assertion_operand_76b111a746a741f0a223fe2180bbea07_0' to true
    assertion_operand_76b111a746a741f0a223fe2180bbea07_0 = "true"
    driver.implicitly_wait(6)

    # Step - 19 : Assert 'Level' text is visible
    assertion_operand_76b111a746a741f0a223fe2180bbea07_0 = "true"
    driver.implicitly_wait(6)

    # Step - 20 : Query 'Institute' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Institute']", "//label[contains(text(),'Institute')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 21 : set the value of variable 'assertion_operand_d9e607e976e84466b00bbb534892841d_0' to true
    assertion_operand_d9e607e976e84466b00bbb534892841d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 22 : Assert 'Institute' text is visible
    assertion_operand_d9e607e976e84466b00bbb534892841d_0 = "true"
    driver.implicitly_wait(6)

    # Step - 23 : Query 'Major/Specialization' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Major/Specialization']", "//label[contains(text(),'Major/Specialization')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 24 : set the value of variable 'assertion_operand_716c6fcce1a24dda99c94703ed3c8c05_0' to true
    assertion_operand_716c6fcce1a24dda99c94703ed3c8c05_0 = "true"
    driver.implicitly_wait(6)

    # Step - 25 : Assert 'Major/Specialization' text is visible
    assertion_operand_716c6fcce1a24dda99c94703ed3c8c05_0 = "true"
    driver.implicitly_wait(6)

    # Step - 26 : Query 'Year' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/div[4]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='Year']", "//label[contains(text(),'Year')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 27 : set the value of variable 'assertion_operand_466f403ed64a43318e03849b00a2649b_0' to true
    assertion_operand_466f403ed64a43318e03849b00a2649b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 28 : Assert 'Year' text is visible
    assertion_operand_466f403ed64a43318e03849b00a2649b_0 = "true"
    driver.implicitly_wait(6)

    # Step - 29 : Query 'GPA/Score' text visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/div[5]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='GPA/Score']", "//label[contains(text(),'GPA/Score')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 30 : set the value of variable 'assertion_operand_05f93f62796545a0913548907cec2c35_0' to true
    assertion_operand_05f93f62796545a0913548907cec2c35_0 = "true"
    driver.implicitly_wait(6)

    # Step - 31 : Assert 'GPA/Score' text is visible
    assertion_operand_05f93f62796545a0913548907cec2c35_0 = "true"
    driver.implicitly_wait(6)

    # Step - 32 : Query 'Start Date' visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 33 : set the value of variable 'assertion_operand_12bffc59fa374e8584dc16b107462734_0' to true
    assertion_operand_12bffc59fa374e8584dc16b107462734_0 = "true"
    driver.implicitly_wait(6)

    # Step - 34 : Assert 'Start Date' text is visible
    assertion_operand_12bffc59fa374e8584dc16b107462734_0 = "true"
    driver.implicitly_wait(6)

    # Step - 35 : Query 'End Date' visibility
    element_locators = ["//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/label[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > form:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//label[text()='End Date']", "//label[contains(text(),'End Date')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 36 : set the value of variable 'assertion_operand_27e3f5143182469ba69eb2cbbd923d61_0' to true
    assertion_operand_27e3f5143182469ba69eb2cbbd923d61_0 = "true"
    driver.implicitly_wait(6)

    # Step - 37 : Assert 'End Date' text is visible
    assertion_operand_27e3f5143182469ba69eb2cbbd923d61_0 = "true"
    driver.implicitly_wait(6)

    # Step - 38 : Query 'Cancel' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 39 : set the value of variable 'assertion_operand_223cce6a231c496e8a1d66b8065ccbbb_0' to true
    assertion_operand_223cce6a231c496e8a1d66b8065ccbbb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 40 : Assert 'Cancel' text is visible
    assertion_operand_223cce6a231c496e8a1d66b8065ccbbb_0 = "true"
    driver.implicitly_wait(6)

    # Step - 41 : Query 'Save' text visibility
    element_locators = ['']
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 42 : set the value of variable 'assertion_operand_e632a7792e144af2bd0c32f0584a992e_0' to true
    assertion_operand_e632a7792e144af2bd0c32f0584a992e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 43 : Assert 'Save' text is visible
    assertion_operand_e632a7792e144af2bd0c32f0584a992e_0 = "true"
    driver.implicitly_wait(6)

    # Step - 44 : Click 'Save' button
    element_locators = ['[type="submit"]', '.oxd-button--secondary', '.oxd-button--medium.oxd-button--secondary', '.oxd-button--ghost + button', "//button[starts-with(@type,'submi')]", "//button[contains(@class,'oxd-button--secondary')]", "//button[contains(@type,'submit')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--secondary')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 45 : Query 'Required' text visibility
    element_locators = ['.oxd-input-field-error-message', '.oxd-text--span.oxd-input-field-error-message', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/span[1]", '#app > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)', "//span[text()='Required']", "//span[contains(@class,'oxd-input-field-error-message')]", "//span[contains(@class,'oxd-text--span') and contains(@class,'oxd-input-field-error-message')]"]
    element = get_element(driver,element_locators)

    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 46 : set the value of variable 'assertion_operand_cd84f60ca002487a842009b776e1bc27_0' to true
    assertion_operand_cd84f60ca002487a842009b776e1bc27_0 = "true"
    driver.implicitly_wait(6)

    # Step - 47 : Assert 'Required' text is visible
    assertion_operand_cd84f60ca002487a842009b776e1bc27_0 = "true"
    driver.implicitly_wait(6)

    # Step - 48 : Click 'Cancel' button
    element_locators = ['.oxd-button--ghost', '.oxd-button--medium.oxd-button--ghost', 'button:has(+ .oxd-button--secondary)', "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[3]/button[1]", 'button:has(+ .oxd-button--medium.oxd-button--secondary)', "//button[contains(@class,'oxd-button--ghost')]", "//button[contains(@class,'oxd-button--medium') and contains(@class,'oxd-button--ghost')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()

    driver.quit()
except Exception as e:
    driver.quit()
