#exercise 5 - webscrapping

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os

conn = pymysql.connect(host= '127.0.0.1', user = 'root', passwd = 'YourPasswordHere', db = 'mysql',
charset = 'utf8')
curr = conn.cursor()
curr.execute("USE Sraperdb")
def store(agency,region, position, plantilla, postingDate, closingDate):
     cur.execute('INSERT INTO listings ....
     curr.connection.commit()