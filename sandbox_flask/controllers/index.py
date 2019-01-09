from flask import jsonify

test = {'test': 'test', 'sample': 10}

def get():
    print('index')
    return jsonify(test)