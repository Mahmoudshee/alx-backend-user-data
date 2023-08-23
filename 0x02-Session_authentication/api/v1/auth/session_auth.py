#!/usr/bin/env python3
""" A module for Session Authentication """

from api.v1.auth.auth import Auth
from uuid import uuid4
from os import getenv


class SessionAuth(Auth):
    """ A class that handles
        session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create session id """
        if user_id is None or type(user_id) is not str:
            return None
        s_id = str(uuid4())
        self.user_id_by_session_id[s_id] = user_id
        return s_id

    def user_id_for_session_id(
                               self,
                               session_id: str = None
                              ) -> str:
        """ return user id """
        if session_id is None or type(session_id) is not str:
            return None
        sess_id = self.user_id_by_session_id.get(
                                              session_id,
                                              None)
        return sess_id

    def current_user(self, request=None):
        """ Return User based on
            cookie value
        """
        cookie = self.session_cookie(request)
        if cookie:
            from models.user import User
            user_id = self.user_id_for_session_id(cookie)
            user = User.get(user_id)
            return user
        return None
