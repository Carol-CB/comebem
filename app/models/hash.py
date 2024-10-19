import hashlib
import time

def gerarhash():
    dados = str(time.time())
    
    id_hash = hashlib.sha256(dados.encode()).hexdigest()
    
    return id_hash