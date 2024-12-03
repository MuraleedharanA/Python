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

listOfLinks = [
    "https://www.moneycontrol.com/india/stockpricequote/infrastructure-general/adaniportsspecialeconomiczone/MPS",
    "https://www.moneycontrol.com/india/stockpricequote/refineries/bharatpetroleumcorporation/BPC",
    "https://www.moneycontrol.com/india/stockpricequote/leather-products/bataindia/BI01",
    "https://www.moneycontrol.com/india/stockpricequote/glassglass-products/asahiindiaglass/AIG01"
    
]
count = 1
for link in listOfLinks:
    driver.get(link)
    time.sleep(10)
    searchbox= driver.find_element(By.ID,"advchart")
    driver.execute_script("arguments[0].scrollIntoView(true);", searchbox)
    filename = link.split("/")[-1]
    print(filename)
    searchbox.screenshot(filename+".png")
    time.sleep(10)
    
driver.quit()