#!/usr/bin/env python3
"""
SessionAuth module
"""

from api.v1.auth.auth import Auth
import uuid  # Import the uuid module


class SessionAuth(Auth):
    """
    SessionAuth class
    """

    user_id_by_session_id = {}  # Class attributes for session_id

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id
        """
        if not user_id or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id  # Store session_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID
        """
        if not session_id or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id, None)

    def destroy_session(self, request=None) -> bool:
        """
        Deletes the user session / logs out
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        if not self.user_id_by_session_id.get(session_id):
            return False

        del self.user_id_by_session_id[session_id]
        return True
