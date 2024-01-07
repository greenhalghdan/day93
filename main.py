from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import Service
from time import sleep
import pandas as pd
import csv
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# code to fill out there form howere trainline seem to block robots....

# web_driver = Service(r'C:\Users\green\Downloads\chromedriver-win32new\chromedriver-win32\chromedriver.exe')
fire_fox_driver = Service('.\geckodriver')
# driver = webdriver.Chrome(service=web_driver)
# driver = webdriver.Firefox(service=fire_fox_driver)

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

def GetResults():
    properties = driver.find_elements(By.CSS_SELECTOR, 'div[class="l-searchResult is-list"]')
    data = []
    i = 0
    for property in properties:
        print(property.get_attribute('data-test'))
        if property.get_attribute('data-test') != "propertyCard-0":
            address = property.find_element(By.CSS_SELECTOR, 'address[class="propertyCard-address property-card-updates"]').text
            bedroom_bathrooms = property.find_element(By.CLASS_NAME, 'property-information')
            bedroom_bathrooms_values = bedroom_bathrooms.find_elements(By.CLASS_NAME, 'text')
            bedroombathroom = []
            try:
                property.find_element(By.ID, 'core-icon--bathroom-icon')
            except:
                for z in bedroom_bathrooms_values:
                    bedroombathroom.append(z.text)
                bedroombathroom.append('N/A')
            else:
                for z in bedroom_bathrooms_values:
                    bedroombathroom.append(z.text)
            price = property.find_element(By.CLASS_NAME, 'propertyCard-priceValue').text
            dict = {
                'address': address,
                'style': bedroombathroom[0],
                'Bedroom': bedroombathroom[1],
                'Bathrooms': bedroombathroom[2],
                'Price': price,
            }
            data.append(dict)
            # data.loc[len(data)] = pd.Series(dict)
            i += 1
    return data


PagesLeft = True
data2 = pd.DataFrame(columns=['address','style','Bedroom','Bathrooms','Price'])
#data2.to_csv(r'test8.csv', index=False, mode='w')
while PagesLeft:
    data = GetResults()
    nextbutton = driver.find_element(By.CSS_SELECTOR,
                                     'button[class="pagination-button pagination-direction pagination-direction--next"]')
    if nextbutton.get_attribute('disabled') == 'true':
        PagesLeft = False
    driver.find_element(By.CSS_SELECTOR,
                        'button[class="pagination-button pagination-direction pagination-direction--next"]').click()
    for dict in data:
        data2.loc[len(data2)] = dict
        print(data2)
data2.to_csv(r'test8.csv', index=False, mode='w')

