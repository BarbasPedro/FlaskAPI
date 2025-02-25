import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/<int:id>')
def pessoas(id):
    return jsonify(
        {
            'id': id,
            'nome': 'Pedro',
            'profissao': 'Desenvolvedor'
        }
    )

# @app.route('/soma/<int:v1>/<int:v2>')
# def soma(v1, v2):
#     return (jsonify(
#         {
#             'v1': v1,
#             'v2': v2,
#             'soma': v1 + v2
#         }
#     )

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
        return jsonify({'total': total})
    elif request.method == 'GET':
        return "GET"

if __name__ == '__main__':
    app.run(debug=True)