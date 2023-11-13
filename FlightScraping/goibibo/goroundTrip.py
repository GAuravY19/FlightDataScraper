# --------------------------------------------------- IMPORTS ------------------------------------------------

import time
import pandas as pd
import numpy as np

# ------------------------------------------------------------------------------------------------------------



# -------------------------------------- INFO FROM USER FOR THE TRAVEL ------------------------------------------

def RoundUserInputs():
    """
    it takes necessary data as inputs for search multicity trip flights

    it returns the data-variables in the format as follows :
    1. FROMCITY
    2. MIDCITY
    3. DESTINATIONCITY
    4. EMBARKDATE
    5. EMBARKWEEKS
    6. EMBARKMONTH
    7. EMBARKYEAR
    8. RETURNDATE
    9. RETURNWEEKS
    10. RETURNMONTH
    11. RETURNYEAR
    12. NUMADULTS
    13. NUMCHILDS
    14. NUMINFANTS
    15. TRAVELCLASS
    16. FARETYPE

    please frameyour variables in this format.
    """
    FROMCITY = input('Enter your source city : ')
    DESTINATIONCITY = input("Enter your destination city : ")

    EMBARKDATE = int(input("Enter the onboarding date of your travel : "))
    EMBARKWEEKS = input("Enter the onboarding day of your travel : ")
    EMBARKMONTH = input("Enter the onboarding Month of your travel : ")
    EMBARKYEAR = input("Enter the onboarding Year of your travel : ")

    RETURNDATE = int(input("Enter the returning date of your travel : "))
    RETURNWEEKS = input("Enter the returning day of your travel : ")
    RETURNMONTH = input("Enter the returning Month of your travel : ")
    RETURNYEAR = input("Enter the returning Year of your travel : ")

    NUMADULTS = int(input("Enter the number of adults : "))
    NUMCHILDS = int(input("Enter the number of Childrens : "))
    NUMINFANTS = int(input("Enter the number of infants : "))

    TRAVELCLASS = input("Enter Your Preferred Travel class : ")
    FARETYPE = input("Enter your fare type : ")

    return FROMCITY, DESTINATIONCITY, EMBARKDATE, EMBARKWEEKS, EMBARKMONTH, EMBARKYEAR, RETURNDATE, RETURNWEEKS, RETURNMONTH, RETURNYEAR, NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, FARETYPE

# ------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    RoundUserInputs
