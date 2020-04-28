from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# set chrome path
driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver.exe")
# Launch URL
driver.get("https://thetestingworld.com/")
# Maximize browser
driver.maximize_window()

act = ActionChains(driver)
# right click
act.context_click()
# Hover on a webelement
act.move_to_element(driver.find_element_by_xpath("//span[text()='TRAINING']")).perform()
# Close the browser
driver.close()