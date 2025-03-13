from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
import os

def create_chromium_driver() -> WebDriver:
  
  # Had to configure to work with headless chrome, as built by docker
  # https://www.selenium.dev/blog/2023/headless-is-going-away/
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("--headless=new")
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--single-process")

  # If deployed in docker container, the chromedriver will be in the specified location. For local testing, will need to retrieve from alternate path
  if os.getenv("DOCKERIZED"):
    service = Service("/usr/bin/chromedriver")
  else:
    service = Service("chromedriver/chromedriver")

  # Establish connection with Chrome
  driver = webdriver.Chrome(service=service, options=chrome_options)

  return driver