from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)

driver.get("https://www.bbc.com")

print(driver.title)
time.sleep(10)
driver.quit()