from selenium import webdriver

driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver.exe")
driver.get("https://www.naukri.com/")
main_window = ""
windowPopups = driver.window_handles
for win in windowPopups:
    driver.switch_to.window(win)
    print(driver.title)
    if "Naukri" in driver.title:
        main_window = win
    else:
        driver.close()
driver.switch_to.window(main_window)
print(driver.current_url)
driver.close()