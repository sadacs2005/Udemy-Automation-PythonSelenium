from selenium import webdriver
from selenium.webdriver.support.select import Select

# set chrome path
driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver.exe")
# Launch URL
driver.get("https://thetestingworld.com/testings/")
# Maximize browser
driver.maximize_window()
# driver.execute_script("window.scrollTo(0, 500")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")