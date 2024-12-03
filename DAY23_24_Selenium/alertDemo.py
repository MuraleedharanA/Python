from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)

driver.get("https://demo.guru99.com/test/delete_customer.php")

searchbox= driver.find_element(By.NAME,"cusid")
searchbox.send_keys("MuraleedharanA")
searchbox.send_keys(Keys.RETURN)

alert =driver.switch_to.alert
alert.accept()

driver.implicitly_wait(5)

time.sleep(10)




driver.quit()