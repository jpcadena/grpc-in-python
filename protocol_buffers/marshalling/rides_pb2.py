# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rides.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0brides.proto\"H\n\x0cStartRequest\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x03\x12\x11\n\tdriver_id\x18\x02 \x01(\t\x12\x15\n\rpassenger_ids\x18\x03 \x03(\tb\x06proto3'
)


_STARTREQUEST = DESCRIPTOR.message_types_by_name['StartRequest']
StartRequest = _reflection.GeneratedProtocolMessageType(
    'StartRequest',
    (_message.Message,),
    {
        'DESCRIPTOR': _STARTREQUEST,
        '__module__': 'rides_pb2'
        # @@protoc_insertion_point(class_scope:StartRequest)
    },
)
_sym_db.RegisterMessage(StartRequest)

if _descriptor._USE_C_DESCRIPTORS is False:
    DESCRIPTOR._options = None
    _STARTREQUEST._serialized_start = 15
    _STARTREQUEST._serialized_end = 87
# @@protoc_insertion_point(module_scope)
