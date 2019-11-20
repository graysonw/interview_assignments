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
        print(tide.findAll("h4"))
        #print(str(tide.td))
        if "Sunrise" in str(tide.td):
            print("foo")
        sun_search = re.search('Sunrise:<span> (.*)</span>', str(tide), re.IGNORECASE)
        #if sun_search:
        #    print(sun_search.group(1).strip())
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

