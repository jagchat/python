import traceback  # to get more info about error
from config import dbsettings  # import our module to read config/settings
import pymssql


def getConnection():
    conn = None
    try:
        conn = pymssql.connect(
            host=dbsettings["server"],
            user=dbsettings["userid"],
            password=dbsettings["password"],
            database=dbsettings["database"],
        )  # open db connection
    except:
        traceback.print_exc()  # print more info to console
    return conn


def executeQuery(sql):
    conn = None
    result = None
    try:
        conn = getConnection()  # get db connection
        # create a cursor (to perform some db operation)
        # dictionary? -> to provide row values with col names
        cur = conn.cursor(as_dict=True)
        cur.execute(sql)  # execute a query
        result = cur.fetchall()  # fetch rows
        cur.close()  # close cursor
    except:
        traceback.print_exc()  # print more info to console
    finally:
        if conn is not None:
            conn.close()  # close connection
    return result  # return rows


def executeDml(sql, values):
    conn = None
    try:
        conn = getConnection()  # get db connection
        cur = conn.cursor()
        cur.executemany(sql, values)
        conn.commit()
        cur.close()  # close cursor
    except:
        traceback.print_exc()  # print more info to console
    finally:
        if conn is not None:
            conn.close()  # close connection
