# --------------------------------------------------- IMPORTS ------------------------------------------------

import time
import pandas as pd
import numpy as np

# ------------------------------------------------------------------------------------------------------------


# ------------------------------------ INFO FROM USER FOR THE TRAVEL -----------------------------------------------

def OnewayUserInputs():
    """
    it takes necessary data as inputs for search multicity trip flights

    it returns the data-variables in the format as follows :
    1. FROMCITY
    2. MIDCITY
    3. DESTINATIONCITY
    4. DATE
    5. WEEKS
    6. MONTH
    7. YEAR
    8. NUMADULTS
    9. NUMCHILDS
    10. NUMINFANTS
    11. TRAVELCLASS
    12. FARETYPE

    please frameyour variables in this format.
    """


    FROMCITY = input('Enter your source city : ')
    DESTINATIONCITY = input("Enter your destination city : ")

    DATE = int(input("Enter the date of your travel : "))
    WEEKS = input("Enter the day of your travel : ")
    MONTH = input("Enter the Month of your travel : ")
    YEAR = input("Enter the Year of your travel : ")

    NUMADULTS = int(input("Enter the number of adults : "))
    NUMCHILDS = int(input("Enter the number of Childrens : "))
    NUMINFANTS = int(input("Enter the number of infants : "))

    TRAVELCLASS = input("Enter Your Preferred Travel class : ")
    FARETYPE = input("Enter your fare type : ")

    return FROMCITY, DESTINATIONCITY, DATE, WEEKS, MONTH, YEAR, NUMADULTS, NUMCHILDS, NUMINFANTS, TRAVELCLASS, FARETYPE

# -------------------------------------------------------------------------------------------------------------------



# ----------------------------------------- SCROLLING THE WEBPAGE SLOWLY ------------------------------------------------
# scroll_pos_init = DRIVER.execute_script("return window.pageYOffset;")
# stepScroll = 300

# while True:
#     DRIVER.execute_script(f"window.scrollBy(0, {stepScroll});")
#     scroll_pos_end = DRIVER.execute_script("return window.pageYOffset;")
#     time.sleep(0.75)

#     print('complete 1')
#     if scroll_pos_init >= scroll_pos_end:
#         break
#     scroll_pos_init = scroll_pos_end

# -------------------------------------------------------------------------------------------------------------------



# ---------------------------------- CREATING OF THE DATASET ------------------------------------------------

DATA = {
    "Company Name":[],
    "Source Code":[],
    "Source Time":[],
    "Destination Code":[],
    "Destination Time":[],
    "Trip Hour":[],
    "Price":[]
}

OneWay = pd.DataFrame(DATA)

# -------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    OnewayUserInputs
