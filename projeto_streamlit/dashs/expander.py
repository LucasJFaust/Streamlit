import streamlit as st

st.header('Expander')
st.line_chart({'Data': [1,5,2,6,2,1]})
with st.expander('Ver detalhes'):
    st.write("""Esse é um exemplo do Expander.
             Você vai ver como usá-lo""")
    st.image('./Mídia/dice.jpg')