🤖 NLP-Driven Customer Service Agent (Task 3)
📌 Project Overview
Developed as part of the Agentic AI Internship, this project implements an end-to-end Natural Language Processing (NLP) dialogue system designed to automate customer service interactions. The system accurately interprets unstructured user instructions, classifies core intents, extracts critical entities, queries a mock customer database, and delivers dynamic, contextual responses through both a CLI demo and an interactive web dashboard.

🚀 Key Features & Capabilities
Intent Recognition (5 Core Intents):

Order_Status: Tracks shipment and delivery states.

Cancel_Subscription: Handles membership and subscription cancellations.

Product_Info: Provides details and specifications on inventory items.

Refund_Request: Processes order return and refund inquiries.

General_Greeting: Manages conversational onboarding and greetings.

Entity Extraction (3 Entity Types): Automatically isolates order_id formats (e.g., ORD-XXXX), specific product_name inventory items, and actionable keywords.

Mock Order Database: Manages 100 dynamically generated customer records with randomized order statuses (shipped, pending, delivered, processing, cancelled) and products.

Interactive Streamlit Dashboard (app.py): Provides a modern web-based chat interface alongside a real-time Mock Database Inspector for easy testing and evaluation.

🛠️ Project Structure
Plaintext
NLP_Agent_Communication/
│
├── src/
│   ├── database.py         # Mock order database generator (100 orders)
│   ├── nlp_engine.py       # Intent classification & entity extraction engine
│   └── dialogue_manager.py # Response generation & business logic handler
│
├── docs/
│   └── report.md           # Comprehensive 4-page technical documentation
│
├── artifacts/              # Stored visual assets & test logs
├── data/                   # Dataset query variations
├── app.py                  # Interactive Streamlit Web Dashboard
├── demo.py                 # CLI demonstration script (10 test queries)
└── requirements.txt        # Project dependencies
👤 Author
Rao Muhammad Amaan

Agentic AI Internship Program
