"""
A module for interceptor server in the advanced package.
"""

from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from typing import Any, Callable

import grpc
import rides_pb2 as pb
import rides_pb2_grpc as rpc
from grpc._server import _Server as Server
from grpc_reflection.v1alpha import reflection

from server.service import config, log
from streaming.streaming_server import StreamingRides


class TimingInterceptor(grpc.ServerInterceptor):  # type: ignore
    def intercept_service(
        self,
        continuation: Callable[..., Any],
        handler_call_details: grpc.HandlerCallDetails,
    ) -> grpc.RpcMethodHandler:
        start: float = perf_counter()
        try:
            return continuation(handler_call_details)
        finally:
            duration: float = perf_counter() - start
            name = handler_call_details.method
            log.info("%s took %.3fsec", name, duration)


if __name__ == "__main__":
    server: Server = grpc.server(
        ThreadPoolExecutor(),
        interceptors=[TimingInterceptor()],
    )
    rpc.add_RidesServicer_to_server(StreamingRides(), server)
    names: tuple[Any, Any] = (
        pb.DESCRIPTOR.services_by_name["Rides"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(names, server)
    address: str = f"[::]:{config.port}"
    server.add_insecure_port(address)
    server.start()
    log.info("server ready on %s", address)
    server.wait_for_termination()
