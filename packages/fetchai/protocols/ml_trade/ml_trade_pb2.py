# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ml_trade.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="ml_trade.proto",
    package="aea.fetchai.ml_trade.v0_11_0",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\x0eml_trade.proto\x12\x1c\x61\x65\x61.fetchai.ml_trade.v0_11_0"\xc4\x06\n\x0eMlTradeMessage\x12R\n\x06\x61\x63\x63\x65pt\x18\x05 \x01(\x0b\x32@.aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Accept_PerformativeH\x00\x12L\n\x03\x63\x66p\x18\x06 \x01(\x0b\x32=.aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Cfp_PerformativeH\x00\x12N\n\x04\x64\x61ta\x18\x07 \x01(\x0b\x32>.aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Data_PerformativeH\x00\x12P\n\x05terms\x18\x08 \x01(\x0b\x32?.aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Terms_PerformativeH\x00\x1a(\n\x0b\x44\x65scription\x12\x19\n\x11\x64\x65scription_bytes\x18\x01 \x01(\x0c\x1a\x1c\n\x05Query\x12\x13\n\x0bquery_bytes\x18\x01 \x01(\x0c\x1aU\n\x10\x43\x66p_Performative\x12\x41\n\x05query\x18\x01 \x01(\x0b\x32\x32.aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Query\x1a]\n\x12Terms_Performative\x12G\n\x05terms\x18\x01 \x01(\x0b\x32\x38.aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Description\x1aq\n\x13\x41\x63\x63\x65pt_Performative\x12G\n\x05terms\x18\x01 \x01(\x0b\x32\x38.aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Description\x12\x11\n\ttx_digest\x18\x02 \x01(\t\x1am\n\x11\x44\x61ta_Performative\x12G\n\x05terms\x18\x01 \x01(\x0b\x32\x38.aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Description\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x42\x0e\n\x0cperformativeb\x06proto3',
)


_MLTRADEMESSAGE_DESCRIPTION = _descriptor.Descriptor(
    name="Description",
    full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Description",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="description_bytes",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Description.description_bytes",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=391,
    serialized_end=431,
)

_MLTRADEMESSAGE_QUERY = _descriptor.Descriptor(
    name="Query",
    full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Query",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="query_bytes",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Query.query_bytes",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=433,
    serialized_end=461,
)

_MLTRADEMESSAGE_CFP_PERFORMATIVE = _descriptor.Descriptor(
    name="Cfp_Performative",
    full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Cfp_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="query",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Cfp_Performative.query",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=463,
    serialized_end=548,
)

_MLTRADEMESSAGE_TERMS_PERFORMATIVE = _descriptor.Descriptor(
    name="Terms_Performative",
    full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Terms_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Terms_Performative.terms",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=550,
    serialized_end=643,
)

_MLTRADEMESSAGE_ACCEPT_PERFORMATIVE = _descriptor.Descriptor(
    name="Accept_Performative",
    full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Accept_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Accept_Performative.terms",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="tx_digest",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Accept_Performative.tx_digest",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=645,
    serialized_end=758,
)

_MLTRADEMESSAGE_DATA_PERFORMATIVE = _descriptor.Descriptor(
    name="Data_Performative",
    full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Data_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Data_Performative.terms",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Data_Performative.payload",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=760,
    serialized_end=869,
)

_MLTRADEMESSAGE = _descriptor.Descriptor(
    name="MlTradeMessage",
    full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="accept",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.accept",
            index=0,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="cfp",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.cfp",
            index=1,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.data",
            index=2,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.terms",
            index=3,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _MLTRADEMESSAGE_DESCRIPTION,
        _MLTRADEMESSAGE_QUERY,
        _MLTRADEMESSAGE_CFP_PERFORMATIVE,
        _MLTRADEMESSAGE_TERMS_PERFORMATIVE,
        _MLTRADEMESSAGE_ACCEPT_PERFORMATIVE,
        _MLTRADEMESSAGE_DATA_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=49,
    serialized_end=885,
)

