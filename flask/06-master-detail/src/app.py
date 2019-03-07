#DEMO: 
#       -how to use inheritance using (jinja2) templates (to eliminate redundancy in markups)
#       -how to use multiple routes (and route with a parameter)
#       -develop a master/detail page workflow
#       -using bootstrap css framework
#       -using fontawesome icons

#packages needed to install
#>pip install flask
#>pip install mysql-connector-python

#you can run this app with the following (and navigate to http://localhost:8080 in browser)
#>python app.py


from flask import Flask, render_template #necessary to work with template
import dbaccess as db
app = Flask(__name__,
        static_url_path='/content', #this can be empty string if we want "images/title.png" directly
        static_folder='static', #map the static folder to serve files directly
        template_folder='templates' #map the templates folder so that flask picks up templates from here
        )

@app.route("/") #define "root" (or home) route
def home(): 
        dbResult = db.executeQuery("SELECT * FROM sample.emp") #fetch rows
        if dbResult is None:
                return "Sorry! some problem"
        else:
                #render template as string
                #the template uses variable "employees" (which contain rows) to pull data for rendering
                return render_template('employees.html', employees=dbResult) 

@app.route("/employee/<empno>") #define route for employee details
def empDetail(empno): 
        dbResult = db.executeQuery(f"SELECT * FROM sample.emp WHERE empno={empno}") #fetch rows
        if dbResult is None:
                return "Sorry! some problem"
        elif len(dbResult) == 0:
                return render_template('emp-notfound.html', empno=empno) 
        else:
                return render_template('employee.html', emp=dbResult[0]) 

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)