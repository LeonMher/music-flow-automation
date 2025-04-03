from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://localhost:5173/login")

time.sleep(3)

username_field = driver.find_element(By.ID, "first-name-field")
password_field = driver.find_element(By.ID, "last-name-field")
submit = driver.find_element(By.ID, "signUpButton")

username_field.send_keys("mher@gmail.com")  
password_field.send_keys("Kepler22bb!Kepler22bb!")  
submit.click()

time.sleep(30)

driver.quit()