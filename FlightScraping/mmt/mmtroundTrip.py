from mmtShortWeek import ShortWeeks
from mmtShortYear import shortMonths
import time

# ------------------------------------------ INFO FROM THE USER --------------------------------------------------------

def RoundTripInputs():
    """
    This function takes inputs for the RoundTrip Flights on MakeMyTrip.

    It returns the inputs in the following format :-
    1. SOURCECITY
    2. DESTINATIONCITY
    3. ONBOARDDATE
    4. ONBOARDDAY
    5. ONBOARDMONTH
    6. ONBOARDYEAR
    7. RETURNDATE
    8. RETURNDAY
    9. RETURNMONTH
    10. RETURNYEAR
    11. ADULTS
    12. CHILD
    13. INFANTS
    14. CLASS
    """

    SOURCECITY = input('Enter your source data : ')
    DESTINATIONCITY = input('Enter your destination data : ')

    ONBOARDDATE = int(input('Enter your onboarding date : '))
    ONBOARDDAY = input('Enter your onboarding day : ')
    ONBOARDMONTH = input('Enter your onboarding month : ')
    ONBOARDYEAR = int(input('Enter your onboarding Year : '))

    RETURNDATE = int(input('Enter your returning date : '))
    RETURNDAY = input('Enter your returning day : ')
    RETURNMONTH = input('Enter your returning month : ')
    RETURNYEAR = int(input('Enter your returning Year : '))

    ADULTS = int(input('Enter the number of adults : '))
    CHILD = int(input('Enter the number of children : '))
    INFANTS = int(input('Enter the number of infants : '))

    CLASS = input('Enter your preferred class of travel : ')

    return SOURCECITY, DESTINATIONCITY, ONBOARDDATE, ONBOARDDAY, ONBOARDMONTH, ONBOARDYEAR, RETURNDATE, RETURNDAY, RETURNMONTH, RETURNYEAR, ADULTS, CHILD, INFANTS, CLASS

# ----------------------------------------------------------------------------------------------------------------------


# # ------------------------------------------ ENTER ONBOARDING TRAVEL TIME DATA ----------------------------------------------
def Onboarding(DRIVER,DATE, DAY, MONTH, YEAR):
    monthcap = DRIVER.find_elements('xpath', '//div[@class="DayPicker-Caption"]')
    monthcapd = monthcap[0].get_attribute('innerText').split(" ")

    mydates = f"{MONTH}{YEAR}"

    while(mydates != monthcapd[0]):
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

