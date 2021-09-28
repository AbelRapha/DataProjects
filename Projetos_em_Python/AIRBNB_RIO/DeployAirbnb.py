import pandas as pd
import streamlit as st
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
import time
import json

@st.cache()
def rodar_modelo(valores_x):
    global barra_progresso
    dados = pd.read_csv('dados.csv')
    y = dados['price']
    x = dados.drop('price', axis=1)
    
    x_train, x_test, y_train, y_test = train_test_split(x,y,random_state = 10)
    
    modelo = ExtraTreesRegressor()
    
    modelo.fit(x_train,y_train)
   
    preco = modelo.predict(valores_x)
   
    return preco
        
x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_listings_count': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

x_listas = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancelation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
            }


dicionario = {}
for item in x_listas:
    for valor in x_listas[item]:
        dicionario[f'{item}_{valor}'] = 0

st.title("""Projeto de Previsão de valor da diária no Airbnb no Rio de Janeiro
        """)
st.text("""Defina os parâmetros e preveja o valor da diária do seu imóvel""")

for item in x_numericos:
    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        st.write(""" __Custo por pessoa extra__ """)
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}', step=1, value=0)
    x_numericos[item] = valor

for item in x_tf:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    if valor == "Sim":
        x_tf[item] = 1
    else:
        x_tf[item] = 0
    
    
for item in x_listas:
    valor = st.selectbox(f'{item}', x_listas[item])
    dicionario[f'{item}_{valor}'] = 1
    
botao = st.button('Prever Valor do Imóvel')
if botao:
    dicionario.update(x_numericos)
    dicionario.update(x_tf)
    valores_x = pd.DataFrame(dicionario, index=[0])
    convert_archive_to_dict = json.loads(valores_x)
    create_jason_archive = json.dumps(convert_archive_to_dict)
   # barra_progresso = st.progress(0)
    #for percentual_progresso in range(1):
        #time.sleep(0.1)
        #preco = rodar_modelo(valores_x)
        #barra_progresso.progress(percentual_progresso+1)
    #if preco[0]:
     #   st.error(f"O valor a ser cobrado é de R$ {preco[0]:.2f}")
      #  st.button('Reiniciar Parâmetros')
    