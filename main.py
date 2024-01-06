from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from time import sleep

# code to fill out there form howere trainline seem to block robots....

web_driver = Service(r'C:\Users\green\Downloads\chromedriver-win32new\chromedriver-win32\chromedriver.exe')

driver = webdriver.Chrome(service=web_driver)

# url = 'https://www.thetrainline.com/'
#
# driver.get(url)
#
# sleep(3)
# # accept eula
# driver.find_element(By.ID, value='onetrust-accept-btn-handler').click()
# sleep(2)
#
# # login
# driver.find_element(By.CSS_SELECTOR, 'button[data-testid="account-button--unknown"]').click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'input[data-testid="signIn-email-field"]').send_keys('')
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'input[data-testid="signIn-password-field"]').send_keys('')
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'button[data-testid="signIn-submission"]').click()
# sleep(20)
#
# driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[2]/main/div[2]/div/div[4]/div/div/div[1]/section/form/div[1]/div[1]/div/label/div[2]/div/input').send_keys('ipswich')
#
# sleep(2)
# driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[2]/main/div[2]/div/div[4]/div/div/div[1]/section/form/div[1]/div[2]/div/label/div[2]/div/input').send_keys('london liverpool street')
# sleep(2)
# driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[2]/main/div[2]/div/div[4]/div/div/div[1]/section/form/fieldset/div/label[2]/div/input').click()
# sleep(2)
# driver.find_element(By.ID, value='return').click()
# sleep(2)
# driver.find_element(By.ID, 'page.journeySearchForm.outbound.title').click()
#
# sleep(2)
# #outbound journey
# outbound = driver.find_element(By.CSS_SELECTOR, 'fieldset[data-test="outbound-datepicker"]')
#
# driver.find_element(By.CSS_SELECTOR, 'td[data-test="2024-01-09"]').click()
# sleep(2)
# driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/main/div[2]/div/div[4]/div/div/div[1]/section/form/div[3]/fieldset[1]/div[3]/div/select').click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'option[value=arriveBefore]').click()
# sleep(2)
# outbound.find_element(By.ID, 'journey-search-form-time-picker').click()
# hour = outbound.find_element(By.ID, 'journey-search-form-time-picker')
# sleep(2)
# hour.find_element(By.CSS_SELECTOR, 'option[value="09"]').click()
# sleep(2)
#
# #inbound journey
# inbound = driver.find_element(By.CSS_SELECTOR, 'fieldset[data-test="inbound-datepicker"]')
# inbound.find_element(By.CSS_SELECTOR, 'button[data-test="datepicker-same-day-button"]').click()
# sleep(2)
# inbound.find_element(By.ID, 'journey-search-form-time-picker').click()
# sleep(2)
# inbound.find_element(By.CSS_SELECTOR, 'option[value="18"]').click()
# sleep(2)
# inbound.find_element(By.CSS_SELECTOR, '[id="journey-search-form-time-picker"][aria-label="minutes"]').click()
# sleep(2)
# inboundminutes = inbound.find_element(By.CSS_SELECTOR, '[id="journey-search-form-time-picker"][aria-label="minutes"]')
# inboundminutes.find_element(By.CSS_SELECTOR, 'option[value="00"]').click()
# sleep(2)
#
# # adding rail card
#
# passangerinfo = driver.find_element(By.CLASS_NAME, '_bug0dg')
#
# passangerinfo.find_element(By.ID, 'passenger-summary-btn').click()
# sleep(2)
# passangerinfo.find_element(By.CSS_SELECTOR, 'button[data-test="add-railcard"]').click()
# sleep(2)
# passangerinfo.find_element(By.ID, 'railcardRow0').click()
# sleep(2)
# passangerinfo.find_element(By.CSS_SELECTOR, '[id*="-26-30 Railcard"]').click()
# sleep(2)
# passangerinfo.find_element(By.CSS_SELECTOR, 'button[data-test="passenger-summary-btn-done"]').click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'button[data-test="submit-journey-search-button"]').click()
# sleep(2)

