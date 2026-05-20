import streamlit as st

# Configuración de la página (Debe ser la primera línea de Streamlit)
st.set_page_config(
    page_title="JDM Garage - Tienda de Autos",
    page_icon="🏎️",
    layout="wide"
)

# Estilo CSS personalizado para darle vibra JDM (colores oscuros y acentos rojos)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .jdm-title { color: #ff4b4b; font-family: 'Arial Black', sans-serif; text-align: center; }
    .car-card { border: 1px solid #333; padding: 15px; border-radius: 10px; background-color: #161a24; }
    </style>
""", unsafe_allow_html=True)

# Título de la tienda
st.markdown("<h1 class='jdm-title'>🎌 JDM GARAGE 🎌</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: gray;'>Los mejores íconos del automovilismo japonés directos a tu garage.</p>", unsafe_allow_html=True)

# Base de datos simulada de autos (Usamos URLs reales de Unsplash para las imágenes)
autos_jdm = [
    {
        "nombre": "Nissan Skyline GT-R R34 (2002)",
        "precio": "$120,000 USD",
        "motor": "RB26DETT Twin-Turbo L6",
        "hp": "280 HP (Stock)",
        "imagen": "https://images.unsplash.com/photo-1616422285623-13ff0162193c?w=600&auto=format&fit=crop&q=60"
    },
    {
        "nombre": "Toyota Supra MK4 (1998)",
        "precio": "$95,000 USD",
        "motor": "2JZ-GTE Twin-Turbo L6",
        "hp": "320 HP",
        "imagen": "https://images.unsplash.com/photo-1626847037657-fd3622613ce3?w=600&auto=format&fit=crop&q=60"
    },
    {
        "nombre": "Mazda RX-7 FD (1997)",
        "precio": "$65,000 USD",
        "motor": "13B-REW Bi-Rotativo",
        "hp": "255 HP",
        "imagen": "https://images.unsplash.com/photo-1718037302497-293673752e25?w=600&auto=format&fit=crop&q=60"
    },
    {
        "nombre": "Honda Civic Type R EK9 (1999)",
        "precio": "$35,000 USD",
        "motor": "B16B VTEC L4",
        "hp": "185 HP",
        "imagen": "https://images.unsplash.com/photo-1632245889029-e406faaa34cd?w=600&auto=format&fit=crop&q=60"
    }
]

# Inicializar el carrito de compras en la sesión de Streamlit si no existe
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# Layout de pestañas: Tienda y Carrito
tab1, tab2 = st.tabs(["🛒 Catálogo de Autos", "📦 Mi Carrito de Compras"])

with tab1:
    st.subheader("Disponibles en inventario")
    
    # Crear una cuadrícula de 2 columnas para los autos
    col1, col2 = st.columns(2)
    
    for idx, auto in enumerate(autos_jdm):
        # Alternar la posición entre columna 1 y columna 2
        col_actual = col1 if idx % 2 == 0 else col2
        
        with col_actual:
            st.markdown(f"<div class='car-card'>", unsafe_allow_html=True)
            st.image(auto["imagen"], use_column_width=True)
            st.subheader(auto["nombre"])
            st.write(f"**Precio:** {auto['precio']}")
            st.write(f"**Motor:** {auto['motor']} | **Potencia:** {auto['hp']}")
            
            # Botón único para cada auto usando su índice
            if st.button(f"Añadir al Carrito", key=f"btn_{idx}"):
                st.session_state.carrito.append(auto)
                st.success(f"¡{auto['nombre']} añadido al carrito!")
            st.markdown("</div><br>", unsafe_allow_html=True)

with tab2:
    st.subheader("Tu Garage Virtual")
    if len(st.session_state.carrito) == 0:
        st.info("Tu carrito está vacío. ¡Ve a buscar algunos caballos de fuerza!")
    else:
        for item in st.session_state.carrito:
            st.write(f"🏎️ **{item['nombre']}** - {item['precio']}")
        
        st.write("---")
        if st.button("Vaciar Carrito"):
            st.session_state.carrito = []
            st.rerun()
            
        if st.button("Proceder al Pago (Simulación)"):
            st.balloons()
            st.success("¡Felicidades! Tu orden JDM ha sido procesada con éxito. Prepárate para el drift.")