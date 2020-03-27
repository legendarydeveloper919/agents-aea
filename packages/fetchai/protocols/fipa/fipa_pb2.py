# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocols/fipa/fipa.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="protocols/fipa/fipa.proto",
    package="fetch.aea.Fipa",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x19protocols/fipa/fipa.proto\x12\x0e\x66\x65tch.aea.Fipa"\xcc\n\n\x0b\x46ipaMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12"\n\x1a\x64ialogue_starter_reference\x18\x02 \x01(\t\x12$\n\x1c\x64ialogue_responder_reference\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\x05\x12\x34\n\x06\x61\x63\x63\x65pt\x18\x05 \x01(\x0b\x32".fetch.aea.Fipa.FipaMessage.AcceptH\x00\x12\x46\n\x0f\x61\x63\x63\x65pt_w_inform\x18\x06 \x01(\x0b\x32+.fetch.aea.Fipa.FipaMessage.Accept_W_InformH\x00\x12.\n\x03\x63\x66p\x18\x07 \x01(\x0b\x32\x1f.fetch.aea.Fipa.FipaMessage.CfpH\x00\x12\x36\n\x07\x64\x65\x63line\x18\x08 \x01(\x0b\x32#.fetch.aea.Fipa.FipaMessage.DeclineH\x00\x12\x34\n\x06inform\x18\t \x01(\x0b\x32".fetch.aea.Fipa.FipaMessage.InformH\x00\x12@\n\x0cmatch_accept\x18\n \x01(\x0b\x32(.fetch.aea.Fipa.FipaMessage.Match_AcceptH\x00\x12R\n\x15match_accept_w_inform\x18\x0b \x01(\x0b\x32\x31.fetch.aea.Fipa.FipaMessage.Match_Accept_W_InformH\x00\x12\x36\n\x07propose\x18\x0c \x01(\x0b\x32#.fetch.aea.Fipa.FipaMessage.ProposeH\x00\x1a"\n\x0b\x44\x65scription\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\x0c\x1a\x81\x01\n\x05Query\x12\x0f\n\x05\x62ytes\x18\x01 \x01(\x0cH\x00\x12<\n\x07nothing\x18\x02 \x01(\x0b\x32).fetch.aea.Fipa.FipaMessage.Query.NothingH\x00\x12\x15\n\x0bquery_bytes\x18\x03 \x01(\x0cH\x00\x1a\t\n\x07NothingB\x07\n\x05query\x1a\x37\n\x03\x43\x66p\x12\x30\n\x05query\x18\x01 \x01(\x0b\x32!.fetch.aea.Fipa.FipaMessage.Query\x1a\x44\n\x07Propose\x12\x39\n\x08proposal\x18\x01 \x01(\x0b\x32\'.fetch.aea.Fipa.FipaMessage.Description\x1a\x83\x01\n\x0f\x41\x63\x63\x65pt_W_Inform\x12\x43\n\x04info\x18\x01 \x03(\x0b\x32\x35.fetch.aea.Fipa.FipaMessage.Accept_W_Inform.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x8f\x01\n\x15Match_Accept_W_Inform\x12I\n\x04info\x18\x01 \x03(\x0b\x32;.fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aq\n\x06Inform\x12:\n\x04info\x18\x01 \x03(\x0b\x32,.fetch.aea.Fipa.FipaMessage.Inform.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x08\n\x06\x41\x63\x63\x65pt\x1a\t\n\x07\x44\x65\x63line\x1a\x0e\n\x0cMatch_AcceptB\x0e\n\x0cperformativeb\x06proto3'
    ),
)


_FIPAMESSAGE_DESCRIPTION = _descriptor.Descriptor(
    name="Description",
    full_name="fetch.aea.Fipa.FipaMessage.Description",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="description",
            full_name="fetch.aea.Fipa.FipaMessage.Description.description",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
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
    serialized_start=661,
    serialized_end=695,
)

_FIPAMESSAGE_QUERY_NOTHING = _descriptor.Descriptor(
    name="Nothing",
    full_name="fetch.aea.Fipa.FipaMessage.Query.Nothing",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=809,
    serialized_end=818,
)

_FIPAMESSAGE_QUERY = _descriptor.Descriptor(
    name="Query",
    full_name="fetch.aea.Fipa.FipaMessage.Query",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="bytes",
            full_name="fetch.aea.Fipa.FipaMessage.Query.bytes",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="nothing",
            full_name="fetch.aea.Fipa.FipaMessage.Query.nothing",
            index=1,
            number=2,
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
            name="query_bytes",
            full_name="fetch.aea.Fipa.FipaMessage.Query.query_bytes",
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
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
    nested_types=[_FIPAMESSAGE_QUERY_NOTHING,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="query",
            full_name="fetch.aea.Fipa.FipaMessage.Query.query",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=698,
    serialized_end=827,
)

_FIPAMESSAGE_CFP = _descriptor.Descriptor(
    name="Cfp",
    full_name="fetch.aea.Fipa.FipaMessage.Cfp",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="query",
            full_name="fetch.aea.Fipa.FipaMessage.Cfp.query",
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
    serialized_start=829,
    serialized_end=884,
)

_FIPAMESSAGE_PROPOSE = _descriptor.Descriptor(
    name="Propose",
    full_name="fetch.aea.Fipa.FipaMessage.Propose",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="proposal",
            full_name="fetch.aea.Fipa.FipaMessage.Propose.proposal",
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
    serialized_start=886,
    serialized_end=954,
)

_FIPAMESSAGE_ACCEPT_W_INFORM_INFOENTRY = _descriptor.Descriptor(
    name="InfoEntry",
    full_name="fetch.aea.Fipa.FipaMessage.Accept_W_Inform.InfoEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.Fipa.FipaMessage.Accept_W_Inform.InfoEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.Fipa.FipaMessage.Accept_W_Inform.InfoEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
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
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1045,
    serialized_end=1088,
)

_FIPAMESSAGE_ACCEPT_W_INFORM = _descriptor.Descriptor(
    name="Accept_W_Inform",
    full_name="fetch.aea.Fipa.FipaMessage.Accept_W_Inform",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="info",
            full_name="fetch.aea.Fipa.FipaMessage.Accept_W_Inform.info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    nested_types=[_FIPAMESSAGE_ACCEPT_W_INFORM_INFOENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=957,
    serialized_end=1088,
)

_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_INFOENTRY = _descriptor.Descriptor(
    name="InfoEntry",
    full_name="fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform.InfoEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform.InfoEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform.InfoEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
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
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1045,
    serialized_end=1088,
)

_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM = _descriptor.Descriptor(
    name="Match_Accept_W_Inform",
    full_name="fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="info",
            full_name="fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform.info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    nested_types=[_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_INFOENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1091,
    serialized_end=1234,
)

_FIPAMESSAGE_INFORM_INFOENTRY = _descriptor.Descriptor(
    name="InfoEntry",
    full_name="fetch.aea.Fipa.FipaMessage.Inform.InfoEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.Fipa.FipaMessage.Inform.InfoEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.Fipa.FipaMessage.Inform.InfoEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
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
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1045,
    serialized_end=1088,
)

_FIPAMESSAGE_INFORM = _descriptor.Descriptor(
    name="Inform",
    full_name="fetch.aea.Fipa.FipaMessage.Inform",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="info",
            full_name="fetch.aea.Fipa.FipaMessage.Inform.info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    nested_types=[_FIPAMESSAGE_INFORM_INFOENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1236,
    serialized_end=1349,
)

_FIPAMESSAGE_ACCEPT = _descriptor.Descriptor(
    name="Accept",
    full_name="fetch.aea.Fipa.FipaMessage.Accept",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1351,
    serialized_end=1359,
)

_FIPAMESSAGE_DECLINE = _descriptor.Descriptor(
    name="Decline",
    full_name="fetch.aea.Fipa.FipaMessage.Decline",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1361,
    serialized_end=1370,
)

_FIPAMESSAGE_MATCH_ACCEPT = _descriptor.Descriptor(
    name="Match_Accept",
    full_name="fetch.aea.Fipa.FipaMessage.Match_Accept",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1372,
    serialized_end=1386,
)

_FIPAMESSAGE = _descriptor.Descriptor(
    name="FipaMessage",
    full_name="fetch.aea.Fipa.FipaMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="message_id",
            full_name="fetch.aea.Fipa.FipaMessage.message_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_starter_reference",
            full_name="fetch.aea.Fipa.FipaMessage.dialogue_starter_reference",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_responder_reference",
            full_name="fetch.aea.Fipa.FipaMessage.dialogue_responder_reference",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="target",
            full_name="fetch.aea.Fipa.FipaMessage.target",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="accept",
            full_name="fetch.aea.Fipa.FipaMessage.accept",
            index=4,
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
            name="accept_w_inform",
            full_name="fetch.aea.Fipa.FipaMessage.accept_w_inform",
            index=5,
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
            name="cfp",
            full_name="fetch.aea.Fipa.FipaMessage.cfp",
            index=6,
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
            name="decline",
            full_name="fetch.aea.Fipa.FipaMessage.decline",
            index=7,
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
        _descriptor.FieldDescriptor(
            name="inform",
            full_name="fetch.aea.Fipa.FipaMessage.inform",
            index=8,
            number=9,
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
            name="match_accept",
            full_name="fetch.aea.Fipa.FipaMessage.match_accept",
            index=9,
            number=10,
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
            name="match_accept_w_inform",
            full_name="fetch.aea.Fipa.FipaMessage.match_accept_w_inform",
            index=10,
            number=11,
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
            name="propose",
            full_name="fetch.aea.Fipa.FipaMessage.propose",
            index=11,
            number=12,
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
        _FIPAMESSAGE_DESCRIPTION,
        _FIPAMESSAGE_QUERY,
        _FIPAMESSAGE_CFP,
        _FIPAMESSAGE_PROPOSE,
        _FIPAMESSAGE_ACCEPT_W_INFORM,
        _FIPAMESSAGE_MATCH_ACCEPT_W_INFORM,
        _FIPAMESSAGE_INFORM,
        _FIPAMESSAGE_ACCEPT,
        _FIPAMESSAGE_DECLINE,
        _FIPAMESSAGE_MATCH_ACCEPT,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="fetch.aea.Fipa.FipaMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=46,
    serialized_end=1402,
)

_FIPAMESSAGE_DESCRIPTION.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_QUERY_NOTHING.containing_type = _FIPAMESSAGE_QUERY
_FIPAMESSAGE_QUERY.fields_by_name["nothing"].message_type = _FIPAMESSAGE_QUERY_NOTHING
_FIPAMESSAGE_QUERY.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _FIPAMESSAGE_QUERY.fields_by_name["bytes"]
)
_FIPAMESSAGE_QUERY.fields_by_name[
    "bytes"
].containing_oneof = _FIPAMESSAGE_QUERY.oneofs_by_name["query"]
_FIPAMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _FIPAMESSAGE_QUERY.fields_by_name["nothing"]
)
_FIPAMESSAGE_QUERY.fields_by_name[
    "nothing"
].containing_oneof = _FIPAMESSAGE_QUERY.oneofs_by_name["query"]
_FIPAMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _FIPAMESSAGE_QUERY.fields_by_name["query_bytes"]
)
_FIPAMESSAGE_QUERY.fields_by_name[
    "query_bytes"
].containing_oneof = _FIPAMESSAGE_QUERY.oneofs_by_name["query"]
_FIPAMESSAGE_CFP.fields_by_name["query"].message_type = _FIPAMESSAGE_QUERY
_FIPAMESSAGE_CFP.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_PROPOSE.fields_by_name["proposal"].message_type = _FIPAMESSAGE_DESCRIPTION
_FIPAMESSAGE_PROPOSE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_ACCEPT_W_INFORM_INFOENTRY.containing_type = _FIPAMESSAGE_ACCEPT_W_INFORM
_FIPAMESSAGE_ACCEPT_W_INFORM.fields_by_name[
    "info"
].message_type = _FIPAMESSAGE_ACCEPT_W_INFORM_INFOENTRY
_FIPAMESSAGE_ACCEPT_W_INFORM.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_INFOENTRY.containing_type = (
    _FIPAMESSAGE_MATCH_ACCEPT_W_INFORM
)
_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM.fields_by_name[
    "info"
].message_type = _FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_INFOENTRY
_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_INFORM_INFOENTRY.containing_type = _FIPAMESSAGE_INFORM
_FIPAMESSAGE_INFORM.fields_by_name["info"].message_type = _FIPAMESSAGE_INFORM_INFOENTRY
_FIPAMESSAGE_INFORM.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_ACCEPT.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_DECLINE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_MATCH_ACCEPT.containing_type = _FIPAMESSAGE
_FIPAMESSAGE.fields_by_name["accept"].message_type = _FIPAMESSAGE_ACCEPT
_FIPAMESSAGE.fields_by_name[
    "accept_w_inform"
].message_type = _FIPAMESSAGE_ACCEPT_W_INFORM
_FIPAMESSAGE.fields_by_name["cfp"].message_type = _FIPAMESSAGE_CFP
_FIPAMESSAGE.fields_by_name["decline"].message_type = _FIPAMESSAGE_DECLINE
_FIPAMESSAGE.fields_by_name["inform"].message_type = _FIPAMESSAGE_INFORM
_FIPAMESSAGE.fields_by_name["match_accept"].message_type = _FIPAMESSAGE_MATCH_ACCEPT
_FIPAMESSAGE.fields_by_name[
    "match_accept_w_inform"
].message_type = _FIPAMESSAGE_MATCH_ACCEPT_W_INFORM
_FIPAMESSAGE.fields_by_name["propose"].message_type = _FIPAMESSAGE_PROPOSE
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["accept"]
)
_FIPAMESSAGE.fields_by_name["accept"].containing_oneof = _FIPAMESSAGE.oneofs_by_name[
    "performative"
]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["accept_w_inform"]
)
_FIPAMESSAGE.fields_by_name[
    "accept_w_inform"
].containing_oneof = _FIPAMESSAGE.oneofs_by_name["performative"]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["cfp"]
)
_FIPAMESSAGE.fields_by_name["cfp"].containing_oneof = _FIPAMESSAGE.oneofs_by_name[
    "performative"
]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["decline"]
)
_FIPAMESSAGE.fields_by_name["decline"].containing_oneof = _FIPAMESSAGE.oneofs_by_name[
    "performative"
]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["inform"]
)
_FIPAMESSAGE.fields_by_name["inform"].containing_oneof = _FIPAMESSAGE.oneofs_by_name[
    "performative"
]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["match_accept"]
)
_FIPAMESSAGE.fields_by_name[
    "match_accept"
].containing_oneof = _FIPAMESSAGE.oneofs_by_name["performative"]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["match_accept_w_inform"]
)
_FIPAMESSAGE.fields_by_name[
    "match_accept_w_inform"
].containing_oneof = _FIPAMESSAGE.oneofs_by_name["performative"]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["propose"]
)
_FIPAMESSAGE.fields_by_name["propose"].containing_oneof = _FIPAMESSAGE.oneofs_by_name[
    "performative"
]
DESCRIPTOR.message_types_by_name["FipaMessage"] = _FIPAMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FipaMessage = _reflection.GeneratedProtocolMessageType(
    "FipaMessage",
    (_message.Message,),
    dict(
        Description=_reflection.GeneratedProtocolMessageType(
            "Description",
            (_message.Message,),
            dict(
                DESCRIPTOR=_FIPAMESSAGE_DESCRIPTION,
                __module__="protocols.fipa.fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Description)
            ),
        ),
        Query=_reflection.GeneratedProtocolMessageType(
            "Query",
            (_message.Message,),
            dict(
                Nothing=_reflection.GeneratedProtocolMessageType(
                    "Nothing",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_FIPAMESSAGE_QUERY_NOTHING,
                        __module__="protocols.fipa.fipa_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Query.Nothing)
                    ),
                ),
                DESCRIPTOR=_FIPAMESSAGE_QUERY,
                __module__="protocols.fipa.fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Query)
            ),
        ),
        Cfp=_reflection.GeneratedProtocolMessageType(
            "Cfp",
            (_message.Message,),
            dict(
                DESCRIPTOR=_FIPAMESSAGE_CFP,
                __module__="protocols.fipa.fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Cfp)
            ),
        ),
        Propose=_reflection.GeneratedProtocolMessageType(
            "Propose",
            (_message.Message,),
            dict(
                DESCRIPTOR=_FIPAMESSAGE_PROPOSE,
                __module__="protocols.fipa.fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Propose)
            ),
        ),
        Accept_W_Inform=_reflection.GeneratedProtocolMessageType(
            "Accept_W_Inform",
            (_message.Message,),
            dict(
                InfoEntry=_reflection.GeneratedProtocolMessageType(
                    "InfoEntry",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_FIPAMESSAGE_ACCEPT_W_INFORM_INFOENTRY,
                        __module__="protocols.fipa.fipa_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Accept_W_Inform.InfoEntry)
                    ),
                ),
                DESCRIPTOR=_FIPAMESSAGE_ACCEPT_W_INFORM,
                __module__="protocols.fipa.fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Accept_W_Inform)
            ),
        ),
        Match_Accept_W_Inform=_reflection.GeneratedProtocolMessageType(
            "Match_Accept_W_Inform",
            (_message.Message,),
            dict(
                InfoEntry=_reflection.GeneratedProtocolMessageType(
                    "InfoEntry",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_INFOENTRY,
                        __module__="protocols.fipa.fipa_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform.InfoEntry)
                    ),
                ),
                DESCRIPTOR=_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM,
                __module__="protocols.fipa.fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform)
            ),
        ),
        Inform=_reflection.GeneratedProtocolMessageType(
            "Inform",
            (_message.Message,),
            dict(
                InfoEntry=_reflection.GeneratedProtocolMessageType(
                    "InfoEntry",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_FIPAMESSAGE_INFORM_INFOENTRY,
                        __module__="protocols.fipa.fipa_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Inform.InfoEntry)
                    ),
                ),
                DESCRIPTOR=_FIPAMESSAGE_INFORM,
                __module__="protocols.fipa.fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Inform)
            ),
        ),
        Accept=_reflection.GeneratedProtocolMessageType(
            "Accept",
            (_message.Message,),
            dict(
                DESCRIPTOR=_FIPAMESSAGE_ACCEPT,
                __module__="protocols.fipa.fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Accept)
            ),
        ),
        Decline=_reflection.GeneratedProtocolMessageType(
            "Decline",
            (_message.Message,),
            dict(
                DESCRIPTOR=_FIPAMESSAGE_DECLINE,
                __module__="protocols.fipa.fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Decline)
            ),
        ),
        Match_Accept=_reflection.GeneratedProtocolMessageType(
            "Match_Accept",
            (_message.Message,),
            dict(
                DESCRIPTOR=_FIPAMESSAGE_MATCH_ACCEPT,
                __module__="protocols.fipa.fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Match_Accept)
            ),
        ),
        DESCRIPTOR=_FIPAMESSAGE,
        __module__="protocols.fipa.fipa_pb2"
        # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage)
    ),
)
_sym_db.RegisterMessage(FipaMessage)
_sym_db.RegisterMessage(FipaMessage.Description)
_sym_db.RegisterMessage(FipaMessage.Query)
_sym_db.RegisterMessage(FipaMessage.Query.Nothing)
_sym_db.RegisterMessage(FipaMessage.Cfp)
_sym_db.RegisterMessage(FipaMessage.Propose)
_sym_db.RegisterMessage(FipaMessage.Accept_W_Inform)
_sym_db.RegisterMessage(FipaMessage.Accept_W_Inform.InfoEntry)
_sym_db.RegisterMessage(FipaMessage.Match_Accept_W_Inform)
_sym_db.RegisterMessage(FipaMessage.Match_Accept_W_Inform.InfoEntry)
_sym_db.RegisterMessage(FipaMessage.Inform)
_sym_db.RegisterMessage(FipaMessage.Inform.InfoEntry)
_sym_db.RegisterMessage(FipaMessage.Accept)
_sym_db.RegisterMessage(FipaMessage.Decline)
_sym_db.RegisterMessage(FipaMessage.Match_Accept)


_FIPAMESSAGE_ACCEPT_W_INFORM_INFOENTRY._options = None
_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_INFOENTRY._options = None
_FIPAMESSAGE_INFORM_INFOENTRY._options = None
# @@protoc_insertion_point(module_scope)
