"""This module demonstartes web scrapping from the Environment Canada website
and returns a dictionary of dictionaries with the max, min and mean
temperatures based on the user's response to the prompt.
Example:
  input = Enter a number between 1 and 12 (Month): 2
  input = Enter a year: 1998

  output =  1998-02-01:{'Max': -6.2, 'Min': -24.1, 'Mean': -15.2}
            1998-02-02:{'Max': -17.9, 'Min': -28.0, 'Mean': -23.0}
            ...
"""
#Name: Dahnia Simon, Lok Yee Harriet Chiu, Kiet Lam
#Course: Programming in Python - ADEV - 3005 (228331)
#Date Due - Milestone 1: November 25, 2022
#Term 5 - Final Project

from html.parser import HTMLParser
from datetime import datetime

class WeatherScraper(HTMLParser):
    """The WeatherScraper class prompts a user for a month and a year and
    then scraps the web for the max, min and mean temperatures from the user
    specified date to October 1996."""
    def __init__(self):
        """Initializes variables to be used through the class."""
        HTMLParser.__init__(self)
        self.tbody = False
        self.a_tag = False
        self.td_tag = False
        self.th_tag = False
        self.count = 0
        self.user_year = ""
        self.user_month = ""
        self.last_month = False
        self.daily_temps = {}
        self.weather = {}
        self.day = ""
        self.date = ""
        self.complete_date = ""
        self.format = '%Y/%m/%d'
        self.daily_temps_complete = {}

    def handle_starttag(self, tag, attrs):
        """Test for specific start tags to the min, max and mean data and
        checks for attributes in tags to identify the last available month and
        year on the website."""
        if tag == "tbody":
            self.tbody = True
        if tag == "a":
            self.a_tag = True
        if tag == "td":
            self.td_tag = True
        if tag == "th":
            self.th_tag = True

        #used to find the page with missing previous button and stop loop
        if len(attrs) == 2:
            if attrs[1][1] == "previous disabled":
                self.last_month = True

    def handle_endtag(self, tag):
        """Tests for the end tags to find where the min, max and mean data ends."""
        if tag == "a":
            self.a_tag = False
        if tag == "tbody":
            self.tbody = False
        if tag == "td":
            self.td_tag = False
        if tag == "th":
            self.th_tag = False

    def handle_data(self, data):
        """Identifies all valid max, min and mean data and populates
        the corresponding dictionaries with values."""
        if self.tbody:
            if self.th_tag:
                try:
                    int(data)
                    self.count = 0
                    self.day = data
                except ValueError:
                    return False
            if self.td_tag:
                self.count+=1
                if self.a_tag:
                    if "M" in data:
                        self.count = 4
                if self.a_tag:
                    if "E" in data:
                        self.count-=1
                if self.count <= 3:
                    try:
                        float(data)
                        if self.count == 1:
                            self.daily_temps["Max"] = float(data.strip())
                        elif self.count == 2:
                            self.daily_temps["Min"] = float(data.strip())
                        elif self.count == 3:
                            self.daily_temps["Mean"] = float(data.strip())
                            self.daily_temps_complete = self.daily_temps
                            self.daily_temps = {}
                            self.date = f"{self.user_year}/{self.user_month}/{self.day}"
                            #self.complete_date = datetime.strptime(self.date, self.format).date()
                            self.complete_date = self.date
                            self.weather[self.complete_date] = self.daily_temps_complete
                    except ValueError:
                        return False
