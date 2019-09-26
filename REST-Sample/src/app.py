# packages needed to install
# >pip install flask
# >pip install flask-restful
# >pip install pymssql

from flask import Flask, render_template, request
from flask_restful import Resource, Api
from config import settings  # import our module to read config/settings

import empRepository

app = Flask(__name__,
            # this can be empty string if we want "images/title.png" directly
            static_url_path='/content',
            static_folder='static',  # map the static folder to serve files directly
            # map the templates folder so that flask picks up templates from here
            template_folder='templates'
            )
api = Api(app)


@app.route("/")  # define "root" (or home) route
def home():
    # render template as string
    # the template uses variable "settings"
    return render_template('home.html', settings=settings)


class Employees(Resource):

    def get(self, empno=None):
        if(empno is None):
            return empRepository.getList()
        else:
            return empRepository.getDetail(empno)

    def post(self):
        data = request.get_json(force=True)
        result = empRepository.add(data)
        if(result == True):
            return True, 200
        else:
            return False, 503

    def put(self):
        data = request.get_json(force=True)
        result = empRepository.update(data)
        if(result == True):
            return True, 200
        else:
            return False, 503

    def delete(self):
        data = request.get_json(force=True)
        result = empRepository.delete(data)
        if(result == True):
            return True, 200
        else:
            return False, 503

api.add_resource(Employees,
                 '/employees',
                 '/employees/<string:empno>'
                 )

if __name__ == '__main__':
    app.run()
    # app.run(host=settings["host"], port=settings["port"], debug=True)
