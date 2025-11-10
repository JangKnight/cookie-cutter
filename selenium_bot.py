from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
#from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
import time

#A more focused selenium project where I'm basically cheating on a 'cookie clicking' game

chrome_driver_path = "/Users/ah/Desktop/100DaysOfCode/Web_Scraping/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
stats = ""
# try:
#     f = open("stats.txt")
#     stats = f.readline()
#     if stats[0].lower() == 'c':
#         stats = "0.1251|0|0|15|0|100|0|500|0|2000|0|7000|0|50000|0|1000000|0|123456789"
#     f.close()
# except:
#     print("FILE EITHER DOESN'T EXIST OR DOES NOT CONTAIN CORRECT INFORMATION")
#     stats = "0.1251|0|0|15|0|100|0|500|0|2000|0|7000|0|50000|0|1000000|0|123456789"
driver.find_element(By.ID, "importSave").click()
Alert(driver).send_keys("0.1251|10000|0|15|0|100|0|500|0|2000|0|7000|0|50000|0|1000000|0|123456789") #more cheating
Alert(driver).accept()
cookie = driver.find_element(By.ID, "cookie")
checkpoint = time.time() + 10
endpoint = time.time() + 600
while(True):
    cookie.click()
    if checkpoint < time.time():
        cookies = driver.find_element(By.ID, "money").text.replace(',','')
        if int(cookies) > 123456789:
            driver.find_element(By.ID, "buyTime machine").click()
        elif int(cookies) > 1000000:
            driver.find_element(By.ID, "buyPortal").click()
        elif int(cookies) > 50000:
            driver.find_element(By.ID, "buyAlchemy Lab").click()
        elif int(cookies) > 7000:
            driver.find_element(By.ID, "buyShipment").click()
        elif int(cookies) > 2000:
            driver.find_element(By.ID, "buyMine").click()
        elif int(cookies) > 500:
            driver.find_element(By.ID, "buyFactory").click()
        elif int(cookies) > 100:
            driver.find_element(By.ID, "buyGrandma").click()
        elif int(cookies) > 15:
            driver.find_element(By.ID, "buyCursor").click()
        
        checkpoint = time.time() + 3
    
    if endpoint < time.time():
        break

# driver.find_element(By.ID, "exportSave").click()
# stats = Alert(driver).__getattribute__("value")
# print(str(stats))
# f = open("stats.txt", "w")
# f.write(stats)
# f.close
    