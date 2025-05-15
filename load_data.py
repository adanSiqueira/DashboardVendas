import pandas as pd
import requests

def carregar_dados(query_string):
    url = 'https://labdados.com/produtos'
    response = requests.get(url, params = query_string)
    dados = pd.DataFrame.from_dict(response.json())
    dados['Data da Compra'] = pd.to_datetime(dados['Data da Compra'], format='%d/%m/%Y')
    return dados