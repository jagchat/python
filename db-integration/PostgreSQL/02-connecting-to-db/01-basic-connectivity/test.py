#run this at command prompt, prior to executing this script
#>pip install psycopg2-binary


import psycopg2 #import the module which can work with PostgreSQL

#conn = psycopg2.connect("host=localhost port=5432 dbname=postgres user=postgres password=admin123")
#or
conn = psycopg2.connect("dbname=postgres user=postgres password=admin123") #open db connection

cur = conn.cursor() #create a cursor (to perform some db operation)
cur.execute("SELECT * FROM emp") #execute a query
for table in cur.fetchall():
    print(table)
cur.close() #close cursor
conn.close() #close connection


