import streamlit as st
import time

myBar = st.progress(0)
for num in range(100):
    time.sleep(0.01)
    myBar.progress(num+1)


with st.spinner("Aguarde..."):
    time.sleep(1)
st.success('Seu dataset foi carregado')
st.error('Caractere inválido')
st.warning('Data fora do intervalo')
st.info('Os resultados já foram carregados na base')

e = RuntimeError("Exceção do tipo RuntimeError")
st.exception(e)

st.snow()
st.balloons()