"""This module assisted by the Scrape_Weather class demonstartes
web scrapping from the Environment Canada website and returns a
dictionary of dictionaries with the max, min and mean temperatures
based on the user's response provided in the command prompt menu.
"""
#Name: Dahnia Simon, Lok Yee Harriet Chiu, Kiet Lam
#Course: Programming in Python - ADEV - 3005 (228331)
#Date Due - Milestone 1: November 25, 2022
#Term 5 - Final Project
# pylint - 9.51

from datetime import datetime
import urllib.request
import scrape_weather

class Helper():
    """The Helper class is used to scrap the web for the max, min and mean temperatures
    based on the option selected at the command prompt menu and the data gathered from the
    Helper class."""
    @staticmethod
    def get_all_data():
        """Scraps all available weather data on the Environment Canada site and returns it to the
        dictionary of dictionaries."""
        myparser = scrape_weather.WeatherScraper()

        myparser.user_month = datetime.now().month
        myparser.user_year = datetime.now().year

        while(int(myparser.user_month) >= 1 and not myparser.last_month):
            with urllib.request.urlopen(f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={myparser.user_year}&Month={myparser.user_month}#') as response:
                html = str(response.read())
                myparser.feed(html)
                if int(myparser.user_month) == 1:
                    myparser.user_year = int(myparser.user_year) - 1
                    myparser.user_month = "12"
                else:
                    myparser.user_month = int(myparser.user_month) - 1

        return myparser.weather

    def update_data(self, ending_date:datetime):
        """Scraps only the weather data from the latest date available in the database up to
        the current date from the Environment Canada site and returns it to the
        dictionary of dictionaries."""
        myparser = scrape_weather.WeatherScraper()

        myparser.user_month = datetime.now().month
        myparser.user_year = datetime.now().year
        completed = False

        while not completed:

            if(ending_date.month == myparser.user_month) and (
                ending_date.year == myparser.user_year):
                completed = True
                break

            with urllib.request.urlopen(f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={myparser.user_year}&Month={myparser.user_month}#') as response:
                html = str(response.read())
                myparser.feed(html)
                if int(myparser.user_month) == 1:
                    myparser.user_year = int(myparser.user_year) - 1
                    myparser.user_month = "12"
                else:
                    myparser.user_month = int(myparser.user_month) - 1

        return myparser.weather

    @staticmethod
    def get_specified_data():
        """Scraps the weather data for user specified month and year on the
        Environment Canada site and returns it to the dictionary of dictionaries.
        NB: [Used to test update function]
        """
        myparser = scrape_weather.WeatherScraper()

        #collects user input for month and year
        myparser.user_month = input("Enter a number between 1 and 12 (Month): ")
        if len(myparser.user_month) > 2:
            raise ValueError("Month must be two digits or less in length.")
        try:
            int(myparser.user_month)
        except ValueError:
            print("Error: Month must be a number.")
        myparser.user_year = input("Enter a year: ")
        if not len(myparser.user_year) == 4:
            raise ValueError("Year must be four digits in length.")
        try:
            int(myparser.user_year)
        except ValueError:
            print("Error: Year must be a number.")
        if(myparser.user_month == "" or myparser.user_year == ""):
            raise Exception("A value must be entered to display weather data.")

        while(int(myparser.user_month) >= 1 and not myparser.last_month):
            with urllib.request.urlopen(f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={myparser.user_year}&Month={myparser.user_month}#') as response:
                html = str(response.read())
                myparser.feed(html)
                if int(myparser.user_month) == 1:
                    myparser.user_year = int(myparser.user_year) - 1
                    myparser.user_month = "12"
                else:
                    myparser.user_month = int(myparser.user_month) - 1

        return myparser.weather
