from database import MockOrderDatabase
from nlp_engine import NLPEngine

class DialogueManager:
    def __init__(self):
        self.db = MockOrderDatabase()
        self.nlp = NLPEngine()
        
    def process_query(self, user_query):
        intent = self.nlp.recognize_intent(user_query)
        entities = self.nlp.extract_entities(user_query)
        
        # Handle responses based on recognized intent
        if intent == "Order_Status":
            order_id = entities.get("order_id")
            if not order_id:
                return "I'd be happy to check your order status. Could you please provide your Order ID (e.g., ORD-1001)?"
            
            order_info = self.db.get_order(order_id)
            if order_info:
                return f"Your order {order_id} ({order_info['product_name']}) is currently {order_info['status']}."
            else:
                return f"I couldn't find an order with ID {order_id}. Please check and try again."
                
        elif intent == "Cancel_Subscription":
            return "Your subscription cancellation request has been noted. We're sorry to see you go!"
            
        elif intent == "Product_Info":
            product_name = entities.get("product_name")
            if product_name:
                return f"The {product_name} is one of our top-rated items with high customer satisfaction and a 1-year warranty."
            else:
                return "Which product would you like to know more about? We offer wireless headphones, smartwatches, and more."
                
        elif intent == "Refund_Request":
            order_id = entities.get("order_id")
            if order_id:
                return f"A refund request has been initiated for order {order_id}. Funds will return to your account within 3-5 business days."
            else:
                return "I can help with your refund. Please provide the Order ID associated with your purchase."
                
        elif intent == "General_Greeting":
            return "Hello! Welcome to Customer Support. How can I assist you with your orders or products today?"
            
        else:
            return "I'm sorry, I didn't quite catch that. Could you please rephrase your request or ask about your order status?"

if __name__ == "__main__":
    dm = DialogueManager()
    test_inputs = [
        "Hi there!",
        "Where is my order ORD-1050?",
        "Can you tell me about Mechanical Keyboard?",
        "I want to cancel my subscription",
        "I need a refund for ORD-1025"
    ]
    
    for query in test_inputs:
        print(f"User: {query}")
        print(f"Agent: {dm.process_query(query)}\n")