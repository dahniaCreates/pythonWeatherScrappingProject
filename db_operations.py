import sqlite3
import helper

class DBOperations():

    def __init__(self):
        self.conn = sqlite3.connect("weather.sqlite")
        print ("Database opened successfully")

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
        data = DBOperations.get_data(helper.Helper.formatOutput())

        sql = """insert into samples
        (sample_date, location, min_temp, max_temp, avg_temp)
        values(?, 'Winnipeg, MB', ?, ?, ?)"""

        for d in data:
            try:
                self.cur.execute(sql, d)
            except sqlite3.IntegrityError:
                return

        self.conn.commit()
        self.cur.close()
        self.conn.close()   

    def purge_data(self):
        """Delete all data from table"""
        self.cur.execute("""delete from samples""")
        print("Deleted all data from database")

        self.conn.commit()
        self.cur.close()
        self.conn.close() 
        
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

run = DBOperations()
run.purge_data()        