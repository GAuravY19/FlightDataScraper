# --------------------------------------------------- IMPORTS ------------------------------------------------

import time
import pandas as pd
import numpy as np

# ------------------------------------------------------------------------------------------------------------



# -------------------------------------- INFO FROM USER FOR THE TRAVEL ------------------------------------------

def UserInputs():
    """
    it takes necessary data as inputs for search multicity trip flights

    it returns the data-variables in the format as follows :
    1. FROMCITY
    2. MIDCITY
    3. DESTINATIONCITY
    4. FIRSTDATE
    5. FIRSTWEEKS
    6. FIRSTMONTH
    7. FIRSTYEAR
    8. SECONDDATE
    9. SECONDWEEKS
    10. SECONDMONTH
    11. SECONDYEAR
    12. NUMADULTS
    13. NUMCHILDS
    14. NUMINFANTS
    15. TRAVELCLASS
    16. FARETYPE

    please frameyour variables in this format.
    """

    FROMCITY = input('Enter your source city : ')
    MIDCITY = input(f"Enter the next city from {FROMCITY} : ")
    DESTINATIONCITY = input(f"Enter your next city {MIDCITY}: ")

    FIRSTDATE = int(input(f"Enter the onboarding date from {FROMCITY} to {MIDCITY} your travel : "))
    FIRSTWEEKS = input(f"Enter the onboarding day from {FROMCITY} to {MIDCITY} your travel : ")
    FIRSTMONTH = input(f"Enter the onboarding Month from {FROMCITY} to {MIDCITY} your travel : ")
    FIRSTYEAR = input(f"Enter the onboarding Year from {FROMCITY} to {MIDCITY} your travel : ")

    SECONDDATE = int(input(f"Enter the returning date from {MIDCITY} t0 {DESTINATIONCITY} your travel : "))
    SECONDWEEKS = input(f"Enter the returning day from {MIDCITY} t0 {DESTINATIONCITY}  your travel : ")
    SECONDMONTH = input(f"Enter the returning Month from {MIDCITY} t0 {DESTINATIONCITY}  your travel : ")
    SECONDYEAR = input(f"Enter the returning Year from {MIDCITY} t0 {DESTINATIONCITY}  your travel : ")

    NUMADULTS = int(input("Enter the number of adults : "))
    NUMCHILDS = int(input("Enter the number of Childrens : "))
    NUMINFANTS = int(input("Enter the number of infants : "))

    TRAVELCLASS = input("Enter Your Preferred Travel class : ")
    FARETYPE = input("Enter your fare type : ")

    return FROMCITY, MIDCITY, DESTINATIONCITY, FIRSTDATE, FIRSTWEEKS, FIRSTMONTH, FIRSTYEAR, SECONDDATE, SECONDMONTH, SECONDWEEKS, SECONDYEAR, NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, FARETYPE

# ------------------------------------------------------------------------------------------------------------


# --------------------------------------------- ENTERING MIDCITY DATA -------------------------------------------------------

def MidCityBox(MIDCITY:str, DRIVER):
    MidTextBox = DRIVER.find_element('xpath', '//div/span[contains(text(),"To")]/following-sibling::input')
    MidTextBox.send_keys(MIDCITY)

    time.sleep(1)

    MidBoxSelect = DRIVER.find_element('xpath', '//span[contains(@class, "autoCompleteTitle")]')
    MidBoxSelect.click()

    time.sleep(1)

# ------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    UserInputs
    MidCityBox
