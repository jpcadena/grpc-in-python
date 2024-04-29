"""
A module for json encoding in the protocol_buffers.json encoding package.
"""

from datetime import datetime

import rides_pb2 as pb
from google.protobuf.json_format import MessageToJson

request = pb.StartRequest(
    car_id=95,
    driver_id="McQueen",
    passenger_ids=["p1", "p2", "p3"],
    type=pb.POOL,
    location=pb.Location(
        lat=32.5270941,
        lng=34.9404309,
    ),
)

time: datetime = datetime(2022, 2, 13, 14, 39, 42)
request.time.FromDatetime(time)

# region json
data: str = MessageToJson(request)
print(data, type(data))

# region size
print("encode size")
print("- json    :", len(data))
print("- protobuf:", len(request.SerializeToString()))
