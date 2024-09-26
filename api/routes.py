from app import app
from flask import render_template

@app.route('/')
def index():
    return "Bem-vindo ao Meu Primeiro Projeto"
