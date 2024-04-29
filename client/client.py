"""
A module for client in the client package.
"""

from datetime import datetime
from enum import StrEnum
from typing import Any

import grpc
import rides_pb2 as pb
import rides_pb2_grpc as rpc

from server.service import config, log
from server.service.rides_pb2_grpc import RidesStub


class ClientError(Exception):
    """
    Client error exception class
    """

    pass


class Client:
    """
    Client interface
    """

    def __init__(self, address: str):
        self.chan: grpc.Channel = grpc.insecure_channel(address)
        self.stub: RidesStub = rpc.RidesStub(self.chan)
        log.info("connected to %s", address)

    def close(self) -> None:
        """
        Close the connection to the server
        :return: None
        :rtype: NoneType
        """
        self.chan.close()

    def ride_start(
        self,
        car_id: int,
        driver_id: str,
        passenger_ids: list[str],
        _type: StrEnum,
        lat: float,
        lng: float,
        time: datetime,
    ) -> Any:
        """
        Starts a new ride instance in the client
        :param car_id: The unique identifier for the car
        :type car_id: int
        :param driver_id: The unique identifier for the driver
        :type driver_id: str
        :param passenger_ids: The unique identifier for the passengers
        :type passenger_ids: list[str]
        :param _type: The type of driver
        :type _type: StrEnum
        :param lat: The lat coordinate
        :type lat: float
        :param lng: The lng coordinate
        :type lng: float
        :param time: The time coordinate
        :type time: datetime
        :return: The id of the response
        :rtype: Any
        """
        request = pb.StartRequest(
            car_id=car_id,
            driver_id=driver_id,
            passenger_ids=passenger_ids,
            type=pb.POOL if _type == "POOL" else pb.REGULAR,
            location=pb.Location(lat=lat, lng=lng),
        )
        request.time.FromDatetime(time)
        log.info("ride started: %s", request)
        try:
            response = self.stub.Start(request, timeout=3)
        except grpc.RpcError as err:
            log.error("start: %s (%s)", err, err.__class__.__mro__)
            raise ClientError(f"{err.code()}: {err.details()}") from err
        return response.id


if __name__ == "__main__":
    addr: str = f"{config.host}:{config.port}"
    client: Client = Client(addr)
    try:
        ride_id = client.ride_start(
            car_id=7,
            driver_id="Bond",
            passenger_ids=["M", "Q"],
            _type="POOL",  # type: ignore
            lat=51.4871871,
            lng=-0.1266743,
            time=datetime(2021, 9, 30, 20, 15),
        )
        log.info("ride ID: %s", ride_id)
    except ClientError as exc:
        raise SystemExit(f"error: {exc}") from exc
