
import streamlit as st
import pandas as pd

st.header("ANALISIS SENTIMEN REVIEW APLIKASI PEDULI LINDUNGI")
with st.sidebar:
    clicked1 = st.button(
        "HOME"
    )
    clicked2 = st.button(
        "PraProcess Data"
    )
     clicked3 = st.button(
        "MODEL"
    )
    clicked4 = st.button(
        "Visualization"
    )


uploaded_file = st.file_uploader("Choose a file")
     
dataframe = pd.read_csv(uploaded_file)
st.write(dataframe)

