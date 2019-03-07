#DEMO: 
#       -read connection info from config/settings
#       -connect to mysql, fetch a set of rows, show in HTML table
#       -using crude/raw method (and not using any templates)
#       -code/files not well organized (yet)

#packages needed to install
#>pip install flask
#>pip install mysql-connector-python

#you can run this app with the following (and navigate to http://localhost:8080 in browser)
#>python app.py


from flask import Flask
import dbaccess as db
app = Flask(__name__)

@app.route("/") #define "root" (or home) route (using "route" decorator)
def home(): #this function gets executed for the above route
    return ( #just a multi-line string, for now
        f'''<html>
                <body>
                        <h2>
                        List of Employees
                        </h2>
                        {getEmpGridTable()}
                </body>
                </html>''')

def getEmpGridTable():
        dbResult = db.executeQuery("SELECT * FROM sample.emp") #fetch rows
        uiResult = None

        if dbResult is None:
                #something wrong in fetching rows
                uiResult = "Some Error"
        else:
                #frame HTML table from fetched rows
                ui = "<table width='50%'>"
                ui += "<thead><td>Id</td><td>Name</td><td>Salary</td><td>Dept.</td></thead>"
                for r in dbResult:
                        ui += "<tr>"
                        ui += f"<td>{r['empno']}</td>"
                        ui += f"<td>{r['ename']}</td>"
                        ui += f"<td>{r['sal']}</td>"
                        ui += f"<td>{r['deptno']}</td>"
                        ui += "</tr>"
                ui += "</table>"
                uiResult = ui

        return uiResult

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)