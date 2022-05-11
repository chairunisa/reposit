
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.header("ANALISIS SENTIMEN REVIEW APLIKASI PEDULI LINDUNGI")

with st.sidebar:
    selected = option_menu(
        menu_title = "ANALISIS SENTIMEN",
        options = ["Dashboard","Preprocessing","Klasifikasi","Visualisasi"],
    )
    
if selected == "Dasboard":
    st.title(f"UPLOAD DATA {selected}")

    
if selected == "Preprocessing":
    st.title(f"YOU SELECTED {selected}")

    

