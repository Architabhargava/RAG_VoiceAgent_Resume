import asyncio
from typing import Dict, Optional

class SessionManager:
    """
    Manages active voice sessions and handles interruptions.
    """
    def __init__(self):
        # Maps session_id to current response task
        self.active_tasks: Dict[str, asyncio.Task] = {}

    def register_task(self, session_id: str, task: asyncio.Task):
        """
        Registers a new task for a session and cancels any existing task.
        """
        if session_id in self.active_tasks:
            self.cancel_task(session_id)

        self.active_tasks[session_id] = task

    def cancel_task(self, session_id: str):
        """
        Cancels the active task for a session.
        """
        task = self.active_tasks.get(session_id)
        if task and not task.done():
            task.cancel()
            print(f"Cancelled active task for session {session_id}")

        if session_id in self.active_tasks:
            del self.active_tasks[session_id]

    def clear_session(self, session_id: str):
        """
        Cleans up session data.
        """
        self.cancel_task(session_id)
