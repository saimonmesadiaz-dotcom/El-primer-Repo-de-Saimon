import streamlit as st
from PIL import Image

# -----------------------------
# CONFIGURACIÓN
# -----------------------------

st.set_page_config(
    page_title="Snoopy World Club Fans",
    layout="wide"
)

# -----------------------------
# ESTILOS
# -----------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap');

.stApp {
    background: linear-gradient(
        180deg,
        #9ED9F5 0%,
        #CDEEFF 45%,
        #FFF9E8 100%
    );
    font-family: 'Comic Neue', cursive;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

h1 {
    color: #222222 !important;
    text-align: center;
    font-size: 3.2rem !important;
    font-weight: 700 !important;
}

h2, h3 {
    color: #333333 !important;
    font-weight: 700 !important;
}

p {
    color: #333333;
    font-size: 1.1rem;
}

/* -----------------------------
   TARJETAS
----------------------------- */

.card {
    background: rgba(255,255,255,0.92);
    padding: 25px;
    border-radius: 25px;
    border: 3px solid #222222;
    box-shadow: 8px 8px 0px #222222;
    margin-bottom: 25px;
}

/* -----------------------------
   IMÁGENES
----------------------------- */

.stImage img {
    width: 100%;
    height: 320px;
    object-fit: cover;
    border-radius: 22px;
    border: 3px solid #222222;
    box-shadow: 7px 7px 0px #222222;
}

/* -----------------------------
   INPUTS
----------------------------- */

.stTextInput input {
    border: 3px solid #222222;
    border-radius: 15px;
    background-color: white;
}

/* -----------------------------
   SEPARADORES
----------------------------- */

hr {
    border: none;
    height: 3px;
    background-color: #222222;
    margin: 35px 0;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# TÍTULO
# -----------------------------

st.markdown(
    "<h1>Snoopy World Club Fans</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="card">
        <h3>☁️ ¡Bienvenido al mundo de Snoopy!</h3>
        <p>
        En este repositorio encontrarás información acerca de las
        novedades de la merch, programas y contenido de Snoopy
        y sus amigos.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# BANNER PRINCIPAL
# -----------------------------

image = Image.open("SnoopyBanner.jpg")

st.image(
    image,
    use_container_width=True
)


# -----------------------------
# MENSAJE
# -----------------------------

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="card">
        <h3>💬 Déjale un mensaje a Snoopy</h3>
    </div>
    """,
    unsafe_allow_html=True
)

texto = st.text_input(
    "Escribe algo:",
    "Este es mi texto"
)

st.write("El texto escrito es:", texto)


# =====================================================
# PRIMERA FILA DE IMÁGENES
# =====================================================

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    "<h2 style='text-align:center;'>🐾 Snoopy y sus amigos 🐾</h2>",
    unsafe_allow_html=True
)

img1, img2 = st.columns(2)

with img1:
    imagen_snoopy = Image.open("SnoopyFondo.jpg")
    st.image(imagen_snoopy)

with img2:
    imagen_woodstock = Image.open("Woodstock.jpg")
    st.image(imagen_woodstock)


# =====================================================
# LAS DOS COLUMNAS ORIGINALES
# =====================================================

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    "<h2 style='text-align:center;'>🎨 Interfaces multimodales</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


# -----------------------------
# PRIMERA COLUMNA
# -----------------------------

with col1:

    st.markdown(
        """
        <div class="card">
        """,
        unsafe_allow_html=True
    )

    st.subheader("Esta es la primera columna")

    st.write("Las interfaces multimodales mejoran la UX")

    resp = st.checkbox("Estoy de acuerdo")

    if resp:
        st.write("Correcto")

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# -----------------------------
# SEGUNDA COLUMNA
# -----------------------------

with col2:

    st.markdown(
        """
        <div class="card">
        """,
        unsafe_allow_html=True
    )

    st.subheader("Esta es la segunda columna")

    modo = st.radio(
        "Que Modalidad es la principal en tu interfaz",
        ("Visual", "Auditiva", "Táctil")
    )

    if modo == "Visual":
        st.write("La vista es fundamental para tu interfaz")

    if modo == "Auditiva":
        st.write("La audición es fundamental para tu interfaz")

    if modo == "Táctil":
        st.write("El tacto es fundamental para tu interfaz")

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =====================================================
# SEGUNDA FILA DE IMÁGENES
# =====================================================

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    "<h2 style='text-align:center;'>⭐ El mundo de Peanuts ⭐</h2>",
    unsafe_allow_html=True
)

img3, img4 = st.columns(2)

with img3:
    imagen_merch = Image.open("SnoopyMerch.jpg")
    st.image(imagen_merch)

with img4:
    imagen_peanuts = Image.open("Peanuts.jpg")
    st.image(imagen_peanuts)


# -----------------------------
# PIE DE PÁGINA
# -----------------------------

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align:center;">
        <h3>Snoopy World Club Fans</h3>
        <p>Un pequeño rincón dedicado al universo de Snoopy y Peanuts.</p>
        <p>⭐ 🐾 ☁️ 🐾 ⭐</p>
    </div>
    """,
    unsafe_allow_html=True
)
