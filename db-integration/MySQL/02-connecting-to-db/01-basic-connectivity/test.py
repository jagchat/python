#run this at command prompt, prior to executing this script
#>pip install mysql-connector-python


import mysql.connector #import the module which can work with mysql

conn = mysql.connector.connect(
    host="localhost",
    database="sample",
    user="root",
    password="admin123") #open db connection

cur = conn.cursor() #create a cursor (to perform some db operation)
cur.execute("SELECT * FROM sample.emp") #execute a query
for r in cur.fetchall():
    print(r)
cur.close() #close cursor
conn.close() #close connection