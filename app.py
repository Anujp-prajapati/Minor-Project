import streamlit as st

# Check if 'chat_session' is not in st.session_state
if 'chat_session' not in st.session_state:
    # Initialize 'chat_session' with an empty dictionary
    st.session_state['chat_session'] = {}

# Now you can use st.session_state['chat_session'] in your code
