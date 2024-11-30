from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)

driver.get("https://www.github.com/login")

#searchbox= driver.find_element(By.ID,"login_field")
searchbox= driver.find_element(By.CLASS_NAME,"form-control input-block js-login-field")
searchbox.send_keys("MuraleedharanA")

#searchbox= driver.find_element(By.ID,"password")
searchbox= driver.find_element(By.CLASS_NAME,"form-control form-control input-block js-password-field")
searchbox.send_keys("Beta$123455")


searchbox.send_keys(Keys.RETURN)



driver.implicitly_wait(5)



print(driver.title)
time.sleep(10)
driver.quit()