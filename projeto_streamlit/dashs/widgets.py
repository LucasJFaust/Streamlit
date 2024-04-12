import pandas as pd
import streamlit as st
import datetime

df = pd.read_excel(
    io= '/home/faust/Projetos/Streamlit/projeto_streamlit/dashs/Datasets/faturamento.xlsx',
    engine= 'openpyxl',
    sheet_name= 'Interação',
    usecols= 'A:C',
    nrows=40,
)

st.subheader('Botão')
if st.button('Clique Aqui'):
    st.write('Você cliclou')

def convert_df(df):
    return df.to_csv().encode('utf-8')

st.subheader('Botão de Download')
st.download_button(
    label= 'Baixar Arquivo CSV',
    data= convert_df(df),
    file_name= 'df.csv',
    mime= 'text/csv'
)

st.subheader('Checkbox')
select = st.checkbox('Marque a Caixa')
if select == True:
    st.write('Fui Selecionado')

st.subheader('Radio Button')
tipo_relatorio = st.radio(
    'Selecione o tipo de relatório:',
    ('Mensal', 'Semestral', 'Anual'))
st.write('Você selecionou o tipo:', tipo_relatorio)


st.subheader('Caixa de Seleção')
opcoes = st.selectbox(
    'Selecione a matéri-prima:',
    ('Aco','Plástico','Borracha', 'Madeira'))
st.write('Você selecionou: ', opcoes)


st.subheader('Seleção Múltipla')
multi = st.multiselect(
    'Selecione o banco para consulta:',
    {'Bradesco', 'Caixa', 'Itaú', 'Banco do Brasil', 'Nu Bank'})
st.write(multi)


st.subheader('Slider')
parcela = st.slider(
    'Com quantas parcelas deseja simular?', 0,60,30)
st.write('Você selecionou:', parcela, 'parcelas')

intervalo = st.slider(
    'Qual o intervalo desejado?',
    0.0,100.0, (25.0,75.0)
)
st.write('Intervalo:',intervalo)

st.subheader('Datas')
d = st.date_input(
    'Selecione a data:',
    datetime.date(2022,10,1)
)
st.write('A data selecionada foi:', d)


