#!/usr/bin/env python3
"""
Session Exp Auth
"""

from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    Session Exp Auth class
    """

    def __init__(self):
        """
        Constructor
        """
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except (ValueError, TypeError):
            self.session_duration = 0
