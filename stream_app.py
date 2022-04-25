
import streamlit as st
import pandas as pd

st.header("ANALISIS SENTIMEN REVIEW APLIKASI PEDULI LINDUNGI")
with st.sidebar:
    clicked = st.button(
        "HOME"
    )

uploaded_file = st.file_uploader("Choose a file")
     
dataframe = pd.read_csv(uploaded_file)
st.write(dataframe)

