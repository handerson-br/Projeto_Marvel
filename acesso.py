
# essa linha importa os recursos
from ctypes.wintypes import PBOOL
from unicodedata import name
import requests
from datetime import datetime
import hashlib
from dados import chaves
import json
import pandas as pd


def buscar_dados():
    #Chaves de Acesso (Trasformar em Objeto)
    nome= input("Digite o nome do Personagem (em inglês): ")
    KEY = chaves[0] #Chave publica
    PKEY = chaves[1]# Chave Privada

    #Criação de timestamp
    dt = datetime.now()
    ts = datetime.timestamp(dt)

    print("Date and time is:", dt)  #Verificação de data
    print("Timestamp is:", ts)        #verificação de TimeStamp

    HASH0 = ((str(ts))+""+(str(PKEY))+""+(str(KEY)))

    #Informa o hash MD5
    print("A base da chave é: ",HASH0)

    crypto= hashlib.md5(HASH0.encode())
    HASH=crypto.hexdigest()

    print ("A Hash é ",HASH)
    #verificar a escrita do link
    print(f'link com hash: https://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={KEY}&hash={HASH}')

    r = (f'https://gateway.marvel.com:443/v1/public/characters?name={nome}&ts={ts}&apikey={KEY}&hash={HASH}')
    #requisição ao Servidor
    acess= requests.get(r)
    json_data = json.loads(acess.content)

    #Carregando formato JSON / Loading JSON format
    #print(json_data)

    view = pd.DataFrame(json_data) #Transformando amostra em Dataframe / Transforming sample into Dataframe
    print(view.head())

    df = pd.json_normalize(json_data) #expandindo dados e armazenando em um Dataframe / Expanding the data and storing to a Dataframe
    print (df.head())

    print(df.columns.values)
    type(df.columns.values)
