#!/usr/bin/env python3
"""
Session DB Auth
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    Session DB Auth class
    """

    def create_session(self, user_id=None):
        """
        Create a Session ID for a user
        """
        session_id = super().create_session(user_id)
        if session_id:
            user_session = UserSession(user_id=user_id, session_id=session_id)
            user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Return a User ID based on a Session ID
        """
        if session_id:
            user_session = UserSession.search({'session_id': session_id})
            if user_session and self.session_duration <= 0:
                return user_session[0].user_id
            if user_session and 'created_at' in user_session[0]:
                created_at = user_session[0]['created_at']
                if (created_at + timedelta(seconds=self.session_duration) >
                        datetime.now()):
                    return user_session[0].user_id
        return None

    def destroy_session(self, request=None):
        """
        Destroy the user session / log out
        """
        if request:
            session_id = self.session_cookie(request)
            user_session = UserSession.search({'session_id': session_id})
            if user_session:
                user_session[0].remove()
                return True
        return False