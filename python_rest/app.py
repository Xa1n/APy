from flask import Flask, request, abort
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify 

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Get groceries',
        'description': u'Milk, Cheese, Bread, Fruit, Cereal', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Keep doing Python projects', 
        'done': False
    }
]

@app.route('/todo/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


if __name__ == '__main__':
     app.run(port='5000')
     