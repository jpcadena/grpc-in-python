# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rides.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0brides.proto\"$\n\x08Location\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lng\x18\x02 \x01(\x01\"~\n\x0cStartRequest\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x03\x12\x11\n\tdriver_id\x18\x02 \x01(\t\x12\x15\n\rpassenger_ids\x18\x03 \x03(\t\x12\x17\n\x04type\x18\x04 \x01(\x0e\x32\t.RideType\x12\x1b\n\x08location\x18\x05 \x01(\x0b\x32\t.Location*!\n\x08RideType\x12\x0b\n\x07REGULAR\x10\x00\x12\x08\n\x04POOL\x10\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rides_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_RIDETYPE']._serialized_start = 181
    _globals['_RIDETYPE']._serialized_end = 214
    _globals['_LOCATION']._serialized_start = 15
    _globals['_LOCATION']._serialized_end = 51
    _globals['_STARTREQUEST']._serialized_start = 53
    _globals['_STARTREQUEST']._serialized_end = 179
# @@protoc_insertion_point(module_scope)
