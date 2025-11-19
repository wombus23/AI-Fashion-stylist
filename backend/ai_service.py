"""
AI Service - Handles Groq API communication
"""
from groq import Groq
import os

class FashionAIService:
    """Service class for AI-powered fashion advice using Groq"""
    
    def __init__(self, api_key: str = None):
        """Initialize the AI service with API key"""
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.3-70b-versatile"  # Fast and powerful Groq model
        
        self.system_prompt = """You are an expert fashion stylist and personal wardrobe consultant with years of experience. 

Your expertise includes:
- Creating outfit recommendations for any occasion
- Wardrobe organization and capsule wardrobe building
- Color theory and coordination
- Understanding body types and what flatters different shapes
- Keeping up with current trends while respecting timeless style
- Budget-friendly fashion advice
- Sustainable and ethical fashion choices

Your communication style:
- Friendly, warm, and encouraging
- Specific and actionable advice
- Ask clarifying questions when needed
- Provide 2-3 options when suggesting outfits
- Consider practicality and the person's lifestyle
- Be inclusive and respectful of all body types, genders, and budgets

Format your responses with:
- Clear, easy-to-read structure
- Bullet points for outfit suggestions
- Emojis to make it visually appealing (but not overuse)
- Practical tips they can implement immediately"""
    
    def get_fashion_advice(self, user_message: str, conversation_history: list) -> str:
        """
        Get fashion advice from the AI
        
        Args:
            user_message: The user's question
            conversation_history: List of previous messages
        
        Returns:
            AI's response as a string
        """
        try:
            # Prepare messages
            messages = [{"role": "system", "content": self.system_prompt}]
            
            # Add conversation history (last 10 messages for context)
            for msg in conversation_history[-10:]:
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
            
            # Call Groq API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=600,
                top_p=0.9
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}\n\nPlease check your Groq API key in the `.env` file and try again."
    
    def get_welcome_suggestions(self) -> list:
        """Returns a list of conversation starters"""
        return [
            "What should I wear to a job interview?",
            "Help me build a capsule wardrobe",
            "What colors go well with navy blue?",
            "Summer outfit ideas for a beach vacation",
            "How to organize my closet efficiently"
        ]