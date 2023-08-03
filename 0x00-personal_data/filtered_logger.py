#!/usr/bin/env python3
"""
Main file
"""

import logging
import mysql.connector
import os
from typing import List
import re
import bcrypt


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    for field in fields:
        pattern = field + '=.*?' + separator
        replacement = field + '=' + redaction + separator
        message = re.sub(pattern, replacement, message)
    return message


class RedactingFormatter(logging.Formatter):
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=("name", "email", "phone", "ssn", "password"))
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    db = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database,
    )
    return db


def main():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()

    for row in cursor:
        user_data = "; ".join([f"{field}={row[idx]}" for idx, field in enumerate(PII_FIELDS)])
        logger.info(user_data)
        print("Filtered fields:")
        for field in PII_FIELDS:
            print(field)
        print()


if __name__ == "__main__":
    main()
