from env import stringDB, nomeDB
from pymongo import MongoClient
from bson.objectid import ObjectId
from models.hash import gerarhash
from datetime import datetime

client = MongoClient(stringDB)
db = client[nomeDB]
reservas_collection = db['reservas']
usuarios_collection = db['usuarios']


def salvar(data, hora, quantpessoas, observacao):
    reserva = {
        'id': gerarhash(),
        'data': data,
        'hora': hora,
        'quantpessoas': quantpessoas,
        'observacao': observacao,
        'status': 'aberto',
        'criado_em': datetime.now()
    }
    try:
        reservas_collection.insert_one(reserva)
    except Exception as e:
        print(f"ocorreu um erro ao salvar os dados no banco, erro:{e}")
    
    

def cadastrar(nome, aniver, telefone, senha):
    usuario = {
        'id': gerarhash(),
        'nome': nome,
        'data_aniversario': aniver,
        'telefone': telefone,
        'senha': senha,
        'criado_em': datetime.now()
    }
    try:
        usuarios_collection.insert_one(usuario)
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar o usuário no banco, erro: {e}")


def logar(nome, senha):
    usuario = usuarios_collection.find_one({'nome': nome})
    if usuario and usuario['senha'] == senha:
        # return usuario['id']
        return True
    return False


def obter_reservas_usuario(usuario_id):
    try:
        reservas = list(reservas_collection.find({'usuario_id': usuario_id}))
        return reservas
    except Exception as e:
        print(f"Ocorreu um erro ao obter as reservas, erro: {e}")
        return []
