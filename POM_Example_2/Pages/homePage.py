from pycharm.pynative.Selenium.POM_Example_2.Locators.locators import Locators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_welcome(self):
        self.driver.find_element(*Locators.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(*Locators.logout_link_linkText).click()
