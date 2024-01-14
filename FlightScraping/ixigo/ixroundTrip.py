import time
from MonthNum import MonthToNum
import pandas as pd

def RoundTripInputs():
    """
    This function will take inputs from the users only for roundtrip from ixigo website.

    The inputs will be returned in the following formats :
    1. SOURCECITY
    2. DESTINATIONCITY
    3. ONBOARDDATE
    4. ONBOARDMONTH
    5. ONBOARDYEAR
    6. RETURNDATE
    7. RETURNMONTH
    8. RETURNYEAR
    9. ADULTS
    10. CHILD
    11. INFANTS
    12. CLASS
    13. FARETYPE

    """

    SOURCECITY = input("Enter your source city : ")
    DESTINATIONCITY = input("Enter your destination city : ")

    ONBOARDDATE = int(input('Enter the date of onboarding : '))
    ONBOARDMONTH = input("Enter the month of onboarding : ")
    ONBOARDYEAR = int(input("Enter the year of onboarding : "))

    RETURNDATE = int(input('Enter the date of returning : '))
    RETURNMONTH = input("Enter the month of returning : ")
    RETURNYEAR = int(input("Enter the year of returning : "))

    ADULTS = int(input("Enter the number of adults : "))
    CHILD = int(input("Enter the number of children : "))
    INFANTS = int(input("Enter the number of infants : "))

    CLASS = input("Enter your preferred class of travel : ")

    FARETYPE = input("Enter if any faretype you have : ")

    return SOURCECITY, DESTINATIONCITY, ONBOARDDATE, ONBOARDMONTH, ONBOARDYEAR, RETURNDATE, RETURNMONTH, RETURNYEAR, ADULTS, CHILD, INFANTS, CLASS, FARETYPE

# ------------------------------------------------------------------------------------------------------------------



# --------------------------------------- ENTERING RETURNING TIME DATA ---------------------------------------------------------

def ReturnDate(DRIVER, ONDATE:int, REDATE:int, MONTH:str, YEAR:str):
    returnmonthhead = DRIVER.find_element('xpath', f'//button[contains(@class,"rd-back")]/following-sibling::div[text()]')
    new = returnmonthhead.get_attribute('innerText').split(" ")

    while((MONTH != new[0]) and (YEAR != new[1])):
        nextmonth = DRIVER.find_element('xpath','//button[contains(@class,"rd-next")]')
        nextmonth.click()
        new = returnmonthhead.get_attribute('innerText').split(" ")
        print(new)
        time.sleep(1)


    if ((REDATE >= 1) and (REDATE < 10)):
        date = f'0{REDATE}'
        REDATE = date

    RETURNMONTH = MonthToNum(MONTH)

    if ONDATE - REDATE > 2:
        returnmonthclick = DRIVER.find_element('xpath', f'//tr[@class="rd-days-row"]/td[contains(@data-date,"{REDATE}{RETURNMONTH}{YEAR}")]')
        returnmonthclick.click()

# ------------------------------------------------------------------------------------------------------------------


