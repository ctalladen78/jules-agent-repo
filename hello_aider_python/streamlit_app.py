import streamlit as st
import os
from dotenv import load_dotenv
from supabase import Client, create_client
import todo

# Load environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

# Initialize Supabase client.  Error handling is improved.
try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    auth = supabase.auth
    todo_manager = todo.Todo(supabase)
except Exception as e:
    st.error(f"Error initializing Supabase client: {e}")
    st.stop()

st.title("Simple Todo App")

MAX_TOKENS = 500  # Set your desired token limit here

with st.sidebar:
    # ... (Authentication code remains unchanged) ...

    # Display todos (only if signed in)
    session = auth.session()
    if session:
        user = auth.get_user()
        st.write(f"Welcome, {user['email']}!")

        todos = todo_manager.get_todos()
        if todos:
            st.table(todos)
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
                    st.error(f"Todo exceeds token limit ({MAX_TOKENS} tokens).")


        # Delete todo functionality (remains unchanged)
        if todos:
            # ... (Delete todo code remains unchanged) ...
        else:
            st.warning("Please sign in to access your to-do list.")
    else:
        st.warning("Please sign in to access your to-do list.")

# Placeholder for token counting - REPLACE THIS WITH YOUR ACTUAL TOKEN COUNTING LOGIC
def count_tokens(text):
    # This is a placeholder.  Replace with a call to your token counting API or library.
    # For example, you might use a library like tiktoken or a custom API endpoint.
    #  This example just returns a dummy value.
    return len(text.split())

