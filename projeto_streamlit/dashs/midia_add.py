import streamlit as st
from PIL import Image

myDog = Image.open('Mídia/dog.jpg')
st.subheader('1 - Imagem do meu dog')
st.image(myDog, caption='Um Cachorro Desconfiado')

myaudio = open('Mídia/Scratching The Surface.mp3', 'rb')
abrirAudio = myaudio.read()
st.subheader('2-Minha Música')
st.audio(abrirAudio, format='audio/mp3')

arquivoVideo = open('Mídia/Buildings.mp4', 'rb')
abrirVideo = arquivoVideo.read()
st.subheader('3-Vídeo dos Prédios')
st.video(abrirVideo)