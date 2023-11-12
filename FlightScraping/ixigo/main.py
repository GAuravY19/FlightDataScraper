# ------------------------------------------------ IMPORTS --------------------------------------------------------

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# -----------------------------------------------------------------------------------------------------------------



# ---------------------------------------------- SELENIUM SETUP ---------------------------------------------------

options = Options()
options.add_experimental_option('detach', True)

os.environ['PATH'] = r'D:/WebScrapping/WebDrivers/'

DRIVER = webdriver.Chrome(options=options)

DRIVER.get('https://www.ixigo.com/flights')

DRIVER.maximize_window()

# ------------------------------------------------------------------------------------------------------------------



# --------------------------------------- INFO FROM USER ---------------------------------------------------------

# TRIPTYPE = input("Enter the trip type : ")

SOURCECITY = input("Enter your source city : ")
DESTINATIONCITY = input("Enter your destination city : ")

DATE = int(input('Enter the date of onboarding : '))
MONTH = input("Enter the month of onboarding : ")
YEAR = int(input("Enter the year of onboarding : "))

ADULTS = int(input("Enter the number of adults : "))
CHILD = int(input("Enter the number of children : "))
INFANTS = int(input("Enter the number of infants : "))

CLASS = input("Enter your preferred class of travel : ")

FARETYPE = input("Enter if any faretype you have : ")

# ------------------------------------------------------------------------------------------------------------------



# --------------------------------------------- ENTERING SOURCE DATA --------------------------------------------------------
sourcebox = DRIVER.find_element('xpath','//div[@class="c-input-cntr"]/div[contains(text(),"From")]')
sourcebox.click()

time.sleep(1)

sourceboxdata = DRIVER.find_element('xpath', '//div[contains(text(),"From")]/following-sibling::input[contains(@value,"")]')
sourceboxdata.send_keys(SOURCECITY)

time.sleep(1)

firstsource = DRIVER.find_element('xpath', f'//div[@class="city-row "]/div[contains(text(), "{SOURCECITY.title()}")]')
firstsource.click()

time.sleep(1)
# ------------------------------------------------------------------------------------------------------------------



# --------------------------------------------- ENTERING DESTINATION DATA --------------------------------------------------------

destboxdata = DRIVER.find_element('xpath', '//div[contains(text(), "To")]/following-sibling::input')
destboxdata.send_keys(DESTINATIONCITY)

destboxdata = DRIVER.find_element('xpath', f'//div[@class="city-row "]/div[contains(text(), "{DESTINATIONCITY.title()}")]')
destboxdata.click()

# ------------------------------------------------------------------------------------------------------------------


# ----------------------------------------- ENTER THE TRAVEL TIME DATA --------------------------------------------------------

monthhead = DRIVER.find_element('xpath', f'//button[contains(@class,"rd-back")]/following-sibling::div[text()]')
new = monthhead.get_attribute('innerText').split(" ")

while((MONTH != new[0]) and (YEAR != new[1])):
    nextmonth = DRIVER.find_element('xpath','//button[contains(@class,"rd-next")]')
    nextmonth.click()
    new = monthhead.get_attribute('innerText').split(" ")
    print(new)
    time.sleep(1)

# ------------------------------------- MONTH TO NUMBER -----------------------------------------------------------

month = {
    "January":"01",
    "Febuary":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}


def MonthToNum(MONTH:str, month:dict):
    for i,j in month.items():
        if i == MONTH:
            MONTH = j

    return MONTH

MONTH = MonthToNum(MONTH,month)

# ------------------------------------------------------------------------------------------------------------------

if ((DATE >= 1) and (DATE < 10)):
    date = f'0{DATE}'
    DATE = date

monthclick = DRIVER.find_element('xpath', f'//tr[@class="rd-days-row"]/td[contains(@data-date,"{DATE}{MONTH}{YEAR}")]')
monthclick.click()

# ------------------------------------------------------------------------------------------------------------------


# --------------------------------------------- ENTER PASSENGER DATA ------------------------------------------------

if ADULTS > 1:
    adultsbox = DRIVER.find_element('xpath', f'//span[@class="counter-item u-text-center u-ib current" and @data-val="1"]/following-sibling::span[@data-val="{ADULTS}"]')
    adultsbox.click()

if CHILD > 0:
    childbox = DRIVER.find_element('xpath', f"//span[@class='counter-item u-text-center u-ib current' and @data-val='0']/following-sibling::span[@data-val='{CHILD}']")
    childbox.click()

if INFANTS > 0:
    infantbox = DRIVER.find_element('xpath', f'//span[@class="counter-item u-text-center u-ib" and @data-val="1"]/following-sibling::span[@class="counter-item u-text-center u-ib disabled"]')
    infantbox.click()


time.sleep(1)

economysel = DRIVER.find_element('xpath', f'//span[@class = "label u-pos-rel u-ib u-v-align-top" and (text()="{CLASS}")]')
economysel.click()

search = DRIVER.find_element('xpath','//button[contains(text(), "Search")]')
search.click()


print("succssful")
