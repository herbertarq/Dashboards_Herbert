# %%
import pandas as pd

# %%
import numpy as np 
import plotly.express as px 
import streamlit as st
import datetime

# %%
#### CARREGAR OS DADOS ####
Hapvida=pd.read_csv('RECLAMEAQUI_HAPVIDA.csv',sep=',')
Ibyte=pd.read_csv('RECLAMEAQUI_IBYTE.csv',sep=',')
Nagem=pd.read_csv('RECLAMEAQUI_NAGEM.csv',sep=',')

# %%
## DATETIME ####
Hapvida['TEMPO']=pd.to_datetime(Hapvida['TEMPO'])
Ibyte['TEMPO']=pd.to_datetime(Ibyte['TEMPO'])
Nagem['TEMPO']=pd.to_datetime(Nagem['TEMPO'])

# %%
####CRIAR COLUNA ESTADO EM TODOS OS DATASETS ###
Hapvida['UF'] = Hapvida['LOCAL'].str[-2:]
Ibyte['UF'] = Ibyte['LOCAL'].str[-2:]
Nagem['UF'] = Nagem['LOCAL'].str[-2:]



# %%
Hapvida.head

# %%
lista_locais=Hapvida['UF'].unique()


# %%
lista_locais

# %%
##UNIFICANDO DATAFRAMES ## 
GERAL = pd.concat ( [Hapvida, Ibyte, Nagem])
GERAL

# %%
####CRIAR COLUNA EMPRESA EM TODOS OS DATASETS ###
GERAL ['EMPRESA'] = GERAL['URL'].str.replace(pat=r'https://www.reclameaqui.com.br//',repl='', regex= True)
GERAL[['URL', 'EMPRESA']]
GERAL

# %%
GERAL

# %%
GERAL.drop('TEMPO',axis=1).sum()


# %%
##VERICANDO NÚMERO TOTAL DO STATUS###
GERAL.STATUS.value_counts()

# %%
GERAL.info

# %%
#### STREAMLIT###
st.set_page_config(page_title="HERBERT DE SOUSA FERREIRA")
with st.container():
    st.subheader("DASHBOARD - RECLAME AQU")
    st.title('HAPVIDA - IBYTE - NAGEM')
    st.write("Informações sobre reclamações dos clientes por empresa")

# %%
st.write('Esse dashboard apresenta dados do Reclame Aqui da Ibyte, HapVida e Nagem')

# %%
lista_locais=GERAL['UF'].unique()
local = st.selectbox(
    'Selecione o local',
    lista_locais)

