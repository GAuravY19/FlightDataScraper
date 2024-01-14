import time
from MonthNum import MonthToNum

# --------------------------------------- ENTERING SOURCE DATA ---------------------------------------------------------

def SourceCity(DRIVER, SOURCECITY:str):

    '''
        This function is created for selecting the Source airports name.
    '''

    sourcebox = DRIVER.find_element('xpath','//div[@class="c-input-cntr"]/div[contains(text(),"From")]')
    sourcebox.click()

    time.sleep(1)

    sourceboxdata = DRIVER.find_element('xpath', '//div[contains(text(),"From")]/following-sibling::input[contains(@value,"")]')
    sourceboxdata.send_keys(SOURCECITY)

    time.sleep(1)

    firstsource = DRIVER.find_element('xpath', f'//div[@class="city-row "]/div[contains(text(), "{SOURCECITY.title()}")]')
    firstsource.click()

    time.sleep(1)

# ------------------------------------------------------------------------------------------------------------------



# --------------------------------------- ENTERING DESTINATION DATA ---------------------------------------------------------

def DestinationCity(DRIVER, DESTINATIONCITY:str):

    '''
        This function is created for selecting the Destination airports name.
    '''

    destboxdata = DRIVER.find_element('xpath', '//div[contains(text(), "To")]/following-sibling::input')
    destboxdata.send_keys(DESTINATIONCITY)

    time.sleep(1)

    destboxdata = DRIVER.find_element('xpath', f'//div[@class="city-row "]/div[contains(text(), "{DESTINATIONCITY.title()}")]')
    destboxdata.click()

# ------------------------------------------------------------------------------------------------------------------


# --------------------------------------------- ENTER PASSENGER DATA ------------------------------------------------

def PassengerData(DRIVER, ADULTS:int, CHILD:int, INFANTS:int, CLASS:str):

    '''
        This function is created for selecting the passenger data.
    '''


    try:
        trvlclas = DRIVER.find_element('xpath','//div[@class="c-input-cntr"]/label[@class="input-label" and text() = "Travellers | Class"]')
        trvlclas.click()
    except:
        pass


    if ADULTS > 1:
        adultsbox = DRIVER.find_element('xpath', f'//span[@class="counter-item u-text-center u-ib current" and @data-val="1"]/following-sibling::span[@data-val="{ADULTS}"]')
        adultsbox.click()

    if CHILD > 0:
        childbox = DRIVER.find_element('xpath', f"//span[@class='counter-item u-text-center u-ib current' and @data-val='0']/following-sibling::span[@data-val='{CHILD}']")
        childbox.click()

    if INFANTS > 0:
        infantbox = DRIVER.find_element('xpath', f'//span[@class="counter-item u-text-center u-ib" and @data-val="1"]/following-sibling::span[@class="counter-item u-text-center u-ib disabled"]')
        infantbox.click()


    time.sleep(1)

    economysel = DRIVER.find_element('xpath', f'//span[@class = "label u-pos-rel u-ib u-v-align-top" and (text()="{CLASS}")]')
    economysel.click()

# ------------------------------------------------------------------------------------------------------------------



# --------------------------------------------- START SEARCHING FOR DATA ------------------------------------------------
def Search(DRIVER):

    '''
        This function is created for clicking on the search button.
    '''

    search = DRIVER.find_element('xpath','//button[contains(text(), "Search")]')
    search.click()

# ------------------------------------------------------------------------------------------------------------------


# --------------------------------------- ENTERING ONBOARDING TIME DATA ---------------------------------------------------------

def OnboardingDate(DRIVER, DATE:int, MONTH:str, YEAR:str):

    '''
        This function is created for selecting the schedules of the passengers.
    '''

    onboarmonthhead = DRIVER.find_element('xpath', f'//button[contains(@class,"rd-back")]/following-sibling::div[text()]')
    new = onboarmonthhead.get_attribute('innerText').split(" ")

    while((MONTH != new[0]) and (YEAR != new[1])):
        nextmonth = DRIVER.find_element('xpath','//button[contains(@class,"rd-next")]')
        nextmonth.click()
        new = onboarmonthhead.get_attribute('innerText').split(" ")
        print(new)
        time.sleep(1)


    if ((DATE >= 1) and (DATE < 10)):
        date = f'0{DATE}'
        DATE = date

    ONBOARDMONTH = MonthToNum(MONTH)

    onboardmonthclick = DRIVER.find_element('xpath', f'//tr[@class="rd-days-row"]/td[contains(@data-date,"{DATE}{ONBOARDMONTH}{YEAR}")]')
    onboardmonthclick.click()

    time.sleep(1)

# ------------------------------------------------------------------------------------------------------------------
