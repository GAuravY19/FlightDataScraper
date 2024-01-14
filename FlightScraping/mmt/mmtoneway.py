import time
import pandas as pd


# ------------------------------------------ INFO FROM THE USER --------------------------------------------------------

def OneWayInputs():
    """
    This function takes inputs for the One Way trip for the MakeMyTrip website.

    It returns the Input data in the following format:
    1. SOURCECITY
    2. DESTINATIONCITY
    3. DATE
    4. DAY
    5. MONTH
    6. YEAR
    7. ADULTS
    8. CHILD
    9. INFANTS
    10. CLASS

    please maintain this flow for proper inputs extraction.
    """
    SOURCECITY = input('Enter your source data : ')
    DESTINATIONCITY = input('Enter your destination data : ')

    DATE = int(input('Enter your onboarding date : '))
    DAY = input('Enter your onboarding day : ')
    MONTH = input('Enter your onboarding month : ')
    YEAR = int(input('Enter your onboarding Year : '))

    ADULTS = int(input('Enter the number of adults : '))
    CHILD = int(input('Enter the number of children : '))
    INFANTS = int(input('Enter the number of infants : '))

    CLASS = input('Enter your preferred class of travel : ')

    return SOURCECITY, DESTINATIONCITY, DATE, DAY, MONTH, YEAR, ADULTS, CHILD, INFANTS, CLASS

# ----------------------------------------------------------------------------------------------------------------------



#

def OnewayScrapper(DRIVER):

    '''
        This function scraps the data for one way trip.
    '''

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





