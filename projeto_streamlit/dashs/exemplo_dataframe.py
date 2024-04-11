import streamlit as st
import pandas as pd
import numpy as np

st.header('Aula de Dataframe')

df = pd.DataFrame(
    np.random.randn(5,5), # Aqui criamos um df randomico.
    columns = ('col %d' %i for i in range(5))
)

st.dataframe(df)

st.subheader('Exemplo 2 - Alterando Dimensões')
st.dataframe(df, 300, 200) # Aqui só mudamos as dimensões do df.

st.subheader('Exemplo 3 - Dando um destaque nos maiores valores')
st.dataframe(df.style.highlight_max(axis=0)) # Aqui usamos uma função para dar ênfase nos maiores valores da tabela, com o axis=0 estamos cosiderando a partir da coluna 0 verticalmente, se mudarmos para axis=1 a referência vira horizontal.

st.header('Exemplo - Table')
st.table(df)
