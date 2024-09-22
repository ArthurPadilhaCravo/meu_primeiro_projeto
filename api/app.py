from flask import Flask, jsonify
from flask_cors import CORS

# Inicializando a aplicação Flask
app = Flask(__name__)

# Habilitando CORS para permitir chamadas da API de outros domínios
CORS(app)

# Definindo um endpoint simples que retorna uma mensagem JSON


@app.route('/api/mensagem', methods=['GET'])
def get_mensagem():
    """
    Endpoint que retorna uma mensagem JSON.
    Esse é um exemplo básico de API que retorna dados estáticos.
    """
    return jsonify({'mensagem': 'Olá do Flask!'})


# Rodando o servidor Flask
if __name__ == '__main__':
    # Servidor rodando na porta 5000
    app.run()
