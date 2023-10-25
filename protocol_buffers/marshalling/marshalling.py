"""
A module for marshalling in the protocol_buffers package.
"""
import rides_pb2 as pb

request = pb.StartRequest(
    car_id=95,
    driver_id='McQueen',
    passenger_ids=['p1', 'p2', 'p3'],
)
print(request)

# region Marshal
data: bytes = request.SerializeToString()
print(data)
print('type:', type(data))
print('size:', len(data))
# endregion

# region Unmarshal
request2 = pb.StartRequest()
request2.ParseFromString(data)
print(request2)
