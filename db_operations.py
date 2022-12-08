import sqlite3
import helper
from datetime import datetime

class DBOperations():
    def __init__(self):
        self.conn = sqlite3.connect("weather.sqlite")
        print ("🔃 Accessing database ...")

        self.cur = self.conn.cursor()

        self.initialize_db()

    def initialize_db(self):
        """Initialize database."""

        self.cur.execute(
        """create table if not exists samples
        (id integer primary key autoincrement not null,
        sample_date text unique not null,
        location text not null,
        min_temp real not null,
        max_temp real not null,
        avg_temp real not null);""")

    def save_data(self):
        """Save data to the database."""
        data = DBOperations.get_data(helper.Helper.get_all_data())

        sql = """insert into samples
        (sample_date, location, min_temp, max_temp, avg_temp)
        values(?, 'Winnipeg, MB', ?, ?, ?)"""

        for d in data:
            try:
                self.cur.execute(sql, d)
            except sqlite3.IntegrityError:
                return

        self.conn.commit()

    def save_update_data(self):
        """Saves updated data to the database."""
        max_date = self.fetch_last_date()
        if max_date != "":
            for d in max_date:
                latest_date = d.split('/')
        data = DBOperations.get_data(helper.Helper().update_data((datetime(int(latest_date[0]), int(latest_date[1]), int(latest_date[2])))))

        sql = """insert into samples
        (sample_date, location, min_temp, max_temp, avg_temp)
        values(?, 'Winnipeg, MB', ?, ?, ?)"""

        for d in data:
            try:
                self.cur.execute(sql, d)
            except sqlite3.IntegrityError:
                return

        self.conn.commit()

    def purge_data(self):
        """Delete all data from table"""
        self.cur.execute("""delete from samples""")
        print(" ➖ Deleted all data from database")
        self.conn.commit()

    def fetch_data(self):
        """Return requested data for plotting"""
        sql = """select * from samples"""

        self.cur.execute(sql)

        data = self.cur.fetchall()
        return data

    def fetch_last_date(self):
        """Fetches latest date stored in database"""
        self.cur.execute("""SELECT MAX(sample_date) FROM samples""")
        result = self.cur.fetchone()
        return result

    def get_data(data):
        """Receive data from the dictionary and turn convert it into a list."""

        list = []
        for key in data:
            sublist = []
            sublist.append(key)
            for key2 in data[key]:
                sublist.append(data[key][key2])
            list.append(sublist)

        return list

    def __exit__(self):
        self.cur.close()
        self.conn.close()

#run = DBOperations()
#run.purge_data()