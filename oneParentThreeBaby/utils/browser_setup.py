from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():
    driverPath = Service('C:\selenium_drivers\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=driverPath)
    driver.maximize_window()
    return driver