import time
from MonthNum import MonthToNum

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

    RETURNMONTH = MonthToNum(RETURNMONTH)

    if ONDATE - REDATE > 2:
        returnmonthclick = DRIVER.find_element('xpath', f'//tr[@class="rd-days-row"]/td[contains(@data-date,"{REDATE}{RETURNMONTH}{YEAR}")]')
        returnmonthclick.click()

# ------------------------------------------------------------------------------------------------------------------
