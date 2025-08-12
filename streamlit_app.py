import streamlit as st

# CSS laden
def load_css(path):
    with open(path, "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
load_css("./design.css")

st.write("Das ist mein Lernprojekt")

with st.container():
    st.write("text inside the container")
