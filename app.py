import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Calculadora Modo Claro", 
    page_icon="🧮", 
    layout="centered"
)

# 2. ESTILOS CSS PARA MODO CLARO (Alto Contraste)
st.markdown("""
    <style>
    /* Fondo general de la aplicación (Blanco impoluto) */
    .stApp {
        background-color: #ffffff !important;
    }
    
    /* Título principal en color gris oscuro/negro */
    h1 {
        color: #1a1a1a !important;
        text-align: center;
        font-weight: bold !important;
    }

    /* Pantalla de la calculadora (Display) blanca con borde marcado y números negros */
    .stTextInput input {
        background-color: #f7f9fa !important;
        color: #111111 !important; 
        font-size: 42px !important;
        font-family: monospace !important;
        text-align: right !important;
        border-radius: 12px !important;
        border: 2px solid #cccccc !important;
        padding: 20px !important;
        box-shadow: inset 0px 2px 5px rgba(0,0,0,0.05);
    }

    /* Diseño base de los botones de la calculadora */
    div.stButton > button {
        width: 100%;
        height: 70px;
        font-size: 26px !important;
        font-weight: bold !important;
        border-radius: 14px !important;
        border: 1px solid #dddddd !important;
        box-shadow: 0px 3px 6px rgba(0,0,0,0.05);
        transition: background-color 0.2s, transform 0.1s;
    }

    div.stButton > button:active {
        transform: scale(0.96);
    }

    /* BOTONES NUMÉRICOS: Gris claro sutil con NUMEROS NEGROS puros */
    div.num-btn > div > button {
        background-color: #eaeaea !important;
        color: #000000 !important; /* NEGRO ABSOLUTO */
    }
    div.num-btn > div > button:hover {
        background-color: #dfdfdf !important;
        color: #000000 !important;
    }

    /* BOTONES DE OPERADORES: Azul rey nítido con texto blanco */
    div.op-btn > div > button {
        background-color: #0066cc !important;
        color: #ffffff !important;
    }
    div.op-btn > div > button:hover {
        background-color: #0052a3 !important;
        color: #ffffff !important;
    }

    /* BOTÓN DE BORRAR 'C': Naranja/Rojo vibrante con texto blanco */
    div.clear-btn > div > button {
        background-color: #e63946 !important;
        color: #ffffff !important;
    }
    div.clear-btn > div > button:hover {
        background-color: #cc1f2d !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. MEMORIA INTERNA DE LA CALCULADORA
if 'display' not in st.session_state:
    st.session_state.display = ""
if 'reiniciar' not in st.session_state:
    st.session_state.reiniciar = False

# Lógica de procesamiento de operaciones
def presionar(boton):
    if boton == 'C':
        st.session_state.display = ""
        st.session_state.reiniciar = False
    elif boton == '=':
        try:
            if st.session_state.display:
                ecuacion = st.session_state.display.replace('x', '*')
                resultado = eval(ecuacion)
                
                if isinstance(resultado, float):
                    st.session_state.display = f"{resultado:.2f}".rstrip('0').rstrip('.')
                else:
                    st.session_state.display = str(resultado)
                st.session_state.reiniciar = True
        except:
            st.session_state.display = "Error"
            st.session_state.reiniciar = True
    else:
        if st.session_state.reiniciar and boton not in ['+', '-', 'x', '/']:
            st.session_state.display = boton
        else:
            st.session_state.display += boton
        st.session_state.reiniciar = False

# 4. CONSTRUCCIÓN DE LA INTERFAZ
st.title("🧮 Calculadora")
st.write("")

# Render de la pantalla numérica
st.text_input(label="screen", value=st.session_state.display, label_visibility="collapsed", disabled=True)
st.write("")

# Distribución de la botonera
botones = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', 'x'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Dibujar las filas y columnas aplicando el nuevo estilo claro
for fila in botones:
    cols = st.columns(4)
    for i, texto in enumerate(fila):
        if texto == 'C':
            clase_css = "clear-btn"
        elif texto in ['/', 'x', '-', '+', '=']:
            clase_css = "op-btn"
        else:
            clase_css = "num-btn"
        
        with cols[i]:
            st.markdown(f'<div class="{clase_css}">', unsafe_allow_html=True)
            st.button(texto, key=f"btn_{texto}", on_click=presionar, args=(texto,))
            st.markdown('</div>', unsafe_allow_html=True)