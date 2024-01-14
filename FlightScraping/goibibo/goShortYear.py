Month = {
    'January':'Jan',
    'February':'Feb',
    'March':'Mar',
    "April":'Apr',
    'May':'May',
    'June':'June',
    'July':'July',
    'August':'Aug',
    'September':'Sept',
    'October':'Oct',
    'November':'Nov',
    'December':'Dec',
}

def shortMonths(Mon:str):

    '''
        This function is created for Converting the full name of the Months to their short forms.
    '''

    for i,j in Month.items():
        if i == Mon:
            Mon = j

    return Mon


if __name__ == "__main__":
    shortMonths
