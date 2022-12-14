import mysql.connector
from CompyterClasses import Computer, Timestamp


# This data is up to the one implementing it. Please don't leave it as it is, specially if you will have the DB exposed.


class DB:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="TestingPassword",             #TESTING SETTINGS. PLEASE CHANGE IN YOUR IMPLEMENTATION
            database="compyterstats"
        )

    def create_table(self, table_name, column_names, column_types):
        if len(column_names) != len(column_types):
            raise Exception("Error: not the same number of column names to types")
        else:
            query = "CREATE TABLE", table_name + "("
            for x in column_names:
                query = query + column_names[x] + column_types[x] + ","
            query = query[:-1]
            query = query + ")"
            self.mydb.cursor().execute(query)


    def insert_computer_to_table(self, computer):
        # Computer: INSERT INTO compyterstats_computer (name) VALUES('name');
        query = "INSERT INTO compyterstats_computer (id,name) VALUES('" + computer.id + "','" + computer.name + "')"
        print(query)
        print(str(self.mydb.cursor().execute(query)))
        self.mydb.commit()

    def insert_timestamp_to_table(self, timestamp, computer):
        query = "INSERT INTO compyterstats_timestamp (datetime_captured, avg_cpu_usage, virtual_memory_usage, " \
                "virtual_memory_capacity, disk_usage, disk_capacity, computer_id) VALUES ('" + \
                timestamp.captured_time + "','" + \
                str(timestamp.cpu_load_list) + "','" + \
                str(timestamp.vmemory_usage) + "','" + \
                str(timestamp.vmemory_capacity) + "','" + \
                str(timestamp.storage_free) + "','" + \
                str(timestamp.storage_total) + "','" + \
                computer.id + "')"
        print(query)
        self.mydb.cursor().execute(query)
        self.mydb.commit()
        for process in timestamp.processes:
            query = "INSERT INTO compyterstats_process (pid, cpu_usage, name, io_counter, memory_data, virtual_memory_data, origin_timestamp_id) VALUES ('" + \
                    str(process.pid) + "','" + \
                    str(process.cpu) + "','" + \
                    str(process.name) + "','" + \
                    str(process.io_counter) + "','" + \
                    str(process.memory[0]) + "','" + \
                    str(process.virtual_memory) + "','" + \
                    timestamp.captured_time + "')"

            try:
                self.mydb.cursor().execute(query)
                self.mydb.commit()
            except:
                print("===========ERROR==========")
                print(query)



        # Timestamp:INSERT INTO compyterstats_timestamp (datetime_captured, avg_cpu_usage, virtual_memory_usage, virtual_memory_capacity, disk_usage, disk_capacity, computer_id) VALUES ();
        # Process: INSERT INTO compyterstats_process (pid, cpu_usage, name, io_counter, memory_data, virtual_memory_data, origin_timestamp_id) VALUES ()


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
