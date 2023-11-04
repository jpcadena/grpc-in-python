"""
A module for secure server in the advanced package.
"""
from concurrent.futures import ThreadPoolExecutor
from typing import Any

import grpc
import rides_pb2 as pb
import rides_pb2_grpc as rpc
from grpc._server import _Server as Server
from grpc_reflection.v1alpha import reflection

from advanced.interceptor_server import TimingInterceptor
from server.service import config, log
from streaming.streaming_server import StreamingRides


def load_credentials() -> grpc.ServerCredentials:
    """
    Load the server credentials
    :return: The server credentials
    :rtype: ServerCredentials
    """
    with open(config.cert_file, 'rb') as fp:
        cert: bytes = fp.read()
    with open(config.key_file, 'rb') as fp:
        key: bytes = fp.read()
    return grpc.ssl_server_credentials([(key, cert)])


if __name__ == '__main__':
    server: Server = grpc.server(
        ThreadPoolExecutor(),
        interceptors=[TimingInterceptor()],
    )
    rpc.add_RidesServicer_to_server(StreamingRides(), server)
    names: tuple[Any, Any] = (
        pb.DESCRIPTOR.services_by_name['Rides'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(names, server)
    address: str = f'[::]:{config.port}'
    server_credentials: grpc.ServerCredentials = load_credentials()
    server.add_secure_port(address, server_credentials)
    server.start()
    log.info('server ready on %s', address)
    server.wait_for_termination()
