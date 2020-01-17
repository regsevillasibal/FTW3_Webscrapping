#exercise 3 - webscrapping

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
    #Dismiss initial pop up
    element = WebDriverWait(browser,5).until9
         EC.precence_of_element_located((By.XPATH, 'FillThisIn'))

    element.click()
except TimeoutException:
    print("Failed to load element")

#browser.quit()
