import time
from ShortWeek import ShortWeeks
from ShortYear import shortMonths

def SourceData(FROMCITY:str, DRIVER):
    FirstBox = DRIVER.find_element('xpath','//div/span[contains(text(),"From")]/following-sibling:: p[@class="sc-12foipm-20 bhnHeQ"]')
    FirstBox.click()

    time.sleep(1)

    FirstBoxText = DRIVER.find_element('xpath','//div//span[contains(text(), "From")]/following-sibling::input')
    FirstBoxText.send_keys(FROMCITY)

    time.sleep(1)

    FirstBoxSelect = DRIVER.find_element('xpath','//span[contains(@class, "autoCompleteTitle")]')
    FirstBoxSelect.click()

    time.sleep(1)



# --------------------------------------------- ENTERING DESTINATION DATA -------------------------------------------------------
def DestinationData(DESTINATIONCITY:str, DRIVER):
    DestTextBox = DRIVER.find_element('xpath', '//div/span[contains(text(),"To")]/following-sibling::input')
    DestTextBox.send_keys(DESTINATIONCITY)

    time.sleep(2)

    DestFristSelect = DRIVER.find_element('xpath', '//span[contains(@class, "autoCompleteTitle")]')
    DestFristSelect.click()

    time.sleep(2)

# -------------------------------------------------------------------------------------------------------------------



def TravelTimeData(DATE:str,WEEK:str,MONTH:str,YEAR:str, DRIVER):
    DayPickercption = DRIVER.find_element('xpath', "//div//div[contains(@class, 'DayPicker-Caption')]//div")
    Days = DayPickercption.get_attribute('innerText').split(" ")

    while((MONTH != Days[0]) and (YEAR != Days[1])):
        DRIVER.find_element('xpath', '//span[contains(@class, "DayPicker-NavButton--next")]').click()
        Days = DayPickercption.get_attribute('innerText').split(" ")
        time.sleep(1)

    MONTH = shortMonths(MONTH)
    WEEK = ShortWeeks(WEEK)

    if DATE < 10 and DATE > 0:
        DATE = f"0{DATE}"

    dateclicker = DRIVER.find_element('xpath',f"//div[contains(@aria-label, '{WEEK} {MONTH} {DATE} {YEAR}')]//p[contains(@class, 'fsw__date')]")
    dateclicker.click()

    donebox = DRIVER.find_element('xpath', '//div[@class = "sc-12foipm-55 LpzjE"]//span[@class = "fswTrvl__done"]')
    donebox.click()

    time.sleep(1)


def TrvlClsData(Adults:int, children:int, infants:int, Class:str, DRIVER):
    if Adults > 1:
        AdultsBox = DRIVER.find_element('xpath', '//p[contains(text(), "Adults")]/following-sibling::div/span[contains(text(),"1")]')
        DRIVER.execute_script(f"arguments[0].innerText = '{Adults}' ", AdultsBox)

    if children > 0:
        childbox = DRIVER.find_element('xpath','//p[contains(text(), "Children")]/following-sibling::div/span[contains(text(),"0")]')
        DRIVER.execute_script(f"arguments[0].innerText = '{children}' ", childbox)

    if infants > 0:
        InfantBox = DRIVER.find_element('xpath','//p[contains(text(), "Infants")]/following-sibling::div/span[contains(text(),"0")]')
        DRIVER.execute_script(f"arguments[0].innerText = '{infants}' ", InfantBox)


    if Class.lower() == 'economy':
        pass

    elif Class.lower() == 'premium economy':
        Preclass = DRIVER.find_element('xpath','//li[contains(text(), "premium economy")]')
        Preclass.click()

    elif Class.lower() == 'business':
        Busclass = DRIVER.find_element('xpath', '//li[contains(text(), "business")]')
        Busclass.click()

    elif Class.lower() == 'first class':
        firclass = DRIVER.find_element('xpath', '//li[contains(text(), "business")]')
        firclass.click()

    TrvlClassDone = DRIVER.find_element('xpath', '//div/a[contains(text(), "Done")]')
    TrvlClassDone.click()

    time.sleep(1)



def FareType(faretype:str, DRIVER):
    time.sleep(1)

    if faretype.lower() == 'regular':
        pass

    elif faretype.lower() == 'armed forces':
        armfare = DRIVER.find_element('xpath','//ul/li/span[@class = "sc-12foipm-2 isUBMc" and text() = "armed forces"]')
        armfare.click()

    elif faretype.lower() == "senior citizen":
        senfare = DRIVER.find_element('xpath', '//ul/li/span[@class = "sc-12foipm-2 isUBMc" and text() = "senior citizen"]')
        senfare.click()

    elif faretype.lower() == "student":
        stdfare = DRIVER.find_element('xpath', '//ul/li/span[@class = "sc-12foipm-2 isUBMc" and text() = "student"]')
        stdfare.click()

    elif (faretype.lower() == 'doctors') or (faretype.lower() == 'doctors'):
        docfare = DRIVER.find_element('xpath', '//ul/li/span[contains(text(), "doctors")]')
        docfare.click()


def Search(DRIVER):
    time.sleep(1)

    searchbox = DRIVER.find_element('xpath', '//div/span[contains(text(), "SEARCH FLIGHTS")]')
    searchbox.click()

