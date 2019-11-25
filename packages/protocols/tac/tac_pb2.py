# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tac.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tac.proto',
  package='fetch.oef.pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ttac.proto\x12\x0c\x66\x65tch.oef.pb\x1a\x1cgoogle/protobuf/struct.proto\"+\n\nStrIntPair\x12\r\n\x05\x66irst\x18\x01 \x01(\t\x12\x0e\n\x06second\x18\x02 \x01(\x05\"-\n\x0cStrFloatPair\x12\r\n\x05\x66irst\x18\x01 \x01(\t\x12\x0e\n\x06second\x18\x02 \x01(\x01\"+\n\nStrStrPair\x12\r\n\x05\x66irst\x18\x01 \x01(\t\x12\x0e\n\x06second\x18\x02 \x01(\t\"\x93\t\n\rTACController\x1a\x0c\n\nRegistered\x1a\x0e\n\x0cUnregistered\x1a\x0b\n\tCancelled\x1a\x88\x03\n\x08GameData\x12\x34\n\x12\x61mount_by_currency\x18\x01 \x03(\x0b\x32\x18.fetch.oef.pb.StrIntPair\x12?\n\x1b\x65xchange_params_by_currency\x18\x02 \x03(\x0b\x32\x1a.fetch.oef.pb.StrFloatPair\x12\x38\n\x16quantities_by_good_pbk\x18\x03 \x03(\x0b\x32\x18.fetch.oef.pb.StrIntPair\x12>\n\x1autility_params_by_good_pbk\x18\x04 \x03(\x0b\x32\x1a.fetch.oef.pb.StrFloatPair\x12\x0e\n\x06tx_fee\x18\x05 \x01(\x03\x12\x33\n\x11\x61gent_pbk_to_name\x18\x06 \x03(\x0b\x32\x18.fetch.oef.pb.StrStrPair\x12\x32\n\x10good_pbk_to_name\x18\x07 \x03(\x0b\x32\x18.fetch.oef.pb.StrStrPair\x12\x12\n\nversion_id\x18\x08 \x01(\t\x1a\xa1\x01\n\x17TransactionConfirmation\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x34\n\x12\x61mount_by_currency\x18\x02 \x03(\x0b\x32\x18.fetch.oef.pb.StrIntPair\x12\x38\n\x16quantities_by_good_pbk\x18\x03 \x03(\x0b\x32\x18.fetch.oef.pb.StrIntPair\x1aw\n\x0bStateUpdate\x12\x37\n\tgame_data\x18\x01 \x01(\x0b\x32$.fetch.oef.pb.TACController.GameData\x12/\n\x03txs\x18\x02 \x03(\x0b\x32\".fetch.oef.pb.TACAgent.Transaction\x1a\xae\x03\n\x05\x45rror\x12?\n\nerror_code\x18\x01 \x01(\x0e\x32+.fetch.oef.pb.TACController.Error.ErrorCode\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xa6\x02\n\tErrorCode\x12\x11\n\rGENERIC_ERROR\x10\x00\x12\x15\n\x11REQUEST_NOT_VALID\x10\x01\x12 \n\x1c\x41GENT_PBK_ALREADY_REGISTERED\x10\x02\x12!\n\x1d\x41GENT_NAME_ALREADY_REGISTERED\x10\x03\x12\x18\n\x14\x41GENT_NOT_REGISTERED\x10\x04\x12\x19\n\x15TRANSACTION_NOT_VALID\x10\x05\x12\x1c\n\x18TRANSACTION_NOT_MATCHING\x10\x06\x12\x1f\n\x1b\x41GENT_NAME_NOT_IN_WHITELIST\x10\x07\x12\x1b\n\x17\x43OMPETITION_NOT_RUNNING\x10\x08\x12\x19\n\x15\x44IALOGUE_INCONSISTENT\x10\t\"\xac\x02\n\x08TACAgent\x1a\x1e\n\x08Register\x12\x12\n\nagent_name\x18\x01 \x01(\t\x1a\x0c\n\nUnregister\x1a\xdf\x01\n\x0bTransaction\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x14\n\x0c\x63ounterparty\x18\x02 \x01(\t\x12\x34\n\x12\x61mount_by_currency\x18\x03 \x03(\x0b\x32\x18.fetch.oef.pb.StrIntPair\x12\x15\n\rsender_tx_fee\x18\x04 \x01(\x03\x12\x1b\n\x13\x63ounterparty_tx_fee\x18\x05 \x01(\x03\x12\x38\n\x16quantities_by_good_pbk\x18\x06 \x03(\x0b\x32\x18.fetch.oef.pb.StrIntPair\x1a\x10\n\x0eGetStateUpdate\"\xc8\x05\n\nTACMessage\x12\x33\n\x08register\x18\x01 \x01(\x0b\x32\x1f.fetch.oef.pb.TACAgent.RegisterH\x00\x12\x37\n\nunregister\x18\x02 \x01(\x0b\x32!.fetch.oef.pb.TACAgent.UnregisterH\x00\x12\x39\n\x0btransaction\x18\x03 \x01(\x0b\x32\".fetch.oef.pb.TACAgent.TransactionH\x00\x12\x41\n\x10get_state_update\x18\x04 \x01(\x0b\x32%.fetch.oef.pb.TACAgent.GetStateUpdateH\x00\x12<\n\nregistered\x18\x05 \x01(\x0b\x32&.fetch.oef.pb.TACController.RegisteredH\x00\x12@\n\x0cunregistered\x18\x06 \x01(\x0b\x32(.fetch.oef.pb.TACController.UnregisteredH\x00\x12:\n\tcancelled\x18\x07 \x01(\x0b\x32%.fetch.oef.pb.TACController.CancelledH\x00\x12\x39\n\tgame_data\x18\x08 \x01(\x0b\x32$.fetch.oef.pb.TACController.GameDataH\x00\x12W\n\x18transaction_confirmation\x18\t \x01(\x0b\x32\x33.fetch.oef.pb.TACController.TransactionConfirmationH\x00\x12?\n\x0cstate_update\x18\n \x01(\x0b\x32\'.fetch.oef.pb.TACController.StateUpdateH\x00\x12\x32\n\x05\x65rror\x18\x0b \x01(\x0b\x32!.fetch.oef.pb.TACController.ErrorH\x00\x42\t\n\x07\x63ontentb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])



