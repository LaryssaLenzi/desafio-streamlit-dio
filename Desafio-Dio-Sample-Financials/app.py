import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

@st.cache_data
def load_data():
    # URL RAW do GitHub (importante: deve começar com raw.githubusercontent.com)
    url = "https://raw.githubusercontent.com/LaryssaLenzi/desafio-streamlit-dio/main/Financial%20Sample.xlsx"
    
    try:
        # O pandas consegue ler a URL diretamente se tiver o openpyxl instalado
        df = pd.read_excel(url, engine='openpyxl')
        # Limpa espaços extras nos nomes das colunas
        df.columns = [c.strip() for c in df.columns]
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo via URL: {e}")
        return None

df = load_data()

if df is not None:
    st.title("📊 Dashboard Financeiro (via GitHub URL)")
    
    # Sidebar - Filtros
    st.sidebar.header("Filtros")
    paises = st.sidebar.multiselect(
        "Selecione os Países",
        options=df["Country"].unique(),
        default=df["Country"].unique()
    )

    # Filtragem
    df_filtrado = df[df["Country"].isin(paises)]

    # Métricas e Gráfico
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Total de Vendas", f"$ {df_filtrado['Sales'].sum():,.2f}")
        st.dataframe(df_filtrado)
    with col2:
        st.bar_chart(df_filtrado.groupby("Country")["Sales"].sum())
else:
    st.warning("Não foi possível carregar os dados. Verifique a URL ou o arquivo requirements.txt.")
