# --------------------------------------------------- IMPORTS ------------------------------------------------

import time
import pandas as pd
import numpy as np

# ------------------------------------------------------------------------------------------------------------


# ------------------------------------ INFO FROM USER FOR THE TRAVEL -----------------------------------------------

def OnewayUserInputs():
    """
    it takes necessary data as inputs for search multicity trip flights

    it returns the data-variables in the format as follows :
    1. FROMCITY
    2. MIDCITY
    3. DESTINATIONCITY
    4. DATE
    5. WEEKS
    6. MONTH
    7. YEAR
    8. NUMADULTS
    9. NUMCHILDS
    10. NUMINFANTS
    11. TRAVELCLASS
    12. FARETYPE

    please frameyour variables in this format.
    """


    FROMCITY = input('Enter your source city : ')
    DESTINATIONCITY = input("Enter your destination city : ")

    DATE = int(input("Enter the date of your travel : "))
    WEEKS = input("Enter the day of your travel : ")
    MONTH = input("Enter the Month of your travel : ")
    YEAR = input("Enter the Year of your travel : ")

    NUMADULTS = int(input("Enter the number of adults : "))
    NUMCHILDS = int(input("Enter the number of Childrens : "))
    NUMINFANTS = int(input("Enter the number of infants : "))

    TRAVELCLASS = input("Enter Your Preferred Travel class : ")
    FARETYPE = input("Enter your fare type : ")

    return FROMCITY, DESTINATIONCITY, DATE, WEEKS, MONTH, YEAR, NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, FARETYPE

# -------------------------------------------------------------------------------------------------------------------



# ----------------------------------------- SCROLLING THE WEBPAGE SLOWLY ------------------------------------------------

def ScrappingGoibibo(DRIVER):
    time.sleep(20)

    scroll_pos_init = DRIVER.execute_script("return window.pageYOffset;")
    stepScroll = 300

    while True:
        DRIVER.execute_script(f"window.scrollBy(0, {stepScroll});")
        scroll_pos_end = DRIVER.execute_script("return window.pageYOffset;")
        time.sleep(0.75)

        comp = DRIVER.find_elements('xpath', '//span[contains(@class,"carrier-spritestyles__CarrierSprt-sc-18c2e6l-0 cpSzCI")]/following-sibling::span[text()]')
        dpart = DRIVER.find_elements('xpath', '//div//span[contains(@class,"srp-card-uistyles__Time-sc-3flq99-15 iHpsco padT10 f600")]')
        dboard = DRIVER.find_elements('xpath', '//div//span[contains(@class,"srp-card-uistyles__Time-sc-3flq99-15 iHpsco f500  padT10")]')
        durtime = DRIVER.find_elements('xpath', '//span[contains(@class,"srp-card-uistyles__DurTime-sc-3flq99-16 cSxcBC f500 padT10")]')
        layout = DRIVER.find_elements('xpath',"//div[contains(@class, 'srp-card-uistyles__LayoverOfferWrap-sc-3flq99-59 izbRBt dF justifyBetween ')]/div[text()]")
        price = DRIVER.find_elements('xpath', '//div[contains(@class,"srp-card-uistyles__Price-sc-3flq99-17 kxwFaC alignItemsCenter dF f600") and text()]')

        print('complete 1')
        if scroll_pos_init >= scroll_pos_end:
            break
        scroll_pos_init = scroll_pos_end

    COMPANYNAME = []
    DEPARTURETIME = []
    DEBOARDTIME = []
    DURATION = []
    LAYOVER = []
    PRICE = []

    for i in range(len(comp)):
        COMPANYNAME.append(comp[i].get_attribute('innerText'))
        DEPARTURETIME.append(dpart[i].get_attribute('innerText'))
        DEBOARDTIME.append(dboard[i].get_attribute('innerText'))
        DURATION.append(durtime[i].get_attribute('innerText'))
        LAYOVER.append(layout[i].get_attribute('innerText'))
        PRICE.append(price[i].get_attribute('innerText'))


    DATA = {
        "Company Name":[],
        "Departure Time":[],
        "Deboarding Time":[],
        "Trip Hour":[],
        "Layover":[],
        "Price":[]
    }

    for i in range(len(COMPANYNAME)):
        DATA['Company Name'].append(COMPANYNAME[i])
        DATA['Departure Time'].append(DEPARTURETIME[i])
        DATA['Deboarding Time'].append(DEBOARDTIME[i])
        DATA['Trip Hour'].append(DURATION[i])
        DATA['Layover'].append(LAYOVER[i])
        DATA['Price'].append(PRICE[i])

    DATA = pd.DataFrame(DATA)

    DATA.to_csv('OnewayGoibibo.csv')

if __name__ == "__main__":
    OnewayUserInputs
