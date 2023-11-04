"""
A module for streaming server in the streaming package.
"""
from concurrent.futures import ThreadPoolExecutor
from typing import Any

import grpc
import rides_pb2 as pb
import rides_pb2_grpc as rpc
from grpc._server import _Server as Server
from grpc_reflection.v1alpha import reflection

from server.service import config, log
from server.service.server import Rides


class StreamingRides(Rides):

    def Track(self, request_iterator: Any, context: Any) -> Any:
        count: int = 0
        for request in request_iterator:
            # TODO: Store in database
            log.info('track: %s', request)
            count += 1
        return pb.TrackResponse(count=count)


if __name__ == '__main__':
    server: Server = grpc.server(ThreadPoolExecutor())
    rpc.add_RidesServicer_to_server(StreamingRides(), server)
    names: tuple[Any, Any] = (
        pb.DESCRIPTOR.services_by_name['Rides'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(names, server)
    address: str = f'[::]:{config.port}'
    server.add_insecure_port(address)
    server.start()
    log.info('server ready on %s', address)
    server.wait_for_termination()
