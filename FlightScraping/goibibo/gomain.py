# -------------------------------------- IMPORTS ---------------------------------------------------------

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gooneway import OnewayUserInputs, ScrappingGoibibo
from goCommonFunctions import SourceData, DestinationData, TravelTimeData, TrvlClsData, Search
from goroundTrip import RoundUserInputs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pandas as pd

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

    TRIPTYPE = input('Select whether you want to have "One-Way" or "Round-Way" trip : ')

# -------------------------------------------- ONEWAY TRIP ---------------------------------------------

    if TRIPTYPE.lower() == "oneway" or TRIPTYPE.lower() == 'one-way':
        FROMCITY, DESTINATIONCITY, DATE, WEEKS, MONTH, YEAR, NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, FARETYPE = OnewayUserInputs()
        SourceData(FROMCITY, DRIVER)
        DestinationData(DESTINATIONCITY, DRIVER)
        TravelTimeData(DATE, WEEKS, MONTH, YEAR, DRIVER)
        TrvlClsData(NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, DRIVER)
        Search(DRIVER)

        ScrappingGoibibo(DRIVER)

# ----------------------------------------------------------------------------------------------------



# -------------------------------------------- ROUND WAY TRIP ---------------------------------------------

    elif TRIPTYPE.lower() == "roundway" or TRIPTYPE.lower() == 'round-way':
        roundbox = DRIVER.find_element('xpath', '//ul/li/p[contains(text(), "Round-trip")]')
        roundbox.click()

        FROMCITY, DESTINATIONCITY, EMBARKDATE, EMBARKWEEKS, EMBARKMONTH, EMBARKYEAR, RETURNDATE, RETURNWEEKS, RETURNMONTH, RETURNYEAR, NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, FARETYPE = RoundUserInputs()
        SourceData(FROMCITY, DRIVER)
        DestinationData(DESTINATIONCITY, DRIVER)
        TravelTimeData(EMBARKDATE, EMBARKWEEKS, EMBARKMONTH, EMBARKYEAR, DRIVER)
        TrvlClsData(NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, DRIVER)

        returnbox = DRIVER.find_element('xpath', '//div[contains(@class, "sc-12foipm-16 wRKJm fswFld ")]/span[text() = "Return"]')
        returnbox.click()

        TravelTimeData(RETURNDATE, RETURNWEEKS, RETURNMONTH, RETURNYEAR, DRIVER)
        Search(DRIVER)

        time.sleep(20)

        scroll_pos_init = DRIVER.execute_script("return window.pageYOffset;")
        stepScroll = 300

        while True:
            DRIVER.execute_script(f"window.scrollBy(0, {stepScroll});")
            scroll_pos_end = DRIVER.execute_script("return window.pageYOffset;")
            time.sleep(0.75)

            comp = DRIVER.find_elements('xpath', '//div[contains(@class,"srp-card-uistyles__Col3-sc-3flq99-30 dZqYmo flexCol")]/span[contains(@class,"padR10 padT3")]')

            dpart = DRIVER.find_elements('xpath', '//div[contains(@class, "flexCol")]/span[contains(@class,"greyCnt lh1 padB5") and text()]')
            dpartime = DRIVER.find_elements('xpath', '//div[contains(@class, "flexCol")]/span/following-sibling::span[contains(@class,"f500 dF alignItemsCenter")]')

            dboard =DRIVER.find_elements('xpath', '//span[contains(@class,"db flexCol")]/span[contains(@class,"greyCnt padB5 lh1")]')
            dboardtime = DRIVER.find_elements('xpath', '//span[contains(@class,"db flexCol")]//span[contains(@class,"font18")]')

            layout = DRIVER.find_elements('xpath','//div[contains(@class, "srp-card-uistyles__Col5-sc-3flq99-32 hXtfxB alignSelfCenter flexCol")]/div[contains(@class,"greyCnt txtCenter lh1") and text()]')

            dur = DRIVER.find_elements('xpath', '//div[contains(@class, "srp-card-uistyles__Col5-sc-3flq99-32 hXtfxB alignSelfCenter flexCol")]/div[contains(@class,"txtCenter greyCnt lh1 padB5") and text()]')

            price = DRIVER.find_elements('xpath', '//span[contains(@class,"alignItemsCenter dF padT2 f600")]/span[contains(@class,"font18") and text()][string()]')

            print('complete 1')
            if scroll_pos_init >= scroll_pos_end:
                break
            scroll_pos_init = scroll_pos_end


        departcode = dpart[0].get_attribute('innerText')
        boardcode = dboard[0].get_attribute('innerText')

        # FROM SOURCE TO DESTINATION
        COMPANYNAMED = []
        SOURCEDEPARTURE = []
        SOURCEDEPARTURETIME = []
        SOURCEARRIVAL = []
        SOURCEARRIVALTIME = []
        SOURCEDURATION = []
        SOURCEPRICE = []
        SOURCELAYOVER = []


        # FROM DESTINATION TO SOURCE
        COMPANYNAMER = []
        RETURNDEPARTURE = []
        RETURNDEPARTURETIME = []
        RETURNARRIVAL = []
        RETURNARRIVALTIME = []
        RETURNDURATION = []
        RETURNPRICE = []
        RETURNLAYOVER = []
        DEPARTURE = []


        for i in range(len(dpart)):
            if departcode == dpart[i].get_attribute('innerText'): # is it equal BOM
                COMPANYNAMED.append(comp[i].get_attribute('innerText'))
                SOURCEDEPARTURE.append(dpart[i].get_attribute('innerText'))
                SOURCEDEPARTURETIME.append(dpartime[i].get_attribute('innerText'))
                SOURCELAYOVER.append(layout[i].get_attribute('innerText'))
                SOURCEPRICE.append(price[i].get_attribute('innerText'))
                SOURCEDURATION.append(dur[i].get_attribute('innerText'))
                SOURCEARRIVAL.append(dboard[i].get_attribute('innerText'))
                SOURCEARRIVALTIME.append(dboardtime[i].get_attribute('innerText'))

            else: # is it equal to DEL
                COMPANYNAMER.append(comp[i].get_attribute('innerText'))
                RETURNDEPARTURE.append(dpart[i].get_attribute('innerText'))
                RETURNDEPARTURETIME.append(dpartime[i].get_attribute('innerText'))
                RETURNLAYOVER.append(layout[i].get_attribute('innerText'))
                RETURNPRICE.append(price[i].get_attribute('innerText'))
                RETURNDURATION.append(dur[i].get_attribute('innerText'))
                RETURNARRIVAL.append(dboard[i].get_attribute('innerText'))
                RETURNARRIVALTIME.append(dboardtime[i].get_attribute('innerText'))



        SORDATA = {
                "Company Name": [],
                "Source city": [],
                "Departure time": [],
                "Destination City": [],
                "Arrival Time":[],
                "Duration": [],
                "Layover": [],
                "Price": []
            }

        RENDATA = {
                "Company Name": [],
                "Source city": [],
                "Departure time": [],
                "Destination City": [],
                "Arrival Time":[],
                "Duration": [],
                "Layover": [],
                "Price": []
            }


        for i in range(len(COMPANYNAMED)):
            SORDATA['Company Name'].append(COMPANYNAMED[i])
            SORDATA['Source city'].append(SOURCEDEPARTURE[i])
            SORDATA['Departure time'].append(SOURCEDEPARTURETIME[i])
            SORDATA['Destination City'].append(SOURCEARRIVAL[i])
            SORDATA['Arrival Time'].append(SOURCEARRIVALTIME[i])
            SORDATA['Layover'].append(SOURCEDURATION[i])
            SORDATA['Price'].append(SOURCEPRICE[i])

        SORDATA = pd.DataFrame.from_dict(SORDATA, orient='index')

        SORDATA = SORDATA.transpose()

        for i in range(len(COMPANYNAMER)):
            RENDATA['Company Name'].append(COMPANYNAMER[i])
            RENDATA['Source city'].append(RETURNDEPARTURE[i])
            RENDATA['Departure time'].append(RETURNDEPARTURETIME[i])
            RENDATA['Destination City'].append(RETURNARRIVAL[i])
            RENDATA['Arrival Time'].append(RETURNARRIVALTIME[i])
            RENDATA['Layover'].append(RETURNDURATION[i])
            RENDATA['Price'].append(RETURNPRICE[i])


        RENDATA = pd.DataFrame.from_dict(RENDATA, orient='index')

        RENDATA = RENDATA.transpose()

        pd.concat([SORDATA, RENDATA], axis='columns').to_csv('GoibiboRound.csv')





