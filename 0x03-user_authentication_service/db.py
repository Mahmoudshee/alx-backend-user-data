#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError, ValueError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.
        :param email: Email of the user.
        :param hashed_password: Hashed password of the user.
        :return: User object.
        """
        # ... (other methods)

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user in the database based on input arguments.
        :param kwargs: Keyword arguments for filtering.
        :return: User object.
        """
        # ... (other methods)

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes in the database.
        :param user_id: ID of the user to update.
        :param kwargs: Keyword arguments for updating user attributes.
        """
        # ... (other methods)


# Run the script to test
if __name__ == '__main__':
    # ... (testing code)
