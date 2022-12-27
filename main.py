from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
from utils import get_url

print("Enter username: ")
username = input(">")
print("Enter tag: ")
tag = input(">")

def getCompData():
    PATH = "C:\\Users\\vince\\chromedriver.exe"
    s = Service(PATH)
    driver = webdriver.Chrome(service = s)
    url = get_url(username, tag)
    driver.get(url)
    rank = driver.find_element(By.CLASS_NAME, "stat__value").text
    stats = driver.find_elements(By.CLASS_NAME, "numbers")
    for stat in stats:
        name = stat.find_element(By.CLASS_NAME, "name")
        title = name.get_attribute("title")
        print(title)
        value = stat.find_element(By.CLASS_NAME, "value")
        print(value.text)
    time.sleep(5)
   



getCompData()