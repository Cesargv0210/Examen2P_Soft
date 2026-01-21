#importamos las librerias a usar en nuestra página
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

#Configuracion de la pagina
st.set_page_config(
    page_title="Historial de producción del Campo Volve",
    page_icon="ImgCampo.jpg",
    layout="wide",
    initial_sidebar_state="collapsed",
)
#Descripción de la pagina
st.markdown("""
       <div class="stMetric">
       <h4>Historial de producción del Campo Volve</h4>
       <p style="font-size:14px;">
       El campo petrolero offshore Volve se ubica en el Mar del Norte, cerca de Sleipner Øst, 
       descubierto en 1993, con petróleo jurásico en areniscas, desarrollado con una plataforma 
       autoelevable y producción iniciada en 2008, caracterizado por sus reservas y su desarrollo 
       ingenioso para maximizar la producción, incluyendo un buque de almacenamiento (Navion Saga). 
       </p>
       </div>
       """, unsafe_allow_html=True)
st.image(
    "ImgCampo.jpg",
    use_container_width=True
)
#Realizacion del menu usando sidebar
with st.sidebar:
    st.markdown(
        """
        <div style="
            color:#f39c12;
            text-align:center;
            font-size:30px;
            font-weight:700;
            margin-bottom:12px;
        ">
            Bienvenido a la página de datos del campo VOLVE
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown(
        """
        <h4 style="
            color:#f39c12;
            text-align:left;
            margin:10px 0px 5px 0px;
        ">
            Menú de opciones
        </h4>
        """,
        unsafe_allow_html=True
    )
    selected = option_menu(
        menu_title=None,
        options=["Home", "Data", "Plots"],
        icons=["house", "database", "graph-up-arrow"],
        menu_icon="list",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0e1117"},
            "icon": {"color": "#f39c12", "font-size": "18px"},
            "nav-link": {"color": "white", "font-size": "15px", "text-align": "left",
                         "margin": "0px"},
            "nav-link-selected": {"background-color": "#262730"},
        }
    )

#Seccion HOME
if selected == "Home":

    # --- HERO SECTION ---
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #0e1117, #1f2933);
        padding: 40px;
        border-radius: 20px;
        margin-bottom: 30px;
    ">
        <h1 style="color:#f39c12; font-size:42px; margin-bottom:10px;">
            Página de incio - Campo VOLVE - 
        </h1>
        <p style="color:#d1d5db; font-size:18px; max-width:900px;">
             El campo petrolero offshore Volve se ubica en el Mar del Norte, cerca de Sleipner Øst, 
       descubierto en 1993, con petróleo jurásico en areniscas, desarrollado con una plataforma 
       autoelevable y producción iniciada en 2008, caracterizado por sus reservas y su desarrollo 
       ingenioso para maximizar la producción, incluyendo un buque de almacenamiento (Navion Saga).
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- IMAGEN DEBAJO DEL HERO ---

