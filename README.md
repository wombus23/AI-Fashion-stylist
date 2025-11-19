# 👔 AI Fashion Stylist
 
 A simple AI-powered fashion advisor chatbot built with Streamlit and Groq API. Get personalized fashion advice, outfit recommendations, and wardrobe organization tips.

**Your Personal AI-Powered Fashion Advisor**

[Features](#features) • [Demo](#demo) • [Installation](#installation) • [Usage](#usage) • [Contributing](#contributing)

---

## 📸 Screenshots

### Main Chat Interface
![Main Interface](./Images/Main.png)
*Beautiful gradient UI with real-time fashion advice*

### Example Conversation
![Example Chat](./Images/Chat.png)
*Get personalized outfit recommendations*

---

## ✨ Features

🎨 **Modern UI Design**
- Beautiful gradient interface with purple theme
- Smooth animations and transitions
- Responsive design for all screen sizes

💬 **Intelligent Fashion Advice**
- Powered by Groq's Llama 3.3 70B model
- Context-aware conversations
- Personalized outfit recommendations

🗂️ **Smart Organization**
- Wardrobe organization tips
- Capsule wardrobe building
- Seasonal styling suggestions

🎯 **Quick Actions**
- Pre-made example questions
- Chat history management
- One-click conversation starters

🌈 **Comprehensive Styling**
- Color coordination advice
- Body type recommendations
- Occasion-specific outfit ideas
- Budget-friendly fashion tips

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key ([Get one free here](https://console.groq.com/keys))
- Git (optional, for cloning)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/ai-fashion-stylist.git
cd ai-fashion-stylist
```

2. **Create virtual environment**
```bash
python -m venv venv

# Activate it:
# Mac/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your Groq API key
# GROQ_API_KEY=your_actual_groq_api_key_here
```

5. **Run the application**
```bash
streamlit run app.py
```

6. **Open your browser**
Navigate to `http://localhost:8501`

---

## 📁 Project Structure

```
ai-fashion-stylist/
│
├── app.py                      # Main entry point
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore file
├── README.md                  # This file
│
├── backend/
│   ├── __init__.py
│   └── ai_service.py          # Groq API integration
│
└── frontend/
    ├── __init__.py
    ├── styles.py              # Custom CSS styling
    ├── components.py          # Reusable UI components
    └── pages/
        ├── __init__.py
        └── chat.py            # Main chat interface
```

---

## 🎯 Usage

### Basic Conversation

Simply type your fashion question in the chat box:

```
"What should I wear to a summer wedding?"
"Help me organize my closet"
"What colors go well with navy blue?"
```

### Example Questions

Click any of the example questions in the sidebar to get started quickly:

- 💡 What should I wear to a summer wedding?
- 💡 How do I build a capsule wardrobe?
- 💡 What colors match with olive green?
- 💡 Help me organize my closet efficiently
- 💡 What's trending in fashion this season?
- 💡 Business casual outfit ideas?

### Clear Chat History

Use the "🗑️ Clear Chat History" button in the sidebar to start a fresh conversation.

---

## 🛠️ Configuration

### Change AI Model

Edit `backend/ai_service.py` line 14:

```python
self.model = "llama-3.3-70b-versatile"  # Current model
```

**Available Groq models:**
- `llama-3.3-70b-versatile` - Best balance (recommended)
- `llama-3.1-70b-versatile` - Good alternative
- `mixtral-8x7b-32768` - Excellent for long context
- `gemma2-9b-it` - Faster, lighter model

### Customize Styling

Edit `frontend/styles.py` to change colors, fonts, and layout:

```python
# Change gradient colors
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Getting Started

1. **Fork the repository**
2. **Create a feature branch**
```bash
git checkout -b feature/amazing-feature
```

3. **Make your changes**
4. **Commit your changes**
```bash
git commit -m "feat: add amazing feature"
```

5. **Push to your branch**
```bash
git push origin feature/amazing-feature
```

6. **Open a Pull Request**

### Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "Command not found: streamlit"**
```bash
# Solution: Activate virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
```

**Issue: "No module named 'groq'"**
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

**Issue: API Error 401**
```bash
# Solution: Check your .env file
# Make sure GROQ_API_KEY is set correctly
```

**Issue: White text not visible**
```bash
# Solution: Clear browser cache and refresh
# Or restart the Streamlit app
```


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing fast AI inference
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Llama 3.3](https://ai.meta.com/llama/) by Meta AI for the language model

---

## 📧 Contact

Have questions or suggestions? Feel free to:

- Open an issue
- Submit a pull request
- Contact the maintainer

---

<div align="center">

**Made with ❤️ and AI**

If you found this project helpful, please consider giving it a ⭐!

[⬆ Back to Top](#-ai-fashion-stylist)

</div>
