# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state_update.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x12state_update.proto\x12\x1f\x61\x65\x61.fetchai.state_update.v1_0_0"\x93\x0c\n\x12StateUpdateMessage\x12W\n\x05\x61pply\x18\x05 \x01(\x0b\x32\x46.aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Apply_PerformativeH\x00\x12S\n\x03\x65nd\x18\x06 \x01(\x0b\x32\x44.aea.fetchai.state_update.v1_0_0.StateUpdateMessage.End_PerformativeH\x00\x12\x61\n\ninitialize\x18\x07 \x01(\x0b\x32K.aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Initialize_PerformativeH\x00\x1a\xbc\x06\n\x17Initialize_Performative\x12\x93\x01\n\x1e\x65xchange_params_by_currency_id\x18\x01 \x03(\x0b\x32k.aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Initialize_Performative.ExchangeParamsByCurrencyIdEntry\x12\x89\x01\n\x19utility_params_by_good_id\x18\x02 \x03(\x0b\x32\x66.aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Initialize_Performative.UtilityParamsByGoodIdEntry\x12\x82\x01\n\x15\x61mount_by_currency_id\x18\x03 \x03(\x0b\x32\x63.aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Initialize_Performative.AmountByCurrencyIdEntry\x12\x82\x01\n\x15quantities_by_good_id\x18\x04 \x03(\x0b\x32\x63.aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Initialize_Performative.QuantitiesByGoodIdEntry\x1a\x41\n\x1f\x45xchangeParamsByCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a<\n\x1aUtilityParamsByGoodIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\x39\n\x17\x41mountByCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x39\n\x17QuantitiesByGoodIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x88\x03\n\x12\x41pply_Performative\x12}\n\x15\x61mount_by_currency_id\x18\x01 \x03(\x0b\x32^.aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Apply_Performative.AmountByCurrencyIdEntry\x12}\n\x15quantities_by_good_id\x18\x02 \x03(\x0b\x32^.aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Apply_Performative.QuantitiesByGoodIdEntry\x1a\x39\n\x17\x41mountByCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x39\n\x17QuantitiesByGoodIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x12\n\x10\x45nd_PerformativeB\x0e\n\x0cperformativeb\x06proto3'
)


