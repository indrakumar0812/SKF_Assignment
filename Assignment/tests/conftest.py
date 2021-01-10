import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Assignment.utilities.ReadProperties import ReadConfig

config = ReadConfig()

#-------------Hook to accept the browser value from command line. Default browser if chrome------------#
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome")

#--------Tear up function----------#
@pytest.fixture(scope='class')
def setup(request):

    browser_name=request.config.getoption("--browser")

    if browser_name == 'chrome':
        driver= webdriver.Chrome(ChromeDriverManager().install())

    elif browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get(config.getUrl())
    driver.maximize_window()
    time.sleep(2)
    request.cls.driver = driver
    yield
    driver.close()



