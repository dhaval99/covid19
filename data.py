import os
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
from covid.settings import DEBUG

url = "https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"

GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = Options()
chrome_options.add_argument("--headless")
if not DEBUG:

    chrome_options.binary_location = GOOGLE_CHROME_BIN

if not DEBUG:

    with Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options) as browser:
        browser.get(url)
        time.sleep(2)
        html = browser.page_source
else:

    with Chrome(options=chrome_options) as browser:
        browser.get(url)
        time.sleep(2)
        html = browser.page_source

html = BeautifulSoup(html, 'html.parser')

result = html.find("margin-container", {"class": "left right top"})
kvpairs = {}
orig_pairs = {}
for tag in result.find_all("h5"):
    dataGroup = tag.contents
    num = dataGroup[0].get_text()
    if dataGroup[2].get_text() == "US":
        org_country = "United States Of America"
    elif dataGroup[2].get_text() == "Korea, South":
        org_country = "South Korea"
    else:
        org_country = dataGroup[2].get_text()
    country = dataGroup[2].get_text().lower()
    kvpairs[country] = num
    orig_pairs[org_country] = num
