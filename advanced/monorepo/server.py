"""
A module for server in the advanced package.
"""

from concurrent.futures import ThreadPoolExecutor
from typing import Any

import grpc
import rides_pb2 as pb
import rides_pb2_grpc as rpc
from grpc._server import _Server as Server
from grpc_reflection.v1alpha import reflection

from server.service import config, log
from streaming.streaming_server import StreamingRides


def build_server(server_port: int) -> Server:
    """
    Builds a server using a given port
    :param server_port: The port to connect to
    :type server_port: int
    :return: The server instance
    :rtype: Server
    """
    grpc_server: Server = grpc.server(ThreadPoolExecutor())
    rpc.add_RidesServicer_to_server(StreamingRides(), grpc_server)
    names: tuple[Any, Any] = (
        pb.DESCRIPTOR.services_by_name["Rides"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(names, grpc_server)
    address: str = f"[::]:{server_port}"
    grpc_server.add_insecure_port(address)
    return grpc_server


if __name__ == "__main__":
    server: Server = build_server(config.port)
    server.start()
    log.info("server ready on %s", config.port)
    server.wait_for_termination()
