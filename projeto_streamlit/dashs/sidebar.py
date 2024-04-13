import pandas as pd
import streamlit as st
import datetime as datetime, time

varModal = st.sidebar.selectbox(
    'Selecionar o modal de transporte:',
    ('Rodoviário', 'Marítimo', 'Aéreo', 'Trem', 'Outro')
)

st.write('O modal selecionado foi: ', varModal)

with st.sidebar:
    varCliente = st.radio(
        'Selecione o cliente:',
        ('Sapace X', 'Microsoft', 'Apple', 'Goofle', 'Amazon')
    )
    varBancos = st.multiselect(
    'Selecione o banco:',
    ('Bradesco', 'Itaú', 'NU Bank', 'Caixa', 'Banco do Brasil')
)
    verParcelas = st.slider(
        'Quantas parcelas deseja financiar?', 0,60,20
    )
    verData = st.date_input(
        'Selecione a data do vencimento:',
        datetime.date(2024,1,1)
    )
    with st.spinner('Carrgando...'):
        time.sleep(2)
    st.success('Pronto')


st.write('Cliente:', varCliente)
st.write('Banco:', varBancos)
st.write('Parcelas:', verParcelas)
st.write('Data de Vencimento:', verData)
