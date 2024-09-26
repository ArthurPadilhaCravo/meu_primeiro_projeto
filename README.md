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

## Instalação
   - Clone o repositório:
      git clone https://github.com/ArthurPadilhaCravo/meu_primeiro_projeto.git
      cd meu_primeiro_projeto
   - Instale as dependências:
      pip install -r requirements.txt
   - Execute o projeto:
      python app.py

## Uso
   Acesse http://localhost:5000 no navegador e utilize o sistema de cadastro e login.

## Melhorias Futuras
   - Implementar verificação de email.
   - Adicionar uma camada de autenticação JWT.
   - Melhorar o design da interface web.

### Requisitos

- **Python 3.x**
- **Flask** (`pip install flask`)
- **Flask-CORS** (`pip install flask-cors`)

## Segurança da informação

### Exemplo prático

Foi removido o debug=True do app.py, o que é importante para segurança. Isso vai garantir que em produção o modo de depuração não estará habilitado, o que pode expor informações sensíveis.

- Substituído:

if __name__ == '__main__':

app.run(debug=True)

- Por:

if __name__ == '__main__':

app.run()

## Licença
Este projeto está sob a licença MIT.
