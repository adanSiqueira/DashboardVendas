import plotly.express as px

def criar_graficos(receita_estados, vendas_estados, receita_mensal, receita_categorias, vendas_mensal, vendas_categorias):
    fig_mapa_receita = px.scatter_geo(receita_estados,
                                      lat='lat',
                                      lon='lon',
                                      scope='south america',
                                      size='Preço',
                                      template='seaborn',
                                      hover_name='Local da compra',
                                      hover_data={'lat': False, 'lon': False},
                                      title='Receita por estado')

    fig_mapa_vendas = px.scatter_geo(vendas_estados,
                                     lat='lat',
                                     lon='lon',
                                     scope='south america',
                                     size='Vendas',
                                     template='seaborn',
                                     hover_name='Local da compra',
                                     hover_data={'lat': False, 'lon': False},
                                     title='Vendas por estado')

    fig_receita_mensal = px.line(receita_mensal,
                                 x='Mes',
                                 y='Preço',
                                 markers=True,
                                 range_y=(0, receita_mensal.max()),
                                 color='Ano',
                                 line_dash='Ano',
                                 title='Receita Mensal por ano',
                                 labels={'Mes': 'Mês', 'Preço': 'Faturamento'})
    fig_receita_mensal.update_layout(yaxis_title='Receita')
    fig_receita_mensal.update_xaxes(tickmode='linear', tick0=1, dtick=1, title='Mês')

    fig_vendas_mensal = px.line(vendas_mensal,
                                 x='Mes',
                                 y='Vendas',
                                 markers=True,
                                 range_y=(0, receita_mensal.max()),
                                 color='Ano',
                                 line_dash='Ano',
                                 title='Vendas Mensal por ano',
                                 labels={'Mes': 'Mês'})
    fig_receita_mensal.update_layout(yaxis_title='Vendas')
    fig_receita_mensal.update_xaxes(tickmode='linear', tick0=1, dtick=1, title='Mês')

    fig_receita_estados = px.bar(receita_estados.head(),
                                 x='Local da compra',
                                 y='Preço',
                                 text_auto=True,
                                 title='Estados com maior faturamento')
    fig_receita_estados.update_layout(yaxis_title='Receita')

    fig_vendas_estados = px.bar(vendas_estados.head(),
                                 x='Local da compra',
                                 y='Vendas',
                                 text_auto=True,
                                 title='Estados com maior numero de vendas')
    fig_vendas_estados.update_layout(yaxis_title='Vendas')

    fig_receita_categorias = px.bar(receita_categorias.head(),
                                    x='Categoria do Produto',
                                    y='Preço',
                                    text_auto=True,
                                    color_discrete_sequence = ['orange'],
                                    title='Categorias de produto com maior faturamento')
    fig_receita_categorias.update_layout(yaxis_title='Receita')

    fig_vendas_categorias = px.bar(vendas_categorias.head(),
                                    x='Categoria do Produto',
                                    y='Vendas',
                                    text_auto=True,
                                    color_discrete_sequence = ['orange'],
                                    title='Categorias de produto com maior quantidade de vedas')
    fig_vendas_categorias.update_layout(yaxis_title='Vendas')

    return fig_mapa_receita, fig_mapa_vendas, fig_receita_mensal, fig_receita_estados, fig_receita_categorias, fig_vendas_mensal, fig_vendas_estados, fig_vendas_categorias
