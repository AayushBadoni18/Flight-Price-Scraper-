"""
MakeMyTrip Flight Price Scraper (Python 3)
-----------------------------------------
Fetches one-way and round-trip flight data
and stores structured results in CSV format.

Author: Aayush Badoni
"""

import json
from datetime import datetime, date
from urllib.request import urlopen
from urllib.error import HTTPError
from dateutil.rrule import rrule, DAILY

BASE_URL = "http://flights.makemytrip.com/makemytrip/"


class MakeMyTrip(object):
    """
    Handles fetching, parsing, and exporting
    MakeMyTrip flight data.
    """

    def __init__(self):
        self.raw_response = ""
        self.arrival_time = ""

    # ----------------------------------------------------------
    # HTTP Fetch Layer
    # ----------------------------------------------------------

    def browse(self, url, roundtrip=False):
        """
        Fetch API response and extract flight JSON.

        :param url: API endpoint
        :param roundtrip: Boolean flag
        :return: Parsed JSON list or 1 on failure
        """
        try:
            print("Fetching:", url)
            self.raw_response = urlopen(url).read().decode("utf-8")
        except HTTPError:
            print("HTTP ERROR while fetching data")
            return 1

        if roundtrip:
            try:
                parsed = json.loads(self.raw_response)
                return json.loads(parsed['fd'])
            except (ValueError, KeyError):
                return 1

        return self._extract_flights_data(self.raw_response)

    def _extract_flights_data(self, response):
        """
        Extract JavaScript variable `flightsData`
        from HTML response.
        """
        for line in response.splitlines():
            if "flightsData" in line:
                try:
                    cleaned = (
                        line.replace("var flightsData = ", "")
                        .strip()
                        .rstrip(";")
                    )
                    return json.loads(cleaned)
                except ValueError:
                    return 1
        return 1

    # ----------------------------------------------------------
    # Journey Builders
    # ----------------------------------------------------------

    def journey_oneway(self, origin, destination, depart_date,
                       adult=1, children=0, infant=0):
        """
        Build one-way journey URL and fetch data.
        """
        url = (
            BASE_URL +
            "search/O/O/E/{}/{}/{}/S/V0/{}_{}_{}"
        ).format(adult, children, infant, origin, destination, depart_date)

        return self.browse(url)

    def journey_roundtrip(self, origin, destination, depart_date,
                          return_date, adult=1, children=0, infant=0):
        """
        Build round-trip journey URL and fetch data.
        """
        url = (
            BASE_URL +
            "splitRTDataService.json?"
            "classType=E&deptDate={}&fromCity={}&toCity={}"
            "&noOfAdlts={}&noOfChd={}&noOfInfnt={}"
            "&returnDate={}&tripType=R&tripTypeDup=R"
        ).format(
            depart_date, origin, destination,
            adult, children, infant, return_date
        )

        return self.browse(url, roundtrip=True)

    # ----------------------------------------------------------
    # CSV Writer
    # ----------------------------------------------------------

    def write_csv(self, flights, origin, destination, flight_date, file_handle):
        """
        Write parsed flight data to CSV.
        """
        header = (
            "Origin,Destination,Dept_Date,Dept_Time,Arr_Time,"
            "Total_Fare,Base_Fare,Fuel_Fare,Airways,Available,"
            "Duration,Class_Type,Flight_Number,Flight_Code,"
            "FlightID,Hopping,Taken\n"
        )
        file_handle.write(header)

        if flights == 1:
            file_handle.write(
                "{},{},{},NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,{}\n"
                .format(origin, destination, flight_date, date.today())
            )
            return

        for flight in flights:
            leg = flight['le'][0]

            file_handle.write(
                "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                    leg['o'],
                    leg['d'],
                    leg['dep'],
                    leg['fdt'],
                    leg['fat'],
                    flight['af'],
                    leg['flightFare']['baseFare'],
                    leg['flightFare']['fuelSurcharge'],
                    leg['an'],
                    leg['flightFare']['bookingClass']['availability'],
                    flight['td'],
                    leg['cls'],
                    leg['fn'],
                    leg['oc'],
                    flight['fi'],
                    flight['hff'],
                    date.today()
                )
            )


# ----------------------------------------------------------
# Script Entry Point
# ----------------------------------------------------------

if __name__ == "__main__":

    print("=" * 40)

    origin = "DEL"
    destination = "GAU"

    start_date = date(2016, 10, 21)
    end_date = date(2016, 11, 2)

    scraper = MakeMyTrip()

    with open("buff.csv", "a", encoding="utf-8") as f:
        for dt in rrule(DAILY, dtstart=start_date, until=end_date):
            dept_date = dt.strftime("%d-%m-%Y")
            print("Processing:", dept_date)

            flights = scraper.journey_oneway(
                origin, destination, dept_date
            )

            scraper.write_csv(
                flights, origin, destination, dept_date, f
            )
