# -Code in this file is susceptible for SQL injection attacks
# -Only for (simple) emo

import traceback #to get more info about error
from config import dbsettings #import our module to read config/settings
import mysql.connector #import the module which can work with mysql

def getConnection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host=dbsettings["host"],
            database=dbsettings["database"],
            user=dbsettings["user"],
            password=dbsettings["password"]) #open db connection
    except:
        traceback.print_exc() #print more info to console
    return conn

def executeQuery(sql):
    conn = None
    result = None
    try:
        conn = getConnection() #get db connection
        #create a cursor (to perform some db operation)
        cur = conn.cursor(dictionary=True) #dictionary? -> to provide row values with col names
        cur.execute(sql) #execute a query
        result = cur.fetchall() #fetch rows
        cur.close() #close cursor
    except:
        traceback.print_exc() #print more info to console
    finally:
        if conn is not None:
            conn.close() #close connection
    return result #return rows