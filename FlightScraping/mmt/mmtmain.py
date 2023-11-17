# --------------------------------------- IMPORTS -----------------------------------------------------------

import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from mmtoneway import OneWayInputs
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

        cross = DRIVER.find_element('xpath', '//div/span[@class="bgProperties  overlayCrossIcon icon20"]')
        cross.click()

        time.sleep(2)

        scroll_pos_init = DRIVER.execute_script("return window.pageYOffset;")
        stepScroll = 300

        while True:
            DRIVER.execute_script(f"window.scrollBy(0, {stepScroll});")
            scroll_pos_end = DRIVER.execute_script("return window.pageYOffset;")
            time.sleep(0.75)

            comp = DRIVER.find_elements('xpath', '//p[@class="boldFont blackText airlineName" and text()]')
            code = DRIVER.find_elements('xpath', '//p[@class="fliCode" and text()]')
            dpart = DRIVER.find_elements('xpath', '//div[contains(@class,"flexOne timeInfoLeft")]/p[contains(@class,"appendBottom2 flightTimeInfo")]/span[text()]')
            dboard = DRIVER.find_elements('xpath', '//div[contains(@class,"flexOne timeInfoRight")]/p[contains(@class,"appendBottom2 flightTimeInfo")]/span[text()]')
            durtime = DRIVER.find_elements('xpath', '//div[contains(@class, "stop-info flexOne")]/p[text()]')
            layout = DRIVER.find_elements('xpath',"//p[@class='flightsLayoverInfo' and text()]")
            price = DRIVER.find_elements('xpath', '//div[@class="blackText fontSize18 blackFont white-space-no-wrap clusterViewPrice" and text()]')

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

        DATA.to_csv('OnewayMMT.csv')





























































































































































































































































































































































































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
