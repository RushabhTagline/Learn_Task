import json

from flask import Flask, jsonify, request

app = Flask(__name__)
# @app.route('/')
# def index():
#     return jsonify({'name': 'alice',
#                        'email': 'alice@outlook.com'})


@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    print("name", name)
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found...!'})

@app.route('/', methods=['PUT'])  
def create_record():
    record = json.loads(request.data)
    with open('/tmp/data.txt','r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/tmp/data.txt','w') as f:
        f.write(json.dumps(records, indent=2))

    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []

    with open('/tmp/data.txt', 'r') as f:
        data =  f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email'] 
        new_records.append(r)


    with open('/tmp/data.txt','r') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    new_records = []
    with open('tmp/data.txtx', 'r') as f:
        data = f.read()
        records = json.loads



if __name__ == '__main__':
    print("__name__: ", __name__)
    app.run(debug=True)