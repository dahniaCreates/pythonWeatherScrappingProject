import scrape_weather
import urllib.request

class Helper():

    def formatOutput():
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

        #gets data from the url for the user entered month and year and previous years up to December 1996.
        while(int(myparser.user_month) >= 1 and not myparser.last_month):
            with urllib.request.urlopen(f'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={myparser.user_year}&Month={myparser.user_month}#') as response:
                HTML = str(response.read())
                myparser.feed(HTML)
                if int(myparser.user_month) == 1:
                    myparser.user_year = int(myparser.user_year) - 1
                    myparser.user_month = "12"
                else:
                    myparser.user_month = int(myparser.user_month) - 1

        #prints out the formatted dictionary of dictionaries
        # for k, v in myparser.weather.items():
        #     result = f"{k}:{v}"
        #     print(result)

        return myparser.weather