import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


@pytest.fixture()
def setUp():
    driver = webdriver.Chrome()
    driver.maximize_window()
