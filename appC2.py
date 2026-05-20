import streamlit as st
import math

# Configuración de la página
st.set_page_config(page_title="Calculadora Pro", page_icon="🧮", layout="centered")

st.title("🧮 Calculadora Multifunción")
st.write("Selecciona una categoría y realiza tus cálculos fácilmente.")

# Categorías de operaciones
categoria = st.selectbox("Selecciona el tipo de operación:", [
    "Aritmética Básica", 
    "Trigonometría", 
    "Logaritmos y Avanzados"
])

st.divider()

if categoria == "Aritmética Básica":
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Primer número:", value=0.0)
    with col2:
        num2 = st.number_input("Segundo número:", value=0.0)
        
    operacion = st.radio("Operación:", ["Suma (+)", "Resta (-)", "Multiplicación (*)", "División (/)", "Potencia (x^y)", "Porcentaje (%)"], horizontal=True)
    
    if st.button("Calcular", type="primary"):
        if operacion == "Suma (+)":
            st.success(f"Resultado: {num1 + num2}")
        elif operacion == "Resta (-)":
            st.success(f"Resultado: {num1 - num2}")
        elif operacion == "Multiplicación (*)":
            st.success(f"Resultado: {num1 * num2}")
        elif operacion == "División (/)":
            if num2 == 0:
                st.error("Error: No se puede dividir entre cero.")
            else:
                st.success(f"Resultado: {num1 / num2}")
        elif operacion == "Potencia (x^y)":
            st.success(f"Resultado: {num1 ** num2}")
        elif operacion == "Porcentaje (%)":
            st.success(f"Resultado: {num1 * (num2 / 100)}")

elif categoria == "Trigonometría":
    num = st.number_input("Ingresa el ángulo en grados (°):", value=0.0)
    operacion = st.radio("Función:", ["Seno (sin)", "Coseno (cos)", "Tangente (tan)"], horizontal=True)
    
    if st.button("Calcular", type="primary"):
        rad = math.radians(num)
        if operacion == "Seno (sin)":
            st.success(f"Resultado: {math.sin(rad)}")
        elif operacion == "Coseno (cos)":
            st.success(f"Resultado: {math.cos(rad)}")
        elif operacion == "Tangente (tan)":
            # Validar indeterminación de la tangente (90, 270, etc.)
            if math.isclose(math.cos(rad), 0.0, abs_tol=1e-9):
                st.error("Error: La tangente no está definida para este ángulo.")
            else:
                st.success(f"Resultado: {math.tan(rad)}")

elif categoria == "Logaritmos y Avanzados":
    num = st.number_input("Ingresa el número:", value=1.0)
    operacion = st.radio("Operación:", ["Raíz Cuadrada (√)", "Logaritmo Base 10", "Logaritmo Natural (ln)", "Factorial (!)"], horizontal=True)
    
    if st.button("Calcular", type="primary"):
        if operacion == "Raíz Cuadrada (√)":
            if num < 0: st.error("Error: No existe raíz de un número negativo.")
            else: st.success(f"Resultado: {math.sqrt(num)}")
        elif operacion in ["Logaritmo Base 10", "Logaritmo Natural (ln)"]:
            if num <= 0: st.error("Error: El logaritmo está indefinido para números menores o iguales a cero.")
            elif operacion == "Logaritmo Base 10": st.success(f"Resultado: {math.log10(num)}")
            else: st.success(f"Resultado: {math.log(num)}")
        elif operacion == "Factorial (!)":
            if num < 0 or not num.is_integer(): st.error("Error: El factorial requiere un número entero positivo.")
            else: st.success(f"Resultado: {math.factorial(int(num))}")