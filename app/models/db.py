from env import stringDB, nomeDB
from pymongo import MongoClient
from bson.objectid import ObjectId
from models.hash import gerarhash
from datetime import datetime

client = MongoClient(stringDB)
db = client[nomeDB]
reservas_collection = db['reservas']
usuarios_collection = db['usuarios']


def salvar(idUser, nomeUser, data, hora, quantpessoas, observacao):
    reserva = {
        'id': gerarhash(),
        'idUser': idUser,
        'nomeUser': nomeUser,
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
        return usuario['id']
    return False


def obter_reservas_usuario(usuario_id):
    try:
        reservas = list(reservas_collection.find({'idUser': usuario_id}))
        
        for reserva in reservas:
            reserva['_id'] = str(reserva['_id']) 
        
        return reservas 
    except Exception as e:
        print(f"Ocorreu um erro ao obter as reservas, erro: {e}")
        return [] 

def pegarNome(id):
    nomeUser = usuarios_collection.find_one({'id': id})
    return nomeUser['nome']

def obter_reservas():
    try:
        reservas = list(reservas_collection.find({}, {'_id': False})) 
        return reservas
    except Exception as e:
        print(f"Erro ao obter reservas: {e}")
        return []



def atualizar_reserva(reserva_id, status):
    try:
        resultado = reservas_collection.update_one(
            {'id': reserva_id},
            {'$set': {'status': status, 'atualizado_em': datetime.now()}}
        )
        if resultado.matched_count == 0:
            raise ValueError(f"Nenhuma reserva encontrada com o ID: {reserva_id}")
    except Exception as e:
        print(f"Erro ao atualizar reserva: {e}")
        raise


