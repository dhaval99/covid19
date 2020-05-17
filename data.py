from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"

chrome_options = Options()
chrome_options.add_argument("--headless")

with Chrome(options=chrome_options) as browser:

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

for i in kvpairs:
    print(i+"-"+kvpairs[i])