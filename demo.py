import sys
import os

# Add src to path so we can import modules easily
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from dialogue_manager import DialogueManager

def run_demo():
    print("=" * 60)
    print("🤖 NLP CUSTOMER SERVICE AGENT - 10 QUERY DEMO")
    print("=" * 60)
    
    dm = DialogueManager()
    
    sample_queries = [
        "Hello there!",
        "Where is my order ORD-1012?",
        "Can you tell me about Smartwatch?",
        "I want to cancel my subscription",
        "I need a refund for order ORD-1045",
        "Hi, good morning!",
        "Check status of order ORD-1088",
        "What are the features of Wireless Headphones?",
        "Please stop my membership",
        "Can I get a refund please?"
    ]
    
    for i, query in enumerate(sample_queries, 1):
        print(f"\n[Query {i:02d}] User: {query}")
        response = dm.process_query(query)
        print(f"       Agent: {response}")
        
    print("\n" + "=" * 60)
    print("✅ Demo completed successfully! All 10 queries processed.")
    print("=" * 60)

if __name__ == "__main__":
    run_demo()