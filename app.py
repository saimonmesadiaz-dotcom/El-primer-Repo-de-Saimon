import streamlit as st
from PIL import Image
st.title("Hola! Bienvenidos a Snoopy World Club Fans")

st.header("En este repositorio, encontrarás información acerca de las novedades de la merch y programas de Snoopy y sus amigos")
image = Image.open('SnoopyBanner.jpg')
st.image(image, caption='SnoopyBanner')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la UX")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio ("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'Auditivo':
    st.write('La audición es fundamental para tu interfaz')
  if modo == 'Táctil':
    st.write('El tacto es fundamental para tu interfaz')
