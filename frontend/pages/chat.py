"""
Main chat interface for the Fashion Stylist
"""
import streamlit as st
from dotenv import load_dotenv
from backend.ai_service import FashionAIService
from frontend.components import (
    render_header, 
    render_welcome_message, 
    render_sidebar,
    render_quick_tips
)

# Load environment variables
load_dotenv()

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "ai_service" not in st.session_state:
        st.session_state.ai_service = FashionAIService()

def render_chat_page():
    """Renders the main chat interface"""
    
    # Initialize session
    initialize_session_state()
    
    # Render header
    render_header()
    
    # Render sidebar and get example question if clicked
    example_question = render_sidebar()
    
    # Show welcome message if no conversation yet
    if len(st.session_state.messages) == 0:
        render_welcome_message()
        render_quick_tips()
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Handle example question from sidebar
    if example_question:
        process_user_input(example_question)
        st.rerun()
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about fashion... 💬"):
        process_user_input(prompt)

def process_user_input(user_input: str):
    """Process user input and get AI response"""
    
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("✨ Crafting your style advice..."):
            try:
                # Get response from AI service
                response = st.session_state.ai_service.get_fashion_advice(
                    user_input,
                    st.session_state.messages
                )
                
                # Display response
                st.markdown(response)
                
                # Add to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })
                
            except Exception as e:
                error_msg = f"😔 Oops! Something went wrong: {str(e)}\n\nPlease make sure your API key is set correctly in the `.env` file."
                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })