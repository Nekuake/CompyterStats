import mysql.connector
import psutil

# Dump to SQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="TestingPassword",
  database="pesao"
)

def get_overall_usage():
  pass
mycursor = mydb.cursor()
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM penes")

myresult = mycursor.fetchall()

#mycursor.execute("CREATE TABLE alvaropesao (id INT AUTO_INCREMENT PRIMARY KEY, pesao VARCHAR(255), mupesao VARCHAR(255))")