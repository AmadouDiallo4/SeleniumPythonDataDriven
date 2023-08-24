import time
from selenium import webdriver
import pytest
from utilities.customLog import logGen
from  pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_Login_001:
    baseURL = ReadConfig.getApplicationURL()
    user = ReadConfig.getUsername()
    pwd = ReadConfig.getPassword()

    lg = logGen().loggen()
    def test_homePage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lg.info("################## Test_Login_001 ############## ")
        self.lg.info("################## Verifying page title ############## ")
        time.sleep(5)
        ExpectedTite = "OrangeHRM"
        ActualTitle = self.driver.title


        if ActualTitle == ExpectedTite:
            self.lg.info("################## home page test is passed ############## ")
            self.driver.close()
            assert True
        else:
            print("------------- Test failed -----------------")
            self.driver.save_screenshot(".//Screenshots/ss_test_homePage.png")
            self.lg.error("################## home page test is failed ############## ")
            self.driver.close()
            assert False



    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        time.sleep(5)

        self.lg.info("################## Test_Login_001 ############## ")
        self.lg.info("################## Verifying test login ############## ")

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.user)
        self.lp.setPassword(self.pwd)
        self.lp.clickLoginButton()

        ExpectedTitle = "OrangeHRM"
        ActualTitle = self.driver.title

        if ActualTitle == ExpectedTitle:
            print("------------- Test passed -----------------")
            self.lg.info("################## login test is passed ############## ")
            self.driver.close()
            assert True

        else:
            print("------------Test failed --------------------")
            self.driver.save_screenshot(".//Screenshots/ss_test_login.png")
            self.lg.error("################## login test is failed ############## ")
            assert False
            self.driver.close()


