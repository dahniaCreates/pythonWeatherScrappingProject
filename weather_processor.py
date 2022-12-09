"""This model provides a user interface to users through the console. The user will be
able to scrape all weather data from the Environment Canada site, update the database
with most recent weather data, generate a box plot, generate a line plot and scrape
by a specified month and year.
Demo:
  [1] Scrape all weather data.
  [2] Update weather data.
  [3] Generate a box plot.
  [4] Generate a line plot.
  [5] Scrape specified data.
  [6] Exit.
  Enter your option: {user_input}
  user_input = 1 || 2 || 3 || 4 || 5 || 6

"""
#Name: Dahnia Simon, Lok Yee Harriet Chiu, Kiet Lam
#Course: Programming in Python - ADEV - 3005 (228331)
#Date Due - Milestone 2: December 2, 2022
#Term 5 - Final Project
# pylint - 9.83

import sqlite3
import plot_operations
import db_operations

class WeatherProcessor():
    """The WeatherProcessor class prompts user for input to perform processes specified in the
    menu."""
    @staticmethod
    def menu():
        """Prints out a menu to the console."""
        print("[1] Scrape all weather data.")
        print("[2] Update weather data.")
        print("[3] Generate a box plot.")
        print("[4] Generate a line plot.")
        print("[5] Scrape specified data.")
        print("[6] Exit.")

    menu()
    option = int(input("Enter your option: "))
    while option != 0:
        if option == 1:
            try:
                db_operations.DBOperations().purge_data()
                print("🔃 Starting scraping...")
                db_operations.DBOperations().save_data()
                print("✅ Data successfully added to database!")
                break
            except sqlite3.DatabaseError as d_error:
                print("An error occured: ", d_error)
        elif option == 2:
            try:
                print("🔃 Starting scraping...")
                db_operations.DBOperations().save_update_data()
                print("✅ Data has been successfully updated.")
                break
            except sqlite3.DatabaseError as d_error:
                print("An error occured: ", d_error)
        elif option == 3:
            try:
                plot_operations.PlotOperations().box_plot()
                break
            except sqlite3.DatabaseError as d_error:
                print("An error occured: ", d_error)
        elif option == 4:
            try:
                plot_operations.PlotOperations().line_plot()
                break
            except sqlite3.DatabaseError as d_error:
                print("An error occured: ", d_error)
        elif option == 5:
            try:
                db_operations.DBOperations().purge_data()
                print("🔃 Starting scraping...")
                db_operations.DBOperations().save_specified_data()
                print("✅ Data successfully added to database!")
                break
            except sqlite3.DatabaseError as d_error:
                print("An error occured: ", d_error)
        elif option == 6:
            break
        else:
            print("❌ Invalid option. Please try again.")
            menu()
            option = int(input("Enter your option: "))

    print("Program has be closed. Thank you 😊")
