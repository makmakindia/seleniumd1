import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class mydemoex1sample(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def testsearch_1(self):
        self.driver.get("https:\\www.google.in")
        self.driver.find_element_by_name("q").send_keys("Automation Testing")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        #  self.driver.find_element_by_name("btnK").click()
        titlestr1 = self.driver.title
        print(titlestr1)
        self.assertEqual(titlestr1,"Automation Testing - Google Search")

    def testsearch_2(self):
        self.driver.get("https:\\www.google.in")
        self.driver.find_element_by_name("q").send_keys("Webservices Testing")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        #  self.driver.find_element_by_name("btnK").click()
        titlestr2 = self.driver.title
        print(titlestr2)
        self.assertEqual(titlestr2,"Webservices Testing - Google Search")



