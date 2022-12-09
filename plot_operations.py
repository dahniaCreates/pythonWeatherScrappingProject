"""This module retrieves specific data which is stored in our database (db_operations.py).
It returns a basic boxplot of mean temperatures in a date range, displaying one box per month,
so it shows all 12 months of the year on one plot.
In addition, a line plot of a particular months mean temperature data, which shows
the mean daily temp of a particular month and year. For example, it can display all the daily
mean temperatures from January 2020, with the x axis being the day, and the y
axis being temperature.
Example:
  input = From year: 2000
  input = To year: 2022
  input = Enter a specific month and year: 8 2021
  output =
            ...
"""
#Name: Dahnia Simon, Lok Yee Harriet Chiu, Kiet Lam
#Course: Programming in Python - ADEV - 3005 (228331)
#Date Due - Milestone 2: December 2, 2022
#Term 5 - Final Project
# pylint - 9.78

#pip install matplotlib
# for types of plottting available: https://matplotlib.org/stable/gallery/index
#for line styles: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

import calendar
import matplotlib.pyplot as plt
import db_operations


# if user provides a month and a year --> line plot (all days in that particular month and year)
# if user only provides a year --> box plot (mean_temp, dates)

class PlotOperations():
    """The PlotOperations class fetches data from the database and returns either a box plot from a
    year range of data or a line plot for a particular month."""
    def __init__(self):
        """Initializes variables to be used in the class."""
        self.dates = []
        self.mean_temp = []
        self.yearly_temps= []

        db_connection = db_operations.DBOperations()
        self.data = db_connection.fetch_data()

    def line_plot(self):
        """Generates a line plot with all days mean temp of the prompted specific month and year."""
        month = input("Enter a number between 1 and 12 (Month): ")
        if len(month) > 2:
            raise ValueError("❌ Month must be two digits or less in length.")
        try:
            int(month)
        except ValueError:
            print("❌ Error: Month must be a number.")

        year = input("Enter a year: ")
        if not len(year) == 4:
            raise ValueError("❌ Year must be four digits in length.")
        try:
            int(year)
        except ValueError:
            print("❌ Error: Year must be a number.")
        if(month == "" or year == ""):
            raise Exception("❌ A value must be entered to display weather data.")

        data = self.get_data_line(month, year)

        # x-axis - date
        self.dates = data[0]
        # y-axis - mean_temp
        self.mean_temp = data[1]

        if not data[0]:
            raise Exception("""❌ Data does not exist in our database.
            Please try again with other month and year. """)

        x = self.dates
        y = self.mean_temp
        plt.plot(x, y, "g*-")
        plt.xlabel("Day of Month")
        plt.ylabel("Mean Temp in Celsius")
        plt.title("Daily Temperatures of " + calendar.month_name[int(month)])
        plt.show()

    def box_plot(self):
        """Generates a box plot with all months with prompted year."""
        year_1 = input("Enter the starting year: ")

        try:
            int(year_1)
        except ValueError:
            print("❌ Error: Year must be a number.")

        year_2 = input("Enter the ending year: ")

        try:
            int(year_2)
        except ValueError:
            print("❌ Error: Year must be a number.")

        if len(year_1) != 4 or len(year_2) != 4:
            raise ValueError("❌ Year must be four digits in length.")

        if year_1 == "" or year_2 == "":
            raise Exception("❌ A value must be entered to display weather data.")

        if int(year_1) > int(year_2):
            raise Exception("❌ Starting year cannot be larger than ending year.")

        plt.boxplot(self.get_data_box(year_1, year_2))
        plt.xlabel("Months")
        plt.ylabel("Temperatures")
        plt.title("Monthly Temperature Distribution between " + year_1 + " and " + year_2)
        plt.show()

    def get_data_line(self, input_month: int, input_year: int):
        """Get data from the db for line plotting"""
        mean_temp = []
        day = []

        result = []

        for item in self.data:
            date = item[1].split('/')
            month = date[1]
            year = date[0]

            if month == str(input_month) and year == str(input_year):
                day.append(date[2])
                mean_temp.append(item[5])

        result.append(day)
        result.append(mean_temp)

        return result

    def get_data_box(self, input_year_1: int, input_year_2: int):
        """Get data from the db for box plotting"""
        result = []
        current_month = 1

        for month in range(12):
            temp_list = []
            for item in self.data:
                date = item[1].split('/')
                month = date[1]
                year = date[0]

                if int(year) >= int(input_year_1) and int(year) <= int(input_year_2):
                    if int(month) == current_month:
                        temp_list.append(item[5])

            result.append(temp_list)
            current_month += 1

        if not temp_list:
            raise Exception("""❌ Data does not exist in our database.
                            Please try again with other month and year. """)

        return result
