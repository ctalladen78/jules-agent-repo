import streamlit as st
from supabase import create_client, Client, Auth
import os
from dotenv import load_dotenv
from todo import Todo
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Load environment variables (if available, but prioritize sidebar input)
load_dotenv()

MAX_TOKENS = int(os.getenv("MAX_TOKENS", 500))  # Default to 500 if not set

st.set_page_config(page_title="To-Do App", page_icon="✅")

# Sidebar for credentials
st.sidebar.header("Credentials")
supabase_url = st.sidebar.text_input("Supabase URL", type="password")
supabase_key = st.sidebar.text_input("Supabase Key", type="password")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# Initialize Supabase client (only if credentials are provided)
supabase = None
if supabase_url and supabase_key:
    try:
        supabase = create_client(supabase_url, supabase_key)
        todo_manager = Todo(supabase)
    except Exception as e:
        st.error(f"Error connecting to Supabase: {e}")

# Authentication and main app logic
if supabase:
    auth = supabase.auth
    session = auth.session()
    if session:
        user = auth.get_user()
        st.write(f"Welcome, {user['email']}!")

        todos = todo_manager.get_todos()
        if todos:
            st.table(todos)
            for todo in todos:
                if st.button(f"Delete {todo['task']}", key=todo['id']):
                    if todo_manager.delete_todo(todo['id']):
                        st.success(f"Todo '{todo['task']}' deleted successfully!")
                        st.experimental_rerun()
                    else:
                        st.error(f"Error deleting todo '{todo['task']}'.")
        else:
            st.write("No todos found.")

        # Add todo form - Now uses React component for input
        st.components.v1.html(
            """
            <div id="root"></div>
            <script src="/static/build/static/js/main.js"></script>
            """,
            height=150,
        )

        # Handle todo addition from React component
        if st.request.method == 'POST':
            data = st.request.json()
            if data and 'prompt' in data:
                new_todo = data['prompt']
                if openai_api_key:
                    token_count = count_tokens(new_todo, openai_api_key)
                    if token_count == -1:
                        st.error("Error counting tokens. Please check your OpenAI API key.")
                    else:
                        st.session_state['token_count'] = token_count
                        if token_count <= MAX_TOKENS:
                            result = todo_manager.add_todo(new_todo)
                            if result:
                                st.success("Todo added successfully!")
                                st.experimental_rerun()
                            else:
                                st.error("Error adding todo.")
                        else:
                            st.error(f"Todo exceeds token limit ({MAX_TOKENS} tokens). Please shorten your input.")
                else:
                    st.warning("Please enter your OpenAI API key.")

    else:
        st.warning("Please sign in to access your to-do list.")
else:
    st.warning("Please enter your Supabase credentials.")

def count_tokens(text, openai_api_key):
    # Simulate token counting. Replace with your actual implementation using the OpenAI API.
    #  This example uses a simple word count as a proxy for token count.
    try:
        return len(text.split())  # Placeholder
    except Exception as e:
        logging.error(f"Error counting tokens: {e}")
        return -1 # Indicate an error

