from selenium.webdriver.common.by import By

from Library.CommonMethods import selectFromDropDown, waitUntilElementTextPresent


class Registration:
    def __init__(self, driver):
        self.driver = driver

    userName = (By.CSS_SELECTOR, "input[name='fld_username']")
    passWord = (By.CSS_SELECTOR, "input[name='fld_password']")
    email = (By.CSS_SELECTOR, "input[name='fld_email']")
    stateDropDown = (By.ID, 'stateId')
    cityDropDown = (By.ID, 'cityId')
    readDetailsLink = (By.XPATH, "//a[text()='Read Detail']")
    closeReadDetailsPopUp = (By.XPATH, "//a[text()='X']")

    def getRadioButton(self, value):
        return By.XPATH, "//input[@type='radio' and @value='" + value + "']"

    def getChooseGender(self, name):
        return By.NAME, name

    def enterUsername(self, uName):
        self.driver.find_element(*Registration.userName).send_keys(uName)

    def enterPassword(self, pwd):
        self.driver.find_element(*Registration.passWord).send_keys(pwd)

    def enterEmail(self, emailID):
        self.driver.find_element(*Registration.email).send_keys(emailID)

    def ClickOnAddressType(self, value):
        self.driver.find_element(*Registration.getRadioButton(self, value)).click()

    def SelectDropDown(self, DropDownName, DropDownValue):
        selectFromDropDown(DropDownValue, self.driver.find_element(*Registration.getChooseGender(self, DropDownName)))

    def waitForStateDropDownToPopulate(self, text):
        waitUntilElementTextPresent(self.driver, self.stateDropDown, text)

    def waitForCityDropDownToPopulate(self, text):
        waitUntilElementTextPresent(self.driver, self.cityDropDown, text)

    def readTermsAndConditions(self):
        self.driver.find_element(*Registration.readDetailsLink).click()
        self.driver.find_element(*Registration.closeReadDetailsPopUp).click()




