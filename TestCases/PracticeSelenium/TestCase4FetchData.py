from selenium import webdriver
from selenium.webdriver.support.select import Select

# set chrome path
driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver.exe")
# Launch URL
driver.get("https://thetestingworld.com/testings/")
# Maximize browser
driver.maximize_window()
# Fetch data dynamically
print("Title of the page is "+driver.title)
print("The URL of the page is "+driver.current_url)
# print("The Page source is "+driver.page_source)
# Get text of the webelement
print("Text on the element is "+driver.find_element_by_xpath("//em//a[@href='#']").text)
# Get attribute name
print("The attribute value is "+driver.find_element_by_xpath("//input[@value='Sign up']").get_attribute("type"))

# Fetch data in the dropdown button
sel = Select(driver.find_element_by_name("country"))
sel.select_by_value("20")
# Print the selected option
print("The selected drop down is " + sel.first_selected_option.text)
# Print all options
for i in sel.options:
    print(i.text)
# Close browser
driver.close()

