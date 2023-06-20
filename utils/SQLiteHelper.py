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

    def table_exists(self, table_name):
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
        cursor = self.conn.execute(query, (table_name,))
        return cursor.fetchone() is not None

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
        if not self.table_exists(table_name):
            self.insert_data(table_name, {"email": "", "access_token": "", "device_name": "", "did": "", "uuid": ""})
        self.close_connection()

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

    def update_did(self, did):
        self.connect()
        self.update_data("trader_info", {"did": did}, "ROWID = 1")
        self.close_connection()

    def update_uuid(self, uuid):
        self.connect()
        self.update_data("trader_info", {"uuid": uuid}, "ROWID = 1")
        self.close_connection()

    def update_access_token(self, access_token):
        self.connect()
        self.update_data("trader_info", {"access_token": access_token}, "ROWID = 1")
        self.close_connection()

    def update_device_name(self, device_name):
        self.connect()
        self.update_data("trader_info", {"device_name": device_name}, "ROWID = 1")
        self.close_connection()


