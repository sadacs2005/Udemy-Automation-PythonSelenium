# This is module for all common methods
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def selectFromDropDown(option, elm):
    selSex = Select(elm)
    selSex.select_by_visible_text(option)


def waitUntilElementTextPresent(driver, locator, text):
    wait = WebDriverWait(driver, 20)
    wait.until(expected_conditions.text_to_be_present_in_element(locator, text))
