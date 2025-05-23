# Dashboard Interativo de Vendas para Franquia de Lojas 

Este projeto consiste em um **Dashboard Interativo de Vendas**, desenvolvido com o objetivo de fornecer à gestão uma ferramenta intuitiva, visualmente impactante e altamente funcional para **análise de dados, acompanhamento de métricas e KPI's**, auxiliando na **tomada de decisões estratégicas**.

## Objetivos

- Prover uma **visualização clara e dinâmica** dos dados de vendas.
- Facilitar o **monitoramento de indicadores-chave** (KPI's).
- Permitir a **análise detalhada por região, categoria de produto, vendedor e período**.
- Disponibilizar uma interface para **exploração e download de dados brutos**.

## Tecnologias e Frameworks Utilizados

- **Python** — linguagem de programação principal.
- **Streamlit** — para construção da interface web interativa.
- **Pandas** — manipulação e tratamento de dados.
- **Plotly Express** — geração de gráficos interativos e visuais impactantes.
- **Requests** — obtenção de dados via API.
- **NumPy** — suporte ao processamento numérico.

## Estrutura do Projeto

O projeto foi cuidadosamente modularizado, promovendo **organização, reutilização de código e escalabilidade**:

- `app.py` — Arquivo principal, responsável pela interface, filtros, exibição de gráficos e métricas.
- `load_data.py` — Módulo para **carregar dados de uma API pública**.
- `preprocessing.py` — Responsável pelo **tratamento e geração das tabelas analíticas**.
- `visualizations.py` — Funções para criação de **gráficos interativos** com Plotly.
- `utils.py` — Utilitários, como função para **formatar números monetários**.
- `pages/Dados_brutos.py` — Página dedicada à **exploração e download dos dados brutos**, com múltiplos filtros customizáveis.

## Funcionalidades

✅ Filtros interativos por região, ano e vendedores.  
✅ Gráficos de receita e quantidade de vendas por estado, mês e categoria de produto.  
✅ Mapas geográficos para visualização espacial de vendas e receita.  
✅ Análise de **top vendedores**, por receita e volume de vendas.  
✅ Download de dados brutos, com filtros customizados e exportação em **CSV**.  
✅ Modularização clara que facilita a **manutenção e expansão** do sistema.

## Como Executar

1. Clone o repositório.
2. Instale as dependências:  
   ```bash
   pip install -r requirements.txt

3. Execute a aplicação:
  ```bash
  streamlit run app.py
  ```

## Requisitos
Python 3.10+
Plotly 6.0.1
Pandas 2.2.3
Numpy 2.2.5
Requests 2.32.3

## Diferenciais
Design intuitivo e responsivo com layout em abas e colunas.

Uso de múltiplas páginas no Streamlit para separar análise de vendas e dados brutos.

Gráficos interativos que promovem uma análise exploratória rica.

Arquitetura clean code e orientada a modularização.

## Dados
Os dados utilizados neste projeto são obtidos automaticamente de uma API pública de produtos:
https://labdados.com/produtos

## Resultados Esperados
Este Dashboard possibilita uma visão estratégica e detalhada da operação de vendas da franquia, oferecendo insights valiosos para decisões relacionadas a marketing, estoque, desempenho regional e metas comerciais.
