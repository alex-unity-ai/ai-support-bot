"""
AI Customer Support Bot
Simple NLP-based ticket categorization system
"""

import json
import re

class AISupportBot:
    def __init__(self):
        self.patterns = {
            'login': r'(login|sign in|password|access)',
            'payment': r'(payment|invoice|bill|charge|price)',
            'refund': r'(refund|return|cancel|money back)',
            'technical': r'(bug|error|crash|not working|issue)'
        }
        
        self.responses = {
            'login': "Please reset your password via 'Forgot Password' or contact support@example.com",
            'payment': "Payment issues are escalated to our billing team. Expected response: 24 hours.",
            'refund': "Refund requests are processed within 5-7 business days. Case ID:",
            'technical': "Our technical team will contact you. Please share error screenshots.",
            'default': "Thank you for your message. A human agent will respond shortly."
        }
    
    def categorize_ticket(self, user_message):
        """Categorize user message using regex patterns"""
        user_message = user_message.lower()
        
        for category, pattern in self.patterns.items():
            if re.search(pattern, user_message):
                return category
        return 'default'
    
    def generate_response(self, user_message):
        """Generate AI response based on category"""
        category = self.categorize_ticket(user_message)
        response = self.responses.get(category, self.responses['default'])
        
        if category == 'refund':
            import random
            response += f" REF-{random.randint(1000,9999)}"
        
        return {
            'category': category,
            'response': response,
            'confidence': 'high' if category != 'default' else 'medium'
        }

# Demo function
def demo():
    bot = AISupportBot()
    
    test_messages = [
        "I can't login to my account",
        "My payment was charged twice",
        "I want a refund for my purchase",
        "The app keeps crashing"
    ]
    
    print("🤖 AI Support Bot Demo\n" + "="*30)
    for msg in test_messages:
        result = bot.generate_response(msg)
        print(f"User: {msg}")
        print(f"Category: {result['category']}")
        print(f"Response: {result['response']}")
        print("-" * 30)

if __name__ == "__main__":
    demo()
