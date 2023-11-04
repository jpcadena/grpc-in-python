"""
A module for test server in the advanced package.
"""
from datetime import datetime
from socket import socket
from typing import Any, Generator
from unittest.mock import MagicMock

import grpc
import pytest
import rides_pb2 as pb
import rides_pb2_grpc as rpc
from grpc._server import _Server as Server

from advanced.monorepo.server import build_server
from streaming.streaming_server import StreamingRides


def test_start() -> None:
    request = pb.StartRequest(
        car_id=7,
        driver_id='Bond',
        passenger_ids=['M', 'Q'],
        type=pb.POOL,
        location=pb.Location(
            lat=51.4871871,
            lng=-0.1266743,
        ),
    )
    request.time.FromDatetime(
        datetime(2022, 2, 22, 22, 22, 22, 22)
    )
    context: MagicMock = MagicMock()
    rides: StreamingRides = StreamingRides()
    resp = rides.Start(request, context)
    assert resp.id != ''


def free_port() -> int:
    """
    Free port
    :return: The port number
    :rtype: int
    """
    with socket() as sock:
        sock.bind(('localhost', 0))
        _, port = sock.getsockname()
        return int(port)


@pytest.fixture
def conn() -> Generator[tuple[Server, rpc.RidesStub], Any, None]:
    """
    Connection to server
    :return: The server instance and the corresponding rides stub
    :rtype: Generator[tuple[Server, rpc.RidesStub], Any, None]
    """
    port: int = free_port()
    server: Server = build_server(port)
    server.start()
    with grpc.insecure_channel(f'localhost:{port}') as chan:
        rides_stub: rpc.RidesStub = rpc.RidesStub(chan)
        yield server, rides_stub
    server.stop(grace=0.1)


def test_start_server(conn: tuple[Server, rpc.RidesStub]) -> None:
    server, rides_stub = conn
    request = pb.StartRequest(
        car_id=7,
        driver_id='Bond',
        passenger_ids=['M', 'Q'],
        type=pb.POOL,
        location=pb.Location(
            lat=51.4871871,
            lng=-0.1266743,
        ),
    )
    request.time.FromDatetime(datetime(2022, 2, 22, 22, 22, 22, 22))
    response = rides_stub.Start(request)
    assert response.id != ''
