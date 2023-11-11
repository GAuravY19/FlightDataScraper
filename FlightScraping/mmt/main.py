# --------------------------------------- IMPORTS -----------------------------------------------------------

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# ------------------------------------------------------------------------------------------------------------



# ------------------------------------------- SELENIUM SETUP ------------------------------------------------

options = Options()
options.add_experimental_option('detach', True)

os.environ['PATH'] = r'D:/WebScrapping/WebDrivers/'

driver = webdriver.Chrome(options=options)
driver.get('https://www.makemytrip.com/')
driver.maximize_window()

# ----------------------------------------------------------------------------------------------------------


