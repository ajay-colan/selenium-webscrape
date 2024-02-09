from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://pypi.org/project/selenium/')

cookies = driver.capabilities
head = driver.find_element(By.CLASS_NAME, "package-header__name").text

with open('data.json', mode='w', encoding='utf-8', ) as file :
    json.dump(cookies, file, indent=4)
file.close()