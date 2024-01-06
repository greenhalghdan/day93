from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from time import sleep

# code to fill out there form howere trainline seem to block robots....

web_driver = Service(r'C:\Users\green\Downloads\chromedriver-win32new\chromedriver-win32\chromedriver.exe')

driver = webdriver.Chrome(service=web_driver)

url = 'https://www.rightmove.co.uk/'

driver.get(url)

sleep(5)

# Perform Search

driver.find_element(By.CSS_SELECTOR, 'button[id="onetrust-reject-all-handler"]').click()
sleep(1)

driver.find_element(By.CSS_SELECTOR, 'input[name="typeAheadInputField"]').send_keys('Ipswich, Suffolk')
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div[1]/div/div/div/button[1]').click()
sleep(2)
property_type = driver.find_element(By.ID, 'displayPropertyType')
property_type.find_element(By.CSS_SELECTOR, 'option[value="houses"]').click()
number_bedrooms = driver.find_element(By.ID, 'minBedrooms')
number_bedrooms.find_element(By.CSS_SELECTOR, 'option[value="3"]').click()
driver.find_element(By.ID, 'submit').click()

# Scrape data of houses from page

properties = driver.find_elements(By.CLASS_NAME, 'propertyCard-wrapper')
for property in properties:
    address = property.find_element(By.CSS_SELECTOR, 'meta[itemprop="streetAddress"]')
    print(address)

sleep(60)


