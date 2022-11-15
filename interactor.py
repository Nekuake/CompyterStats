import mysql.connector
from CompyterClasses import Computer, Timestamp


# This data is up to the one implementing it. Please don't leave it as it is, specially if you will have the DB exposed.


class DB:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )


    def create_table(self, table_name, column_names, column_types):
        if len(column_names)!= len(column_types):
            raise Exception("Error: not the same number of column names to types")
        else:
            query="CREATE TABLE",table_name+"("
            for x in column_names:
                query=query+column_names[x]+column_types[x]+","
            query=query[:-1]
            query=query+")"
            self.mydb.cursor().execute(query)

    def insert_to_table(self, timestamp):
        pass


# Create a database in case there are none created. THIS MUST BE EXECUTED BEFORE DJANGO AS IT DOESN'T CREATE MYSQL DATABASES
def create_database(host, user, password, new_database_name):
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
    )
    mydb.cursor().execute("CREATE DATABASE", new_database_name)
    new_database = DB(host, user, password, new_database_name)
    return new_database
