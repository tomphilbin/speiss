# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ephemeris.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ephemeris.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\020SpeissApi.Protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x65phemeris.proto\"\x93\x02\n\x16SatellitePassesRequest\x12\x12\n\nstart_date\x18\x01 \x01(\x03\x12\x10\n\x08\x65nd_date\x18\x02 \x01(\x03\x12(\n\x03tle\x18\x03 \x01(\x0b\x32\x1b.SatellitePassesRequest.Tle\x12\x32\n\x08location\x18\x04 \x01(\x0b\x32 .SatellitePassesRequest.Location\x1a\x31\n\x03Tle\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05line1\x18\x02 \x01(\t\x12\r\n\x05line2\x18\x03 \x01(\t\x1a\x42\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x11\n\televation\x18\x03 \x01(\x05\"\xb9\x02\n\x17SatellitePassesResponse\x12;\n\x05items\x18\x01 \x03(\x0b\x32,.SatellitePassesResponse.SatellitePassesItem\x1a\xe0\x01\n\x13SatellitePassesItem\x12\x12\n\nstart_time\x18\x01 \x01(\x03\x12\x17\n\x0fstart_elevation\x18\x02 \x01(\x01\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\x03\x12\x15\n\rend_elevation\x18\x04 \x01(\x01\x12\x11\n\tpeak_time\x18\x05 \x01(\x03\x12\x16\n\x0epeak_elevation\x18\x06 \x01(\x01\x12\x11\n\tmagnitude\x18\x07 \x01(\x01\x12\x1d\n\x15satellite_is_eclipsed\x18\x08 \x01(\x08\x12\x16\n\x0esun_is_visible\x18\t \x01(\x08\x32Y\n\tEphemeris\x12L\n\x15GetAllSatellitePasses\x12\x17.SatellitePassesRequest\x1a\x18.SatellitePassesResponse\"\x00\x42\x13\xaa\x02\x10SpeissApi.Protosb\x06proto3'
)




_SATELLITEPASSESREQUEST_TLE = _descriptor.Descriptor(
  name='Tle',
  full_name='SatellitePassesRequest.Tle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SatellitePassesRequest.Tle.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line1', full_name='SatellitePassesRequest.Tle.line1', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line2', full_name='SatellitePassesRequest.Tle.line2', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=178,
  serialized_end=227,
)

_SATELLITEPASSESREQUEST_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='SatellitePassesRequest.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='SatellitePassesRequest.Location.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='SatellitePassesRequest.Location.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='elevation', full_name='SatellitePassesRequest.Location.elevation', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=295,
)

_SATELLITEPASSESREQUEST = _descriptor.Descriptor(
  name='SatellitePassesRequest',
  full_name='SatellitePassesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_date', full_name='SatellitePassesRequest.start_date', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='SatellitePassesRequest.end_date', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tle', full_name='SatellitePassesRequest.tle', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='SatellitePassesRequest.location', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SATELLITEPASSESREQUEST_TLE, _SATELLITEPASSESREQUEST_LOCATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=295,
)


_SATELLITEPASSESRESPONSE_SATELLITEPASSESITEM = _descriptor.Descriptor(
  name='SatellitePassesItem',
  full_name='SatellitePassesResponse.SatellitePassesItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='SatellitePassesResponse.SatellitePassesItem.start_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_elevation', full_name='SatellitePassesResponse.SatellitePassesItem.start_elevation', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='SatellitePassesResponse.SatellitePassesItem.end_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_elevation', full_name='SatellitePassesResponse.SatellitePassesItem.end_elevation', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peak_time', full_name='SatellitePassesResponse.SatellitePassesItem.peak_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peak_elevation', full_name='SatellitePassesResponse.SatellitePassesItem.peak_elevation', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='magnitude', full_name='SatellitePassesResponse.SatellitePassesItem.magnitude', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='satellite_is_eclipsed', full_name='SatellitePassesResponse.SatellitePassesItem.satellite_is_eclipsed', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sun_is_visible', full_name='SatellitePassesResponse.SatellitePassesItem.sun_is_visible', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=611,
)

