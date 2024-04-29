"""
A module for validate in the server-service package.
"""

from typing import Any


class Error(ValueError):
    """
    Error raised class based on Value Error
    """

    def __init__(self, field: Any, reason: Any) -> None:
        super().__init__(f"{field}: {reason}")
        self.field: Any = field
        self.reason: Any = reason


def start_request(request: Any) -> None:
    """
    Start a request
    :param request: The request to start
    :type request: Any
    :return: None
    :rtype: NoneType
    """
    if not request.driver_id:
        raise Error("driver_id", "empty")
    # TODO: Validate more fields
