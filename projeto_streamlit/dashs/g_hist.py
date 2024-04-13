import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io= '/home/faust/Projetos/Streamlit/projeto_streamlit/dashs/Datasets/normal_dist.xlsx',
    engine= 'openpyxl',
    sheet_name= 'Sheet1',
    usecols= 'A:C',
    nrows=87,
)

if st.button("Iniciar"):
    st.experimental_rerun()
if st.button("Parar"):
    st.stop()


Hist = alt.Chart(df).mark_bar().encode(
    x = alt.X('x', bin=alt.Bin(step=5)), # com o uso do bin nos agrupamos o eixo x em 5.
    y = 'sum(count)'
)

st.subheader('Histograma - Notas de 1000 Alunos')

st.altair_chart(Hist,use_container_width=True)

df