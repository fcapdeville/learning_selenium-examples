# Example of POM using selenium
# https://www.youtube.com/watch?v=9_5Wqgni_Xw&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&index=5

import unittest
from selenium import webdriver
import page
import time


class PythonOrgSearch(unittest.TestCase):
    driver = webdriver.Chrome("C:/Program Files (x86)/chromedriver.exe")
    driver.get("http://www.python.org")

    def SetUp(self):
        print("Setting up variables...")

    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()

        main_page.search_text_element = "pycon"
        main_page.click_go_button()

        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        print("Closing variables after test is finished...")
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
