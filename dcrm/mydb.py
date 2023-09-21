import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'yhjhfgjhh279'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRMDatabase")

print("All Done!")