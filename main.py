import streamlit as st

st.set_page_config(layout="wide")
col1,col2= st.columns(2)

with col1:
    st.image("D:Project_Showcase/images.zip/photo.png")

with col2:
    st.title("Gokul Teja")
    content=''' Hi  i Am Gokul teja  '''
    st.info(content)
