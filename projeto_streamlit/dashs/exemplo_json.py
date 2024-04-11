import streamlit as st

meu_objeto = {
    'banana': 'amarela',
    'limão': 'verde',
    'laranja': 'laranja'
}

st.json(meu_objeto)