_TACCONTROLLER_ERROR_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='fetch.oef.pb.TACController.Error.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GENERIC_ERROR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_NOT_VALID', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGENT_PBK_ALREADY_REGISTERED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGENT_NAME_ALREADY_REGISTERED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGENT_NOT_REGISTERED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSACTION_NOT_VALID', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSACTION_NOT_MATCHING', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGENT_NAME_NOT_IN_WHITELIST', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPETITION_NOT_RUNNING', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIALOGUE_INCONSISTENT', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1072,
  serialized_end=1366,
)
_sym_db.RegisterEnumDescriptor(_TACCONTROLLER_ERROR_ERRORCODE)


_STRINTPAIR = _descriptor.Descriptor(
  name='StrIntPair',
  full_name='fetch.oef.pb.StrIntPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='fetch.oef.pb.StrIntPair.first', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second', full_name='fetch.oef.pb.StrIntPair.second', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=100,
)


_STRFLOATPAIR = _descriptor.Descriptor(
  name='StrFloatPair',
  full_name='fetch.oef.pb.StrFloatPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='fetch.oef.pb.StrFloatPair.first', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second', full_name='fetch.oef.pb.StrFloatPair.second', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=147,
)


_STRSTRPAIR = _descriptor.Descriptor(
  name='StrStrPair',
  full_name='fetch.oef.pb.StrStrPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='fetch.oef.pb.StrStrPair.first', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second', full_name='fetch.oef.pb.StrStrPair.second', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=192,
)


_TACCONTROLLER_REGISTERED = _descriptor.Descriptor(
  name='Registered',
  full_name='fetch.oef.pb.TACController.Registered',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=212,
  serialized_end=224,
)

_TACCONTROLLER_UNREGISTERED = _descriptor.Descriptor(
  name='Unregistered',
  full_name='fetch.oef.pb.TACController.Unregistered',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=226,
  serialized_end=240,
)

_TACCONTROLLER_CANCELLED = _descriptor.Descriptor(
  name='Cancelled',
  full_name='fetch.oef.pb.TACController.Cancelled',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=242,
  serialized_end=253,
)

