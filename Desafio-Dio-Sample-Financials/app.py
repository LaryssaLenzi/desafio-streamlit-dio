import streamlit as st
import pandas as pd

# Configuração da página (opcional, mas recomendado)
st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

@st.cache_data
def load_data():
    # O nome do arquivo deve ser exatamente como está no seu GitHub
    file_path = "Financial Sample.xlsx"
    try:
        # Carrega o arquivo usando o motor openpyxl
        df = pd.read_excel(file_path, engine='openpyxl')
        # Limpa espaços em branco dos nomes das colunas
        df.columns = [c.strip() for c in df.columns]
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None

# Carregando os dados
df = load_data()

if df is not None:
    st.title("📊 Desafio Streamlit - DIO")
    
    # Barra Lateral
    st.sidebar.header("Filtros")
    
    # Filtro de Países
    paises = st.sidebar.multiselect(
        "Selecione os Países",
        options=df["Country"].unique(),
        default=df["Country"].unique()
    )
    
    # Filtro de Produtos
    produtos = st.sidebar.multiselect(
        "Selecione os Produtos",
        options=df["Product"].unique(),
        default=df["Product"].unique()
    )

    # Aplicando os filtros no dataframe
    df_filtrado = df[df["Country"].isin(paises) & df["Product"].isin(produtos)]

    # Exibindo métricas simples
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Vendas Totais", f"$ {df_filtrado['Sales'].sum():,.2f}")
    with col2:
        st.metric("Lucro Total", f"$ {df_filtrado['Profit'].sum():,.2f}")
    with col3:
        st.metric("Unidades Vendidas", f"{df_filtrado['Units Sold'].sum():,.0f}")

    # Exibindo o dataframe
    st.subheader("Visualização dos Dados")
    st.dataframe(df_filtrado)

    # Gráfico simples
    st.subheader("Vendas por Segmento")
    st.bar_chart(df_filtrado.groupby("Segment")["Sales"].sum())

else:
    st.info("Por favor, verifique se o arquivo 'Financial Sample.xlsx' está na raiz do repositório.")
