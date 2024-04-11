import altair as alt
import pandas as pd
import streamlit as st

fonte = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})


# Estamos usando o altarir junto com streamlit para plotar o gráfico. 
graf_barras = alt.Chart(fonte).mark_bar().encode(
    x= 'a',
    y='b',
    color='a',
    tooltip=['a','b']
)

rotulo_barra = graf_barras.mark_text(
    dy= -6,
    size=17
).encode(
    text= 'b',
)
st.subheader('Plot do Gráfico de Barras')
st.altair_chart(graf_barras+rotulo_barra, use_container_width=True)

graf_barras_novo = alt.Chart(fonte).mark_bar(
    cornerRadiusTopLeft=10, # Arredondar cantos
    cornerRadiusTopRight=10
).encode(
    x=alt.X('a', sort= 'y'), # Classificação do menor valor para o maior, se quisermos inverter é só colocar -y
    y = 'b',
    color= alt.condition( # Aqui aplicamos uma condição
        alt.datum.b > 43, # A condição define que valores maiores que 43 vão estar em azul e menores em preto
        alt.value('steelblue'),
        alt.value('black')
        )
)

rotulo = graf_barras_novo.mark_text(
    align='center',
    baseline='middle',
    size=14,
    dy=-10
).encode(text='b')

linha_media = alt.Chart(fonte).mark_rule(color='red').encode(
    y='mean(b)'
)

st.altair_chart(graf_barras_novo+rotulo+linha_media, use_container_width=True)