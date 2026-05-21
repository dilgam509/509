import streamlit as st
import random
import time

# Configuración de la página con tema claro por defecto
st.set_page_config(page_title="JDM Car Memory Game", page_icon="🚗", layout="centered")

# Estilos CSS para asegurar fondo claro y alta visibilidad
st.markdown("""
    <style>
    .stApp {
        background-color: #F8F9FA;
        color: #212529;
    }
    h1, h3 {
        color: #1A1D20 !important;
        text-align: center;
    }
    /* Estilo de los botones del memorama */
    .stButton>button {
        background-color: #FFFFFF !important;
        color: #212529 !important;
        border: 2px solid #CED4DA !important;
        border-radius: 8px;
        height: 80px;
        width: 100%;
        font-size: 28px !important;
        font-weight: bold;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        border-color: #0D6EFD !important;
        background-color: #E9ECEF !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚗 JDM Car Memorama")
st.write("¡Encuentra las parejas de autos deportivos! Haz clic en las tarjetas para voltearlas.")

# 1. Inicializar el estado del juego
CARROS = ["🏎️", "🚗", "🚙", "🚓", "🚘", "🚨", "🏎️", "🚗", "🚙", "🚓", "🚘", "🚨"]

if "tablero" not in st.session_state:
    random.shuffle(CARROS)
    st.session_state.tablero = CARROS
    st.session_state.volteadas = [False] * 12
    st.session_state.seleccionadas = []
    st.session_state.parejas_encontradas = set()
    st.session_state.intentos = 0

# Función para reiniciar el juego
def reiniciar_juego():
    random.shuffle(CARROS)
    st.session_state.tablero = CARROS
    st.session_state.volteadas = [False] * 12
    st.session_state.seleccionadas = []
    st.session_state.parejas_encontradas = set()
    st.session_state.intentos = 0

# 2. Lógica de selección
if len(st.session_state.seleccionadas) == 2:
    idx1, idx2 = st.session_state.seleccionadas
    st.session_state.intentos += 1
    
    # Si coinciden, se quedan volteadas permanentemente
    if st.session_state.tablero[idx1] == st.session_state.tablero[idx2]:
        st.session_state.parejas_encontradas.add(st.session_state.tablero[idx1])
    else:
        # Si no coinciden, esperamos un momento y las volvemos a ocultar
        time.sleep(1.0)
        st.session_state.volteadas[idx1] = False
        st.session_state.volteadas[idx2] = False
        
    st.session_state.seleccionadas = []
    st.rerun()

# 3. Renderizar el tablero (Matriz de 3x4)
cols_matriz = 4
for i in range(0, 12, cols_matriz):
    cols = st.columns(cols_matriz)
    for j in range(cols_matriz):
        idx = i + j
        with cols[j]:
            # Determinar qué mostrar en el botón
            if st.session_state.volteadas[idx] or st.session_state.tablero[idx] in st.session_state.parejas_encontradas:
                label = st.session_state.tablero[idx]
                deshabilitado = True
            else:
                label = "❓"
                deshabilitado = False
            
            # Acción al hacer clic
            if st.button(label, key=f"btn_{idx}", disabled=deshabilitado):
                if len(st.session_state.seleccionadas) < 2 and not st.session_state.volteadas[idx]:
                    st.session_state.volteadas[idx] = True
                    st.session_state.seleccionadas.append(idx)
                    st.rerun()

# 4. Marcador y Estado Final
st.write("---")  # Línea divisoria en formato Streamlit correcto
st.subheader(f"Intentos: {st.session_state.intentos} | Parejas: {len(st.session_state.parejas_encontradas)}/6")

if len(st.session_state.parejas_encontradas) == 6:
    st.balloons()
    st.success(f"🏆 ¡Felicidades! Completaste el memorama en {st.session_state.intentos} intentos.")

if st.button("🔄 Reiniciar Juego"):
    reiniciar_juego()
    st.rerun()