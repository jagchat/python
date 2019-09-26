import traceback  # to get more info about error
import dbaccess as db


def getList():
    dbResult = db.executeQuery(f"SELECT * FROM emp")
    if dbResult is None:
        return "Sorry ! some problem"
    else:
        return dbResult


def getDetail(empno):
    dbResult = db.executeQuery(f"SELECT * FROM emp WHERE empno = {empno}")
    if dbResult is None:
        return "Sorry ! some problem"
    elif len(dbResult) == 0:
        return "Not found"  # or some http erro3r code
    else:
        return dbResult[0]


def add(data):
    try:
        empno = data["Empno"]
        ename = data["Ename"]
        sal = data["Sal"]
        deptno = data["Deptno"]

        sql = f"INSERT INTO emp VALUES (%d, %s, %d, %d)"
        values = [(empno, ename, sal, deptno)]
        db.executeDml(sql, values)
        return True
    except:
        traceback.print_exc()  # print more info to console
        return False  

def update(data):
    try:
        empno = data["Empno"]
        ename = data["Ename"]
        sal = data["Sal"]
        deptno = data["Deptno"]

        sql = f"UPDATE emp SET ename = %s, sal = %d, deptno = %d WHERE empno = %d"
        values = [(ename, sal, deptno, empno)]
        db.executeDml(sql, values)
        return True
    except:
        traceback.print_exc()  # print more info to console
        return False  

def delete(data):
    try:
        empno = data["Empno"]

        sql = f"DELETE FROM emp WHERE empno = %d"
        values = [(empno)]
        db.executeDml(sql, values)
        return True
    except:
        traceback.print_exc()  # print more info to console
        return False  