from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify 

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "Hello Xain"

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
        

api.add_resource(Employees, '/employees') # Route_1


if __name__ == '__main__':
     app.run(port='5000')
     