_MLTRADEMESSAGE_DESCRIPTION.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE_QUERY.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE_CFP_PERFORMATIVE.fields_by_name[
    "query"
].message_type = _MLTRADEMESSAGE_QUERY
_MLTRADEMESSAGE_CFP_PERFORMATIVE.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE_TERMS_PERFORMATIVE.fields_by_name[
    "terms"
].message_type = _MLTRADEMESSAGE_DESCRIPTION
_MLTRADEMESSAGE_TERMS_PERFORMATIVE.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE_ACCEPT_PERFORMATIVE.fields_by_name[
    "terms"
].message_type = _MLTRADEMESSAGE_DESCRIPTION
_MLTRADEMESSAGE_ACCEPT_PERFORMATIVE.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE_DATA_PERFORMATIVE.fields_by_name[
    "terms"
].message_type = _MLTRADEMESSAGE_DESCRIPTION
_MLTRADEMESSAGE_DATA_PERFORMATIVE.containing_type = _MLTRADEMESSAGE
_MLTRADEMESSAGE.fields_by_name[
    "accept"
].message_type = _MLTRADEMESSAGE_ACCEPT_PERFORMATIVE
_MLTRADEMESSAGE.fields_by_name["cfp"].message_type = _MLTRADEMESSAGE_CFP_PERFORMATIVE
_MLTRADEMESSAGE.fields_by_name["data"].message_type = _MLTRADEMESSAGE_DATA_PERFORMATIVE
_MLTRADEMESSAGE.fields_by_name[
    "terms"
].message_type = _MLTRADEMESSAGE_TERMS_PERFORMATIVE
_MLTRADEMESSAGE.oneofs_by_name["performative"].fields.append(
    _MLTRADEMESSAGE.fields_by_name["accept"]
)
_MLTRADEMESSAGE.fields_by_name[
    "accept"
].containing_oneof = _MLTRADEMESSAGE.oneofs_by_name["performative"]
_MLTRADEMESSAGE.oneofs_by_name["performative"].fields.append(
    _MLTRADEMESSAGE.fields_by_name["cfp"]
)
_MLTRADEMESSAGE.fields_by_name["cfp"].containing_oneof = _MLTRADEMESSAGE.oneofs_by_name[
    "performative"
]
_MLTRADEMESSAGE.oneofs_by_name["performative"].fields.append(
    _MLTRADEMESSAGE.fields_by_name["data"]
)
_MLTRADEMESSAGE.fields_by_name[
    "data"
].containing_oneof = _MLTRADEMESSAGE.oneofs_by_name["performative"]
_MLTRADEMESSAGE.oneofs_by_name["performative"].fields.append(
    _MLTRADEMESSAGE.fields_by_name["terms"]
)
_MLTRADEMESSAGE.fields_by_name[
    "terms"
].containing_oneof = _MLTRADEMESSAGE.oneofs_by_name["performative"]
DESCRIPTOR.message_types_by_name["MlTradeMessage"] = _MLTRADEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MlTradeMessage = _reflection.GeneratedProtocolMessageType(
    "MlTradeMessage",
    (_message.Message,),
    {
        "Description": _reflection.GeneratedProtocolMessageType(
            "Description",
            (_message.Message,),
            {
                "DESCRIPTOR": _MLTRADEMESSAGE_DESCRIPTION,
                "__module__": "ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Description)
            },
        ),
        "Query": _reflection.GeneratedProtocolMessageType(
            "Query",
            (_message.Message,),
            {
                "DESCRIPTOR": _MLTRADEMESSAGE_QUERY,
                "__module__": "ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Query)
            },
        ),
        "Cfp_Performative": _reflection.GeneratedProtocolMessageType(
            "Cfp_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _MLTRADEMESSAGE_CFP_PERFORMATIVE,
                "__module__": "ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Cfp_Performative)
            },
        ),
        "Terms_Performative": _reflection.GeneratedProtocolMessageType(
            "Terms_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _MLTRADEMESSAGE_TERMS_PERFORMATIVE,
                "__module__": "ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Terms_Performative)
            },
        ),
        "Accept_Performative": _reflection.GeneratedProtocolMessageType(
            "Accept_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _MLTRADEMESSAGE_ACCEPT_PERFORMATIVE,
                "__module__": "ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Accept_Performative)
            },
        ),
        "Data_Performative": _reflection.GeneratedProtocolMessageType(
            "Data_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _MLTRADEMESSAGE_DATA_PERFORMATIVE,
                "__module__": "ml_trade_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.ml_trade.v0_11_0.MlTradeMessage.Data_Performative)
            },
        ),
        "DESCRIPTOR": _MLTRADEMESSAGE,
        "__module__": "ml_trade_pb2"
        # @@protoc_insertion_point(class_scope:aea.fetchai.ml_trade.v0_11_0.MlTradeMessage)
    },
)
_sym_db.RegisterMessage(MlTradeMessage)
_sym_db.RegisterMessage(MlTradeMessage.Description)
_sym_db.RegisterMessage(MlTradeMessage.Query)
_sym_db.RegisterMessage(MlTradeMessage.Cfp_Performative)
_sym_db.RegisterMessage(MlTradeMessage.Terms_Performative)
_sym_db.RegisterMessage(MlTradeMessage.Accept_Performative)
_sym_db.RegisterMessage(MlTradeMessage.Data_Performative)


# @@protoc_insertion_point(module_scope)
