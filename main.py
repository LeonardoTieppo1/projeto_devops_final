from flask import Flask, jsonify
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class HelloWorld(Resource):
    def get(self):
        """
        Exemplo de endpoint que retorna 'Hello, World!'
        ---
        responses:
          200:
            description: Mensagem de saudação
        """
        return jsonify({'message': 'Hello, World!'})

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
