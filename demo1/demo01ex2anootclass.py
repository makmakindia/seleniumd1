import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Testreporthtml1(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def testsearch_3(self):
        self.driver.get("https:\\www.google.in")
        self.driver.find_element_by_name("q").send_keys("Automation Testing")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        #  self.driver.find_element_by_name("btnK").click()
        titlestr3 = self.driver.title
        print(titlestr3)
        self.assertEqual("Automation Testing - Google Search", titlestr3)

    def testsearch_4(self):
        self.driver.get("https:\\www.google.in")
        self.driver.find_element_by_name("q").send_keys("Webservices Testing")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        #  self.driver.find_element_by_name("btnK").click()
        titlestr4 = self.driver.title
        print(titlestr4)
        self.assertEqual(titlestr4, "Webservices Testing - Google Search")

    def testsearch_5(self):
        self.driver.get("https:\\www.google.in")
        self.driver.find_element_by_name("q").send_keys("skip Testing")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        #  self.driver.find_element_by_name("btnK").click()
        titlestr5 = self.driver.title
        print(titlestr5)
        self.assertEqual(titlestr5, "Skp Testing - Google Search")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/ArunD/result'), )
