import streamlit as st
from PIL import Image

myDog = Image.open('dashs/Mídia/dog.jpg')
st.subheader('1 - Imagem do meu dog')
st.image(myDog, caption='Um Cachorro Desconfiado')