
import streamlit as st


st.header("ANALISIS SENTIMEN REVIEW APLIKASI PEDULI LINDUNGI")

df = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)
df 

with st.sidebar:
    add_button = st.button(
       ("HOME")
    )
