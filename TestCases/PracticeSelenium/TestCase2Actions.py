from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# set chrome path
driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver.exe")
# Launch URL
driver.get("https://thetestingworld.com/testings/")
# Maximize browser
driver.maximize_window()
# Enter username
driver.find_element_by_css_selector("input[name='fld_username']").send_keys("sadacs2005")

act = ActionChains(driver)
act.send_keys(Keys.CONTROL + 'a').perform()
act.send_keys(Keys.TAB).perform()
