import streamlit as st
from streamlit_supabase import auth, create_client # Added import for create_client
import os
from dotenv import load_dotenv
from todo import Todo

# Load environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 500)) # Default to 500 if not set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # Added for OpenAI API usage


# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
todo_manager = Todo(supabase)

# Placeholder function - Replace with your actual token counting logic using OpenAI API
def count_tokens(text):
    # Simulate token counting. Replace with your actual implementation using the OpenAI API.
    #  This example uses a simple word count as a proxy for token count.
    return len(text.split())


st.set_page_config(page_title="To-Do App", page_icon="✅")

# Authentication
if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("Please set SUPABASE_URL and SUPABASE_KEY environment variables.")
elif not OPENAI_API_KEY:
    st.error("Please set OPENAI_API_KEY environment variable.")
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

        # Add todo form -  Now uses React component for input
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
                token_count = count_tokens(new_todo) # Placeholder - Replace with actual token counting

                if token_count <= MAX_TOKENS:
                    result = todo_manager.add_todo(new_todo)
                    if result:
                        st.success("Todo added successfully!")
                        st.experimental_rerun()
                    else:
                        st.error("Error adding todo.")
                else:
                    st.error(f"Todo exceeds token limit ({MAX_TOKENS} tokens).  Please shorten your input.")

    else:
        st.warning("Please sign in to access your to-do list.")

