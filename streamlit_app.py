
import streamlit as st

#? --- PAGE SETUP ---#
st.set_page_config(layout="wide")

sucursales_page = st.Page(
    page="views/sucursales.py",
    title="Sucursales",
    icon="📋",
    default=True
)

#? --- NAVEGATION SETUP [WITH SECTIONS] ---#
pg = st.navigation(
    {
        "Información de sucursales": [sucursales_page],
    }
)

#? --- SHARE ON ALL PAGES ---#
st.logo("assets/narcisse.png")
st.sidebar.text("Made with ❤️ by Narcisse")

#? --- RUN NAVEGATION ---#
pg.run()