_TACCONTROLLER_GAMEDATA = _descriptor.Descriptor(
  name='GameData',
  full_name='fetch.oef.pb.TACController.GameData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount_by_currency', full_name='fetch.oef.pb.TACController.GameData.amount_by_currency', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange_params_by_currency', full_name='fetch.oef.pb.TACController.GameData.exchange_params_by_currency', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantities_by_good_pbk', full_name='fetch.oef.pb.TACController.GameData.quantities_by_good_pbk', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='utility_params_by_good_pbk', full_name='fetch.oef.pb.TACController.GameData.utility_params_by_good_pbk', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_fee', full_name='fetch.oef.pb.TACController.GameData.tx_fee', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_pbk_to_name', full_name='fetch.oef.pb.TACController.GameData.agent_pbk_to_name', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='good_pbk_to_name', full_name='fetch.oef.pb.TACController.GameData.good_pbk_to_name', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='fetch.oef.pb.TACController.GameData.version_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=648,
)

_TACCONTROLLER_TRANSACTIONCONFIRMATION = _descriptor.Descriptor(
  name='TransactionConfirmation',
  full_name='fetch.oef.pb.TACController.TransactionConfirmation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='fetch.oef.pb.TACController.TransactionConfirmation.transaction_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_by_currency', full_name='fetch.oef.pb.TACController.TransactionConfirmation.amount_by_currency', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantities_by_good_pbk', full_name='fetch.oef.pb.TACController.TransactionConfirmation.quantities_by_good_pbk', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=651,
  serialized_end=812,
)

_TACCONTROLLER_STATEUPDATE = _descriptor.Descriptor(
  name='StateUpdate',
  full_name='fetch.oef.pb.TACController.StateUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_data', full_name='fetch.oef.pb.TACController.StateUpdate.game_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txs', full_name='fetch.oef.pb.TACController.StateUpdate.txs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=814,
  serialized_end=933,
)

_TACCONTROLLER_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='fetch.oef.pb.TACController.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='fetch.oef.pb.TACController.Error.error_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='fetch.oef.pb.TACController.Error.error_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='details', full_name='fetch.oef.pb.TACController.Error.details', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TACCONTROLLER_ERROR_ERRORCODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=936,
  serialized_end=1366,
)

_TACCONTROLLER = _descriptor.Descriptor(
  name='TACController',
  full_name='fetch.oef.pb.TACController',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_TACCONTROLLER_REGISTERED, _TACCONTROLLER_UNREGISTERED, _TACCONTROLLER_CANCELLED, _TACCONTROLLER_GAMEDATA, _TACCONTROLLER_TRANSACTIONCONFIRMATION, _TACCONTROLLER_STATEUPDATE, _TACCONTROLLER_ERROR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=1366,
)


_TACAGENT_REGISTER = _descriptor.Descriptor(
  name='Register',
  full_name='fetch.oef.pb.TACAgent.Register',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_name', full_name='fetch.oef.pb.TACAgent.Register.agent_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1381,
  serialized_end=1411,
)

_TACAGENT_UNREGISTER = _descriptor.Descriptor(
  name='Unregister',
  full_name='fetch.oef.pb.TACAgent.Unregister',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1413,
  serialized_end=1425,
)

_TACAGENT_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='fetch.oef.pb.TACAgent.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='fetch.oef.pb.TACAgent.Transaction.transaction_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counterparty', full_name='fetch.oef.pb.TACAgent.Transaction.counterparty', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_by_currency', full_name='fetch.oef.pb.TACAgent.Transaction.amount_by_currency', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_tx_fee', full_name='fetch.oef.pb.TACAgent.Transaction.sender_tx_fee', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counterparty_tx_fee', full_name='fetch.oef.pb.TACAgent.Transaction.counterparty_tx_fee', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantities_by_good_pbk', full_name='fetch.oef.pb.TACAgent.Transaction.quantities_by_good_pbk', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1428,
  serialized_end=1651,
)

_TACAGENT_GETSTATEUPDATE = _descriptor.Descriptor(
  name='GetStateUpdate',
  full_name='fetch.oef.pb.TACAgent.GetStateUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1653,
  serialized_end=1669,
)

_TACAGENT = _descriptor.Descriptor(
  name='TACAgent',
  full_name='fetch.oef.pb.TACAgent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_TACAGENT_REGISTER, _TACAGENT_UNREGISTER, _TACAGENT_TRANSACTION, _TACAGENT_GETSTATEUPDATE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1369,
  serialized_end=1669,
)


