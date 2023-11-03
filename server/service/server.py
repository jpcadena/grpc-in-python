"""
A module for server in the server-service package.
"""
from concurrent.futures import ThreadPoolExecutor
from typing import Any
from uuid import uuid4

import grpc
import log
import rides_pb2 as pb
import rides_pb2_grpc as rpc
import validate
from grpc._server import _Server as Server
from grpc_reflection.v1alpha import reflection

from server.service import config


def new_ride_id() -> str:
    """
    Generates an unique identifier
    :return: The unique identifier from hex UUID
    :rtype: str
    """
    return uuid4().hex


class Rides(rpc.RidesServicer):  # type: ignore
    def Start(self, request: Any, context: Any) -> Any:
        log.info('ride: %r', request)
        try:
            validate.start_request(request)
        except validate.Error as err:
            log.error('bad request: %s', err)
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(f'{err.field} is {err.reason}')
            raise err
        ride_id: str = new_ride_id()
        return pb.StartResponse(id=ride_id)


if __name__ == '__main__':
    server: Server = grpc.server(ThreadPoolExecutor())
    rpc.add_RidesServicer_to_server(Rides(), server)
    service_names: tuple[Any, Any] = (
        pb.DESCRIPTOR.services_by_name['Rides'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_names, server)
    address: str = f'[::]:{config.port}'
    server.add_insecure_port(address)
    server.start()
    log.info('server ready on %s', address)
    server.wait_for_termination()
