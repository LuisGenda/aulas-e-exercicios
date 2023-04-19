from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET'])
def pesquisa():

    resposta = {'mensagem': 'Consulta realizada com sucesso'}
    return jsonify(resposta), 200

if __name__ == '__main__':
    app.run()
