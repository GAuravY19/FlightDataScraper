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
    for i,j in Month.items():
        if i == Mon:
            Mon = j

    return Mon


if __name__ == "__main__":
    shortMonths
