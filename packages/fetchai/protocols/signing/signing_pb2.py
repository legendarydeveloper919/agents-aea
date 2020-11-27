# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: signing.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="signing.proto",
    package="aea.fetchai.signing",
    syntax="proto3",
    serialized_pb=_b(
        '\n\rsigning.proto\x12\x13\x61\x65\x61.fetchai.signing"\xd4\x0b\n\x0eSigningMessage\x12G\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x36.aea.fetchai.signing.SigningMessage.Error_PerformativeH\x00\x12U\n\x0csign_message\x18\x06 \x01(\x0b\x32=.aea.fetchai.signing.SigningMessage.Sign_Message_PerformativeH\x00\x12]\n\x10sign_transaction\x18\x07 \x01(\x0b\x32\x41.aea.fetchai.signing.SigningMessage.Sign_Transaction_PerformativeH\x00\x12Y\n\x0esigned_message\x18\x08 \x01(\x0b\x32?.aea.fetchai.signing.SigningMessage.Signed_Message_PerformativeH\x00\x12\x61\n\x12signed_transaction\x18\t \x01(\x0b\x32\x43.aea.fetchai.signing.SigningMessage.Signed_Transaction_PerformativeH\x00\x1a\xb5\x01\n\tErrorCode\x12O\n\nerror_code\x18\x01 \x01(\x0e\x32;.aea.fetchai.signing.SigningMessage.ErrorCode.ErrorCodeEnum"W\n\rErrorCodeEnum\x12 \n\x1cUNSUCCESSFUL_MESSAGE_SIGNING\x10\x00\x12$\n UNSUCCESSFUL_TRANSACTION_SIGNING\x10\x01\x1a!\n\nRawMessage\x12\x13\n\x0braw_message\x18\x01 \x01(\x0c\x1a)\n\x0eRawTransaction\x12\x17\n\x0fraw_transaction\x18\x01 \x01(\x0c\x1a\'\n\rSignedMessage\x12\x16\n\x0esigned_message\x18\x01 \x01(\x0c\x1a/\n\x11SignedTransaction\x12\x1a\n\x12signed_transaction\x18\x01 \x01(\x0c\x1a\x16\n\x05Terms\x12\r\n\x05terms\x18\x01 \x01(\x0c\x1a\xa6\x01\n\x1dSign_Transaction_Performative\x12\x38\n\x05terms\x18\x01 \x01(\x0b\x32).aea.fetchai.signing.SigningMessage.Terms\x12K\n\x0fraw_transaction\x18\x02 \x01(\x0b\x32\x32.aea.fetchai.signing.SigningMessage.RawTransaction\x1a\x9a\x01\n\x19Sign_Message_Performative\x12\x38\n\x05terms\x18\x01 \x01(\x0b\x32).aea.fetchai.signing.SigningMessage.Terms\x12\x43\n\x0braw_message\x18\x02 \x01(\x0b\x32..aea.fetchai.signing.SigningMessage.RawMessage\x1at\n\x1fSigned_Transaction_Performative\x12Q\n\x12signed_transaction\x18\x01 \x01(\x0b\x32\x35.aea.fetchai.signing.SigningMessage.SignedTransaction\x1ah\n\x1bSigned_Message_Performative\x12I\n\x0esigned_message\x18\x01 \x01(\x0b\x32\x31.aea.fetchai.signing.SigningMessage.SignedMessage\x1aW\n\x12\x45rror_Performative\x12\x41\n\nerror_code\x18\x01 \x01(\x0b\x32-.aea.fetchai.signing.SigningMessage.ErrorCodeB\x0e\n\x0cperformativeb\x06proto3'
    ),
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


