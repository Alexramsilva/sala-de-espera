# -*- coding: utf-8 -*-
"""Sala de espera.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G5mJcyBbD2XEtHgbIa0QHndDj85pjJDX
"""

import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Harry Markowitz frente a la Inteligencia Artificial", layout="centered")

st.image("URC.png", caption="LCFI-URC Universidad Rosario Castellanos", width=200)

st.title("Sala de Espera (Conferencia: Harry Markowitz frente a la Inteligencia Artificial) ")

# Configura la hora de la reunión
meeting_time_str = "2024-11-08 13:00:00"  # Reemplaza con la fecha y hora de tu reunión
meeting_time = datetime.strptime(meeting_time_str, "%Y-%m-%d %H:%M:%S")


# Función para calcular el tiempo restante
def get_time_remaining():
    now = datetime.now()
    return meeting_time - now

# Muestra un mensaje de bienvenida
st.markdown("<p style='font-size:20px; font-weight:bold;'>¡Nos dará mucho gusto que nos puedas acompañar!</p>", unsafe_allow_html=True)
st.write("La reunión comenzará en la siguiente fecha y hora:")
st.write(meeting_time.strftime("%d %B %Y, %H:%M:%S"))

# Calcula el tiempo restante y muestra un temporizador
time_remaining = get_time_remaining()

if time_remaining.total_seconds() > 0:
    days, seconds = time_remaining.days, time_remaining.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    st.write(f"Tiempo restante: {days} días, {hours} horas, {minutes} minutos, {seconds} segundos")
else:
    st.write("La reunión ha comenzado. Puedes unirte ahora.")

# Liga de Zoom
meeting_link = "https://us06web.zoom.us/j/82156977959?pwd=A8TZOI6dQSzYTxr5T3BZpacQtEfZb3.1"  # Coloca aquí el enlace de Zoom
st.markdown(f"[Unirse a la reunión en Zoom]({meeting_link})", unsafe_allow_html=True)
st.markdown(<p style='font-size:20px; font-weight:bold;'>"Clave de acceso: 360529", unsafe_allow_html=True)

# Personalización de diseño
st.markdown("""
<style>
    .stApp {
        background-color:  #00FF00;
    }
    .css-1d391kg {
        color:  #faf7f8;
    }
</style>
""", unsafe_allow_html=True)

# Añadir la línea separadora
st.markdown("<hr>", unsafe_allow_html=True)

# Insertar el código HTML con estilos personalizados
st.markdown("""
    <div class="container col-sm-5 creditos text-center">
        <p style="margin-top:0;margin-bottom:0;font-size:15px;color: #424040;text-align:center">
            <strong>2DA EDICIÓN DE JORNADAS FINANCIERAS</strong>
        </p>
        <p style="margin-top:0;margin-bottom:0;font-size:12px;color:  #979394 ;text-align:center">
            <strong>"Harry Markowitz frente a la Inteligencia Artificial"</strong>
        </p>
        <p style="margin-top:0;margin-bottom:0;font-size:12px;color:  #979394 ;text-align:center">
            <strong>LCFI-URC</strong>
        </p>
    </div>
""", unsafe_allow_html=True)