def RoundTripScraper(DRIVER):

    time.sleep(20)

    srcity = DRIVER.find_elements('xpath', '//div[contains(@class,"airport-code u-ib")]')

    time.sleep(2)

    scroll_pos_init = DRIVER.execute_script("return window.pageYOffset;")
    stepScroll = 300

    while True:
        DRIVER.execute_script(f"window.scrollBy(0, {stepScroll});")
        scroll_pos_end = DRIVER.execute_script("return window.pageYOffset;")
        time.sleep(0.75)

        # from source to destination
        srccomp = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"airline-text")]')

        srcdparttime = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"time-group")]/div[contains(@class,"time")][1]')
        srcdboardtime = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"time-group")]/div[contains(@class,"time")][2]')

        srcdur = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"duration-info")]/div[contains(@class,"duration")]')

        srclayout = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"duration-info")]/div[contains(@class,"stop")]')

        srcprice = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"c-price-display u-text-ellipsis ")]')

        # Returning

        rncomp = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"airline-text")]')

        rndparttime = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"time-group")]/div[contains(@class,"time")][1]')
        rndboardtime = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"time-group")]/div[contains(@class,"time")][2]')

        rndur = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"duration-info")]/div[contains(@class,"duration")]')

        rnlayout = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"duration-info")]/div[contains(@class,"stop")]')

        rnprice = DRIVER.find_elements('xpath', '//div[contains(@class, "result-col outr")]//div[contains(@class,"c-price-display u-text-ellipsis ")]')


        if scroll_pos_init >= scroll_pos_end:
            break
        scroll_pos_init = scroll_pos_end


    # FROM SOURCE TO DESTINATION
    SOURCECOMP = []
    SOURDEPCITY = []
    SOURDEPTIME = []
    SOURBOARDTIME = []
    SOURBOARDCITY = []
    SOURCEDUR = []
    SOURLAY = []
    SOURPR = []

    # RETURN
    RNCECOMP = []
    RNDEPTIME = []
    RNBOARDTIME = []
    RNCEDUR = []
    RNLAY = []
    RNPR = []
    RNDEPCITY = []
    RNBOARDCITY = []

    srccity = srcity[0].get_attribute('innerText')
    descity = srcity[1].get_attribute('innerText')

    for i in range(len(srccomp)):
        SOURCECOMP.append(srccomp[i].get_attribute('innerText'))
        SOURDEPTIME.append(srcdparttime[i].get_attribute('innerText'))
        SOURBOARDTIME.append(srcdboardtime[i].get_attribute('innerText'))
        SOURCEDUR.append(srcdur[i].get_attribute('innerText'))
        SOURLAY.append(srclayout[i].get_attribute('innerText'))
        SOURPR.append(srcprice[i].get_attribute('innerText'))
        SOURDEPCITY.append(srccity)
        SOURBOARDCITY.append(descity)


    for i in range(len(srccomp)):
        RNCECOMP.append(rncomp[i].get_attribute('innerText'))
        RNDEPTIME.append(rndparttime[i].get_attribute('innerText'))
        RNBOARDTIME.append(rndboardtime[i].get_attribute('innerText'))
        RNCEDUR.append(rndur[i].get_attribute('innerText'))
        RNLAY.append(rnlayout[i].get_attribute('innerText'))
        RNPR.append(rnprice[i].get_attribute('innerText'))
        RNDEPCITY.append(descity)
        RNBOARDCITY.append(srccity)


    GOING = {
    'company':[],
    'Departure City':[],
    'Departure time':[],
    'Boarding City':[],
    "Boarding time":[],
    'Duration':[],
    "Layover":[],
    "Price":[]
    }


    for i in range(len(SOURCECOMP)):
        GOING['company'].append(SOURCECOMP[i])
        GOING['Departure City'].append(SOURDEPCITY[i])
        GOING['Departure time'].append(SOURDEPTIME[i])
        GOING['Boarding City'].append(SOURBOARDCITY[i])
        GOING['Boarding time'].append(SOURBOARDTIME[i])
        GOING['Duration'].append(SOURCEDUR[i])
        GOING['Layover'].append(SOURLAY[i])
        GOING['Price'].append(SOURPR[i])


    GOING = pd.DataFrame.from_dict(GOING, orient='index')
    GOING = GOING.transpose()

    RETURN = {
    'company':[],
    'Departure City':[],
    'Departure time':[],
    'Boarding City':[],
    "Boarding time":[],
    'Duration':[],
    "Layover":[],
    "Price":[]
    }

    for i in range(len(RNCECOMP)):
        RETURN['company'].append(RNCECOMP[i])
        RETURN['Departure City'].append(RNDEPCITY[i])
        RETURN['Departure time'].append(RNDEPTIME[i])
        RETURN['Boarding City'].append(RNBOARDCITY[i])
        RETURN['Boarding time'].append(RNBOARDTIME[i])
        RETURN['Duration'].append(RNCEDUR[i])
        RETURN['Layover'].append(RNLAY[i])
        RETURN['Price'].append(RNPR[i])

    RETURN = pd.DataFrame.from_dict(RETURN, orient='index')
    RETURN = RETURN.transpose()

    FINAL = pd.concat([GOING, RETURN], axis='columns').to_csv('IxigoRound.csv')

