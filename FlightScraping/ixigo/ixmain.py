# ------------------------------------------------ IMPORTS --------------------------------------------------------

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from ixroundTrip import RoundTripInputs, ReturnDate
from ixcommonFunctions import SourceCity, DestinationCity, OnboardingDate, PassengerData, Search
from ixoneway import OneWayInputs, ScrapingIxigoOneway
import pandas as pd
import time


# -----------------------------------------------------------------------------------------------------------------






if __name__ == "__main__":
    # ---------------------------------------------- SELENIUM SETUP ---------------------------------------------------

    options = Options()
    options.add_experimental_option('detach', True)

    os.environ['PATH'] = r'D:/WebScrapping/WebDrivers/'

    DRIVER = webdriver.Chrome(options=options)

    DRIVER.get('https://www.ixigo.com/flights')

    DRIVER.maximize_window()

    # ------------------------------------------------------------------------------------------------------------------

    time.sleep(3)

    TRIPTYPE = input("Enter the trip type : ")

    if TRIPTYPE.lower() == 'oneway' or TRIPTYPE.lower() == 'one-way':
        SOURCECITY, DESTINATIONCITY, DATE, MONTH, YEAR, ADULTS, CHILD, INFANTS, CLASS = OneWayInputs()

        SourceCity(DRIVER, SOURCECITY)
        DestinationCity(DRIVER, DESTINATIONCITY)
        OnboardingDate(DRIVER, DATE, MONTH, YEAR)
        PassengerData(DRIVER, ADULTS, CHILD, INFANTS, CLASS)
        Search(DRIVER)

        ScrapingIxigoOneway(DRIVER)






































































































































































































































































































    elif TRIPTYPE.lower() == 'roundtrip' or TRIPTYPE.lower() == 'round-trip':
        # INPUTS FROM THE USER
        SOURCECITY, DESTINATIONCITY, ONBOARDDATE, ONBOARDMONTH, ONBOARDYEAR, RETURNDATE, RETURNMONTH, RETURNYEAR, ADULTS, CHILD, INFANTS, CLASS, FARETYPE = RoundTripInputs()

        # --------------------------------------- SELECTING ROUND TRIP ---------------------------------------------------------

        roundtripbox = DRIVER.find_element('xpath', "//span[@class='nav-list-item u-ib u-uppercase' and text() = 'Round Trip']")
        roundtripbox.click()

        # ------------------------------------------------------------------------------------------------------------------


        # --------------------------------------- ENTERING SOURCE DATA ---------------------------------------------------------

        SourceCity(DRIVER, SOURCECITY)
        DestinationCity(DRIVER, DESTINATIONCITY)
        OnboardingDate(DRIVER, ONBOARDDATE, ONBOARDMONTH, ONBOARDYEAR)
        ReturnDate(DRIVER, ONBOARDDATE, RETURNDATE, RETURNMONTH, RETURNYEAR)
        PassengerData(DRIVER, ADULTS, CHILD, INFANTS, CLASS)
        Search(DRIVER)
