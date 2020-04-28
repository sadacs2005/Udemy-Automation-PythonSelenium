
def takePageScreenshot(driver, name):
    driver.get_screenshot_as_file("../.././"+name+".png")