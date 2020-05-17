import os
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"

GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')


with Chrome(execution_path=str(os.environ.get('CHROMEDRIVER_PATH')), options=chrome_options) as browser:

    browser.get(url)
    time.sleep(2)
    html = browser.page_source

html = BeautifulSoup(html, 'html.parser')

result = html.find("margin-container", {"class": "left right top"})
kvpairs = {}

for tag in result.find_all("h5"):

    dataGroup = tag.contents
    num = dataGroup[0].get_text()
    country = dataGroup[2].get_text().lower()
    if country == "us":
        country = "usa"
    kvpairs[country] = num

# for i in kvpairs:
#     print(i+"-"+kvpairs[i])
