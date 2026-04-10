import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

@st.cache_data
def load_data():
    # 1. Procurar o arquivo em qualquer lugar do repositório
    target_file = "Financial Sample.xlsx"
    file_path = None
    
    for root, dirs, files in os.walk("."):
        if target_file in files:
            file_path = os.path.join(root, target_file)
            break
    
    if file_path is None:
        st.error(f"Arquivo '{target_file}' não encontrado no repositório!")
        return None

    try:
        # 2. Ler o arquivo usando o caminho encontrado
        df = pd.read_excel(file_path, engine='openpyxl')
        df.columns = [c.strip() for c in df.columns]
        return df
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
        return None

# Execução
df = load_data()

if df is not None:
    st.title("📊 Dashboard Financeiro DIO")
    
    # Filtros na Sidebar
    st.sidebar.header("Filtros")
    paises = st.sidebar.multiselect("Países", df["Country"].unique(), df["Country"].unique())
    
    df_filtrado = df[df["Country"].isin(paises)]

    # Layout de colunas
    m1, m2, m3 = st.columns(3)
    m1.metric("Vendas", f"$ {df_filtrado['Sales'].sum():,.2f}")
    m2.metric("Lucro", f"$ {df_filtrado['Profit'].sum():,.2f}")
    m3.metric("Unidades", f"{df_filtrado['Units Sold'].sum():,.0f}")

    st.divider()
    
    # Gráfico e Tabela
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Vendas por Produto")
        st.bar_chart(df_filtrado.groupby("Product")["Sales"].sum())
    with c2:
        st.subheader("Dados Filtrados")
        st.dataframe(df_filtrado, height=400)
else:
    st.info("💡 Dica: Certifique-se de que o arquivo 'Financial Sample.xlsx' foi enviado ao GitHub.")
