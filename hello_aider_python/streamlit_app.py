import streamlit as st
import os
from dotenv import load_dotenv
from supabase import Client, create_client
import todo

# Load environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

# Initialize Supabase client.  Error handling is minimal here for brevity.
try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    todo_manager = todo.Todo(supabase)
except Exception as e:
    st.error(f"Error initializing Supabase client: {e}")
    st.stop()


st.title("Simple Todo App")

# Display todos
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
        st.experimental_rerun() # Refresh the page to show the new todo
    else:
        st.error("Error adding todo.")


# Delete todo functionality (basic example - needs improvement for production)
if todos:
    todo_to_delete = st.selectbox("Select todo to delete:", [str(t["id"]) for t in todos])
    if st.button("Delete Todo"):
        result = todo_manager.delete_todo(int(todo_to_delete))
        if result:
            st.success("Todo deleted successfully!")
            st.experimental_rerun()
        else:
            st.error("Error deleting todo.")

