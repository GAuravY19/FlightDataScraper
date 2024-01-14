Week = {
    "Sunday":"Sun",
    'Monday':"Mon",
    "Tuesday":"Tue",
    "Wednesday":"Wed",
    "Thursday":"Thu",
    "Friday":"Fri",
    "Saturday":"Sat",
}

def ShortWeeks(day:str):

    '''
        This function is created for Converting the full name of the weekdays to their short forms.
    '''

    for i,j in Week.items():
        if i == day:
            day = j

    return day


if __name__ == "__main__":
    ShortWeeks
