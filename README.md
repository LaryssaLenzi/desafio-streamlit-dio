# 📊 Dashboard Financeiro com Streamlit

Este projeto foi desenvolvido como um desafio de projeto para a **DIO (Digital Innovation One)**. A aplicação consiste em um dashboard interativo para análise de dados financeiros, utilizando Python e Streamlit para transformar planilhas Excel em visualizações dinâmicas.

## 🚀 Acesse o Dashboard Online
A aplicação está publicada no Streamlit Cloud e pode ser acessada pelo link:
👉 **[Visualizar Dashboard](https://desafio-app-dio.streamlit.app/)**

---

## 🛠️ Tecnologias Utilizadas
- **Python**: Linguagem de programação.
- **Streamlit**: Framework para criação de dashboards web.
- **Pandas**: Manipulação e tratamento de dados.
- **Openpyxl**: Engine para leitura de arquivos Excel.

## 📁 Organização do Projeto
- `app.py`: Código principal com a interface e lógica.
- `requirements.txt`: Arquivo com as bibliotecas necessárias para o deploy.
- `Financial Sample.xlsx`: Base de dados utilizada.

## 💡 Funcionalidades
- **Busca de Arquivos**: O script localiza automaticamente a base de dados dentro da estrutura de pastas.
- **Filtros Interativos**: Seleção de Países e Produtos na barra lateral.
- **Métricas de Performance**: Exibição de Vendas Totais, Lucro e Unidades Vendidas.
- **Visualização de Dados**: Gráficos de barras automáticos e tabela de dados filtrada.

## 💻 Como rodar o projeto localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/LaryssaLenzi/desafio-streamlit-dio.git](https://github.com/LaryssaLenzi/desafio-streamlit-dio.git)
   
2. **Instale as dependências:**
   ```bash
    pip install -r requirements.txt
3. **Execute o app:**
      ```bash
    streamlit run app.py
   
