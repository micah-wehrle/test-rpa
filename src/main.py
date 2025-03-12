from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import requests
import time
import json

import os

# Had to configure to work with headless chrome, as built by docker
# https://www.selenium.dev/blog/2023/headless-is-going-away/
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--single-process")

service = Service("/usr/bin/chromedriver")

# Establish connection with Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://rpachallenge.com/')

title = driver.title

driver.quit()

update_url = 'https://ng-proj-2-default-rtdb.firebaseio.com/test.json'

data = {
  'title': title,
  'now': time.time()
}

converted_data = json.dumps(data)

r = requests.post(url=update_url, data=converted_data)

print(r.json())