import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from pageObjects.LoginPage import LoginPage


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("\n***************launching Chrome browser *************")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        print("\n***************launching Firefox browser *************")
    else:
        driver=webdriver.Chrome
    return driver
def pytest_addoption(parser):  # this will get the value from CLI (hooks)
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")

#1st Step: Declare Variables For Setting up LambdaTest
user_name = "diallobis2011"
access_token = "kE4ovVAb9YBE0IVMCnw8h4DqcxvTkAzGnTNS2pqpQhLYcOqzq6"
remote_url = "https://" + user_name + ":" + access_token + "@hub.lambdatest.com/wd/hub"

#2nd Step: Define The Desired Capabilities (3 caps)
chrome_caps = {
    "browserName": "Chrome",
    "browserVersion": "114.0",
    "LT: Options": {
        "build": "1.0",
        "project": "Test Cross Browser",
        "name": "LambdaTest Grid On Firefox",
        "w3c": True,
        "platformName": "Windows 10"
    }
}

firefox_caps = {
    "browserName": "Firefox",
    "browserVersion": "114.0",
    "LT: Options": {
        "build": "2.0",
        "project": "Test Cross Browser",
        "name": "LambdaTest Grid On Firefox",
        "w3c": True,
        "platformName": "Windows 10"
    }
}

edge_caps = {
    "browserName": "MicrosoftEdge",
    "browserVersion": "113.0",
    "LT: Options": {
        "build": "3.0",
        "project": "Test Cross Browser",
        "name": "LambdaTest Grid On Firefox",
        "w3c": True,
        "platformName": "Windows 10"
    }
}
#3rd Step: Connect to LambdaTest Using A RemoteConnection
@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver_initialization(request):
    """
    Initialize Driver For Selenium Grid On LambdaTest
    :param request:
    :return:
    """
    desired_caps = {}

    if request.param == "chrome":
        options = ChromeOptions()
        #desired_caps.update(chrome_caps)
        options.set_capability('chrome:options', chrome_caps)
        driver = webdriver.Remote(remote_url, options=options)
        '''driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            desired_capabilities={"LT:Options":desired_caps})
        '''
    elif request.param == "firefox":
        #desired_caps.update(firefox_caps)
        options = FirefoxOptions()
        options.set_capability('firefox:options', desired_caps)
        driver = webdriver.Remote(
            #command_executor=RemoteConnection(remote_url),
            remote_url,
            options=options)
            #desired_capabilities={"LT:Options":desired_caps})

    elif request.param == "edge":
        desired_caps.update(edge_caps)
        options = EdgeOptions()
        options.set_capability('chrome:options', edge_caps)
        driver = webdriver.Remote(remote_url, options=options)
        '''driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            desired_capabilities={"LT:Options":desired_caps})'''
    request.cls.driver = driver
    yield
    driver.close()
