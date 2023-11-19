# --------------------------------------- IMPORTS -----------------------------------------------------------

import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from mmtoneway import OneWayInputs, OnewayScrapper
from mmtCommonFunctions import SourceCity, DestinationCity, TravelTime, TravelClass, submit
from mmtroundTrip import RoundTripInputs, Onboarding
import time

# ------------------------------------------------------------------------------------------------------------




if __name__ == "__main__":

    # ------------------------------------------- SELENIUM SETUP ------------------------------------------------

    options = Options()
    options.add_experimental_option('detach', True)

    os.environ['PATH'] = r'D:/WebScrapping/WebDrivers/'

    DRIVER = webdriver.Chrome(options=options)
    DRIVER.get('https://www.makemytrip.com/')
    DRIVER.maximize_window()

    time.sleep(7)
    x = 196
    y = 440

    action = ActionChains(DRIVER)
    action.move_by_offset(x,y).click().perform()

    time.sleep(2)

    dialogbx = DRIVER.find_element('xpath', "//span[@class='commonModal__close']")
    dialogbx.click()

    # ----------------------------------------------------------------------------------------------------------


    TRIPTYPE = input("Enter the trip type : ")

    if TRIPTYPE.lower() == "oneway":
        SOURCECITY, DESTINATIONCITY, DATE, DAY, MONTH, YEAR, ADULTS, CHILD, INFANTS, CLASS = OneWayInputs()

        SourceCity(DRIVER, SOURCECITY)
        DestinationCity(DRIVER, DESTINATIONCITY)
        TravelTime(DRIVER, DATE, DAY, MONTH, YEAR)
        TravelClass(DRIVER, ADULTS, CHILD, INFANTS, CLASS)
        submit(DRIVER)

        time.sleep(20)

        try:
            cross = DRIVER.find_element('xpath', '//div/span[@class="bgProperties  overlayCrossIcon icon20"]')
            cross.click()

        except:
            pass


        OnewayScrapper(DRIVER)






























































































































































































































































































































































































    elif TRIPTYPE.lower() == 'roundtrip':

        round = DRIVER.find_element('xpath', '//li[@data-cy = "roundTrip"]/span')
        round.click()

        SOURCECITY, DESTINATIONCITY, ONBOARDDATE, ONBOARDDAY, ONBOARDMONTH, ONBOARDYEAR, RETURNDATE, RETURNDAY, RETURNMONTH, RETURNYEAR, ADULTS, CHILD, INFANTS, CLASS = RoundTripInputs()

        SourceCity(DRIVER, SOURCECITY)
        DestinationCity(DRIVER, DESTINATIONCITY)
        Onboarding(DRIVER, ONBOARDDATE, ONBOARDDAY, ONBOARDMONTH, ONBOARDYEAR)
        Onboarding(DRIVER, RETURNDATE, RETURNDAY, RETURNMONTH,RETURNYEAR)
        TravelClass(DRIVER, ADULTS, CHILD, INFANTS, CLASS)
        submit(DRIVER)
