from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service=service)
driver.maximize_window()

driver.get("https://www.moneycontrol.com/india/stockpricequote/refineries/bharatpetroleumcorporation/BPC")
time.sleep(10)

searchbox= driver.find_element(By.CLASS_NAME,"adv_hed")

driver.execute_script("arguments[0].scrollIntoView(true);", searchbox)


#driver.implicitly_wait(5)
driver.save_screenshot("chart.png")



print(driver.title)
time.sleep(10)
driver.quit()