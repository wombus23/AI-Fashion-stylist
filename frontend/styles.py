"""
Custom CSS styles for the AI Fashion Stylist app
"""

def get_custom_css():
    """Returns custom CSS for the app"""
    return """
    <style>
    /* Main container */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
    }
    
    /* Chat container */
    .stChatFloatingInputContainer {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Header styling */
    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        padding-top: 2rem;
    }
    
    .subtitle {
        text-align: center;
        color: #4a5568;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-weight: 500;
    }
    
    /* Chat messages */
    .stChatMessage {
        background-color: white;
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Make sure text is visible in all chat messages */
    .stChatMessage p, .stChatMessage li, .stChatMessage span {
        color: #2d3748 !important;
    }
    
    /* User message specific */
    [data-testid="stChatMessageContent"]:has(+ [data-testid="stChatMessageAvatar"][alt="user"]) {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 1rem;
    }
    
    /* User message text should be white */
    [data-testid="stChatMessageContent"]:has(+ [data-testid="stChatMessageAvatar"][alt="user"]) p,
    [data-testid="stChatMessageContent"]:has(+ [data-testid="stChatMessageAvatar"][alt="user"]) li,
    [data-testid="stChatMessageContent"]:has(+ [data-testid="stChatMessageAvatar"][alt="user"]) span {
        color: white !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f7fafc 0%, #edf2f7 100%);
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #2d3748;
    }
    
    /* Sidebar text visibility */
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] li {
        color: #2d3748 !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Info box styling */
    .stAlert {
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    
    /* Input box */
    .stChatInputContainer > div {
        border-radius: 15px;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Card-like containers */
    .css-1r6slb0 {
        background-color: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Divider */
    hr {
        margin: 2rem 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
    }
    
    /* Welcome card */
    .welcome-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }
    
    /* Feature badges */
    .feature-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-size: 0.9rem;
        font-weight: 600;
    }
    
    /* Emoji styling */
    .emoji {
        font-size: 1.5rem;
        margin-right: 0.5rem;
    }
    </style>
    """

def get_custom_theme():
    """Returns theme configuration for Streamlit"""
    return {
        "primaryColor": "#667eea",
        "backgroundColor": "#f7fafc",
        "secondaryBackgroundColor": "#ffffff",
        "textColor": "#2d3748",
        "font": "sans-serif"
    }