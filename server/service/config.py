"""
A module for config in the server-service package.
"""
from os import environ

port: int = int(environ.get("PORT", 8888))
host: str = environ.get("HOST", "localhost")
