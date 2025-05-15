import pandas as pd

def gerar_tabelas(dados):
    estado = dados[['Local da compra', 'lat', 'lon']].drop_duplicates()

    #Tabelas de receita
    receita_estados = dados.groupby('Local da compra')['Preço'].sum().reset_index()
    receita_estados = receita_estados.merge(estado, on='Local da compra').sort_values('Preço', ascending=False)

    receita_mensal = dados.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()
    receita_mensal['Ano'] = receita_mensal['Data da Compra'].dt.year
    receita_mensal['Mes'] = receita_mensal['Data da Compra'].dt.month

    receita_categorias = dados.groupby('Categoria do Produto')['Preço'].sum().reset_index().sort_values('Preço', ascending=False)

    #Tabelas de quantidade de vendas
    vendas_estados = dados.groupby('Local da compra')['Preço'].count().reset_index()
    vendas_estados = vendas_estados.merge(estado, on='Local da compra').sort_values('Preço', ascending=False).rename(columns={'Preço': 'Vendas'})

    vendas_mensal = dados.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].count().reset_index()
    vendas_mensal['Ano'] = vendas_mensal['Data da Compra'].dt.year
    vendas_mensal['Mes'] = vendas_mensal['Data da Compra'].dt.month
    vendas_mensal.drop('Data da Compra', axis=1, inplace=True)
    vendas_mensal.rename(columns={'Preço': 'Vendas'}, inplace=True)

    vendas_categorias = dados.groupby('Categoria do Produto')['Preço'].count().reset_index().sort_values('Preço', ascending=False).rename(columns={'Preço': 'Vendas'})

    #Tabelas vendedores
    vendedores = pd.DataFrame(dados.groupby('Vendedor')['Preço'].agg(['sum', 'count']))

    return receita_estados, vendas_estados, receita_mensal, vendas_mensal, receita_categorias, vendas_categorias, vendedores