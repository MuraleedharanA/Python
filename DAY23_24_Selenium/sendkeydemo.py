from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)

driver.get("https://www.duckduckgo.com")

searchbox= driver.find_element(By.NAME,"q")
searchbox.send_keys("Selenium Python")
searchbox.send_keys(Keys.RETURN)

driver.implicitly_wait(5)



print(driver.title)
time.sleep(10)
driver.quit()