_TACMESSAGE = _descriptor.Descriptor(
  name='TACMessage',
  full_name='fetch.oef.pb.TACMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='register', full_name='fetch.oef.pb.TACMessage.register', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unregister', full_name='fetch.oef.pb.TACMessage.unregister', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction', full_name='fetch.oef.pb.TACMessage.transaction', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_state_update', full_name='fetch.oef.pb.TACMessage.get_state_update', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registered', full_name='fetch.oef.pb.TACMessage.registered', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unregistered', full_name='fetch.oef.pb.TACMessage.unregistered', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cancelled', full_name='fetch.oef.pb.TACMessage.cancelled', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_data', full_name='fetch.oef.pb.TACMessage.game_data', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_confirmation', full_name='fetch.oef.pb.TACMessage.transaction_confirmation', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_update', full_name='fetch.oef.pb.TACMessage.state_update', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='fetch.oef.pb.TACMessage.error', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='content', full_name='fetch.oef.pb.TACMessage.content',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1672,
  serialized_end=2384,
)

_TACCONTROLLER_REGISTERED.containing_type = _TACCONTROLLER
_TACCONTROLLER_UNREGISTERED.containing_type = _TACCONTROLLER
_TACCONTROLLER_CANCELLED.containing_type = _TACCONTROLLER
_TACCONTROLLER_GAMEDATA.fields_by_name['amount_by_currency'].message_type = _STRINTPAIR
_TACCONTROLLER_GAMEDATA.fields_by_name['exchange_params_by_currency'].message_type = _STRFLOATPAIR
_TACCONTROLLER_GAMEDATA.fields_by_name['quantities_by_good_pbk'].message_type = _STRINTPAIR
_TACCONTROLLER_GAMEDATA.fields_by_name['utility_params_by_good_pbk'].message_type = _STRFLOATPAIR
_TACCONTROLLER_GAMEDATA.fields_by_name['agent_pbk_to_name'].message_type = _STRSTRPAIR
_TACCONTROLLER_GAMEDATA.fields_by_name['good_pbk_to_name'].message_type = _STRSTRPAIR
_TACCONTROLLER_GAMEDATA.containing_type = _TACCONTROLLER
_TACCONTROLLER_TRANSACTIONCONFIRMATION.fields_by_name['amount_by_currency'].message_type = _STRINTPAIR
_TACCONTROLLER_TRANSACTIONCONFIRMATION.fields_by_name['quantities_by_good_pbk'].message_type = _STRINTPAIR
_TACCONTROLLER_TRANSACTIONCONFIRMATION.containing_type = _TACCONTROLLER
_TACCONTROLLER_STATEUPDATE.fields_by_name['game_data'].message_type = _TACCONTROLLER_GAMEDATA
_TACCONTROLLER_STATEUPDATE.fields_by_name['txs'].message_type = _TACAGENT_TRANSACTION
_TACCONTROLLER_STATEUPDATE.containing_type = _TACCONTROLLER
_TACCONTROLLER_ERROR.fields_by_name['error_code'].enum_type = _TACCONTROLLER_ERROR_ERRORCODE
_TACCONTROLLER_ERROR.fields_by_name['details'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TACCONTROLLER_ERROR.containing_type = _TACCONTROLLER
_TACCONTROLLER_ERROR_ERRORCODE.containing_type = _TACCONTROLLER_ERROR
_TACAGENT_REGISTER.containing_type = _TACAGENT
_TACAGENT_UNREGISTER.containing_type = _TACAGENT
_TACAGENT_TRANSACTION.fields_by_name['amount_by_currency'].message_type = _STRINTPAIR
_TACAGENT_TRANSACTION.fields_by_name['quantities_by_good_pbk'].message_type = _STRINTPAIR
_TACAGENT_TRANSACTION.containing_type = _TACAGENT
_TACAGENT_GETSTATEUPDATE.containing_type = _TACAGENT
_TACMESSAGE.fields_by_name['register'].message_type = _TACAGENT_REGISTER
_TACMESSAGE.fields_by_name['unregister'].message_type = _TACAGENT_UNREGISTER
_TACMESSAGE.fields_by_name['transaction'].message_type = _TACAGENT_TRANSACTION
_TACMESSAGE.fields_by_name['get_state_update'].message_type = _TACAGENT_GETSTATEUPDATE
_TACMESSAGE.fields_by_name['registered'].message_type = _TACCONTROLLER_REGISTERED
_TACMESSAGE.fields_by_name['unregistered'].message_type = _TACCONTROLLER_UNREGISTERED
_TACMESSAGE.fields_by_name['cancelled'].message_type = _TACCONTROLLER_CANCELLED
_TACMESSAGE.fields_by_name['game_data'].message_type = _TACCONTROLLER_GAMEDATA
_TACMESSAGE.fields_by_name['transaction_confirmation'].message_type = _TACCONTROLLER_TRANSACTIONCONFIRMATION
_TACMESSAGE.fields_by_name['state_update'].message_type = _TACCONTROLLER_STATEUPDATE
_TACMESSAGE.fields_by_name['error'].message_type = _TACCONTROLLER_ERROR
_TACMESSAGE.oneofs_by_name['content'].fields.append(
  _TACMESSAGE.fields_by_name['register'])
_TACMESSAGE.fields_by_name['register'].containing_oneof = _TACMESSAGE.oneofs_by_name['content']
_TACMESSAGE.oneofs_by_name['content'].fields.append(
  _TACMESSAGE.fields_by_name['unregister'])
_TACMESSAGE.fields_by_name['unregister'].containing_oneof = _TACMESSAGE.oneofs_by_name['content']
_TACMESSAGE.oneofs_by_name['content'].fields.append(
  _TACMESSAGE.fields_by_name['transaction'])
_TACMESSAGE.fields_by_name['transaction'].containing_oneof = _TACMESSAGE.oneofs_by_name['content']
_TACMESSAGE.oneofs_by_name['content'].fields.append(
  _TACMESSAGE.fields_by_name['get_state_update'])
_TACMESSAGE.fields_by_name['get_state_update'].containing_oneof = _TACMESSAGE.oneofs_by_name['content']
_TACMESSAGE.oneofs_by_name['content'].fields.append(
  _TACMESSAGE.fields_by_name['registered'])
_TACMESSAGE.fields_by_name['registered'].containing_oneof = _TACMESSAGE.oneofs_by_name['content']
_TACMESSAGE.oneofs_by_name['content'].fields.append(
  _TACMESSAGE.fields_by_name['unregistered'])
_TACMESSAGE.fields_by_name['unregistered'].containing_oneof = _TACMESSAGE.oneofs_by_name['content']
_TACMESSAGE.oneofs_by_name['content'].fields.append(
  _TACMESSAGE.fields_by_name['cancelled'])
_TACMESSAGE.fields_by_name['cancelled'].containing_oneof = _TACMESSAGE.oneofs_by_name['content']
_TACMESSAGE.oneofs_by_name['content'].fields.append(
  _TACMESSAGE.fields_by_name['game_data'])
_TACMESSAGE.fields_by_name['game_data'].containing_oneof = _TACMESSAGE.oneofs_by_name['content']
_TACMESSAGE.oneofs_by_name['content'].fields.append(
  _TACMESSAGE.fields_by_name['transaction_confirmation'])
_TACMESSAGE.fields_by_name['transaction_confirmation'].containing_oneof = _TACMESSAGE.oneofs_by_name['content']
_TACMESSAGE.oneofs_by_name['content'].fields.append(
  _TACMESSAGE.fields_by_name['state_update'])
_TACMESSAGE.fields_by_name['state_update'].containing_oneof = _TACMESSAGE.oneofs_by_name['content']
_TACMESSAGE.oneofs_by_name['content'].fields.append(
  _TACMESSAGE.fields_by_name['error'])
_TACMESSAGE.fields_by_name['error'].containing_oneof = _TACMESSAGE.oneofs_by_name['content']
DESCRIPTOR.message_types_by_name['StrIntPair'] = _STRINTPAIR
DESCRIPTOR.message_types_by_name['StrFloatPair'] = _STRFLOATPAIR
DESCRIPTOR.message_types_by_name['StrStrPair'] = _STRSTRPAIR
DESCRIPTOR.message_types_by_name['TACController'] = _TACCONTROLLER
DESCRIPTOR.message_types_by_name['TACAgent'] = _TACAGENT
DESCRIPTOR.message_types_by_name['TACMessage'] = _TACMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StrIntPair = _reflection.GeneratedProtocolMessageType('StrIntPair', (_message.Message,), dict(
  DESCRIPTOR = _STRINTPAIR,
  __module__ = 'tac_pb2'
  # @@protoc_insertion_point(class_scope:fetch.oef.pb.StrIntPair)
  ))
_sym_db.RegisterMessage(StrIntPair)

StrFloatPair = _reflection.GeneratedProtocolMessageType('StrFloatPair', (_message.Message,), dict(
  DESCRIPTOR = _STRFLOATPAIR,
  __module__ = 'tac_pb2'
  # @@protoc_insertion_point(class_scope:fetch.oef.pb.StrFloatPair)
  ))
_sym_db.RegisterMessage(StrFloatPair)

StrStrPair = _reflection.GeneratedProtocolMessageType('StrStrPair', (_message.Message,), dict(
  DESCRIPTOR = _STRSTRPAIR,
  __module__ = 'tac_pb2'
  # @@protoc_insertion_point(class_scope:fetch.oef.pb.StrStrPair)
  ))
_sym_db.RegisterMessage(StrStrPair)

TACController = _reflection.GeneratedProtocolMessageType('TACController', (_message.Message,), dict(

  Registered = _reflection.GeneratedProtocolMessageType('Registered', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_REGISTERED,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.Registered)
    ))
  ,

  Unregistered = _reflection.GeneratedProtocolMessageType('Unregistered', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_UNREGISTERED,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.Unregistered)
    ))
  ,

  Cancelled = _reflection.GeneratedProtocolMessageType('Cancelled', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_CANCELLED,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.Cancelled)
    ))
  ,

  GameData = _reflection.GeneratedProtocolMessageType('GameData', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_GAMEDATA,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.GameData)
    ))
  ,

  TransactionConfirmation = _reflection.GeneratedProtocolMessageType('TransactionConfirmation', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_TRANSACTIONCONFIRMATION,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.TransactionConfirmation)
    ))
  ,

  StateUpdate = _reflection.GeneratedProtocolMessageType('StateUpdate', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_STATEUPDATE,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.StateUpdate)
    ))
  ,

  Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_ERROR,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.Error)
    ))
  ,
  DESCRIPTOR = _TACCONTROLLER,
  __module__ = 'tac_pb2'
  # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController)
  ))
