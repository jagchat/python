#if not flask already installed, run this at command prompt, prior to executing this script
#>pip install flask

#you can run this app with the following (and navigate to http://localhost:8080 in browser)
#>python app.py

from flask import Flask
app = Flask(__name__)

@app.route("/") #define "root" (or home) route (using "route" decorator)
def home(): #this function gets executed for the above route
    return ( #just a multi-line string, for now
        "<html>"
        "   <body>"
        "       <h2>"
        "           Hello! this is Web Page2!"
        "       </h2>"
        "   </body>"
        "</html>")

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)