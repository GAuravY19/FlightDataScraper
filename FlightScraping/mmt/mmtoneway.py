
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






