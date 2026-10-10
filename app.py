import streamlit as st
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from dialogue_manager import DialogueManager

# Page Configuration
st.set_page_config(
    page_title="AI Agent Support Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Customer Service NLP Agent Dashboard")
st.markdown("### Agentic AI Internship - Task 3")
st.divider()

# Initialize Dialogue Manager in Session State
if "dialogue_manager" not in st.session_state:
    st.session_state.dialogue_manager = DialogueManager()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Welcome to Customer Support. How can I assist you with your orders or products today?"}
    ]

# Layout: 2 Columns (Chat Interface + Database Explorer)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 Interactive Agent Chat")
    
    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User Input Field
    if prompt := st.chat_input("Ask about an order (e.g., 'Where is ORD-1005?')..."):
        # Display User Message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Generate and Display Agent Response
        response = st.session_state.dialogue_manager.process_query(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)

with col2:
    st.subheader("📦 Mock Database Inspector")
    st.caption("Quick sample orders for testing:")
    
    db = st.session_state.dialogue_manager.db
    sample_items = list(db.orders.items())[:10]
    
    for order_id, details in sample_items:
        with st.expander(f"Order: {order_id}"):
            st.write(f"**Product:** {details['product_name']}")
            st.write(f"**Status:** `{details['status']}`")

st.divider()
st.caption("Built with Python, Streamlit, and spaCy / RegEx NLP Engine")