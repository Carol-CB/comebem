from flask import Flask, render_template, redirect, request, url_for, jsonify
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
        return render_template('index.html', id=permicao)
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
    idUser = request.form.get('id')
    nomeUser = db.pegarNome(idUser)
    data = request.form.get('data')
    hora = request.form.get('hora')
    quantpessoas = request.form.get('pessoas')
    observacao = request.form.get('observacoes')
    db.salvar(idUser, nomeUser, data, hora, quantpessoas, observacao)
    return redirect('/home')

@app.route('/pegarReservas', methods=['GET'])
def pegarReservas():
    idUser = request.args.get('id') 
    if not idUser:
        return jsonify({"erro": "ID do usuário não fornecido."}), 400

    reservas = db.obter_reservas_usuario(idUser) 
    if not reservas:
        return jsonify({"erro": "Nenhuma reserva encontrada."}), 404

    return jsonify(reservas) 



if __name__ == "__main__":
    app.run(debug=debug, port=port)
