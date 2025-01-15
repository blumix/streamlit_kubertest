from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    print ('data requested')
    dummy_data = {
        "message": "Hello from the Dummy API!",
        "data": [
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25},
            {"id": 3, "name": "Charlie", "age": 35}
        ]
    }
    return jsonify(dummy_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
