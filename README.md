# Meu Primeiro Projeto: API Flask com Frontend em JavaScript

Este é um projeto simples que implementa uma API usando **Flask** (Python) e um frontend básico com **HTML, CSS e JavaScript**. O objetivo principal é demonstrar a criação de uma API RESTful e como interagir com ela a partir do frontend.

## Funcionalidades

- API RESTful com Flask.
- Endpoints que retornam dados JSON.
- Frontend simples que consome a API.

## Tecnologias Utilizadas

- **Flask** (Framework web em Python)
- **JavaScript** (Para comunicação com a API)
- **HTML e CSS** (Para a estrutura e estilo do frontend)

## Como Rodar o Projeto

### Requisitos

- **Python 3.x**
- **Flask** (`pip install flask`)
- **Flask-CORS** (`pip install flask-cors`)

### Instruções

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/meu_primeiro_projeto.git

## Segurança da informação

### Exemplo prático

Foi removido o debug=True do app.py, o que é importante para segurança. Isso vai garantir que em produção o modo de depuração não estará habilitado, o que pode expor informações sensíveis.

- Substituído:
if __name__ == '__main__':

app.run(debug=True)

- Por:
if __name__ == '__main__':

app.run()
