import streamlit as st
import pandas as pd
import plotly.express as px
from utils import formata_numero
from load_data import carregar_dados
from preprocessing import gerar_tabelas
from visualizations import criar_graficos

st.set_page_config(layout='wide')
st.title('DASHBOARD DE VENDAS :shopping_trolley:')

#definindo aba lateral de filtros
st.sidebar.title('Filtros')

#definindo os filtros
regioes = ['Brasil', 'Centro-Oeste', 'Nordeste', 'Norte', 'Sudeste', 'Sul']
regiao = st.sidebar.selectbox('Região', regioes)
if regiao == 'Brasil':
    regiao = ''

todos_anos = st.sidebar.checkbox('Dados de todo o período', value = True)
if todos_anos:
    ano = ''
else:
    ano = st.sidebar.slider('Ano', 2020, 2023)

query_string = {'regiao': regiao.lower(), 'ano': ano}
dados = carregar_dados(query_string)

filtro_vendedores = st.sidebar.multiselect('Vendedores', dados['Vendedor'].unique())
if filtro_vendedores:
    dados = dados[dados['Vendedor'].isin(filtro_vendedores)]  

receita_estados, vendas_estados, receita_mensal, vendas_mensal, receita_categorias, vendas_categorias, vendedores = gerar_tabelas(dados)
fig_mapa_receita, fig_mapa_vendas, fig_receita_mensal, fig_receita_estados, fig_receita_categorias, fig_vendas_mensal, fig_vendas_estados, fig_vendas_categorias = criar_graficos(receita_estados, vendas_estados, receita_mensal, receita_categorias, vendas_mensal, vendas_categorias)

aba1, aba2, aba3 = st.tabs(['Receita', 'Quantidade de vendas', 'Vendedores'])

with aba1:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
        st.plotly_chart(fig_mapa_receita, use_container_width=True)
        st.plotly_chart(fig_receita_estados, use_container_width=True)
    with coluna2:
        for _ in range(6): st.write("")
        st.plotly_chart(fig_receita_mensal, use_container_width=True)
        st.plotly_chart(fig_receita_categorias, use_container_width=True)

with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Quantidade de vendas', formata_numero(dados['Preço'].count()))
        st.plotly_chart(fig_mapa_vendas, use_container_width=True)
        st.plotly_chart(fig_vendas_estados, use_container_width=True)
    with coluna2:
        for _ in range(6): st.write("")
        st.plotly_chart(fig_vendas_mensal, use_container_width=True)
        st.plotly_chart(fig_vendas_categorias, use_container_width=True)

with aba3:
    qtd_vendedores = st.number_input('Quantidade de vendedores', 2, 10, 2)
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        top_vendedores_receita = vendedores[['sum']].sort_values('sum', ascending=False).head(qtd_vendedores)
        top_vendedores_receita = top_vendedores_receita[::-1]
        fig_receita_vendedores = px.bar(top_vendedores_receita,
                                        x = 'sum',
                                        y = top_vendedores_receita.index,
                                        text_auto = True,
                                        title = f'Top {qtd_vendedores} vendedores por receita'
                                        )
        st.plotly_chart(fig_receita_vendedores, use_container_width = True)
    with coluna2:
        top_vendedores_vendas = vendedores[['count']].sort_values('count', ascending=False).head(qtd_vendedores)
        top_vendedores_vendas = top_vendedores_vendas[::-1]
        fig_vendas_vendedores = px.bar(top_vendedores_vendas,
                                        x = 'count',
                                        y = top_vendedores_vendas.index,
                                        text_auto = True,
                                        color_discrete_sequence = ['orange'],
                                        title = f'Top {qtd_vendedores} vendedores por numero de vendas'
                                        )
        st.plotly_chart(fig_vendas_vendedores, use_container_width = True)