_SIGNINGMESSAGE_ERRORCODE_ERRORCODEENUM = _descriptor.EnumDescriptor(
    name="ErrorCodeEnum",
    full_name="aea.fetchai.signing.SigningMessage.ErrorCode.ErrorCodeEnum",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="UNSUCCESSFUL_MESSAGE_SIGNING",
            index=0,
            number=0,
            options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="UNSUCCESSFUL_TRANSACTION_SIGNING",
            index=1,
            number=1,
            options=None,
            type=None,
        ),
    ],
    containing_type=None,
    options=None,
    serialized_start=597,
    serialized_end=684,
)
_sym_db.RegisterEnumDescriptor(_SIGNINGMESSAGE_ERRORCODE_ERRORCODEENUM)


_SIGNINGMESSAGE_ERRORCODE = _descriptor.Descriptor(
    name="ErrorCode",
    full_name="aea.fetchai.signing.SigningMessage.ErrorCode",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="error_code",
            full_name="aea.fetchai.signing.SigningMessage.ErrorCode.error_code",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_SIGNINGMESSAGE_ERRORCODE_ERRORCODEENUM,],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=503,
    serialized_end=684,
)

_SIGNINGMESSAGE_RAWMESSAGE = _descriptor.Descriptor(
    name="RawMessage",
    full_name="aea.fetchai.signing.SigningMessage.RawMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="raw_message",
            full_name="aea.fetchai.signing.SigningMessage.RawMessage.raw_message",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=686,
    serialized_end=719,
)

_SIGNINGMESSAGE_RAWTRANSACTION = _descriptor.Descriptor(
    name="RawTransaction",
    full_name="aea.fetchai.signing.SigningMessage.RawTransaction",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="raw_transaction",
            full_name="aea.fetchai.signing.SigningMessage.RawTransaction.raw_transaction",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=721,
    serialized_end=762,
)

_SIGNINGMESSAGE_SIGNEDMESSAGE = _descriptor.Descriptor(
    name="SignedMessage",
    full_name="aea.fetchai.signing.SigningMessage.SignedMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="signed_message",
            full_name="aea.fetchai.signing.SigningMessage.SignedMessage.signed_message",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=764,
    serialized_end=803,
)

_SIGNINGMESSAGE_SIGNEDTRANSACTION = _descriptor.Descriptor(
    name="SignedTransaction",
    full_name="aea.fetchai.signing.SigningMessage.SignedTransaction",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="signed_transaction",
            full_name="aea.fetchai.signing.SigningMessage.SignedTransaction.signed_transaction",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=805,
    serialized_end=852,
)

_SIGNINGMESSAGE_TERMS = _descriptor.Descriptor(
    name="Terms",
    full_name="aea.fetchai.signing.SigningMessage.Terms",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="aea.fetchai.signing.SigningMessage.Terms.terms",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=854,
    serialized_end=876,
)

_SIGNINGMESSAGE_SIGN_TRANSACTION_PERFORMATIVE = _descriptor.Descriptor(
    name="Sign_Transaction_Performative",
    full_name="aea.fetchai.signing.SigningMessage.Sign_Transaction_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="aea.fetchai.signing.SigningMessage.Sign_Transaction_Performative.terms",
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="raw_transaction",
            full_name="aea.fetchai.signing.SigningMessage.Sign_Transaction_Performative.raw_transaction",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=879,
    serialized_end=1045,
)

_SIGNINGMESSAGE_SIGN_MESSAGE_PERFORMATIVE = _descriptor.Descriptor(
    name="Sign_Message_Performative",
    full_name="aea.fetchai.signing.SigningMessage.Sign_Message_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="terms",
            full_name="aea.fetchai.signing.SigningMessage.Sign_Message_Performative.terms",
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="raw_message",
            full_name="aea.fetchai.signing.SigningMessage.Sign_Message_Performative.raw_message",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1048,
    serialized_end=1202,
)

_SIGNINGMESSAGE_SIGNED_TRANSACTION_PERFORMATIVE = _descriptor.Descriptor(
    name="Signed_Transaction_Performative",
    full_name="aea.fetchai.signing.SigningMessage.Signed_Transaction_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="signed_transaction",
            full_name="aea.fetchai.signing.SigningMessage.Signed_Transaction_Performative.signed_transaction",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1204,
    serialized_end=1320,
)

