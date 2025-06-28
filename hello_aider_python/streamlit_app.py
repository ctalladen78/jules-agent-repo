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

with st.sidebar:
    st.subheader("Authentication")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        try:
            response = auth.sign_in(email=email, password=password)
            if response and response["user"]: # Check for successful sign-in and user data
                st.success("Successfully signed in!")
                st.experimental_rerun() # Refresh the page
            else:
                st.error("Invalid credentials.")
        except Exception as e:
            st.error(f"Error signing in: {e}")

    if st.button("Sign Up"):
        try:
            response = auth.sign_up(email=email, password=password)
            if response and response["user"]: # Check for successful sign-up and user data
                st.success("Successfully signed up!")
                st.experimental_rerun()
            else:
                st.error("Error signing up.")
        except Exception as e:
            st.error(f"Error signing up: {e}")

    if st.button("Sign Out"):
        try:
            auth.sign_out()
            st.success("Successfully signed out!")
            st.experimental_rerun()
        except Exception as e:
            st.error(f"Error signing out: {e}")


# Display todos (only if signed in)
session = auth.session()
if session:
    user = auth.get_user() # Get user information
    st.write(f"Welcome, {user['email']}!") # Display welcome message

    todos = todo_manager.get_todos()
    if todos:
        st.table(todos)
    else:
        st.write("No todos found.")

    # Add todo form
    new_todo = st.text_input("Add a new todo:")
    if st.button("Add Todo"):
        result = todo_manager.add_todo(new_todo)
        if result:
            st.success("Todo added successfully!")
            st.experimental_rerun()
        else:
            st.error("Error adding todo.")

    # Delete todo functionality
    if todos:
        todo_to_delete = st.selectbox("Select todo to delete:", [str(t["id"]) for t in todos])
        if st.button("Delete Todo"):
            result = todo_manager.delete_todo(int(todo_to_delete))
            if result:
                st.success("Todo deleted successfully!")
                st.experimental_rerun()
            else:
                st.error("Error deleting todo.")
else:
    st.warning("Please sign in to access your to-do list.")