_STATEUPDATEMESSAGE = DESCRIPTOR.message_types_by_name["StateUpdateMessage"]
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE = _STATEUPDATEMESSAGE.nested_types_by_name[
    "Initialize_Performative"
]
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY = _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE.nested_types_by_name[
    "ExchangeParamsByCurrencyIdEntry"
]
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY = _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE.nested_types_by_name[
    "UtilityParamsByGoodIdEntry"
]
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY = _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE.nested_types_by_name[
    "AmountByCurrencyIdEntry"
]
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY = _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE.nested_types_by_name[
    "QuantitiesByGoodIdEntry"
]
_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE = _STATEUPDATEMESSAGE.nested_types_by_name[
    "Apply_Performative"
]
_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY = _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE.nested_types_by_name[
    "AmountByCurrencyIdEntry"
]
_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY = _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE.nested_types_by_name[
    "QuantitiesByGoodIdEntry"
]
_STATEUPDATEMESSAGE_END_PERFORMATIVE = _STATEUPDATEMESSAGE.nested_types_by_name[
    "End_Performative"
]
StateUpdateMessage = _reflection.GeneratedProtocolMessageType(
    "StateUpdateMessage",
    (_message.Message,),
    {
        "Initialize_Performative": _reflection.GeneratedProtocolMessageType(
            "Initialize_Performative",
            (_message.Message,),
            {
                "ExchangeParamsByCurrencyIdEntry": _reflection.GeneratedProtocolMessageType(
                    "ExchangeParamsByCurrencyIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Initialize_Performative.ExchangeParamsByCurrencyIdEntry)
                    },
                ),
                "UtilityParamsByGoodIdEntry": _reflection.GeneratedProtocolMessageType(
                    "UtilityParamsByGoodIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Initialize_Performative.UtilityParamsByGoodIdEntry)
                    },
                ),
                "AmountByCurrencyIdEntry": _reflection.GeneratedProtocolMessageType(
                    "AmountByCurrencyIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Initialize_Performative.AmountByCurrencyIdEntry)
                    },
                ),
                "QuantitiesByGoodIdEntry": _reflection.GeneratedProtocolMessageType(
                    "QuantitiesByGoodIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Initialize_Performative.QuantitiesByGoodIdEntry)
                    },
                ),
                "DESCRIPTOR": _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE,
                "__module__": "state_update_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Initialize_Performative)
            },
        ),
        "Apply_Performative": _reflection.GeneratedProtocolMessageType(
            "Apply_Performative",
            (_message.Message,),
            {
                "AmountByCurrencyIdEntry": _reflection.GeneratedProtocolMessageType(
                    "AmountByCurrencyIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Apply_Performative.AmountByCurrencyIdEntry)
                    },
                ),
                "QuantitiesByGoodIdEntry": _reflection.GeneratedProtocolMessageType(
                    "QuantitiesByGoodIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Apply_Performative.QuantitiesByGoodIdEntry)
                    },
                ),
                "DESCRIPTOR": _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE,
                "__module__": "state_update_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.state_update.v1_0_0.StateUpdateMessage.Apply_Performative)
            },
        ),
        "End_Performative": _reflection.GeneratedProtocolMessageType(
            "End_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _STATEUPDATEMESSAGE_END_PERFORMATIVE,
                "__module__": "state_update_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.state_update.v1_0_0.StateUpdateMessage.End_Performative)
            },
        ),
        "DESCRIPTOR": _STATEUPDATEMESSAGE,
        "__module__": "state_update_pb2"
        # @@protoc_insertion_point(class_scope:aea.fetchai.state_update.v1_0_0.StateUpdateMessage)
    },
)
_sym_db.RegisterMessage(StateUpdateMessage)
_sym_db.RegisterMessage(StateUpdateMessage.Initialize_Performative)
_sym_db.RegisterMessage(
    StateUpdateMessage.Initialize_Performative.ExchangeParamsByCurrencyIdEntry
)
_sym_db.RegisterMessage(
    StateUpdateMessage.Initialize_Performative.UtilityParamsByGoodIdEntry
)
_sym_db.RegisterMessage(
    StateUpdateMessage.Initialize_Performative.AmountByCurrencyIdEntry
)
_sym_db.RegisterMessage(
    StateUpdateMessage.Initialize_Performative.QuantitiesByGoodIdEntry
)
_sym_db.RegisterMessage(StateUpdateMessage.Apply_Performative)
_sym_db.RegisterMessage(StateUpdateMessage.Apply_Performative.AmountByCurrencyIdEntry)
_sym_db.RegisterMessage(StateUpdateMessage.Apply_Performative.QuantitiesByGoodIdEntry)
_sym_db.RegisterMessage(StateUpdateMessage.End_Performative)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY._options = (
        None
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY._serialized_options = (
        b"8\001"
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY._options = (
        None
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY._serialized_options = (
        b"8\001"
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._options = None
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._serialized_options = (
        b"8\001"
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._options = None
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._serialized_options = (
        b"8\001"
    )
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._options = None
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._serialized_options = (
        b"8\001"
    )
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._options = None
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._serialized_options = (
        b"8\001"
    )
    _STATEUPDATEMESSAGE._serialized_start = 56
    _STATEUPDATEMESSAGE._serialized_end = 1611
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE._serialized_start = 352
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE._serialized_end = 1180
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY._serialized_start = (
        935
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY._serialized_end = (
        1000
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY._serialized_start = (
        1002
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY._serialized_end = (
        1062
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._serialized_start = (
        1064
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._serialized_end = (
        1121
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._serialized_start = (
        1123
    )
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._serialized_end = (
        1180
    )
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE._serialized_start = 1183
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE._serialized_end = 1575
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._serialized_start = (
        1064
    )
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._serialized_end = (
        1121
    )
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._serialized_start = (
        1123
    )
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._serialized_end = (
        1180
    )
    _STATEUPDATEMESSAGE_END_PERFORMATIVE._serialized_start = 1577
    _STATEUPDATEMESSAGE_END_PERFORMATIVE._serialized_end = 1595
# @@protoc_insertion_point(module_scope)