url = 'https://www.greateranglia.co.uk/'

driver.get(url)

driver.find_element(By.ID, 'CybotCookiebotDialogBodyButtonDecline').click()
sleep(2)
driver.find_element(By.ID, 'from-buytlbf').send_keys('IPSWICH')
sleep(3)
box = driver.find_element(By.ID, 'listbox_from-buytlbf_container')
box.find_element(By.TAG_NAME, 'a').click()
sleep(2)
driver.find_element(By.ID, 'totlbf').send_keys('london liverpool street')
sleep(2)
box2 = driver.find_element(By.ID, 'totlbf')
box2.find_element(By.TAG_NAME, 'a').click()
sleep(2)
driver.find_element(By.ID, 'chip-return-tlbf').click()
sleep(2)
outboudndatepicker = driver.find_element(By.CLASS_NAME, 'outbound display-group-wrapper')
outboudndatepicker.find_element(By.CLASS_NAME, 'input-group').click()
sleep(2)
outboundcalendar = driver.find_element(By.CLASS_NAME,'ui-datepicker-calendar')
outboundcalendar.find_element(By.CSS_SELECTOR, 'a[data-date="9"]').click()
sleep(2)
driver.find_element(By.ID, 'out_journey_indicator_modaltlbf').click()
sleep(2)
levedepart = driver.find_element(By.CSS_SELECTOR, 'li[class="chosen-results"]')
levedepart.find_element(By.CSS_SELECTOR, 'li[data-option-array-index="1"]').click()
sleep(2)
departtimeout = driver.find_element(By.ID, 'out_time_modaltlbf_chosen')
departtimeout.click()
sleep(2)
departtimeout.find_element(By.CSS_SELECTOR, 'li[data-option-array-index="36"]').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Confirm current outbound on Tuesday, 9 January 2024 Arriving before 09:00 and close dialog"]').click()
sleep(2)
driver.find_element(By.CLASS_NAME, 'class="return display-group-wrapper"').click()
sleep(2)
driver.find_element(By.ID, 'id="ret_time_modaltlbf_chosen"').click()
returntime = driver.find_element(By.ID, 'id="ret_time_modaltlbf_chosen"')
sleep(2)
returntime.find_element(By.CSS_SELECTOR, 'li[data-option-array-index="72"]').click()
sleep(3)
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Confirm current return on Tuesday, 9 January 2024 Departing after 18:00 and close dialog"]').click()
sleep(2)
driver.find_element(By.ID, 'railcard_1_desktoptlbf_chosen').click()
sleep(2)
railcard = driver.find_element(By.ID, 'railcard_1_desktoptlbf_chosen')
railcard.find_element(By.CSS_SELECTOR, 'data-option-array-index="3"').click()
sleep(2)
submit = driver.find_element(By.ID, 'id="tls-bkf-tlbf')
submit.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
sleep(2)


sleep(60)


# url = 'https://www.thetrainline.com/book/results?origin=urn%3Atrainline%3Ageneric%3Aloc%3AIPS7217gb&destination=urn%3Atrainline%3Ageneric%3Aloc%3ALST6965gb&outwardDate=2024-01-16T09%3A00%3A00&outwardDateType=departAfter&journeySearchType=return&passengerDiscountCards%5B%5D=14192664f6d0622f48f7898f5083f82ee4cffb9b&passengers%5B%5D=1994-01-06&directSearch=false&splitSave=true&inwardDate=2024-01-16T18%3A00%3A00&inwardDateType=departAfter&selectedOutward=Khw1IaAV6Uc%3D%3AXrn7blEwoTw%3D&selectedInward=fMutf1pKozY%3D%3AgMbqBMdZ7TU%3D'
#
#
# web_driver = Service(r'C:\Users\green\Downloads\chromedriver-win32new\chromedriver-win32\chromedriver.exe')
#
# driver = webdriver.Chrome(service=web_driver)
#
# # url = 'https://www.thetrainline.com/'
#
# driver.get(url)

sleep(60)