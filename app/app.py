from flask import Flask, render_template, redirect, request, url_for
import models.db as db
from env import debug, port

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'teste'

@app.route('/')
def bemvindo():
    return render_template('bemvindo.html')

@app.route('/reserva')
def reserva():
    print("teste")
    return render_template('reserva.html')

@app.route('/minhas_reservas')
def minhas_reservas():
    return render_template('minhasReservas.html')

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logar', methods=['POST'])
def logar():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    permicao = db.logar(nome, senha)
    if permicao:
        return redirect('/home')
    else:
        return render_template('login.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nomeReserva')
    aniver = request.form.get('dataAniversario')
    tel = request.form.get('telefone')
    senha = request.form.get('senha')
    db.cadastrar(nome, aniver, tel, senha)
    return redirect('/home')

@app.route('/reservar', methods=['POST'])
def reservar():
    data = request.form.get('data')
    hora = request.form.get('hora')
    quantpessoas = request.form.get('pessoas')
    observacao = request.form.get('observacoes')
    db.salvar(data, hora, quantpessoas, observacao)
    return redirect('/home')

if __name__ == "__main__":
    app.run(debug=debug, port=port)
