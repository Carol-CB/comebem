from flask import Flask, render_template, redirect, request, url_for
import models.db as db
from env import debug, port

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'teste'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserva')
def reserva():
    return render_template('reserva.html')

@app.route('/reservar', methods=['POST'])
def reservar():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    data = request.form.get('data')
    hora = request.form.get('hora')
    quantpessoas = request.form.get('pessoas')
    observacao = request.form.get('observacao')
    db.salvar(nome, telefone, data, hora, quantpessoas, observacao)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=debug, port=port)
