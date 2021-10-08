import mysql.connector as mysql

db = mysql.connect(
    host = "encoro-production-mysql-db.cimipuwyotb6.us-west-2.rds.amazonaws.com",
    user = "admin",
    passwd = "WearingTheSunsGlasses",
    database = "encoro"
)

cursor = db.cursor()

## defining the Query
query = "SELECT * FROM items ORDER BY sku LIMIT 10"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)
