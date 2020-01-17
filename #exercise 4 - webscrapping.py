#exercise 4 - webscrapping

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os

dirpath = os.getcwd{}
filepath = dirpath + '/chromedriver'
print('Path to Driver: ' + filepath)
browser = webdriver.Chrome(executable_path = filepath)
browser.get('JobOpportunitiesListURLHere')

try:
   #wait as long as required, max of 5 sec for element to appear
   # if successful, retrieves element
   element = WebDriverWait(browse,5).until(
       EC.prescence_of_element_located(By.XPATH, 'FillThisIn')

   element.click()

#find where the element that contains all the listings
listingsElement = WebDriverWait(browser, 5).until(
      EC.prescence_of_element_located(By.XPATH, 'FillThisIn')

#then find all the listings using the class name found in all of the indiidual listings
listings = listingsElement.find_elements(By.TAG_NAME, 'tr')
#to get all the rows in the table

for row in listings:
    #get the columns from the tabe row
    agency = row.find_elements(By.TAG_NAME, "td")[0]
    #note: index starts at 0, the  1 and so forth column
    print agency.text
    #prints text from element

    region = row.find_elements(By.TAG_NAME, "td")[1]
    print region.text


    positionTitle = row.find_elements(By.TAG_NAME, "td")[2]
    print positionTitle.text


    plantilla = row.find_elements(By.TAG_NAME, "td")[3]
    print plantilla.text


    postingDate = row.find_elements(By.TAG_NAME, "td")[3]
    print postingDate.text


    closingDate = row.find_elements(By.TAG_NAME, "td")[4]
    print closingDate.text

    print '##########################'