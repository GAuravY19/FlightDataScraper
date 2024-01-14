import time
from mmtShortWeek import ShortWeeks
from mmtShortYear import shortMonths

# ------------------------------------------ ENTERING THE SOURCE DATA ----------------------------------------------

def SourceCity(DRIVER, SOURCECITY:str):

    '''
        This function is created for selecting the Source airport name.
    '''

    time.sleep(1)

    sourceboxdata = DRIVER.find_element('xpath', '//label[@for = "fromCity"]/span[@class="lbl_input appendBottom10" and text() = "From"]/following-sibling::input')
    sourceboxdata.send_keys(SOURCECITY)

    time.sleep(1)

    sourcecity = DRIVER.find_element('xpath', f'//div[@class="makeFlex hrtlCenter"]//div/p[contains(text(), "{SOURCECITY},")]')
    sourcecity.click()

# ----------------------------------------------------------------------------------------------------------------------



# ------------------------------------------ ENTER DESTINATION DATA ----------------------------------------------

def DestinationCity(DRIVER, DESTINATIONCITY:str):

    '''
        This function is created for selecting the Destination airport name.
    '''

    time.sleep(1)

    destboxdata = DRIVER.find_element('xpath', '//label[@for = "toCity"]/span[@class="lbl_input appendBottom10" and text() = "To"]/following-sibling::input')
    destboxdata.send_keys(DESTINATIONCITY)

    time.sleep(1)

    destcity = DRIVER.find_element('xpath', f'//div[@class="makeFlex hrtlCenter"]//div/p[contains(text(), "{DESTINATIONCITY},")]')
    destcity.click()

    time.sleep(1)

# ----------------------------------------------------------------------------------------------------------------------


# ------------------------------------------ ENTER TRAVEL TIME DATA ----------------------------------------------

def TravelTime(DRIVER, DATE:int, DAY:str, MONTH:str, YEAR:int):

    '''
        This function is created for selecting the departure schedule.
    '''

    monthcap = DRIVER.find_elements('xpath', '//div[@class="DayPicker-Caption"]')
    monthcapd = monthcap[0].get_attribute('innerText').split(" ")

    while(MONTH != monthcapd[0] and YEAR != monthcapd[1]):
        DRIVER.find_element('xpath', '//div[@class="DayPicker-NavBar"]/span[@class="DayPicker-NavButton DayPicker-NavButton--next"]').click() # next button click
        monthcapd = monthcap[0].get_attribute('innerText').split(" ")
        print(monthcapd)
        time.sleep(1)

    if DATE >= 1 and DATE < 10:
        date = f'0{DATE}'
        DATE = date

    DAY = ShortWeeks(DAY)
    MONTH = shortMonths(MONTH)

    time.sleep(1)

    dayclick = DRIVER.find_element('xpath', f'//div[@class="DayPicker-Day" and @aria-label = "{DAY} {MONTH} {DATE} {YEAR}"]')
    dayclick.click()

# ----------------------------------------------------------------------------------------------------------------------



# ------------------------------------------ ENTERING TRAVELLERS DATA ----------------------------------------------

def TravelClass(DRIVER, ADULTS:int, CHILD:int, INFANTS:int, CLASS:str):

    '''
        This function is created for selecting the travel class information.
    '''


    trvlbox = DRIVER.find_element('xpath', '//label[@for = "travellers"]//span[contains(text(), "Travellers")]')
    trvlbox.click()

    if ADULTS > 1:
        adult = DRIVER.find_element('xpath', f'//ul[@class="guestCounter font12 darkText gbCounter"]/li[@data-cy="adults-{ADULTS}"]')
        adult.click()

    if CHILD > 0:
        child = DRIVER.find_element('xpath', f'//ul[@class="guestCounter font12 darkText gbCounter"]/li[@data-cy="children-{CHILD}"]')
        child.click()

    if INFANTS > 0:
        infant = DRIVER.find_element('xpath', f'//ul[@class="guestCounter font12 darkText gbCounter"]/li[@data-cy="infants-{INFANTS}"]')
        infant.click()

    if CLASS.lower() == 'economy':
        trvlcls = DRIVER.find_element('xpath', '//li[@data-cy="travelClass-0"]')
        trvlcls.click()

    elif CLASS.lower() == 'business':
        trvlcls = DRIVER.find_element('xpath', '//li[@data-cy="travelClass-2"]')
        trvlcls.click()

    elif CLASS.lower() == 'premium economy':
        trvlcls = DRIVER.find_element('xpath', '//li[@data-cy="travelClass-1"]')
        trvlcls.click()

    apply = DRIVER.find_element('xpath', '//button[@class="primaryBtn btnApply pushRight" and text() = "APPLY"]')
    apply.click()

# ----------------------------------------------------------------------------------------------------------------------




# ------------------------------------------ SUBMIT BUTTON ----------------------------------------------

def submit(DRIVER):

    '''
        This function is created for clicking on the search button.
    '''

    searchbtn = DRIVER.find_element('xpath', '//p[@data-cy="submit"]//a[@class="primaryBtn font24 latoBold widgetSearchBtn " and text() = "Search"]')
    searchbtn.click()

# ----------------------------------------------------------------------------------------------------------------------




