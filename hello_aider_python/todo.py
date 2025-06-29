from supabase import Client, create_client
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

class Todo:
    def __init__(self, supabase: Client, table_name="todos"):
        self.supabase = supabase
        self.table_name = table_name

    def get_todos(self):
        try:
            response = self.supabase.table(self.table_name).select("*").execute()
            if response.status_code == 200 and response:
                return response.data
            else:
                logging.error(f"Error fetching todos: {response.error}")
                return []
        except Exception as e:
            logging.error(f"Error fetching todos: {e}")
            return []

    def add_todo(self, task):
        if not task:
            logging.error("Error adding todo: Task cannot be empty.")
            return None
        if len(task) > 255:  # Example maximum length; adjust as needed
            logging.error("Error adding todo: Task is too long.")
            return None

        try:
            response = self.supabase.table(self.table_name).insert({"task": task}).execute()
            if response.status_code == 201 and response:
                return response.data[0]
            else:
                logging.error(f"Error adding todo: {response.error}")
                return None
        except Exception as e:
            logging.error(f"Error adding todo: {e}")
            return None

    def delete_todo(self, todo_id):
        if not todo_id:
            logging.error("Error deleting todo: ID cannot be empty.")
            return None
        try:
            #Explicit type checking
            todo_id = int(todo_id)
            response = self.supabase.table(self.table_name).delete().eq("id", todo_id).execute()
            if response.status_code == 200 and response:
                return True
            else:
                logging.error(f"Error deleting todo: {response.error}")
                return False
        except ValueError:
            logging.error("Error deleting todo: Invalid todo ID. Must be an integer.")
            return False
        except Exception as e:
            logging.error(f"Error deleting todo: {e}")
            return False

