import streamlit as st
import altair as alt
import pandas as pd

df = pd.read_csv('/home/faust/Projetos/Streamlit/projeto_streamlit/dashs/Datasets/vega_car.csv')

df

disper = alt.Chart(df).mark_point().encode(
    x = 'Weight_in_lbs:Q',
    y = 'Miles_per_Gallon',
    color = alt.Color('Origin:N')
)

st.subheader("Gráfico de Dispersão: Consumo por Cavalo")

st.altair_chart(disper, use_container_width=True)