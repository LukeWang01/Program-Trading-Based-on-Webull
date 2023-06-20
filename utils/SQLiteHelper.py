import sqlite3


class SQLiteHelper:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.init_trader_info()

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()

    def get_data(self, table_name, columns="*", condition=None):
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_data(self, table_name, column_value_pairs, condition):
        query = f"UPDATE {table_name} SET "
        query += ", ".join([f"{column} = ?" for column in column_value_pairs])
        query += f" WHERE {condition}"
        values = list(column_value_pairs.values())
        self.cursor.execute(query, values)
        self.conn.commit()

    def insert_data(self, table_name, data):
        query = f"INSERT INTO {table_name} ({', '.join(data.keys())}) VALUES ({', '.join(['?' for _ in data.values()])})"
        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        self.cursor = None
        self.conn = None

    def reconnect(self):
        self.close_connection()
        self.connect()

    # Utility functions:
    def init_trader_info(self):
        self.connect()
        table_name = "trader_info"
        columns = "email TEXT, access_token TEXT, device_name TEXT, did TEXT, uuid TEXT"
        self.create_table(table_name, columns)

    def get_device_name(self):
        self.connect()
        data = self.get_data("trader_info", "device_name")
        self.close_connection()
        return data[0][0]

    def get_access_token(self):
        self.connect()
        data = self.get_data("trader_info", "access_token")
        self.close_connection()
        return data[0][0]

    def get_did(self):
        self.connect()
        data = self.get_data("trader_info", "did")
        self.close_connection()
        return data[0][0]

    def get_uuid(self):
        self.connect()
        data = self.get_data("trader_info", "uuid")
        self.close_connection()
        return data[0][0]


