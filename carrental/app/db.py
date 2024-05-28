import pymysql.cursors
from pymysql.err import MySQLError

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._connect()
        return cls._instance

    def _connect(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='rootpass',
                database='CarRental',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
        except MySQLError as e:
            print(f"Error connecting to database: {e}")
            self.connection = None
            self.cursor = None

    def execute_query(self, query, params=None):
        if not self.connection or not self.cursor:
            self._connect()
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except MySQLError as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            self.cursor = None
            self.connection = None
