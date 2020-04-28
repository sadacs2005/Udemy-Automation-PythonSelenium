from selenium import webdriver

# set chrome path
driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver.exe")
# Launch URL
driver.get("https://thetestingworld.com/testings/")
# Maximize browser
driver.maximize_window()
driver.find_element_by_xpath("//label[text()='Login']").click()
driver.find_element_by_name("_txtUserName").send_keys("test")
driver.find_element_by_name("_txtPassword").send_keys("test")
driver.find_element_by_xpath("//input[@value='Login']").click()
driver.find_element_by_xpath("//a[normalize-space(text())='My Account']").click()
driver.find_element_by_xpath("//a[text()='Delete']").click()
maintab = ""
alltabslist = driver.window_handles
for eachtab in alltabslist:
    driver.switch_to.window(eachtab)
    if "dashboard" in driver.current_url:
        maintab = eachtab
    else:
        driver.find_element_by_xpath("//button[text()='Start Download']").click()
        driver.close()
driver.switch_to.window(maintab)
driver.close()
