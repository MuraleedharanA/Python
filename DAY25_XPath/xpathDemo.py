from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)

driver.get("https://www.wikipedia.org")
driver.implicitly_wait(3)


searchBox = driver.find_element(By.XPATH,"//input[@id='searchInput']")
searchBox.send_keys("India")

searchBox = driver.find_element(By.XPATH,"""/html/body/main/div[2]/form/fieldset/button/i""")
searchBox.click()

driver.implicitly_wait(5)

heading = driver.find_element(By.XPATH,"//span[contains(text(),'India')]")
print(heading)

driver.quit()