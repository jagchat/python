#DEMO: 
#       -how to serve static files directly (from a folder)
#       -how to use images and css files as part of markup (using static files)

#packages needed to install
#>pip install flask
#>pip install mysql-connector-python

#you can run this app with the following (and navigate to http://localhost:8080 in browser)
#>python app.py


from flask import Flask
import dbaccess as db
app = Flask(__name__,
        static_url_path='/content', #this can be empty string if we want "images/title.png" directly
        static_folder='static' #map the static folder to serve files directly
        )

@app.route("/") #define "root" (or home) route (using "route" decorator)
def home(): #this function gets executed for the above route
    return ( #just a multi-line string, for now
        f'''<html>
                <head>
                        <link rel="stylesheet" type="text/css" href="content/css/app.css" >
                </head>
                <body>
                        <img src="content/images/title.png" />
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