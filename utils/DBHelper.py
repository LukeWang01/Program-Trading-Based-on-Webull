import sqlite3
import time
import datetime
import os


class DBHelper:
    def __init__(self, data_base_name):
        self.data_base_name = data_base_name
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.data_base_name)
            self.cursor = self.connection.cursor()
            print(f"Connected to database {self.data_base_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database {self.data_base_name}: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print(f"Disconnected from database {self.data_base_name}")

    def create_table(self, create_table_sql):
        try:
            self.cursor.execute(create_table_sql)
            self.connection.commit()
            print("Table created successfully")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def insert_data(self, insert_sql, values):
        try:
            self.cursor.execute(insert_sql, values)
            self.connection.commit()
            print("Data inserted successfully")
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")

    def fetch_data(self, select_sql):
        try:
            self.cursor.execute(select_sql)
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")


