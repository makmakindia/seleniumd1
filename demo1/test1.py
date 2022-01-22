import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions();
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
print(driver.title)
#  driver.find_element_by_name("btnK").click()
time.sleep(2)
driver.close()
driver.quit()
print("Test Completed")