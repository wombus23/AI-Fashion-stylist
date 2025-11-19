"""
Reusable UI components for the Fashion Stylist app
"""
import streamlit as st

def render_header():
    """Renders the main header"""
    st.markdown(
        '<div class="main-header">👔 AI Fashion Stylist</div>', 
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="subtitle">Your personal fashion advisor powered by AI</div>', 
        unsafe_allow_html=True
    )

def render_welcome_message():
    """Renders the welcome card with features"""
    st.markdown("""
        <div class="welcome-card">
            <h2 style="color: #667eea; margin-bottom: 1rem;">✨ Welcome to Your AI Stylist!</h2>
            <p style="color: #4a5568; font-size: 1.1rem; margin-bottom: 1.5rem;">
                I'm here to help you look your best. Here's what I can do:
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                <span class="feature-badge">👗 Outfit Recommendations</span>
                <span class="feature-badge">🎨 Color Coordination</span>
                <span class="feature-badge">🗂️ Wardrobe Organization</span>
                <span class="feature-badge">🌸 Seasonal Styling</span>
                <span class="feature-badge">✨ Fashion Trends</span>
                <span class="feature-badge">💡 Style Tips</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Renders the sidebar with info and tips"""
    with st.sidebar:
        st.markdown("### 📖 About")
        st.markdown("""
            AI Fashion Stylist uses advanced AI to provide personalized 
            fashion advice tailored to your needs.
        """)
        
        st.divider()
        
        st.markdown("### 💬 Example Questions")
        
        examples = [
            "What should I wear to a summer wedding?",
            "How do I build a capsule wardrobe?",
            "What colors match with olive green?",
            "Help me organize my closet efficiently",
            "What's trending in fashion this season?",
            "Business casual outfit ideas?"
        ]
        
        for example in examples:
            if st.button(f"💡 {example}", key=example, use_container_width=True):
                return example
        
        st.divider()
        
        st.markdown("### ⚙️ Actions")
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        st.divider()
        
        st.markdown("### 📊 Stats")
        message_count = len([m for m in st.session_state.get("messages", []) if m["role"] == "user"])
        st.metric("Questions Asked", message_count)
        
        st.divider()
        
        st.markdown("""
            <div style="text-align: center; color: #a0aec0; font-size: 0.9rem;">
                Made with ❤️ using Streamlit
            </div>
        """, unsafe_allow_html=True)
    
    return None

def render_quick_tips():
    """Renders quick tips card"""
    with st.expander("💡 Quick Tips - Click to expand", expanded=False):
        st.markdown("""
            **Get the best advice by:**
            - Being specific about the occasion or event
            - Mentioning your style preferences
            - Describing colors or items you already have
            - Asking follow-up questions for clarification
            
            **Try asking about:**
            - Specific occasions (interviews, dates, weddings)
            - Color combinations and matching
            - Seasonal wardrobe updates
            - Body type recommendations
            - Budget-friendly styling
        """)

def render_typing_indicator():
    """Shows a typing indicator"""
    return st.markdown("""
        <div style="padding: 1rem; text-align: center;">
            <span style="color: #667eea; font-weight: 600;">
                ✨ Styling your look...
            </span>
        </div>
    """, unsafe_allow_html=True)