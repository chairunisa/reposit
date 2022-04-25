
import streamlit as st
import pandas as pd

st.header("ANALISIS SENTIMEN REVIEW APLIKASI PEDULI LINDUNGI")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)
     
dataframe = pd.read_csv(uploaded_file)
st.write(dataframe)

with st.sidebar:
    add_button = st.button(
       ("HOME")
    )
