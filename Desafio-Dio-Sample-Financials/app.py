import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="DIO | Desafio Financials", layout="wide")

# Estilização CSS para parecer um Dashboard profissional
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# 2. CARREGAMENTO DOS DADOS
@st.cache_data
def load_data():
    # O nome deve ser exatamente igual ao arquivo no GitHub
    file_path = "https://raw.githubusercontent.com/julianazanelatto/power_bi_analyst/main/Financial%20Sample.xlsx" 
    df = pd.read_excel(file_path, engine='openpyxl')
    return df



# 3. BARRA LATERAL (SIDEBAR) - Filtros e Navegação
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Power_BI_Logo.png", width=50)
st.sidebar.title("Menu de Navegação")

page = st.sidebar.radio("Selecione a Página:", ["Dashboard Executivo", "Análise Detalhada"])

st.sidebar.divider()
st.sidebar.header("Filtros de Dados")
paises = st.sidebar.multiselect("Países", options=df["Country"].unique(), default=df["Country"].unique())
segmentos = st.sidebar.multiselect("Segmentos", options=df["Segment"].unique(), default=df["Segment"].unique())

# Aplicando Filtros
df_filtered = df[(df["Country"].isin(paises)) & (df["Segment"].isin(segmentos))]

# 4. LÓGICA DAS PÁGINAS

if page == "Dashboard Executivo":
    st.title("📊 Relatório de Vendas (Financials)")
    
    # KPIs - Indicadores principais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Vendas Brutas", f"$ {df_filtered['Gross Sales'].sum()/1e6:.2f}M")
    col2.metric("Unidades Vendidas", f"{df_filtered['Units Sold'].sum():,.0f}")
    col3.metric("Lucro Total", f"$ {df_filtered['Profit'].sum()/1e6:.2f}M")
    col4.metric("Descontos", f"$ {df_filtered['Discounts'].sum()/1e6:.2f}M")

    st.divider()

    # Gráficos Principais
    c1, c2 = st.columns(2)
    
    with c1:
        fig_vendas_mes = px.line(df_filtered.groupby("Month Name")["Sales"].sum().reset_index(), 
                                 x="Month Name", y="Sales", title="Tendência de Vendas por Mês",
                                 markers=True, line_shape="spline", color_discrete_sequence=["#1f77b4"])
        st.plotly_chart(fig_vendas_mes, use_container_width=True)

    with c2:
        fig_profit_country = px.bar(df_filtered.groupby("Country")["Profit"].sum().reset_index(),
                                    x="Country", y="Profit", title="Lucro por País",
                                    color="Profit", color_continuous_scale="Viridis")
        st.plotly_chart(fig_profit_country, use_container_width=True)

elif page == "Análise Detalhada":
    st.title("🔍 Detalhamento e Troca de Visuais")
    
    # Recurso de "Troca de Visual" pedido no desafio (usando tabs ou selectbox)
    tab1, tab2 = st.tabs(["📈 Visão por Produto", "📋 Tabela de Dados"])

    with tab1:
        # Toggle para trocar o tipo de gráfico
        tipo_grafico = st.segmented_control("Formato do Visual:", ["Barras", "Pizza"], default="Barras")
        
        if tipo_grafico == "Barras":
            fig = px.bar(df_filtered, x="Product", y="Sales", color="Segment", barmode="group", title="Vendas por Produto e Segmento")
        else:
            fig = px.pie(df_filtered, values="Sales", names="Product", title="Distribuição de Vendas por Produto")
        
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.write("Dados Filtrados:")
        st.dataframe(df_filtered, use_container_width=True)

# Rodapé
st.sidebar.info("Projeto desenvolvido para o Desafio DIO - Power BI Analyst.")
