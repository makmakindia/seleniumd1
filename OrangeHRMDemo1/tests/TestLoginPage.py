from selenium import webdriver
import HtmlTestRunner
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from OrangeHRMDemo1.pages.LoginPage import loginpageobjs
from OrangeHRMDemo1.pages.HomePage import homepageobjs


class OrangeHRMdemo1(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Dell\\PycharmProjects\\seleniumd1\\drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)

    def test_OHRMLogin(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = loginpageobjs(driver)
        login.setupusername("Admin")
        login.setuppassword("admin123")
        login.clickonloginbtn()
        print("Test Login Page Completed ..................!")

        home = homepageobjs(driver)
        home.clik_welcome()
        home.click_logout()
        print("Test Home page Completed ..................!")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\py'))
