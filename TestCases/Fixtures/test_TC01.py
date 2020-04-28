from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.TakeScreenshot import takePageScreenshot


@pytest.fixture(scope="module")
def setup():
    global driver
    driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver.exe")
    driver.get("https://thetestingworld.com/testings/")
    # Maximize browser
    driver.maximize_window()
    takePageScreenshot(driver, "Login")
    yield
    # Close the browser
    driver.close()


@pytest.mark.Smoke
def test_RegistrationForm(setup):
    print("I am in registration form")
    assert "Login" in driver.title


@pytest.mark.Sanity
def test_RegistrationFormEnterDetails(setup):
    # Enter username
    driver.find_element_by_css_selector("input[name='fld_username']").send_keys("sadacs2005")
    # Enter email id
    driver.find_element_by_css_selector("input[name='fld_email']").send_keys("sadacs2005@gmail.com")
    # Enter password
    driver.find_element_by_css_selector("input[name='fld_password']").send_keys("sadacs2005@gmail.com")
    # Confirm password
    driver.find_element_by_css_selector("input[name='fld_cpassword']").send_keys("sadacs2005@gmail.com")
    # Click on Home radio button
    driver.find_element_by_xpath("//input[@type='radio' and @value='home']").click()
    # Select dropdown
    selSex = Select(driver.find_element_by_name("sex"))
    selSex.select_by_visible_text("Male")
    selCountry = Select(driver.find_element_by_name("country"))
    selCountry.select_by_value("38")
    # Wait for element
    wait = WebDriverWait(driver, 20)
    wait.until(expected_conditions.text_to_be_present_in_element((By.ID, 'stateId'), "British Columbia"))
    selState = Select(driver.find_element_by_name("state"))
    selState.select_by_visible_text("British Columbia")
    takePageScreenshot(driver, "EnteredAllDetails")
    # Click on Link
    driver.find_element_by_xpath("//a[text()='Read Detail']").click()
    takePageScreenshot(driver, "Popup")
    # Close the popup
    driver.find_element_by_xpath("//a[text()='X']").click()



