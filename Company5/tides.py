import datetime
import re
import requests
from bs4 import BeautifulSoup
from dateutil import parser

# Use this to get the tide data from a location by using the search form on the home page.
def get_data(location: str):
    initial_url = "https://www.tide-forecast.com"
    response = requests.post(initial_url + "/locations/catch", data={'query': location})
    return BeautifulSoup(response.text, "html.parser")


# For each table row, look for a low tide, find the height and time, and see if it's during daylight hours.
# If so, print.
def print_low_tides(row: str, sunrise_datetime: datetime.date, sunset_datetime: datetime.date):
    if "Low" in row:
        tide_time_search = re.findall('([0-9]{1,2}:[0-9]{1,2} ?[ap]m)', str(row), re.IGNORECASE)
        tide_height_search = re.findall('([0-9]{1,5}.?[0-9]{1,5} ?f[e]{0,2}t).*', str(row), re.IGNORECASE)
        if sunrise_datetime <= parser.parse(
                str(datetime.date(sunrise_datetime.year, sunrise_datetime.month, sunrise_datetime.day)) + " " +
                tide_time_search[0]) <= sunset_datetime:
            print(tide_time_search[0], "\t", tide_height_search[0])


def calculate_tides(locations: list):
    sunrise_datetime, sunset_datetime = None, None

    for location in locations:
        # If not the first location, print an extra blank line
        if location != locations[0]:
            print("\n")
        print(location)
        print("-" * 30)

        tide_data = get_data(location)
        todays_tides = tide_data.findAll('div', {"class": "tide-times__table"})

        # Huntington Beach returns nothing if you search for the full string, so only search for "Huntington Beach"
        if not todays_tides:
            tide_data = get_data(location.split(",")[0])
            todays_tides = tide_data.findAll('div', {"class": "tide-times__table"})

        # The table format is different for today's tide information vs future ones.
        for tide in todays_tides:
            sun_search = re.search('Sunrise is at (.*) and sunset is at (.*)\.', str(tide.p), re.IGNORECASE)

            if sun_search:
                sunrise = sun_search.group(1).strip()
                sunset = sun_search.group(2).strip()
                print(datetime.date.today().strftime("%A %d %B %Y"))
                sunrise_datetime = parser.parse(str(datetime.date.today()) + " " + sunrise)
                sunset_datetime = parser.parse(str(datetime.date.today()) + " " + sunset)

            for row in tide.findAll("tr"):
                print_low_tides(str(row), sunrise_datetime, sunset_datetime)

        future_tides = tide_data.findAll('div', {"class": "tide-table"})
        for tide in future_tides:
            print("")
            tide_date = tide.findAll("h4")
            tide_date_search = re.search('Tide Times for .*\: (.*)</h4>', str(tide_date), re.IGNORECASE)

            tide_date = None
            if tide_date_search:
                tide_date = tide_date_search.group(1).strip()

            print(tide_date)
            sun_info = tide.findAll("table", {"class": "tide-table__tide-data--sun-moon not_in_print"})[0].findAll("td")
            sunrise = sun_info[0].findAll("span")
            sunset = sun_info[1].findAll("span")

            try:
                sunrise_search = re.search('<span>(.*)<.*', str(sunrise[0]), re.IGNORECASE)
                if sunrise_search:
                    sunrise_datetime = parser.parse(tide_date + " " + sunrise_search.group(1).strip())
                sunset_search = re.search('<span>(.*)<.*', str(sunset[0]), re.IGNORECASE)
                if sunset_search:
                    sunset_datetime = parser.parse(tide_date + " " + sunset_search.group(1).strip())
            # Some dates don't have sunset data. Skip.
            except IndexError:
                print(f"Could not get sunrise/sunset data for {tide_date}. Skipping...")
                continue

            for row in [tide.findAll("tr")]:
                for item in row:
                    print_low_tides(str(item), sunrise_datetime, sunset_datetime)


if __name__ == "__main__":
    locations = ["Half Moon Bay, California",
                 "Huntington Beach, California",
                 "Providence, Rhode Island",
                 "Wrightsville Beach, North Carolina"]
    calculate_tides(locations)

