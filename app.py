from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify({'message': 'Ola, Mundo!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
