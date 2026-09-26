import streamlit as st
from PIL import Image

# -----------------------------
# CONFIGURACIÓN
# -----------------------------

st.set_page_config(
    page_title="Snoopy World Club Fans 🐶",
    page_icon="🐶",
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

/* Contenedor principal */

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Títulos */

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

/* Texto */

p {
    color: #333333;
    font-size: 1.1rem;
}

/* Tarjetas */

.card {
    background: rgba(255,255,255,0.90);
    padding: 25px;
    border-radius: 25px;
    border: 3px solid #222222;
    box-shadow: 8px 8px 0px #222222;
    margin-bottom: 25px;
}

/* Banner */

.banner {
    border-radius: 25px;
    border: 4px solid #222222;
    box-shadow: 10px 10px 0px #222222;
    margin-bottom: 30px;
}

/* Botones */

.stButton > button {
    background-color: #F7D447;
    color: #222222;
    border: 3px solid #222222;
    border-radius: 15px;
    font-family: 'Comic Neue', cursive;
    font-weight: bold;
    box-shadow: 4px 4px 0px #222222;
}

.stButton > button:hover {
    background-color: #F2C62D;
    transform: translateY(-2px);
}

/* Inputs */

.stTextInput input {
    border: 3px solid #222222;
    border-radius: 15px;
    background-color: white;
}

/* Separadores */

hr {
    border: none;
    height: 3px;
    background-color: #222222;
    margin: 35px 0;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# ENCABEZADO
# -----------------------------

st.markdown(
    "<h1>🐶 Snoopy World Club Fans</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="card">
        <h3>☁️ ¡Bienvenido al mundo de Snoopy!</h3>
        <p>
        Un pequeño espacio para descubrir novedades, merchandising,
        programas y curiosidades de Snoopy y sus amigos.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# BANNER
# -----------------------------

image = Image.open("SnoopyBanner.jpg")

st.image(
    image,
    use_container_width=True
)


# -----------------------------
# MENSAJE
# -----------------------------

st.markdown(
    """
    <div class="card">
        <h3>💬 Déjale un mensaje a Snoopy</h3>
    </div>
    """,
    unsafe_allow_html=True
)

texto = st.text_input(
    "Escribe algo para el club:",
    "¡Hola Snoopy! 🐶"
)

st.success(f"Snoopy recibió tu mensaje: {texto}")


# -----------------------------
# SECCIONES
# -----------------------------

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    "<h2 style='text-align:center;'>⭐ Conoce el club ⭐</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

# -----------------------------
# COLUMNA 1
# -----------------------------

with col1:

    st.markdown(
        """
        <div class="card">
            <h3>🐾 Tu opinión</h3>
            <p>
            ¿Te gustan las novedades de Snoopy y sus amigos?
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    resp = st.checkbox("Sí, soy fan de Snoopy 🐶")

    if resp:
        st.balloons()
        st.success("¡Bienvenido oficialmente al Snoopy World Club! ⭐")


# -----------------------------
# COLUMNA 2
# -----------------------------

with col2:

    st.markdown(
        """
        <div class="card">
            <h3>🎨 Tu personaje favorito</h3>
            <p>
            ¿Qué aspecto de Snoopy disfrutas más?
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    modo = st.radio(
        "Elige una opción:",
        (
            "🐶 Snoopy",
            "🐦 Woodstock",
            "🎹 Schroeder",
            "👧 Lucy"
        )
    )

    st.info(f"¡Elegiste {modo}!")


# -----------------------------
# PIE DE PÁGINA
# -----------------------------

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align:center;">
        <h3>☁️ Snoopy World Club Fans 🐶</h3>
        <p>Un pequeño rincón dedicado al universo de Peanuts.</p>
        <p>⭐ 🐾 ☁️ 🐶 ☁️ 🐾 ⭐</p>
    </div>
    """,
    unsafe_allow_html=True
)
