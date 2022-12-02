import mysql.connector as mysql

#Variables
host = "localhost"
user = "root"
password = "arps@1899"

#Conecting to my DB 
try:
    db = mysql.connect(host=host,user=user,password=password)
    print("Connected Successfully!")
except Exception as e:
    print(e)
    print("Connection Failed")
    
#Creating a DB 
try:
    command_handler = db.cursor()
    command_handler.execute("CREATE DATABASE cars")
    print("cars Database has been created successfully!")
except Exception as e:
    print(e)
    print("Could not create Database")

#Connecting to a Databases 
try:
    db1 = mysql.connect(host=host,user=user,password=password,database ="cars")
    print("Connected to the Cars Database!")
except Exception as e:
    print(e)
    print("Cannot connect to Cars Database")


