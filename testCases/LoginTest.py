import time
from selenium import webdriver
import pytest
from  pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By


class Test_Login_001:
    username = "Admin"
    password = "admin123"
    DASHBOARD = ""

    def test_homePage(self):
        self.driver = webdriver.Chrome()
        self.driver.get(LoginPage.BASE_URL)
        self.driver.maximize_window()
        time.sleep(5)
        ExpectedTite = "OrangeHRM"
        ActualTitle = self.driver.title

        if ActualTitle == ExpectedTite:
            assert True
        else:
            assert False

        self.driver.close()

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(LoginPage.BASE_URL)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()

        ExpectedTitle = "OrangeHRM"
        ActualTitle = self.driver.title

        if ActualTitle == ExpectedTitle:
            print("------------- Test passed -----------------")
            self.driver.close()
            assert True

        else:
            print("------------Test failed --------------------")
            assert False
            self.driver.close()


