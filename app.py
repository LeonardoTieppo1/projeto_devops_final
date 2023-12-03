from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bem-vindo à API Flask para a VM do Azure!'

@app.route('/conectar_vm')
def conectar_vm():
    # Lógica para se conectar à VM do Azure
    # Substitua este trecho de código com sua lógica real de conexão à VM

    # Exemplo fictício
    resposta = {
        'mensagem': 'Hello World!'
    }

    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)
