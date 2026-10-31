# Example of POM using selenium and pytest reports
# I strongly recommend this POM example over the first one
# https://www.youtube.com/watch?v=BURK7wMcCwU

# To run from command line:
# python -m

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import unittest
from pycharm.pynative.Selenium.POM_Example_2.Pages.loginPage import LoginPage
from pycharm.pynative.Selenium.POM_Example_2.Pages.homePage import HomePage
import HtmlTestRunner
import pytest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        service = Service(executable_path="C:/Program Files (x86)/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="E:/Temporal/Cursos/Python3-udemy-y-otros/pycharm/pynative/Selenium/POM_Example_2/Reports"))
