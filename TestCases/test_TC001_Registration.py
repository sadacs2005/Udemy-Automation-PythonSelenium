import pytest
from Base import DriverInitialize, conftest
from Base.conftest import setup
from Pages.Login.Registration import Registration
from Library.configReader import readConfigFile
from Utilities import ReadFromXLSXUsingOpenPyXL
import openpyxl


def dataGenerator():
    li = [["uname1", "pass1"], ["uname2", "pass2"]]
    return li


def test_registration(setup):
    rp = Registration(setup)
    rp.enterUsername(readConfigFile("RegFormDetails", "username"))
    rp.enterEmail(readConfigFile("RegFormDetails", "email"))
    rp.enterPassword(readConfigFile("RegFormDetails", "password"))
    rp.ClickOnAddressType(readConfigFile("RegFormDetails", "AddressType"))
    rp.SelectDropDown("sex", "Male")
    rp.SelectDropDown("country", "Canada")
    rp.waitForStateDropDownToPopulate("Alberta")
    rp.SelectDropDown("state", "Alberta")
    rp.waitForCityDropDownToPopulate("Calgary")
    rp.SelectDropDown("city", "Calgary")
    rp.readTermsAndConditions()


@pytest.mark.parametrize('data', dataGenerator())
def test_validatedata(setup, data):
    rp = Registration(setup)
    rp.enterUsername(data[0])
    rp.enterPassword(data[1])


@pytest.mark.parametrize('data', ReadFromXLSXUsingOpenPyXL.readFromExcel())
def test_validatedataFromExcel(setup, data):
    print(data)
    rp = Registration(setup)
    rp.enterUsername(data[0])
    rp.enterPassword(data[1])
