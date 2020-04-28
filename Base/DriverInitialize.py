from selenium import webdriver
from Library import configReader


def startBrowser():
    global driver
    if configReader.readConfigFile("Details", "Browser") == "Chrome":
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
    elif configReader.readConfigFile("Details", "Browser") == "Firefox":
        driver = webdriver.firefox()
    else:
        driver = webdriver.ie()
    driver.get(configReader.readConfigFile("Details", "URL"))
    # Maximize browser
    driver.maximize_window()
    return driver


def closeBrowser():
    driver.close()
