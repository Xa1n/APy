from flask import Flask, request, abort, make_response
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

@app.route('/todo/api/tasks', methods=['POST'])         # insert a new item into task database
def create_task():
    if not request.json or not 'title' in request.json:         # ensures error if data isn't there or doesn't have 'title' item
        abort(400)
    task = {                                            # 
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
     app.run(port='5000')
     