import time
import pandas as pd
# --------------------------------------- INFO FROM USER ---------------------------------------------------------

# TRIPTYPE = input("Enter the trip type : ")
def OneWayInputs():
    """
    This function will take inputs from the users only for roundtrip from ixigo website.

    The inputs will be returned in the following formats :
    1. SOURCECITY
    2. DESTINATIONCITY
    3. DATE
    4. MONTH
    5. YEAR
    6. ADULTS
    7. CHILD
    8. INFANTS
    9. CLASS

    """
    SOURCECITY = input("Enter your source city : ")
    DESTINATIONCITY = input("Enter your destination city : ")

    DATE = int(input('Enter the date of onboarding : '))
    MONTH = input("Enter the month of onboarding : ")
    YEAR = int(input("Enter the year of onboarding : "))

    ADULTS = int(input("Enter the number of adults : "))
    CHILD = int(input("Enter the number of children : "))
    INFANTS = int(input("Enter the number of infants : "))

    CLASS = input("Enter your preferred class of travel : ")

    return SOURCECITY, DESTINATIONCITY, DATE, MONTH, YEAR, ADULTS, CHILD, INFANTS, CLASS

# ------------------------------------------------------------------------------------------------------------------


def ScrapingIxigoOneway(DRIVER):

    '''
        This function is created for scrapping the One way data.
    '''

    time.sleep(20)

    scroll_pos_init = DRIVER.execute_script("return window.pageYOffset;")
    stepScroll = 300

    while True:
        DRIVER.execute_script(f"window.scrollBy(0, {stepScroll});")
        scroll_pos_end = DRIVER.execute_script("return window.pageYOffset;")
        time.sleep(0.75)

        comp = DRIVER.find_elements('xpath', '//div[@class="u-uppercase u-text-ellipsis" and text()]')
        dpart = DRIVER.find_elements('xpath', '//div[@class="left-wing"]/div[@class="time" and text()]')
        dboard = DRIVER.find_elements('xpath', '//div[@class="right-wing"]/div[@class="time" and text()]')
        durtime = DRIVER.find_elements('xpath', '//div[@class="label tl " and text()]')
        layout = DRIVER.find_elements('xpath','//div[@class="label br " and text()]')
        price = DRIVER.find_elements('xpath', '//div[contains(@class,"c-price-display")]/span[@class="" and text()]')

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

    DATA.to_csv('OnewayIxigo.csv')
