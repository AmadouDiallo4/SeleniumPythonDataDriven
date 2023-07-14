import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:


    USERNAME = "username"
    PASSWORD = "password"
    LOGIN_BUTTON = "//button[@type='submit']"
    CLICK_OUT = "//a[normalize-space()='Logout']"


    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.NAME, self.USERNAME).clear()
        self.driver.find_element(By.NAME, self.USERNAME).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.PASSWORD).clear()
        self.driver.find_element(By.NAME, self.PASSWORD).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

