from supabase import Client, create_client
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR) # Set logging level to ERROR to suppress INFO messages

class Todo:
    def __init__(self, supabase: Client, table_name="todos"): # Make table_name configurable
        self.supabase = supabase
        self.table_name = table_name

    def get_todos(self):
        try:
            response = self.supabase.table(self.table_name).select("*").execute()
            if response.
                return response.data
            else:
                return []
        except Exception as e:
            logging.error(f"Error fetching todos: {e}")
            return []

    def add_todo(self, task):
        if not task: #Check for empty task
            logging.error("Error adding todo: Task cannot be empty.")
            return None

        try:
            response = self.supabase.table(self.table_name).insert({"task": task}).execute()
            if response.
                return response.data[0] # Return the inserted todo item
            else:
                logging.error(f"Error adding todo: {response.error}")
                return None
        except Exception as e:
            logging.error(f"Error adding todo: {e}")
            return None

    def delete_todo(self, todo_id):
        if not todo_id: #Check for missing ID
            logging.error("Error deleting todo: ID cannot be empty.")
            return None

        try:
            response = self.supabase.table(self.table_name).delete().eq("id", todo_id).execute()
            if response.
                return True # Indicate successful deletion
            else:
                logging.error(f"Error deleting todo: {response.error}")
                return False
        except Exception as e:
            logging.error(f"Error deleting todo: {e}")
            return False

