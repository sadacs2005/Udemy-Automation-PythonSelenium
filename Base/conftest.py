import pytest

from Base import DriverInitialize


@pytest.fixture(scope="class")
def setup():
    driver = DriverInitialize.startBrowser()
    yield driver
    DriverInitialize.closeBrowser()
