from env import stringDB, nomeDB
from pymongo import MongoClient
from bson.objectid import ObjectId
from models.hash import gerarhash
from datetime import datetime

client = MongoClient(stringDB)
db = client[nomeDB]
reservas_collection = db['reservas'] 


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
    

def buscar_reservas():
    reservas = list(reservas_collection.find({}, {'_id': 0}))
    return reservas

def buscar_reserva_por_id(reserva_id):
    reserva = reservas_collection.find_one({'id': reserva_id}, {'_id': 0})
    if reserva:
        return reserva
    else:
        return "Reserva não encontrada"
