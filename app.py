import streamlit as st

# Configuración de la página web
st.set_page_config(page_title="Calculadora Kivy-Style", page_icon="🧮", layout="centered")

# Estilos CSS personalizados para imitar el diseño oscuro y redondeado de tu código original
st.markdown("""
    <style>
    /* Fondo general oscuro */
    .stApp {
        background-color: #262626;
    }
    /* Estilo para la pantalla de texto (Display) */
    .stTextInput input {
        background-color: #333333 !important;
        color: #ffffff !important;
        font-size: 36px !important;
        text-align: right !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 20px !important;
    }
    /* Estilo base para todos los botones */
    div.stButton > button {
        width: 100%;
        height: 60px;
        font-size: 22px !important;
        font-weight: bold;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        transition: all 0.1s ease;
    }
    /* Botones de operaciones (Azul) */
    div.op-btn > div > button {
        background-color: #1a99cc !important;
        color: #ffffff !important;
    }
    div.op-btn > div > button:hover {
        background-color: #147da6 !important;
        color: #ffffff !important;
    }
    /* Botones numéricos (Blanco/Gris claro) */
    div.num-btn > div > button {
        background-color: #f2f2f2 !important;
        color: #1a1a1a !important;
    }
    div.num-btn > div > button:hover {
        background-color: #d9d9d9 !important;
        color: #1a1a1a !important;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar las variables de estado (para que Streamlit recuerde lo que escribes)
if 'display' not in st.session_state:
    st.session_state.display = ""
if 'last_was_equal' not in st.session_state:
    st.session_state.last_was_equal = False

# Lista de operadores para la lógica
operators = ['+', '-', '*', '/']

# Función que maneja los clics de los botones
def click_button(label):
    if label == 'C':
        st.session_state.display = ""
        st.session_state.last_was_equal = False
    elif label == '=':
        try:
            if st.session_state.display:
                # Evalúa la operación
                result = eval(st.session_state.display)
                # Formatea float si es necesario
                if isinstance(result, float):
                    st.session_state.display = f"{result:.2f}".rstrip('0').rstrip('.')
                else:
                    st.session_state.display = str(result)
                st.session_state.last_was_equal = True
        except Exception:
            st.session_state.display = "Error"
            st.session_state.last_was_equal = False
    else:
        if st.session_state.last_was_equal:
            if label in operators:
                st.session_state.display += label
            else:
                st.session_state.display = label
            st.session_state.last_was_equal = False
        else:
            st.session_state.display += label

# --- INTERFAZ DE USUARIO ---

st.title("🧮 Calculadora")

# Pantalla de la calculadora
st.text_input(label="Resultado", value=st.session_state.display, key="screen", label_visibility="collapsed", disabled=True)

# Distribución de botones en Matriz (4 filas x 4 columnas)
botones = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Renderizar la grilla de botones aplicando los estilos correspondientes
for fila in botones:
    cols = st.columns(4)
    for i, btn_text in enumerate(fila):
        # Determinar si es operador o número para el estilo visual
        is_op = btn_text in operators or btn_text in ['C', '=']
        css_class = "op-btn" if is_op else "num-btn"
        
        with cols[i]:
            # Envolvemos el botón en un contenedor div para que el CSS sepa cuál es cuál
            st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
            if st.button(btn_text, key=f"btn_{btn_text}"):
                click_button(btn_text)
                st.rerun() # Recarga la app para refrescar la pantalla inmediatamente
            st.markdown('</div>', unsafe_allow_html=True)
            