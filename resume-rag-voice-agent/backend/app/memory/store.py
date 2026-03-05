from typing import List, Dict
from backend.app.utils.supabase_client import get_supabase_client

class SupabaseChatMemory:
    """
    Handles storing and retrieving chat history from Supabase.
    """
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.supabase = get_supabase_client()
        self.table_name = "chat_history"

    def add_message(self, role: str, message: str):
        """
        Adds a message to the chat history.
        """
        data = {
            "session_id": self.session_id,
            "role": role,
            "message": message
        }
        self.supabase.table(self.table_name).insert(data).execute()

    def get_messages(self) -> List[Dict[str, str]]:
        """
        Retrieves the chat history for the current session.
        """
        response = self.supabase.table(self.table_name) \
            .select("role", "message") \
            .eq("session_id", self.session_id) \
            .order("id", desc=False) \
            .execute()

        return response.data

    def clear_history(self):
        """
        Clears history for the current session.
        """
        self.supabase.table(self.table_name) \
            .delete() \
            .eq("session_id", self.session_id) \
            .execute()
