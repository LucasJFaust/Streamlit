import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io= '/home/faust/Projetos/Streamlit/projeto_streamlit/dashs/Datasets/faturamento.xlsx',
    engine= 'openpyxl',
    sheet_name= 'flow',
    usecols= 'A:B',
    nrows=15,
)

graf_area = alt.Chart(df).mark_area(
    color='gray',
    line={'color':'black'}
).encode( # Tudo que formos mudar com relação ao gráfico, usamos o () do mark.area.
    x = 'Year:T', # Precisamos definir que tipo de dados está sendo tratado no eixo(se ele é um rótulo, numérico ou temporal), para isso usamos os : e a letra T para temporal.
    y = 'Value:Q'
)

rotulos = graf_area.mark_text(
    size=14,
    color='black',
    align='center',
    dy= -18
).encode(text='Value')

st.subheader('KPI de Resultados Anuais')
st.altair_chart(graf_area+rotulos, use_container_width=True)

