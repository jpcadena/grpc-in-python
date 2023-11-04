"""
A module for config in the server-service package.
"""
from os import environ
from pathlib import Path
from typing import Union

here: Path = Path(__file__).absolute().parent
port: int = int(environ.get("PORT", 8888))
host: str = environ.get("HOST", "localhost")
cert_file: Union[str, Path] = environ.get('CERT_FILE', here / 'cert.pem')
key_file: Union[str, Path] = environ.get('KEY_FILE', here / 'key.pem')
