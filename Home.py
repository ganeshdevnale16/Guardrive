import streamlit as st

st.set_page_config(
    page_title="Guardrive",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Guardrive")

st.write("Driver-controlled location sharing")

if st.button("🚗 Driver Portal", use_container_width=True):
    st.switch_page("Driver.py")

if st.button("👥 Family Access", use_container_width=True):
    st.switch_page("Family_Chat.py")
