import streamlit as st
import numpy as np

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader('Coluna 1')
    st.image('./Mídia/cat.jpg')

with col2:
    st.subheader('Coluna 2')
    st.image('./Mídia/dog.jpg')

with col3:
    st.subheader('Coluna 3')
    st.image('./Mídia/owl.jpg')

with col4:
    st.subheader('Coluna 4')
    st.image('./Mídia/dog_2.jpg')

col_1, col_2 = st.columns([3,1]) # Aqui estou dizendo para streamlit que eu quero 2 colunas mas a primeira com o triplo do tamanho que a segunda.
data = np.random.rand(100,1)

col_1.line_chart(data)
col_2.write(data)