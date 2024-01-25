
import pandas as pd
import numpy as np 
import plotly.express as px 
import streamlit as st
import datetime

#### CARREGAR OS DADOS ####
Hapvida=pd.read_csv('RECLAMEAQUI_HAPVIDA.csv',sep=',')
Ibyte=pd.read_csv('RECLAMEAQUI_IBYTE.csv',sep=',')
Nagem=pd.read_csv('RECLAMEAQUI_NAGEM.csv',sep=',')

Ibyte.head

##VERICANDO STATUS DO DATAFRAME###
Ibyte.STATUS.value_counts()

##VERICANDO STATUS DO DATAFRAME###
Nagem.STATUS.value_counts()

##VERICANDO NÚMERO TOTAL DO STATUS###
df_Hapvida.STATUS.value_counts()

## DATETIME ####
Hapvida['TEMPO']=pd.to_datetime(Hapvida['TEMPO'])
Ibyte['TEMPO']=pd.to_datetime(Ibyte['TEMPO'])
Nagem['TEMPO']=pd.to_datetime(Nagem['TEMPO'])

####CRIAR COLUNA ESTADO EM TODOS OS DATASETS ###
Hapvida['LOCAL'].iloc[0].split(' - ')[1].strip()
Ibyte['LOCAL'].iloc[0].split(' - ')[1].strip()
Nagem['LOCAL'].iloc[0].split(' - ')[1].strip()
Hapvida

estado_lista=[]
for i in range(len(Hapvida)):
    estado_lista.append(Hapvida['LOCAL'].iloc[i].split(' - ',2)[1].strip())


estado_lista

# %%
Hapvida.head

# %%
lista_locais=Hapvida['ESTADO'].unique()


# %%
lista_locais

# %%
##UNIFICANDO DATAFRAMES ## 
GERAL = pd.concat ( [Hapvida, Ibyte, Nagem])
GERAL

# %%
#### STREAMLIT###
st.title('DASHBOARD - RECLAME AQUI - IBYTE, HAPVIDA E NAGEM')

# %%
st.write('Esse dashboard apresenta dados do Reclame Aqui da Ibyte, HapVida e Nagem')

# %%
lista_locais=GERAL['ESTADO'].unique()
local = st.selectbox(
    'Selecione o local',
    lista_locais)


