"""This module handles all calls to the weather.sqlite database. It is called and used
in various related classes to establish a connection to the database, insert,
create tables, fetch, save and purge records.
"""
#Name: Dahnia Simon, Lok Yee Harriet Chiu, Kiet Lam
#Course: Programming in Python - ADEV - 3005 (228331)
#Date Due - Milestone 1: November 25, 2022
#Term 5 - Final Project
# pylint - 9.69

from datetime import datetime
import sqlite3
import helper

class DBOperations():
    """The DBOperations class create or connects to a database that stores weather
    data for various years about the city of winnipeg and returns the values."""
    def __init__(self):
        """Initializes the connection to the database and creates the table."""
        try:
            self.conn = sqlite3.connect("weather.sqlite")
            print ("🔃 Accessing database ...")

            self.cur = self.conn.cursor()

            self.initialize_db()
        except sqlite3.DatabaseError as e_error:
            print("An error occured: ", e_error)

    def initialize_db(self):
        """Initialize the database."""
        try:
            self.cur.execute(
            """create table if not exists samples
            (id integer primary key autoincrement not null,
            sample_date text unique not null,
            location text not null,
            min_temp real not null,
            max_temp real not null,
            avg_temp real not null);""")
        except sqlite3.DatabaseError as e_error:
            print("An error occured: ", e_error)

    def save_data(self):
        """Saves all scraped data to the database."""
        try:
            data = DBOperations.get_data(helper.Helper.get_all_data())

            sql = """insert into samples
            (sample_date, location, min_temp, max_temp, avg_temp)
            values(?, 'Winnipeg, MB', ?, ?, ?)"""

            for item in data:
                try:
                    self.cur.execute(sql, item)
                except sqlite3.IntegrityError:
                    return

            self.conn.commit()
        except sqlite3.DatabaseError as e_error:
            print("An error occured: ", e_error)

    def save_specified_data(self):
        """Saves user specified data to the database."""
        try:
            data = DBOperations.get_data(helper.Helper.get_specified_data())

            sql = """insert into samples
            (sample_date, location, min_temp, max_temp, avg_temp)
            values(?, 'Winnipeg, MB', ?, ?, ?)"""

            for item in data:
                try:
                    self.cur.execute(sql, item)
                except sqlite3.IntegrityError:
                    return

            self.conn.commit()
        except sqlite3.DatabaseError as e_error:
            print("An error occured: ", e_error)

    def save_update_data(self):
        """Saves requested updated data to the database."""
        try:
            max_date = self.fetch_last_date()
            if max_date != "":
                for item in max_date:
                    latest_date = item.split('/')
            data = DBOperations.get_data(helper.Helper().update_data((datetime(int(latest_date[0]),
                                                                            int(latest_date[1]),
                                                                            int(latest_date[2])))))

            sql = """insert into samples
            (sample_date, location, min_temp, max_temp, avg_temp)
            values(?, 'Winnipeg, MB', ?, ?, ?)"""

            for item in data:
                try:
                    self.cur.execute(sql, item)
                except sqlite3.IntegrityError:
                    return
            self.conn.commit()
        except sqlite3.DatabaseError as e_error:
            print("An error occured: ", e_error)

    def purge_data(self):
        """Deletes all data from samples table."""
        try:
            self.cur.execute("""delete from samples""")
            print(" ➖ Deleted all data from database")
            self.conn.commit()
        except sqlite3.DatabaseError as e_error:
            print("An error occured: ", e_error)

    def fetch_data(self):
        """Returns requested data for plotting."""
        try:
            sql = """select * from samples"""

            self.cur.execute(sql)
            data = self.cur.fetchall()
            return data
        except sqlite3.DatabaseError as e_error:
            print("An error occured: ", e_error)

    def fetch_last_date(self):
        """Fetches latest date stored in database."""
        try:
            self.cur.execute("""SELECT MAX(sample_date) FROM samples""")

            result = self.cur.fetchone()
            return result
        except sqlite3.DatabaseError as e_error:
            print("An error occured: ", e_error)

    @staticmethod
    def get_data(data):
        """Receive data from the dictionary and converts it into a list."""
        try:
            main_list = []
            for key in data:
                sublist = []
                sublist.append(key)
                for key2 in data[key]:
                    sublist.append(data[key][key2])
                main_list.append(sublist)
            return main_list
        except sqlite3.DatabaseError as e_error:
            print("An error occured: ", e_error)


    def __exit__(self, exception_type, exception_value, traceback):
        """Closes connection to the database."""
        try:
            self.cur.close()
            self.conn.close()
        except sqlite3.DatabaseError as e_error:
            print("An error occured: ", e_error)
