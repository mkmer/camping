from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver import Edge as Edge
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import msvcrt
import datetime
import os

# Modify these values for your reservation
mySites = ["151"]
days = 15
StartDate = "2022-07-11"

# Calculate the end date
EndDateDT = datetime.datetime.strptime(StartDate,"%Y-%m-%d") + datetime.timedelta(days=days)
EndDate = EndDateDT.strftime("%Y-%m-%d")

# general variables
ReserveButton = "addToStay"
site = "site-label-text"
delay = 10 #seconds
#GrandHaven beachfront
myurl = f'https://midnrreservations.com/create-booking/results?resourceLocationId=-2147483593&mapId=-2147483479&searchTabGroupId=0&bookingCategoryId=0&startDate={StartDate}&endDate={EndDate}&isReserving=true&equipmentId=-32768&subEquipmentId=-32765&partySize=4&-32761=%5B%5B1%5D,0,1%5D'
#GrandHaven back half
#myurl = f'https://midnrreservations.com/create-booking/results?resourceLocationId=-2147483593&mapId=-2147483480&searchTabGroupId=0&bookingCategoryId=0&startDate={StartDate}&endDate={EndDate}&isReserving=true&equipmentId=-32768&subEquipmentId=-32765&partySize=4&-32761=%5B%5B1%5D,0,1%5D'
#Pentwater front
#myurl = f'https://midnrreservations.com/create-booking/results?resourceLocationId=-2147483555&mapId=-2147483276&searchTabGroupId=0&bookingCategoryId=0&startDate={StartDate}&endDate={EndDate}&isReserving=true&equipmentId=-32768&subEquipmentId=-32765&partySize=4&-32761=%5B%5B1%5D,0,1%5D'
#Pentwater Back
#myurl = f'https://midnrreservations.com/create-booking/results?resourceLocationId=-2147483555&mapId=-2147483277&searchTabGroupId=0&bookingCategoryId=0&startDate={StartDate}&endDate={EndDate}&isReserving=true&equipmentId=-32768&subEquipmentId=-32765&partySize=4&-32761=%5B%5B1%5D,0,1%5D'

tabs = list(range(1,1))
# Build up the list of tabs 


driver = Edge(verbose=False,service_log_path=os.devnull)
driver.get(myurl)

#wait for consent button
try:
    consent = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,"consentButton")))
except:
    print ("I timed out  looking for consent:(")

time.sleep(2) 
action_chains = ActionChains(driver)
action_chains.move_to_element(consent).click()
action_chains.pause(1)
action_chains.perform()

#here we wait for the site map to load....
try:
    map = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CLASS_NAME,site)))
    time.sleep(2)
except:
    print ("I timed out looking for the site")


sites = driver.find_elements_by_class_name(site)
for theSite in sites: # find the site we're looking for and click on it
    if theSite.text == mySites[0]:
        action_chains = ActionChains(driver)
        action_chains.move_to_element(theSite).click()
        #action_chains.pause(1)
        action_chains.perform()
        break
NumberOfSites = len(mySites)


#Just open one tab for the "keep clicking"
#driver.execute_script("window.open(arguments[0], \
#                        arguments[1]);",("about:blank",x))
#driver.switch_to.window(driver.window_handles[(x)])
#driver.get(myurl)

#Wait for the site map to load... not quite right but I can't figure out another way....

#time.sleep(3)
#now find the reserve button
print ("start clicking")
#msvcrt.getch()
#tabs.insert(0,0)
while (True):
    #driver.switch_to.window(driver.window_handles[(x)])
    #time.sleep(1)
    try:
        reserve = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,ReserveButton)))
        action_chains = ActionChains(driver)
        action_chains.move_to_element(reserve).click()
        action_chains.perform()

    except:
        print ("I timed out  looking for reserve:(")

    try:
        close_dialog = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,"//button[.='Close']")))
        action_chains = ActionChains(driver)
        action_chains.move_to_element(close_dialog).click()
        #action_chains.pause(1)
        action_chains.perform()

    except:
        print ("I timed out  looking for close:(")
        break
#reserve = driver.find_elements_by_id(ReserveButton)


print ("Keep the broswer Open")
msvcrt.getch()




