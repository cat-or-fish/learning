import streamlit as st

# CSS laden
def load_css(path):
    with open(path, "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
css_path = "./design.css"
load_css(css_path)

st.write("Das ist mein Lernprojekt")

st.container(key="green"):
    st.write("text inside the container")

st.button("Click me", key="blue")
