from selenium import webdriver
import pytest

from selenium.webdriver.support.select import Select


@pytest.mark.Smoke
def test_RegistrationForm():
    driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver.exe")
    driver.get("https://thetestingworld.com/testings/")
    driver.implicitly_wait(5)
    # Maximize browser
    driver.maximize_window()
    # Close the browser
    driver.close()

@pytest.mark.Sanity
def test_RegistrationFormEnterDetails():
    driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver.exe")
    driver.get("https://thetestingworld.com/testings/")
    # Maximize browser
    driver.maximize_window()
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
    # Close the browser
    driver.close()


@pytest.mark.skip("Dont not execute")
def test_SkipTheTest():
    driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver.exe")
    driver.get("https://thetestingworld.com/testings/")
    # Maximize browser
    driver.maximize_window()
    # Close the browser
    driver.close()
