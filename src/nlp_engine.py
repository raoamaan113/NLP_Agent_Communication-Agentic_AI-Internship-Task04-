import re

class NLPEngine:
    def __init__(self):
        # Define keywords/patterns for 5 Intent Types
        self.intent_patterns = {
            "Order_Status": r"(status|where|track|shipped|delivery|check my order)",
            "Cancel_Subscription": r"(cancel|stop|terminate|unsubscribe)\s+(my\s+)?(subscription|membership|service)",
            "Product_Info": r"(tell me about|info|details|what is|features of)\s+(.+)",
            "Refund_Request": r"(refund|money back|return|reimburse)",
            "General_Greeting": r"^(hi|hello|hey|greetings|good morning|good afternoon)\b"
        }

    def recognize_intent(self, query):
        query_lower = query.lower().strip()
        for intent, pattern in self.intent_patterns.items():
            if re.search(pattern, query_lower):
                return intent
        return "Unknown_Intent"

    def extract_entities(self, query):
        entities = {}
        
        # 1. Extract Order ID (e.g., ORD-1005)
        order_match = re.search(r"ORD-\d+", query, re.IGNORECASE)
        if order_match:
            entities["order_id"] = order_match.group(0).upper()
            
        # 2. Extract Product Names based on known inventory
        known_products = [
            "Wireless Headphones", "Smartwatch", "Running Shoes", 
            "Mechanical Keyboard", "Gaming Mouse", "Bluetooth Speaker", "Fitness Tracker"
        ]
        for prod in known_products:
            if prod.lower() in query.lower():
                entities["product_name"] = prod
                break
                
        # 3. Extract Action/Status Keywords (e.g., shipped, refund, cancel)
        if "cancel" in query.lower():
            entities["action"] = "cancel"
        elif "refund" in query.lower():
            entities["action"] = "refund"
        elif "shipped" in query.lower():
            entities["action"] = "shipped"
            
        return entities

if __name__ == "__main__":
    engine = NLPEngine()
    sample_queries = [
        "Where is my order ORD-1005?",
        "I want to cancel my subscription",
        "Can you tell me about Smartwatch?",
        "I need a refund for my purchase."
    ]
    
    for q in sample_queries:
        intent = engine.recognize_intent(q)
        entities = engine.extract_entities(q)
        print(f"Query: '{q}'\n -> Intent: {intent} | Entities: {entities}\n")