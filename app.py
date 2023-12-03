from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify({'message': 'Olá, mundo!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
