"""
AI Fashion Stylist - Main Entry Point
Run with: streamlit run app.py
"""
import streamlit as st
from frontend.pages.chat import render_chat_page
from frontend.styles import get_custom_css

# Page configuration
st.set_page_config(
    page_title="AI Fashion Stylist",
    page_icon="👔",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Render the chat page
render_chat_page()