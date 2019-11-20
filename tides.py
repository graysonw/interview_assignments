import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

"""
args = ["Half Moon Bay, California", 
        "Huntington Beach, California", 
        "Providence, Rhode Island",
        "Wrightsville Beach, North Carolina"]
"""

args = ["Half Moon Bay, California"]

initial_url = "https://www.tide-forecast.com"

for arg in args:
    response = requests.post(initial_url + "/locations/catch", data={'query': arg})
    this_soup = BeautifulSoup(response.text, "html.parser")
    todays_tides = this_soup.findAll('div', {"class": "tide-header__today"})
    for tide in todays_tides:
        #print(tide.h3)
        #print(tide.p)
        sun_search = re.search('Sunrise is at (.*) and sunset is at (.*)\.', str(tide.p), re.IGNORECASE)

        if sun_search:
            sunrise = sun_search.group(1).strip()
            sunset = sun_search.group(2).strip()
            print(sunrise, sunset)
    future_tides = this_soup.findAll('div', {"class": "tide-table"})
    for tide in future_tides:
        tide_date = tide.findAll("h4")
        tide_date_search = re.search('Tide Times for .*\: (.*)</h4>', str(tide_date), re.IGNORECASE)

        if tide_date_search:
            print(tide_date_search.group(1).strip())

        sun_info = tide.findAll("table", {"class":"tide-table__tide-data--sun-moon not_in_print"})[0].findAll("td")
        #print(sun_info[0].findAll("td"))
        #if "Sunrise" in str(tide.td):
        #    print("foo")
        sunrise = sun_info[0].findAll("span")
        sunset = sun_info[1].findAll("span")
        sunrise_search = re.search('<span>(.*)<.*', str(sunrise[0]), re.IGNORECASE)
        if sunrise_search:
            print(sunrise_search.group(1).strip())
        sunset_search = re.search('<span>(.*)<.*', str(sunset[0]), re.IGNORECASE)
        if sunset_search:
            print(sunset_search.group(1).strip())
    #print(tides[0])
    #print(tides[1])
    #for tide in tides:
    #    print(tide)
    """
        if 'sunrise' in tide.lower():
            print(tide)
        if 'sunset' in tide.lower():
            print(tide)
    """
    #print(tides)

#for arg in args:
#    print([k for k in locations if arg.split(",")[0].replace(" ", "-") in k])
#    if arg.split(",")[0] in locations:

#  location = args.replace(",", "").replace(" ", "-")
#  url = https://www.tide-forecast.com/locations/Huntington-Beach/tides/latest

