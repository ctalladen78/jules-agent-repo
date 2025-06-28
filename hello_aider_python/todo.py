from supabase import Client, create_client

class Todo:
    def __init__(self, supabase: Client):
        self.supabase = supabase
        self.table_name = "todos"  # Replace with your actual table name

    def get_todos(self):
        try:
            response = self.supabase.table(self.table_name).select("*").execute()
            if response.
                return response.data
            else:
                return []
        except Exception as e:
            print(f"Error fetching todos: {e}")
            return []

    def add_todo(self, task):
        try:
            response = self.supabase.table(self.table_name).insert({"task": task}).execute()
            return response.data
        except Exception as e:
            print(f"Error adding todo: {e}")
            return None

    def delete_todo(self, id):
        try:
            response = self.supabase.table(self.table_name).delete().eq("id", id).execute()
            return response.data
        except Exception as e:
            print(f"Error deleting todo: {e}")
            return None

