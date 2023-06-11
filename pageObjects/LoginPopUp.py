from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    # Login Page locators
    username_name = "httpd_username"
    password_name = "httpd_password"
    button_login_name = "signin"
    link_logout_linkText = "Sign out"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(by=By.NAME, value=self.username_name).clear()
        self.driver.find_element(by=By.NAME, value=self.username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(by=By.NAME, value=self.password_name).clear()
        self.driver.find_element(by=By.NAME, value=self.password_name).send_keys(password)

    def getUsername(self, username):
        return

    def clickLogin(self):
        self.driver.find_element(by=By.NAME, value=self.button_login_name).click()

    def clickLogOut(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.link_logout_linkText).click()
