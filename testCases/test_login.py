from pageObjects.LoginPopUp import Login
from colorama import Fore

from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "NTB 149268 Signin":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "failed_homepage_title.png")
            self.driver.close()
            print(Fore.RED + "FAILED TO DISPLAY THE LOGIN PAGE")
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = Login(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        actual_title = self.driver.title
        if actual_title == "NTB 149268 Home":
            assert True
            self.driver.close()
            print(Fore.GREEN + "SUCCESSFULLY LOGGED INTO NTB AS " + Fore.BLUE + self.username + Fore.GREEN + " USER")
        else:
            # self.driver.save_screenshot(
            #     ".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            print(Fore.RED + "FAILED TO LOG INTO NTB AS " + self.username + " USER")
            assert False
