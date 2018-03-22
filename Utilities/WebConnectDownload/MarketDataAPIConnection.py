from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

__author__ = 'vfourrier'

source__ = 'https://impythonist.wordpress.com/2015/07/12/build-an-api-under-30-lines-of-code-with-python-and-flask/'

"""
    Create connection to a restful API. Pack required:
    - pip install flask
    - pip install flask-restful
    - pip install sqlalchemy    
"""

# Create a engine for connecting to SQLite3.
# Assuming salaries.db is in your app root folder

e = create_engine('sqlite:///salaries.db')

app = Flask(__name__)
api = Api(app)


class DepartmentsMeta(Resource):
    def get(self):
        # Connect to databse
        conn = e.connect()
        # Perform query and return JSON data
        query = conn.execute("select distinct DEPARTMENT from salaries")
        return {'departments': [i[0] for i in query.cursor.fetchall()]}


class DepartmentalSalary(Resource):
    def get(self, department_name):
        conn = e.connect()
        query = conn.execute("select * from salaries where Department='%s'" % department_name.upper())
        # Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return result
        # We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient


api.add_resource(DepartmentalSalary, '/dept/<string:department_name>')
api.add_resource(DepartmentsMeta, '/departments')

if __name__ == '__main__':
    app.run()