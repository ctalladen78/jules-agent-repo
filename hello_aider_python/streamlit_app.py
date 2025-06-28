import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

st.title("Simple Todo App")

if SUPABASE_URL and SUPABASE_ANON_KEY:
    st.write("Supabase credentials loaded successfully.")
else:
    st.error("Supabase credentials not found. Please set SUPABASE_URL and SUPABASE_ANON_KEY environment variables.")

# Placeholder for todo list display
st.write("Todo list will be displayed here.")

