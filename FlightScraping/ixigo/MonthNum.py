# ------------------------------------- MONTH TO NUMBER -----------------------------------------------------------

month = {
    "January":"01",
    "Febuary":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}


def MonthToNum(MONTH:str):

    '''
        This function was created for converting the months to their numerical equivalent.
    '''

    for i,j in month.items():
        if i == MONTH:
            MONTH = j

    return MONTH


# ------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    MonthToNum
