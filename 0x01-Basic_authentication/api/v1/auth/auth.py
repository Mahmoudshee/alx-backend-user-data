#!/usr/bin/env python3i
""" Manage API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ A class to manage API
    authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Require the auth

            Args:
                path: path to authenticate
                excluded_paths: list of excluded path to authenticate

            Return:
                True if is authenticated otherwise false
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] is not '/':
            path += '/'

        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Authorization header """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user """
        return None
