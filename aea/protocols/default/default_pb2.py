# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: default.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="default.proto",
    package="fetch.aea.Default",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\rdefault.proto\x12\x11\x66\x65tch.aea.Default"\x97\x06\n\x0e\x44\x65\x66\x61ultMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12"\n\x1a\x64ialogue_starter_reference\x18\x02 \x01(\t\x12$\n\x1c\x64ialogue_responder_reference\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\x05\x12\x45\n\x05\x62ytes\x18\x05 \x01(\x0b\x32\x34.fetch.aea.Default.DefaultMessage.Bytes_PerformativeH\x00\x12\x45\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x34.fetch.aea.Default.DefaultMessage.Error_PerformativeH\x00\x1a\xdb\x01\n\tErrorCode\x12M\n\nerror_code\x18\x01 \x01(\x0e\x32\x39.fetch.aea.Default.DefaultMessage.ErrorCode.ErrorCodeEnum"\x7f\n\rErrorCodeEnum\x12\x18\n\x14UNSUPPORTED_PROTOCOL\x10\x00\x12\x12\n\x0e\x44\x45\x43ODING_ERROR\x10\x01\x12\x13\n\x0fINVALID_MESSAGE\x10\x02\x12\x15\n\x11UNSUPPORTED_SKILL\x10\x03\x12\x14\n\x10INVALID_DIALOGUE\x10\x04\x1a%\n\x12\x42ytes_Performative\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x1a\xf3\x01\n\x12\x45rror_Performative\x12?\n\nerror_code\x18\x01 \x01(\x0b\x32+.fetch.aea.Default.DefaultMessage.ErrorCode\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12W\n\nerror_data\x18\x03 \x03(\x0b\x32\x43.fetch.aea.Default.DefaultMessage.Error_Performative.ErrorDataEntry\x1a\x30\n\x0e\x45rrorDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x42\x0e\n\x0cperformativeb\x06proto3'
    ),
)


_DEFAULTMESSAGE_ERRORCODE_ERRORCODEENUM = _descriptor.EnumDescriptor(
    name="ErrorCodeEnum",
    full_name="fetch.aea.Default.DefaultMessage.ErrorCode.ErrorCodeEnum",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="UNSUPPORTED_PROTOCOL",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="DECODING_ERROR", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INVALID_MESSAGE",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="UNSUPPORTED_SKILL",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="INVALID_DIALOGUE",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=400,
    serialized_end=527,
)
_sym_db.RegisterEnumDescriptor(_DEFAULTMESSAGE_ERRORCODE_ERRORCODEENUM)


_DEFAULTMESSAGE_ERRORCODE = _descriptor.Descriptor(
    name="ErrorCode",
    full_name="fetch.aea.Default.DefaultMessage.ErrorCode",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="error_code",
            full_name="fetch.aea.Default.DefaultMessage.ErrorCode.error_code",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_DEFAULTMESSAGE_ERRORCODE_ERRORCODEENUM,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=308,
    serialized_end=527,
)

_DEFAULTMESSAGE_BYTES_PERFORMATIVE = _descriptor.Descriptor(
    name="Bytes_Performative",
    full_name="fetch.aea.Default.DefaultMessage.Bytes_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="content",
            full_name="fetch.aea.Default.DefaultMessage.Bytes_Performative.content",
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
    serialized_start=529,
    serialized_end=566,
)

_DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY = _descriptor.Descriptor(
    name="ErrorDataEntry",
    full_name="fetch.aea.Default.DefaultMessage.Error_Performative.ErrorDataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.Default.DefaultMessage.Error_Performative.ErrorDataEntry.key",
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
            full_name="fetch.aea.Default.DefaultMessage.Error_Performative.ErrorDataEntry.value",
            index=1,
            number=2,
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
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=764,
    serialized_end=812,
)

_DEFAULTMESSAGE_ERROR_PERFORMATIVE = _descriptor.Descriptor(
    name="Error_Performative",
    full_name="fetch.aea.Default.DefaultMessage.Error_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="error_code",
            full_name="fetch.aea.Default.DefaultMessage.Error_Performative.error_code",
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
            name="error_msg",
            full_name="fetch.aea.Default.DefaultMessage.Error_Performative.error_msg",
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
            name="error_data",
            full_name="fetch.aea.Default.DefaultMessage.Error_Performative.error_data",
            index=2,
            number=3,
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
    nested_types=[_DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=569,
    serialized_end=812,
)

_DEFAULTMESSAGE = _descriptor.Descriptor(
    name="DefaultMessage",
    full_name="fetch.aea.Default.DefaultMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="message_id",
            full_name="fetch.aea.Default.DefaultMessage.message_id",
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
            full_name="fetch.aea.Default.DefaultMessage.dialogue_starter_reference",
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
            full_name="fetch.aea.Default.DefaultMessage.dialogue_responder_reference",
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
            full_name="fetch.aea.Default.DefaultMessage.target",
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
            name="bytes",
            full_name="fetch.aea.Default.DefaultMessage.bytes",
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
            name="error",
            full_name="fetch.aea.Default.DefaultMessage.error",
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
    ],
    extensions=[],
    nested_types=[
        _DEFAULTMESSAGE_ERRORCODE,
        _DEFAULTMESSAGE_BYTES_PERFORMATIVE,
        _DEFAULTMESSAGE_ERROR_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="fetch.aea.Default.DefaultMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=37,
    serialized_end=828,
)

_DEFAULTMESSAGE_ERRORCODE.fields_by_name[
    "error_code"
].enum_type = _DEFAULTMESSAGE_ERRORCODE_ERRORCODEENUM
_DEFAULTMESSAGE_ERRORCODE.containing_type = _DEFAULTMESSAGE
_DEFAULTMESSAGE_ERRORCODE_ERRORCODEENUM.containing_type = _DEFAULTMESSAGE_ERRORCODE
_DEFAULTMESSAGE_BYTES_PERFORMATIVE.containing_type = _DEFAULTMESSAGE
_DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY.containing_type = (
    _DEFAULTMESSAGE_ERROR_PERFORMATIVE
)
_DEFAULTMESSAGE_ERROR_PERFORMATIVE.fields_by_name[
    "error_code"
].message_type = _DEFAULTMESSAGE_ERRORCODE
_DEFAULTMESSAGE_ERROR_PERFORMATIVE.fields_by_name[
    "error_data"
].message_type = _DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY
_DEFAULTMESSAGE_ERROR_PERFORMATIVE.containing_type = _DEFAULTMESSAGE
_DEFAULTMESSAGE.fields_by_name[
    "bytes"
].message_type = _DEFAULTMESSAGE_BYTES_PERFORMATIVE
_DEFAULTMESSAGE.fields_by_name[
    "error"
].message_type = _DEFAULTMESSAGE_ERROR_PERFORMATIVE
_DEFAULTMESSAGE.oneofs_by_name["performative"].fields.append(
    _DEFAULTMESSAGE.fields_by_name["bytes"]
)
_DEFAULTMESSAGE.fields_by_name[
    "bytes"
].containing_oneof = _DEFAULTMESSAGE.oneofs_by_name["performative"]
_DEFAULTMESSAGE.oneofs_by_name["performative"].fields.append(
    _DEFAULTMESSAGE.fields_by_name["error"]
)
_DEFAULTMESSAGE.fields_by_name[
    "error"
].containing_oneof = _DEFAULTMESSAGE.oneofs_by_name["performative"]
DESCRIPTOR.message_types_by_name["DefaultMessage"] = _DEFAULTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DefaultMessage = _reflection.GeneratedProtocolMessageType(
    "DefaultMessage",
    (_message.Message,),
    dict(
        ErrorCode=_reflection.GeneratedProtocolMessageType(
            "ErrorCode",
            (_message.Message,),
            dict(
                DESCRIPTOR=_DEFAULTMESSAGE_ERRORCODE,
                __module__="default_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Default.DefaultMessage.ErrorCode)
            ),
        ),
        Bytes_Performative=_reflection.GeneratedProtocolMessageType(
            "Bytes_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_DEFAULTMESSAGE_BYTES_PERFORMATIVE,
                __module__="default_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Default.DefaultMessage.Bytes_Performative)
            ),
        ),
        Error_Performative=_reflection.GeneratedProtocolMessageType(
            "Error_Performative",
            (_message.Message,),
            dict(
                ErrorDataEntry=_reflection.GeneratedProtocolMessageType(
                    "ErrorDataEntry",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY,
                        __module__="default_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.Default.DefaultMessage.Error_Performative.ErrorDataEntry)
                    ),
                ),
                DESCRIPTOR=_DEFAULTMESSAGE_ERROR_PERFORMATIVE,
                __module__="default_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Default.DefaultMessage.Error_Performative)
            ),
        ),
        DESCRIPTOR=_DEFAULTMESSAGE,
        __module__="default_pb2"
        # @@protoc_insertion_point(class_scope:fetch.aea.Default.DefaultMessage)
    ),
)
_sym_db.RegisterMessage(DefaultMessage)
_sym_db.RegisterMessage(DefaultMessage.ErrorCode)
_sym_db.RegisterMessage(DefaultMessage.Bytes_Performative)
_sym_db.RegisterMessage(DefaultMessage.Error_Performative)
_sym_db.RegisterMessage(DefaultMessage.Error_Performative.ErrorDataEntry)


_DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
