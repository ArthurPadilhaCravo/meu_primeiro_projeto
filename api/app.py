from flask import Flask, jsonify
from flask_cors import CORS  # Importando CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS

@app.route('/api/mensagem', methods=['GET'])
def get_mensagem():
    return jsonify({"mensagem": "Olá! Esta é sua primeira API em Flask."})

if __name__ == '__main__':
    app.run(debug=True)

