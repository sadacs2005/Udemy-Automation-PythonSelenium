from selenium import webdriver

driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver.exe")
driver.get("https://demoqa.com/iframe-practice-page/")
driver.maximize_window()


