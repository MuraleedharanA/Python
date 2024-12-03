"""
Create a menu driven program to take a movie name from the user and get its rating using selenium from an online source (IMBD) and other details

The menu should have options to save it to a file
when user press quit all details shld be saved to a file
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd

#method to get movie details from IMDP. Method gets rating, director, writer and cast
def getMovieDetailsIMDP(movieName):
    #try:
        driver_path = r'geckodriver.exe'
        service = Service(driver_path)
        driver = webdriver.Firefox(service=service)
        driver.get("https://www.imdb.com/")
        driver.maximize_window()
        driver.implicitly_wait(3)

        searchBox = driver.find_element(By.XPATH,"""//*[@id="suggestion-search"]""")
        searchBox.send_keys(movieName)
        searchBox.submit()
        driver.implicitly_wait(3)
        
        movieTitleElements = driver.find_elements(By.CLASS_NAME,"ipc-metadata-list-summary-item__c")
        movieTitleElement = movieTitleElements[0]
        time.sleep(10)
        movieTitleElement.click()
        #driver.implicitly_wait(3)
        time.sleep(10)

        #ratingElement = driver.find_element(By.XPATH, """//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]/span[1]""")
        ratingElement = driver.find_element(By.XPATH,"//span[@class='sc-d541859f-1 imUuxf']")
        rating = ratingElement.text

        directorElement = driver.find_element(By.XPATH,"""//a[@class='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link']""")
        director = directorElement.text
        
        movieDF = pd.DataFrame({
                "Movie" : [movieName],
                "Director" : [director],
                "Rating" : [rating]
        })
        driver.quit()
        return movieDF
    #except Exception:
        #print("Exception occured")



#Main Code
mainDF = pd.DataFrame()
option=0
while(option!=4):
    print("Menu\n1. Get Movie Rating\n2. View all movies searched\n3. Save all movies to File\n4. Exit")
    option = int(input("Enter your option:"))
    if option==1:
            movieName = input("Enter Movie name to get details : ")
            moviedf = getMovieDetailsIMDP(movieName)
            print(moviedf)
            mainDF = mainDF.append(moviedf)

    elif option==2:
            print(mainDF)
    elif option==3:
            print("Saving content to file - Movie Rating.csv")
            mainDF.to_csv("Movie Rating.csv")
