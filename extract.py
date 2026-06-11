import requests, pandas as pd, os
url_api = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL'

api_key = os.getenv('api_key')

parametros = {
    'token' : api_key
}

response = requests.get(url_api, params= parametros)

if response.status_code == 200:
    response_json = response.json()
    df_response = pd.DataFrame(response_json)


# transformação com transposição padrão (T)
df_response = df_response.reset_index()
# print(df_response)
df_response = df_response.set_index("index")

df_largo = df_response.T

df_largo = df_largo.reset_index().rename(columns= {'index': 'moeda'})
#print(df_largo)

# filtro
df_alvo = df_largo[['code', 'bid', 'create_date']]
df_alvo = df_alvo.rename(columns={'code': 'moeda_code'})
print(df_alvo)



df_alvo.to_csv('Tabela_valor_eur_usd')
