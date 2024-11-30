from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)

driver.get("https://en.wikipedia.org/wiki/India")



searchbox= driver.find_elements(By.LINK_TEXT,"Modern humans")
#searchbox= driver.find_elements(By.TAG_NAME,"a")

for item in searchbox:
    print(item.get_attribute('href'))

driver.get(item.get_attribute('href'))
driver.back()

#searchbox.send_keys(Keys.RETURN)



driver.implicitly_wait(5)
driver.save_screenshot("screenshot.png")



print(driver.title)
time.sleep(10)
driver.quit()