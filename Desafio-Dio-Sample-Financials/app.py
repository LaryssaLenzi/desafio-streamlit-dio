import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

@st.cache_data
def load_data():
    target_file = "Financial Sample.xlsx"
    file_path = None
    # Busca o arquivo em qualquer pasta do repositório
    for root, dirs, files in os.walk("."):
        if target_file in files:
            file_path = os.path.join(root, target_file)
            break
    
    if file_path is None:
        return None

    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        df.columns = [c.strip() for c in df.columns]
        return df
    except:
        return None

df = load_data()

if df is not None:
    st.title("📊 Dashboard Financeiro - DIO")
    
    # Barra Lateral com Filtros
    st.sidebar.header("Filtros")
    
    # Filtro de Países
    paises = st.sidebar.multiselect(
        "Selecione os Países", 
        options=df["Country"].unique(), 
        default=df["Country"].unique()
    )

    # Filtro de Produtos (Novo)
    produtos = st.sidebar.multiselect(
        "Selecione os Produtos", 
        options=df["Product"].unique(), 
        default=df["Product"].unique()
    )
    
    # Aplicando os dois filtros simultaneamente
    df_filtrado = df[
        (df["Country"].isin(paises)) & 
        (df["Product"].isin(produtos))
    ]

    # Exibição de Métricas
    c1, c2, c3 = st.columns(3)
    c1.metric("Vendas Totais", f"$ {df_filtrado['Sales'].sum():,.2f}")
    c2.metric("Lucro Total", f"$ {df_filtrado['Profit'].sum():,.2f}")
    c3.metric("Unidades Vendidas", f"{df_filtrado['Units Sold'].sum():,.0f}")

    st.divider()

    # Gráficos
    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("Vendas por País")
        st.bar_chart(df_filtrado.groupby("Country")["Sales"].sum())
    with col_right:
        st.subheader("Vendas por Produto")
        st.bar_chart(df_filtrado.groupby("Product")["Sales"].sum())

    # Tabela de Dados
    st.subheader("Visualização dos Dados Filtrados")
    st.dataframe(df_filtrado, use_container_width=True)
else:
    st.error("Arquivo de dados não encontrado. Verifique se 'Financial Sample.xlsx' está no repositório.")
