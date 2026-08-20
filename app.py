import streamlit as st
from PIL import Image
st.title("Hola! Bienvenidos a Snoopy World Club Fans")

st.header("En este repositorio, encontrarás información acerca de las novedades de la merch y programas de Snoopy y sus amigos")
image = Image.open('SnoopyBanner.jpg')
st.image(image, caption='SnoopyBanner')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)
