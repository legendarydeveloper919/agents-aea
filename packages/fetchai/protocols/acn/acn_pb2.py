# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: acn.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="acn.proto",
    package="aea.aea.acn.v1_0_0",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\tacn.proto\x12\x12\x61\x65\x61.aea.acn.v1_0_0"\x92\x0b\n\nAcnMessage\x12P\n\x0c\x61\x65\x61_envelope\x18\x05 \x01(\x0b\x32\x38.aea.aea.acn.v1_0_0.AcnMessage.Aea_Envelope_PerformativeH\x00\x12T\n\x0elookup_request\x18\x06 \x01(\x0b\x32:.aea.aea.acn.v1_0_0.AcnMessage.Lookup_Request_PerformativeH\x00\x12V\n\x0flookup_response\x18\x07 \x01(\x0b\x32;.aea.aea.acn.v1_0_0.AcnMessage.Lookup_Response_PerformativeH\x00\x12H\n\x08register\x18\x08 \x01(\x0b\x32\x34.aea.aea.acn.v1_0_0.AcnMessage.Register_PerformativeH\x00\x12\x44\n\x06status\x18\t \x01(\x0b\x32\x32.aea.aea.acn.v1_0_0.AcnMessage.Status_PerformativeH\x00\x1a\xac\x01\n\x0b\x41gentRecord\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12\x11\n\tledger_id\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x12\n\npublic_key\x18\x04 \x01(\t\x12\x17\n\x0fpeer_public_key\x18\x05 \x01(\t\x12\x11\n\tsignature\x18\x06 \x01(\t\x12\x12\n\nnot_before\x18\x07 \x01(\t\x12\x11\n\tnot_after\x18\x08 \x01(\t\x1a\x92\x03\n\nStatusBody\x12\x46\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x38.aea.aea.acn.v1_0_0.AcnMessage.StatusBody.StatusCodeEnum\x12\x0c\n\x04msgs\x18\x02 \x03(\t"\xad\x02\n\x0eStatusCodeEnum\x12\x0b\n\x07SUCCESS\x10\x00\x12\x1d\n\x19\x45RROR_UNSUPPORTED_VERSION\x10\x01\x12\x1c\n\x18\x45RROR_UNEXPECTED_PAYLOAD\x10\x02\x12\x11\n\rERROR_GENERIC\x10\x03\x12\x10\n\x0c\x45RROR_DECODE\x10\x04\x12\x1d\n\x19\x45RROR_WRONG_AGENT_ADDRESS\x10\n\x12\x1a\n\x16\x45RROR_WRONG_PUBLIC_KEY\x10\x0b\x12\x17\n\x13\x45RROR_INVALID_PROOF\x10\x0c\x12\x1c\n\x18\x45RROR_UNSUPPORTED_LEDGER\x10\r\x12\x1f\n\x1b\x45RROR_UNKNOWN_AGENT_ADDRESS\x10\x14\x12\x19\n\x15\x45RROR_AGENT_NOT_READY\x10\x15\x1aS\n\x15Register_Performative\x12:\n\x06record\x18\x01 \x01(\x0b\x32*.aea.aea.acn.v1_0_0.AcnMessage.AgentRecord\x1a\x34\n\x1bLookup_Request_Performative\x12\x15\n\ragent_address\x18\x01 \x01(\t\x1aZ\n\x1cLookup_Response_Performative\x12:\n\x06record\x18\x01 \x01(\x0b\x32*.aea.aea.acn.v1_0_0.AcnMessage.AgentRecord\x1ai\n\x19\x41\x65\x61_Envelope_Performative\x12\x10\n\x08\x65nvelope\x18\x01 \x01(\x0c\x12:\n\x06record\x18\x02 \x01(\x0b\x32*.aea.aea.acn.v1_0_0.AcnMessage.AgentRecord\x1aN\n\x13Status_Performative\x12\x37\n\x04\x62ody\x18\x01 \x01(\x0b\x32).aea.aea.acn.v1_0_0.AcnMessage.StatusBodyB\x0e\n\x0cperformativeb\x06proto3',
)


_ACNMESSAGE_STATUSBODY_STATUSCODEENUM = _descriptor.EnumDescriptor(
    name="StatusCodeEnum",
    full_name="aea.aea.acn.v1_0_0.AcnMessage.StatusBody.StatusCodeEnum",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SUCCESS", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_UNSUPPORTED_VERSION",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_UNEXPECTED_PAYLOAD",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_GENERIC", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_DECODE", index=4, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_WRONG_AGENT_ADDRESS",
            index=5,
            number=10,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_WRONG_PUBLIC_KEY",
            index=6,
            number=11,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_INVALID_PROOF",
            index=7,
            number=12,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_UNSUPPORTED_LEDGER",
            index=8,
            number=13,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_UNKNOWN_AGENT_ADDRESS",
            index=9,
            number=20,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_AGENT_NOT_READY",
            index=10,
            number=21,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=725,
    serialized_end=1026,
)
_sym_db.RegisterEnumDescriptor(_ACNMESSAGE_STATUSBODY_STATUSCODEENUM)


_ACNMESSAGE_AGENTRECORD = _descriptor.Descriptor(
    name="AgentRecord",
    full_name="aea.aea.acn.v1_0_0.AcnMessage.AgentRecord",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="service_id",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.AgentRecord.service_id",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="ledger_id",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.AgentRecord.ledger_id",
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
        _descriptor.FieldDescriptor(
            name="address",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.AgentRecord.address",
            index=2,
            number=3,
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
        _descriptor.FieldDescriptor(
            name="public_key",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.AgentRecord.public_key",
            index=3,
            number=4,
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
        _descriptor.FieldDescriptor(
            name="peer_public_key",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.AgentRecord.peer_public_key",
            index=4,
            number=5,
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
        _descriptor.FieldDescriptor(
            name="signature",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.AgentRecord.signature",
            index=5,
            number=6,
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
        _descriptor.FieldDescriptor(
            name="not_before",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.AgentRecord.not_before",
            index=6,
            number=7,
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
        _descriptor.FieldDescriptor(
            name="not_after",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.AgentRecord.not_after",
            index=7,
            number=8,
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
    serialized_start=449,
    serialized_end=621,
)

_ACNMESSAGE_STATUSBODY = _descriptor.Descriptor(
    name="StatusBody",
    full_name="aea.aea.acn.v1_0_0.AcnMessage.StatusBody",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="code",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.StatusBody.code",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
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
            name="msgs",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.StatusBody.msgs",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
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
    nested_types=[],
    enum_types=[_ACNMESSAGE_STATUSBODY_STATUSCODEENUM,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=624,
    serialized_end=1026,
)

_ACNMESSAGE_REGISTER_PERFORMATIVE = _descriptor.Descriptor(
    name="Register_Performative",
    full_name="aea.aea.acn.v1_0_0.AcnMessage.Register_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="record",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.Register_Performative.record",
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
    serialized_start=1028,
    serialized_end=1111,
)

_ACNMESSAGE_LOOKUP_REQUEST_PERFORMATIVE = _descriptor.Descriptor(
    name="Lookup_Request_Performative",
    full_name="aea.aea.acn.v1_0_0.AcnMessage.Lookup_Request_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="agent_address",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.Lookup_Request_Performative.agent_address",
            index=0,
            number=1,
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
    serialized_start=1113,
    serialized_end=1165,
)

_ACNMESSAGE_LOOKUP_RESPONSE_PERFORMATIVE = _descriptor.Descriptor(
    name="Lookup_Response_Performative",
    full_name="aea.aea.acn.v1_0_0.AcnMessage.Lookup_Response_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="record",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.Lookup_Response_Performative.record",
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
    serialized_start=1167,
    serialized_end=1257,
)

_ACNMESSAGE_AEA_ENVELOPE_PERFORMATIVE = _descriptor.Descriptor(
    name="Aea_Envelope_Performative",
    full_name="aea.aea.acn.v1_0_0.AcnMessage.Aea_Envelope_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="envelope",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.Aea_Envelope_Performative.envelope",
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
        _descriptor.FieldDescriptor(
            name="record",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.Aea_Envelope_Performative.record",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1259,
    serialized_end=1364,
)

_ACNMESSAGE_STATUS_PERFORMATIVE = _descriptor.Descriptor(
    name="Status_Performative",
    full_name="aea.aea.acn.v1_0_0.AcnMessage.Status_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="body",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.Status_Performative.body",
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
    serialized_start=1366,
    serialized_end=1444,
)

_ACNMESSAGE = _descriptor.Descriptor(
    name="AcnMessage",
    full_name="aea.aea.acn.v1_0_0.AcnMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="aea_envelope",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.aea_envelope",
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
            name="lookup_request",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.lookup_request",
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
            name="lookup_response",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.lookup_response",
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
            name="register",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.register",
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
        _descriptor.FieldDescriptor(
            name="status",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.status",
            index=4,
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
    ],
    extensions=[],
    nested_types=[
        _ACNMESSAGE_AGENTRECORD,
        _ACNMESSAGE_STATUSBODY,
        _ACNMESSAGE_REGISTER_PERFORMATIVE,
        _ACNMESSAGE_LOOKUP_REQUEST_PERFORMATIVE,
        _ACNMESSAGE_LOOKUP_RESPONSE_PERFORMATIVE,
        _ACNMESSAGE_AEA_ENVELOPE_PERFORMATIVE,
        _ACNMESSAGE_STATUS_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="aea.aea.acn.v1_0_0.AcnMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=34,
    serialized_end=1460,
)

_ACNMESSAGE_AGENTRECORD.containing_type = _ACNMESSAGE
_ACNMESSAGE_STATUSBODY.fields_by_name[
    "code"
].enum_type = _ACNMESSAGE_STATUSBODY_STATUSCODEENUM
_ACNMESSAGE_STATUSBODY.containing_type = _ACNMESSAGE
_ACNMESSAGE_STATUSBODY_STATUSCODEENUM.containing_type = _ACNMESSAGE_STATUSBODY
_ACNMESSAGE_REGISTER_PERFORMATIVE.fields_by_name[
    "record"
].message_type = _ACNMESSAGE_AGENTRECORD
_ACNMESSAGE_REGISTER_PERFORMATIVE.containing_type = _ACNMESSAGE
_ACNMESSAGE_LOOKUP_REQUEST_PERFORMATIVE.containing_type = _ACNMESSAGE
_ACNMESSAGE_LOOKUP_RESPONSE_PERFORMATIVE.fields_by_name[
    "record"
].message_type = _ACNMESSAGE_AGENTRECORD
_ACNMESSAGE_LOOKUP_RESPONSE_PERFORMATIVE.containing_type = _ACNMESSAGE
_ACNMESSAGE_AEA_ENVELOPE_PERFORMATIVE.fields_by_name[
    "record"
].message_type = _ACNMESSAGE_AGENTRECORD
_ACNMESSAGE_AEA_ENVELOPE_PERFORMATIVE.containing_type = _ACNMESSAGE
_ACNMESSAGE_STATUS_PERFORMATIVE.fields_by_name[
    "body"
].message_type = _ACNMESSAGE_STATUSBODY
_ACNMESSAGE_STATUS_PERFORMATIVE.containing_type = _ACNMESSAGE
_ACNMESSAGE.fields_by_name[
    "aea_envelope"
].message_type = _ACNMESSAGE_AEA_ENVELOPE_PERFORMATIVE
_ACNMESSAGE.fields_by_name[
    "lookup_request"
].message_type = _ACNMESSAGE_LOOKUP_REQUEST_PERFORMATIVE
_ACNMESSAGE.fields_by_name[
    "lookup_response"
].message_type = _ACNMESSAGE_LOOKUP_RESPONSE_PERFORMATIVE
_ACNMESSAGE.fields_by_name["register"].message_type = _ACNMESSAGE_REGISTER_PERFORMATIVE
_ACNMESSAGE.fields_by_name["status"].message_type = _ACNMESSAGE_STATUS_PERFORMATIVE
_ACNMESSAGE.oneofs_by_name["performative"].fields.append(
    _ACNMESSAGE.fields_by_name["aea_envelope"]
)
_ACNMESSAGE.fields_by_name[
    "aea_envelope"
].containing_oneof = _ACNMESSAGE.oneofs_by_name["performative"]
_ACNMESSAGE.oneofs_by_name["performative"].fields.append(
    _ACNMESSAGE.fields_by_name["lookup_request"]
)
_ACNMESSAGE.fields_by_name[
    "lookup_request"
].containing_oneof = _ACNMESSAGE.oneofs_by_name["performative"]
_ACNMESSAGE.oneofs_by_name["performative"].fields.append(
    _ACNMESSAGE.fields_by_name["lookup_response"]
)
_ACNMESSAGE.fields_by_name[
    "lookup_response"
].containing_oneof = _ACNMESSAGE.oneofs_by_name["performative"]
_ACNMESSAGE.oneofs_by_name["performative"].fields.append(
    _ACNMESSAGE.fields_by_name["register"]
)
_ACNMESSAGE.fields_by_name["register"].containing_oneof = _ACNMESSAGE.oneofs_by_name[
    "performative"
]
_ACNMESSAGE.oneofs_by_name["performative"].fields.append(
    _ACNMESSAGE.fields_by_name["status"]
)
_ACNMESSAGE.fields_by_name["status"].containing_oneof = _ACNMESSAGE.oneofs_by_name[
    "performative"
]
DESCRIPTOR.message_types_by_name["AcnMessage"] = _ACNMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AcnMessage = _reflection.GeneratedProtocolMessageType(
    "AcnMessage",
    (_message.Message,),
    {
        "AgentRecord": _reflection.GeneratedProtocolMessageType(
            "AgentRecord",
            (_message.Message,),
            {
                "DESCRIPTOR": _ACNMESSAGE_AGENTRECORD,
                "__module__": "acn_pb2"
                # @@protoc_insertion_point(class_scope:aea.aea.acn.v1_0_0.AcnMessage.AgentRecord)
            },
        ),
        "StatusBody": _reflection.GeneratedProtocolMessageType(
            "StatusBody",
            (_message.Message,),
            {
                "DESCRIPTOR": _ACNMESSAGE_STATUSBODY,
                "__module__": "acn_pb2"
                # @@protoc_insertion_point(class_scope:aea.aea.acn.v1_0_0.AcnMessage.StatusBody)
            },
        ),
        "Register_Performative": _reflection.GeneratedProtocolMessageType(
            "Register_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _ACNMESSAGE_REGISTER_PERFORMATIVE,
                "__module__": "acn_pb2"
                # @@protoc_insertion_point(class_scope:aea.aea.acn.v1_0_0.AcnMessage.Register_Performative)
            },
        ),
        "Lookup_Request_Performative": _reflection.GeneratedProtocolMessageType(
            "Lookup_Request_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _ACNMESSAGE_LOOKUP_REQUEST_PERFORMATIVE,
                "__module__": "acn_pb2"
                # @@protoc_insertion_point(class_scope:aea.aea.acn.v1_0_0.AcnMessage.Lookup_Request_Performative)
            },
        ),
        "Lookup_Response_Performative": _reflection.GeneratedProtocolMessageType(
            "Lookup_Response_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _ACNMESSAGE_LOOKUP_RESPONSE_PERFORMATIVE,
                "__module__": "acn_pb2"
                # @@protoc_insertion_point(class_scope:aea.aea.acn.v1_0_0.AcnMessage.Lookup_Response_Performative)
            },
        ),
        "Aea_Envelope_Performative": _reflection.GeneratedProtocolMessageType(
            "Aea_Envelope_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _ACNMESSAGE_AEA_ENVELOPE_PERFORMATIVE,
                "__module__": "acn_pb2"
                # @@protoc_insertion_point(class_scope:aea.aea.acn.v1_0_0.AcnMessage.Aea_Envelope_Performative)
            },
        ),
        "Status_Performative": _reflection.GeneratedProtocolMessageType(
            "Status_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _ACNMESSAGE_STATUS_PERFORMATIVE,
                "__module__": "acn_pb2"
                # @@protoc_insertion_point(class_scope:aea.aea.acn.v1_0_0.AcnMessage.Status_Performative)
            },
        ),
        "DESCRIPTOR": _ACNMESSAGE,
        "__module__": "acn_pb2"
        # @@protoc_insertion_point(class_scope:aea.aea.acn.v1_0_0.AcnMessage)
    },
)
_sym_db.RegisterMessage(AcnMessage)
_sym_db.RegisterMessage(AcnMessage.AgentRecord)
_sym_db.RegisterMessage(AcnMessage.StatusBody)
_sym_db.RegisterMessage(AcnMessage.Register_Performative)
_sym_db.RegisterMessage(AcnMessage.Lookup_Request_Performative)
_sym_db.RegisterMessage(AcnMessage.Lookup_Response_Performative)
_sym_db.RegisterMessage(AcnMessage.Aea_Envelope_Performative)
_sym_db.RegisterMessage(AcnMessage.Status_Performative)


# @@protoc_insertion_point(module_scope)
