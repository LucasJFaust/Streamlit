import pandas as pd
import streamlit as st
import datetime as datetime, time


def mostra_resultado():
    st.write('Cliente:', varCliente)
    st.write('Banco:', varBancos)
    st.write('Parcelas:', verParcelas)
    st.write('Data de Vencimento:', verData)
    st.write('Filial', verChackbox)

with st.form("Formulário de Seleção de Parâmetros"):

    st.subheader('Formulários no Streamlit')
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
    verChackbox = st.checkbox("Filial Campinas")
    
    botao_form = st.form_submit_button("Filtrar")
    '------------------------'
    if botao_form:
        st.success('Obrigado por filtrar os dados')
        mostra_resultado()