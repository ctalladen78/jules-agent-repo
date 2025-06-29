import streamlit as st
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from todo import Todo
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Load environment variables (only for Supabase)
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 500))  # Default to 500 if not set


# Initialize connection.
# conn = st.connection("supabase",type=SupabaseConnection)

# Initialize Supabase client
@st.cache_resource
def init_connection():
    return create_client(SUPABASE_URL, SUPABASE_KEY)
    

supabase = init_connection()
todo_manager = Todo(supabase)

# Placeholder function - Replace with your actual token counting logic using OpenAI API
def count_tokens(text, openai_api_key):
    # Simulate token counting. Replace with your actual implementation using the OpenAI API.
    #  This example uses a simple word count as a proxy for token count.
    try:
        # Your actual OpenAI API token counting logic here using openai_api_key
        # Example (replace with your actual implementation):
        # import openai
        # openai.api_key = openai_api_key
        # response = openai.Completion.create(...)
        # token_count = response['usage']['prompt_tokens']
        # return token_count
        return len(text.split())  # Placeholder
    except Exception as e:
        logging.error(f"Error counting tokens: {e}")
        return -1 # Indicate an error


st.set_page_config(page_title="To-Do App", page_icon="✅")

# Authentication
if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("Please set SUPABASE_URL and SUPABASE_KEY environment variables.")
else:
    # Authentication
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

        # OpenAI API key input in sidebar
        openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

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

