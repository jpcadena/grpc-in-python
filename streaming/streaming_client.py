"""
A module for client in the streaming package.
"""
from typing import Any, Generator

import rides_pb2 as pb

from client.client import Client, ClientError
from server.service import config
from streaming.event import LocationEvent, rand_events


class StreamingClient(Client):

    def track(self, events: Generator[LocationEvent, Any, None]) -> None:
        """
        Track events for streaming client
        :param events: The events to track
        :type events: LocationEvent iterator
        :return: None
        :rtype: NoneType
        """
        self.stub.Track(  # type: ignore
            track_request(event) for event in events
        )


def track_request(event: LocationEvent) -> Any:
    """
    Track upcoming requests for streaming client event
    :param event: The events to track
    :type event: LocationEvent
    :return: The tracked request
    :rtype: Any
    """
    request = pb.TrackRequest(
        car_id=event.car_id,
        location=pb.Location(lat=event.lat, lng=event.lng),
    )
    request.time.FromDatetime(event.time)
    return request


if __name__ == '__main__':
    address: str = f'{config.host}:{config.port}'
    client: StreamingClient = StreamingClient(address)
    random_events: Generator[LocationEvent, Any, None] = rand_events(7)
    try:
        client.track(random_events)
    except ClientError as err:
        raise SystemExit(f'error: {err}')