_SATELLITEPASSESRESPONSE = _descriptor.Descriptor(
  name='SatellitePassesResponse',
  full_name='SatellitePassesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='SatellitePassesResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SATELLITEPASSESRESPONSE_SATELLITEPASSESITEM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=611,
)

_SATELLITEPASSESREQUEST_TLE.containing_type = _SATELLITEPASSESREQUEST
_SATELLITEPASSESREQUEST_LOCATION.containing_type = _SATELLITEPASSESREQUEST
_SATELLITEPASSESREQUEST.fields_by_name['tle'].message_type = _SATELLITEPASSESREQUEST_TLE
_SATELLITEPASSESREQUEST.fields_by_name['location'].message_type = _SATELLITEPASSESREQUEST_LOCATION
_SATELLITEPASSESRESPONSE_SATELLITEPASSESITEM.containing_type = _SATELLITEPASSESRESPONSE
_SATELLITEPASSESRESPONSE.fields_by_name['items'].message_type = _SATELLITEPASSESRESPONSE_SATELLITEPASSESITEM
DESCRIPTOR.message_types_by_name['SatellitePassesRequest'] = _SATELLITEPASSESREQUEST
DESCRIPTOR.message_types_by_name['SatellitePassesResponse'] = _SATELLITEPASSESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SatellitePassesRequest = _reflection.GeneratedProtocolMessageType('SatellitePassesRequest', (_message.Message,), {

  'Tle' : _reflection.GeneratedProtocolMessageType('Tle', (_message.Message,), {
    'DESCRIPTOR' : _SATELLITEPASSESREQUEST_TLE,
    '__module__' : 'ephemeris_pb2'
    # @@protoc_insertion_point(class_scope:SatellitePassesRequest.Tle)
    })
  ,

  'Location' : _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
    'DESCRIPTOR' : _SATELLITEPASSESREQUEST_LOCATION,
    '__module__' : 'ephemeris_pb2'
    # @@protoc_insertion_point(class_scope:SatellitePassesRequest.Location)
    })
  ,
  'DESCRIPTOR' : _SATELLITEPASSESREQUEST,
  '__module__' : 'ephemeris_pb2'
  # @@protoc_insertion_point(class_scope:SatellitePassesRequest)
  })
_sym_db.RegisterMessage(SatellitePassesRequest)
_sym_db.RegisterMessage(SatellitePassesRequest.Tle)
_sym_db.RegisterMessage(SatellitePassesRequest.Location)

SatellitePassesResponse = _reflection.GeneratedProtocolMessageType('SatellitePassesResponse', (_message.Message,), {

  'SatellitePassesItem' : _reflection.GeneratedProtocolMessageType('SatellitePassesItem', (_message.Message,), {
    'DESCRIPTOR' : _SATELLITEPASSESRESPONSE_SATELLITEPASSESITEM,
    '__module__' : 'ephemeris_pb2'
    # @@protoc_insertion_point(class_scope:SatellitePassesResponse.SatellitePassesItem)
    })
  ,
  'DESCRIPTOR' : _SATELLITEPASSESRESPONSE,
  '__module__' : 'ephemeris_pb2'
  # @@protoc_insertion_point(class_scope:SatellitePassesResponse)
  })
_sym_db.RegisterMessage(SatellitePassesResponse)
_sym_db.RegisterMessage(SatellitePassesResponse.SatellitePassesItem)


DESCRIPTOR._options = None

_EPHEMERIS = _descriptor.ServiceDescriptor(
  name='Ephemeris',
  full_name='Ephemeris',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=613,
  serialized_end=702,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllSatellitePasses',
    full_name='Ephemeris.GetAllSatellitePasses',
    index=0,
    containing_service=None,
    input_type=_SATELLITEPASSESREQUEST,
    output_type=_SATELLITEPASSESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EPHEMERIS)

DESCRIPTOR.services_by_name['Ephemeris'] = _EPHEMERIS

# @@protoc_insertion_point(module_scope)
