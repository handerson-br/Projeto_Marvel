import json
import pandas as pd
import requests
from pandas.io.json import json_normalize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from acesso import buscar_dados

request_data = buscar_dados #Realizando requisição dos dados / Realize data request 
json_data = json.loads(buscar_dados.content) #Carregando formato JSON / Loading JSON format
print(json_data[0])