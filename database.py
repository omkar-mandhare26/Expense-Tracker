from dotenv import load_dotenv
from mysql.connector import Error
import mysql.connector
import os

class mySQLdatabase:
    def __init__(self):
        load_dotenv()
        self.__DB_host = os.getenv('MYSQL_HOST')
        self.__DB_user = os.getenv('MYSQL_USER')
        self.__DB_password = os.getenv('MYSQL_PASSWORD')
        self.__DB_database = os.getenv('MYSQL_DATABASE')
        self.__conn = mysql.connector.connect(
                host = self.__DB_host,
                user = self.__DB_user,
                password = self.__DB_password,
                database = self.__DB_database
            )

    def addExpense(self,Name,Price):
        cursor = self.__conn.cursor()
        query = "INSERT INTO expenses (name,amount) values (%s,%s)"
        cursor.execute(query,(Name,Price))
        self.__conn.commit()

    def deleteAll(self):
        cursor = self.__conn.cursor()
        query = "DELETE FROM expenses"
        cursor.execute(query)
        self.__conn.commit()
    
    def getAllExpenses(self):
        cursor = self.__conn.cursor(dictionary=True)
        query = "SELECT * FROM expenses"
        cursor.execute(query)
        data = cursor.fetchall()
        return data