_sym_db.RegisterMessage(TACController)
_sym_db.RegisterMessage(TACController.Registered)
_sym_db.RegisterMessage(TACController.Unregistered)
_sym_db.RegisterMessage(TACController.Cancelled)
_sym_db.RegisterMessage(TACController.GameData)
_sym_db.RegisterMessage(TACController.TransactionConfirmation)
_sym_db.RegisterMessage(TACController.StateUpdate)
_sym_db.RegisterMessage(TACController.Error)

TACAgent = _reflection.GeneratedProtocolMessageType('TACAgent', (_message.Message,), dict(

  Register = _reflection.GeneratedProtocolMessageType('Register', (_message.Message,), dict(
    DESCRIPTOR = _TACAGENT_REGISTER,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACAgent.Register)
    ))
  ,

  Unregister = _reflection.GeneratedProtocolMessageType('Unregister', (_message.Message,), dict(
    DESCRIPTOR = _TACAGENT_UNREGISTER,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACAgent.Unregister)
    ))
  ,

  Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
    DESCRIPTOR = _TACAGENT_TRANSACTION,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACAgent.Transaction)
    ))
  ,

  GetStateUpdate = _reflection.GeneratedProtocolMessageType('GetStateUpdate', (_message.Message,), dict(
    DESCRIPTOR = _TACAGENT_GETSTATEUPDATE,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACAgent.GetStateUpdate)
    ))
  ,
  DESCRIPTOR = _TACAGENT,
  __module__ = 'tac_pb2'
  # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACAgent)
  ))
_sym_db.RegisterMessage(TACAgent)
_sym_db.RegisterMessage(TACAgent.Register)
_sym_db.RegisterMessage(TACAgent.Unregister)
_sym_db.RegisterMessage(TACAgent.Transaction)
_sym_db.RegisterMessage(TACAgent.GetStateUpdate)

TACMessage = _reflection.GeneratedProtocolMessageType('TACMessage', (_message.Message,), dict(
  DESCRIPTOR = _TACMESSAGE,
  __module__ = 'tac_pb2'
  # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACMessage)
  ))
_sym_db.RegisterMessage(TACMessage)


# @@protoc_insertion_point(module_scope)
