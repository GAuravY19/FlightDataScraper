
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
