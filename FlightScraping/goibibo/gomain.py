# -------------------------------------- IMPORTS ---------------------------------------------------------

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gooneway import OnewayUserInputs
from goCommonFunctions import SourceData, DestinationData, TravelTimeData, TrvlClsData, FareType, Search
from goroundTrip import RoundUserInputs
# --------------------------------------------------------------------------------------------------------

def ClearDiaBox():
    try:
        dialogCross = DRIVER.find_element('xpath', '//div//span[@class = "logSprite icClose"]')
        dialogCross.click()

    except:
        print('The Box was not found')


if __name__ == "__main__":
# -------------------------------------------- DRIVER SETUP ---------------------------------------------

    options = Options()
    options.add_experimental_option('detach', True)

    os.environ['PATH'] = r'D:/WebScrapping/WebDrivers/'

    DRIVER = webdriver.Chrome(options=options)

    DRIVER.get('https://www.goibibo.com/')

    DRIVER.maximize_window()

    ClearDiaBox()

# ----------------------------------------------------------------------------------------------------

    TRIPTYPE = input('Select whether you want to have "One-Way" or "Round-Way" or "Multi-way" trip : ')

    if TRIPTYPE.lower() == "oneway" or TRIPTYPE.lower() == 'one-way':
        FROMCITY, DESTINATIONCITY, DATE, WEEKS, MONTH, YEAR, NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, FARETYPE = OnewayUserInputs()
        SourceData(FROMCITY, DRIVER)
        DestinationData(DESTINATIONCITY, DRIVER)
        TravelTimeData(DATE, WEEKS, MONTH, YEAR, DRIVER)
        TrvlClsData(NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, DRIVER)
        FareType(FARETYPE, DRIVER)
        Search(DRIVER)




    elif TRIPTYPE.lower() == "roundway" or TRIPTYPE.lower() == 'round-way':
        roundbox = DRIVER.find_element('xpath', '//ul/li/p[contains(text(), "Round-trip")]')
        roundbox.click()

        FROMCITY, DESTINATIONCITY, EMBARKDATE, EMBARKWEEKS, EMBARKMONTH, EMBARKYEAR, RETURNDATE, RETURNWEEKS, RETURNMONTH, RETURNYEAR, NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, FARETYPE = RoundUserInputs()
        SourceData(FROMCITY, DRIVER)
        DestinationData(DESTINATIONCITY, DRIVER)
        TravelTimeData(EMBARKDATE, EMBARKWEEKS, EMBARKMONTH, EMBARKYEAR, DRIVER)

        returnbox = DRIVER.find_element('xpath', '//div/span[@class="fswFld__heading" and text()="Return"]')
        returnbox.click()

        TravelTimeData(RETURNDATE, RETURNWEEKS, RETURNMONTH, RETURNYEAR, DRIVER)
        TrvlClsData(NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, DRIVER)
        FareType(FARETYPE, DRIVER)
        Search(DRIVER)
