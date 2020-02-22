# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: merkledag.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='merkledag.proto',
  package='merkledag.pb',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0fmerkledag.proto\x12\x0cmerkledag.pb\"3\n\x06PBLink\x12\x0c\n\x04Hash\x18\x01 \x01(\x0c\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\r\n\x05Tsize\x18\x03 \x01(\x04\";\n\x06PBNode\x12#\n\x05Links\x18\x02 \x03(\x0b\x32\x14.merkledag.pb.PBLink\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\x0c')
)




_PBLINK = _descriptor.Descriptor(
  name='PBLink',
  full_name='merkledag.pb.PBLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Hash', full_name='merkledag.pb.PBLink.Hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Name', full_name='merkledag.pb.PBLink.Name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Tsize', full_name='merkledag.pb.PBLink.Tsize', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=84,
)


_PBNODE = _descriptor.Descriptor(
  name='PBNode',
  full_name='merkledag.pb.PBNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Links', full_name='merkledag.pb.PBNode.Links', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Data', full_name='merkledag.pb.PBNode.Data', index=1,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=145,
)

_PBNODE.fields_by_name['Links'].message_type = _PBLINK
DESCRIPTOR.message_types_by_name['PBLink'] = _PBLINK
DESCRIPTOR.message_types_by_name['PBNode'] = _PBNODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PBLink = _reflection.GeneratedProtocolMessageType('PBLink', (_message.Message,), dict(
  DESCRIPTOR = _PBLINK,
  __module__ = 'merkledag_pb2'
  # @@protoc_insertion_point(class_scope:merkledag.pb.PBLink)
  ))
_sym_db.RegisterMessage(PBLink)

PBNode = _reflection.GeneratedProtocolMessageType('PBNode', (_message.Message,), dict(
  DESCRIPTOR = _PBNODE,
  __module__ = 'merkledag_pb2'
  # @@protoc_insertion_point(class_scope:merkledag.pb.PBNode)
  ))
_sym_db.RegisterMessage(PBNode)


# @@protoc_insertion_point(module_scope)
