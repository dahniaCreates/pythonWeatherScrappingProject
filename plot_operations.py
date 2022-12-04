#Name: Dahnia Simon, Lok Yee Harriet Chiu, Kiet Lam
#Course: Programming in Python - ADEV - 3005 (228331)
#Date Due - Milestone 2: December 2, 2022
#Term 5 - Final Project

"""This module retrieves specific data which is stored in our database (db_operations.py).
It returns a basic boxplot of mean temperatures in a date range, displaying one box per month, so it shows all 12 months of the year on
one plot.
In addition, a line plot of a particular months mean temperature data, which shows the mean daily temp of a particular month and year.
For example, it can display all the daily mean temperatures from January 2020, with the x axis being the day, and the y axis being temperature.
Example:
  input = From year: 2000
  input = To year: 2022
  input = Enter a specific month and year: 8 2021
  output =

            ...
"""

#pip install matplotlib
# for types of plottting available: https://matplotlib.org/stable/gallery/index
#for line styles: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

import matplotlib.pyplot as plt
import db_operations
# import numpy as np

# if user provides a month and a year --> line plot (all days in that particular month and year)
# if user only provides a year --> box plot (mean_temp, dates)

class PlotOperations():
  def __init__(self):
      """Init function."""
      self.dates = []
      self.mean_temp = []
      self.yearly_temps= []
      db = db_operations.DBOperations()
      self.data = db.fetch_data()

  def line_plot(self):
      """Generates a line plot with all days mean temp of the prompted specific month and year."""
      # x-coordinate - date
      self.dates = []
      # y-coordinate - mean_temp
      self.mean_temp = []
      x = self.dates
      y = self.mean_temp
      plt.plot(x, y, "g*-") # OR plt.plot(sales_years, sales_amounts)
      plt.xlabel("Day of Month")
      plt.ylabel("Mean Temp in C")
      plt.title("Daily Temperatures")
      plt.show()

  def box_plot(self):
      """Generates a box plot with all months with prompted year."""
      #Data for plotting (box plot)
      jan = []
      feb = []
      mar = []
      self.yearly_temps = [jan, feb, mar] # list of list

      plt.boxplot(self.yearly_temps)
      plt.xlabel("Months")
      plt.ylabel("Temperatures")
      plt.title("Monthly Temperature Distribution")

      plt.show()