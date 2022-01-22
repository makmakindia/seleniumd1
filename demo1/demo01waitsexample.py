from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By




driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")


driver.get("http:\\www.google.com")
driver.find_element_by_name("q").send_keys("Test Automation ....!")


wait = WebDriverWait(driver, 10)
try:
    element = wait.until(ec.element_to_be_clickable((By.NAME,"btnK")))
    print("element is clickable ....!")
except:
    print("element is not clickable : ","IndentationError: unexpected indent")
    exit(1)
element.click()

driver.quit()
print("Test completed.......................!")