_SIGNINGMESSAGE_SIGNED_MESSAGE_PERFORMATIVE = _descriptor.Descriptor(
    name="Signed_Message_Performative",
    full_name="aea.fetchai.signing.SigningMessage.Signed_Message_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="signed_message",
            full_name="aea.fetchai.signing.SigningMessage.Signed_Message_Performative.signed_message",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1322,
    serialized_end=1426,
)

_SIGNINGMESSAGE_ERROR_PERFORMATIVE = _descriptor.Descriptor(
    name="Error_Performative",
    full_name="aea.fetchai.signing.SigningMessage.Error_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="error_code",
            full_name="aea.fetchai.signing.SigningMessage.Error_Performative.error_code",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1428,
    serialized_end=1515,
)

_SIGNINGMESSAGE = _descriptor.Descriptor(
    name="SigningMessage",
    full_name="aea.fetchai.signing.SigningMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="error",
            full_name="aea.fetchai.signing.SigningMessage.error",
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="sign_message",
            full_name="aea.fetchai.signing.SigningMessage.sign_message",
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="sign_transaction",
            full_name="aea.fetchai.signing.SigningMessage.sign_transaction",
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="signed_message",
            full_name="aea.fetchai.signing.SigningMessage.signed_message",
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="signed_transaction",
            full_name="aea.fetchai.signing.SigningMessage.signed_transaction",
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
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[
        _SIGNINGMESSAGE_ERRORCODE,
        _SIGNINGMESSAGE_RAWMESSAGE,
        _SIGNINGMESSAGE_RAWTRANSACTION,
        _SIGNINGMESSAGE_SIGNEDMESSAGE,
        _SIGNINGMESSAGE_SIGNEDTRANSACTION,
        _SIGNINGMESSAGE_TERMS,
        _SIGNINGMESSAGE_SIGN_TRANSACTION_PERFORMATIVE,
        _SIGNINGMESSAGE_SIGN_MESSAGE_PERFORMATIVE,
        _SIGNINGMESSAGE_SIGNED_TRANSACTION_PERFORMATIVE,
        _SIGNINGMESSAGE_SIGNED_MESSAGE_PERFORMATIVE,
        _SIGNINGMESSAGE_ERROR_PERFORMATIVE,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="aea.fetchai.signing.SigningMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=39,
    serialized_end=1531,
)

_SIGNINGMESSAGE_ERRORCODE.fields_by_name[
    "error_code"
].enum_type = _SIGNINGMESSAGE_ERRORCODE_ERRORCODEENUM
_SIGNINGMESSAGE_ERRORCODE.containing_type = _SIGNINGMESSAGE
_SIGNINGMESSAGE_ERRORCODE_ERRORCODEENUM.containing_type = _SIGNINGMESSAGE_ERRORCODE
_SIGNINGMESSAGE_RAWMESSAGE.containing_type = _SIGNINGMESSAGE
_SIGNINGMESSAGE_RAWTRANSACTION.containing_type = _SIGNINGMESSAGE
_SIGNINGMESSAGE_SIGNEDMESSAGE.containing_type = _SIGNINGMESSAGE
_SIGNINGMESSAGE_SIGNEDTRANSACTION.containing_type = _SIGNINGMESSAGE
_SIGNINGMESSAGE_TERMS.containing_type = _SIGNINGMESSAGE
_SIGNINGMESSAGE_SIGN_TRANSACTION_PERFORMATIVE.fields_by_name[
    "terms"
].message_type = _SIGNINGMESSAGE_TERMS
_SIGNINGMESSAGE_SIGN_TRANSACTION_PERFORMATIVE.fields_by_name[
    "raw_transaction"
].message_type = _SIGNINGMESSAGE_RAWTRANSACTION
_SIGNINGMESSAGE_SIGN_TRANSACTION_PERFORMATIVE.containing_type = _SIGNINGMESSAGE
_SIGNINGMESSAGE_SIGN_MESSAGE_PERFORMATIVE.fields_by_name[
    "terms"
].message_type = _SIGNINGMESSAGE_TERMS
_SIGNINGMESSAGE_SIGN_MESSAGE_PERFORMATIVE.fields_by_name[
    "raw_message"
].message_type = _SIGNINGMESSAGE_RAWMESSAGE
_SIGNINGMESSAGE_SIGN_MESSAGE_PERFORMATIVE.containing_type = _SIGNINGMESSAGE
_SIGNINGMESSAGE_SIGNED_TRANSACTION_PERFORMATIVE.fields_by_name[
    "signed_transaction"
].message_type = _SIGNINGMESSAGE_SIGNEDTRANSACTION
_SIGNINGMESSAGE_SIGNED_TRANSACTION_PERFORMATIVE.containing_type = _SIGNINGMESSAGE
_SIGNINGMESSAGE_SIGNED_MESSAGE_PERFORMATIVE.fields_by_name[
    "signed_message"
].message_type = _SIGNINGMESSAGE_SIGNEDMESSAGE
_SIGNINGMESSAGE_SIGNED_MESSAGE_PERFORMATIVE.containing_type = _SIGNINGMESSAGE
_SIGNINGMESSAGE_ERROR_PERFORMATIVE.fields_by_name[
    "error_code"
].message_type = _SIGNINGMESSAGE_ERRORCODE
_SIGNINGMESSAGE_ERROR_PERFORMATIVE.containing_type = _SIGNINGMESSAGE
_SIGNINGMESSAGE.fields_by_name[
    "error"
].message_type = _SIGNINGMESSAGE_ERROR_PERFORMATIVE
_SIGNINGMESSAGE.fields_by_name[
    "sign_message"
].message_type = _SIGNINGMESSAGE_SIGN_MESSAGE_PERFORMATIVE
_SIGNINGMESSAGE.fields_by_name[
    "sign_transaction"
].message_type = _SIGNINGMESSAGE_SIGN_TRANSACTION_PERFORMATIVE
_SIGNINGMESSAGE.fields_by_name[
    "signed_message"
].message_type = _SIGNINGMESSAGE_SIGNED_MESSAGE_PERFORMATIVE
_SIGNINGMESSAGE.fields_by_name[
    "signed_transaction"
].message_type = _SIGNINGMESSAGE_SIGNED_TRANSACTION_PERFORMATIVE
_SIGNINGMESSAGE.oneofs_by_name["performative"].fields.append(
    _SIGNINGMESSAGE.fields_by_name["error"]
)
_SIGNINGMESSAGE.fields_by_name[
    "error"
].containing_oneof = _SIGNINGMESSAGE.oneofs_by_name["performative"]
_SIGNINGMESSAGE.oneofs_by_name["performative"].fields.append(
    _SIGNINGMESSAGE.fields_by_name["sign_message"]
)
_SIGNINGMESSAGE.fields_by_name[
    "sign_message"
].containing_oneof = _SIGNINGMESSAGE.oneofs_by_name["performative"]
_SIGNINGMESSAGE.oneofs_by_name["performative"].fields.append(
    _SIGNINGMESSAGE.fields_by_name["sign_transaction"]
)
_SIGNINGMESSAGE.fields_by_name[
    "sign_transaction"
].containing_oneof = _SIGNINGMESSAGE.oneofs_by_name["performative"]
_SIGNINGMESSAGE.oneofs_by_name["performative"].fields.append(
    _SIGNINGMESSAGE.fields_by_name["signed_message"]
)
_SIGNINGMESSAGE.fields_by_name[
    "signed_message"
].containing_oneof = _SIGNINGMESSAGE.oneofs_by_name["performative"]
_SIGNINGMESSAGE.oneofs_by_name["performative"].fields.append(
    _SIGNINGMESSAGE.fields_by_name["signed_transaction"]
)
_SIGNINGMESSAGE.fields_by_name[
    "signed_transaction"
].containing_oneof = _SIGNINGMESSAGE.oneofs_by_name["performative"]
DESCRIPTOR.message_types_by_name["SigningMessage"] = _SIGNINGMESSAGE

SigningMessage = _reflection.GeneratedProtocolMessageType(
    "SigningMessage",
    (_message.Message,),
    dict(
        ErrorCode=_reflection.GeneratedProtocolMessageType(
            "ErrorCode",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNINGMESSAGE_ERRORCODE,
                __module__="signing_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage.ErrorCode)
            ),
        ),
        RawMessage=_reflection.GeneratedProtocolMessageType(
            "RawMessage",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNINGMESSAGE_RAWMESSAGE,
                __module__="signing_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage.RawMessage)
            ),
        ),
        RawTransaction=_reflection.GeneratedProtocolMessageType(
            "RawTransaction",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNINGMESSAGE_RAWTRANSACTION,
                __module__="signing_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage.RawTransaction)
            ),
        ),
        SignedMessage=_reflection.GeneratedProtocolMessageType(
            "SignedMessage",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNINGMESSAGE_SIGNEDMESSAGE,
                __module__="signing_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage.SignedMessage)
            ),
        ),
        SignedTransaction=_reflection.GeneratedProtocolMessageType(
            "SignedTransaction",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNINGMESSAGE_SIGNEDTRANSACTION,
                __module__="signing_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage.SignedTransaction)
            ),
        ),
        Terms=_reflection.GeneratedProtocolMessageType(
            "Terms",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNINGMESSAGE_TERMS,
                __module__="signing_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage.Terms)
            ),
        ),
        Sign_Transaction_Performative=_reflection.GeneratedProtocolMessageType(
            "Sign_Transaction_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNINGMESSAGE_SIGN_TRANSACTION_PERFORMATIVE,
                __module__="signing_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage.Sign_Transaction_Performative)
            ),
        ),
        Sign_Message_Performative=_reflection.GeneratedProtocolMessageType(
            "Sign_Message_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNINGMESSAGE_SIGN_MESSAGE_PERFORMATIVE,
                __module__="signing_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage.Sign_Message_Performative)
            ),
        ),
        Signed_Transaction_Performative=_reflection.GeneratedProtocolMessageType(
            "Signed_Transaction_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNINGMESSAGE_SIGNED_TRANSACTION_PERFORMATIVE,
                __module__="signing_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage.Signed_Transaction_Performative)
            ),
        ),
        Signed_Message_Performative=_reflection.GeneratedProtocolMessageType(
            "Signed_Message_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNINGMESSAGE_SIGNED_MESSAGE_PERFORMATIVE,
                __module__="signing_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage.Signed_Message_Performative)
            ),
        ),
        Error_Performative=_reflection.GeneratedProtocolMessageType(
            "Error_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNINGMESSAGE_ERROR_PERFORMATIVE,
                __module__="signing_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage.Error_Performative)
            ),
        ),
        DESCRIPTOR=_SIGNINGMESSAGE,
        __module__="signing_pb2"
        # @@protoc_insertion_point(class_scope:aea.fetchai.signing.SigningMessage)
    ),
)
_sym_db.RegisterMessage(SigningMessage)
_sym_db.RegisterMessage(SigningMessage.ErrorCode)
_sym_db.RegisterMessage(SigningMessage.RawMessage)
_sym_db.RegisterMessage(SigningMessage.RawTransaction)
_sym_db.RegisterMessage(SigningMessage.SignedMessage)
_sym_db.RegisterMessage(SigningMessage.SignedTransaction)
_sym_db.RegisterMessage(SigningMessage.Terms)
_sym_db.RegisterMessage(SigningMessage.Sign_Transaction_Performative)
_sym_db.RegisterMessage(SigningMessage.Sign_Message_Performative)
_sym_db.RegisterMessage(SigningMessage.Signed_Transaction_Performative)
_sym_db.RegisterMessage(SigningMessage.Signed_Message_Performative)
_sym_db.RegisterMessage(SigningMessage.Error_Performative)


# @@protoc_insertion_point(module_scope)
