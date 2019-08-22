#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

tests = [
    {
        'name': 'Sho',
        'age': 27,
        'country': 'Japan'
    },
    {
        'name': 'Tsu',
        'age': 27,
        'country': 'Japan'
    },
    {
        'name': 'Nat',
        'age': 26,
        'country': 'Japan'
    },
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tests', methods=['GET'])
def get_tests():
    return jsonify({'tests': tests})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
