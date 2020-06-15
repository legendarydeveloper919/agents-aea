# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ledger_api.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="ledger_api.proto",
    package="fetch.aea.LedgerApi",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x10ledger_api.proto\x12\x13\x66\x65tch.aea.LedgerApi"\xa0\x0c\n\x10LedgerApiMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12"\n\x1a\x64ialogue_starter_reference\x18\x02 \x01(\t\x12$\n\x1c\x64ialogue_responder_reference\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\x05\x12M\n\x07\x62\x61lance\x18\x05 \x01(\x0b\x32:.fetch.aea.LedgerApi.LedgerApiMessage.Balance_PerformativeH\x00\x12\x61\n\x11generate_tx_nonce\x18\x06 \x01(\x0b\x32\x44.fetch.aea.LedgerApi.LedgerApiMessage.Generate_Tx_Nonce_PerformativeH\x00\x12U\n\x0bget_balance\x18\x07 \x01(\x0b\x32>.fetch.aea.LedgerApi.LedgerApiMessage.Get_Balance_PerformativeH\x00\x12m\n\x17get_transaction_receipt\x18\x08 \x01(\x0b\x32J.fetch.aea.LedgerApi.LedgerApiMessage.Get_Transaction_Receipt_PerformativeH\x00\x12k\n\x16is_transaction_settled\x18\t \x01(\x0b\x32I.fetch.aea.LedgerApi.LedgerApiMessage.Is_Transaction_Settled_PerformativeH\x00\x12g\n\x14is_transaction_valid\x18\n \x01(\x0b\x32G.fetch.aea.LedgerApi.LedgerApiMessage.Is_Transaction_Valid_PerformativeH\x00\x12O\n\x08transfer\x18\x0b \x01(\x0b\x32;.fetch.aea.LedgerApi.LedgerApiMessage.Transfer_PerformativeH\x00\x12Q\n\ttx_digest\x18\x0c \x01(\x0b\x32<.fetch.aea.LedgerApi.LedgerApiMessage.Tx_Digest_PerformativeH\x00\x1a>\n\x18Get_Balance_Performative\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x1a\xfb\x01\n\x15Transfer_Performative\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x1b\n\x13\x64\x65stination_address\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x05\x12\x0e\n\x06tx_fee\x18\x04 \x01(\x05\x12\x10\n\x08tx_nonce\x18\x05 \x01(\x05\x12S\n\x04\x64\x61ta\x18\x06 \x03(\x0b\x32\x45.fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aK\n#Is_Transaction_Settled_Performative\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x11\n\ttx_digest\x18\x02 \x01(\t\x1aI\n!Is_Transaction_Valid_Performative\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x11\n\ttx_digest\x18\x02 \x01(\t\x1aL\n$Get_Transaction_Receipt_Performative\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x11\n\ttx_digest\x18\x02 \x01(\t\x1a\x33\n\x1eGenerate_Tx_Nonce_Performative\x12\x11\n\tledger_id\x18\x01 \x01(\t\x1a)\n\x14\x42\x61lance_Performative\x12\x11\n\tledger_id\x18\x01 \x01(\t\x1a\x18\n\x16Tx_Digest_PerformativeB\x0e\n\x0cperformativeb\x06proto3'
    ),
)


_LEDGERAPIMESSAGE_GET_BALANCE_PERFORMATIVE = _descriptor.Descriptor(
    name="Get_Balance_Performative",
    full_name="fetch.aea.LedgerApi.LedgerApiMessage.Get_Balance_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="ledger_id",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Get_Balance_Performative.ledger_id",
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
            name="address",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Get_Balance_Performative.address",
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=926,
    serialized_end=988,
)

_LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE_DATAENTRY = _descriptor.Descriptor(
    name="DataEntry",
    full_name="fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative.DataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative.DataEntry.key",
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
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative.DataEntry.value",
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
    serialized_start=1199,
    serialized_end=1242,
)

_LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE = _descriptor.Descriptor(
    name="Transfer_Performative",
    full_name="fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="ledger_id",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative.ledger_id",
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
            name="destination_address",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative.destination_address",
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
            name="amount",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative.amount",
            index=2,
            number=3,
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
            name="tx_fee",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative.tx_fee",
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
            name="tx_nonce",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative.tx_nonce",
            index=4,
            number=5,
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
            name="data",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative.data",
            index=5,
            number=6,
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
    nested_types=[_LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE_DATAENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=991,
    serialized_end=1242,
)

_LEDGERAPIMESSAGE_IS_TRANSACTION_SETTLED_PERFORMATIVE = _descriptor.Descriptor(
    name="Is_Transaction_Settled_Performative",
    full_name="fetch.aea.LedgerApi.LedgerApiMessage.Is_Transaction_Settled_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="ledger_id",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Is_Transaction_Settled_Performative.ledger_id",
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
            name="tx_digest",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Is_Transaction_Settled_Performative.tx_digest",
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1244,
    serialized_end=1319,
)

_LEDGERAPIMESSAGE_IS_TRANSACTION_VALID_PERFORMATIVE = _descriptor.Descriptor(
    name="Is_Transaction_Valid_Performative",
    full_name="fetch.aea.LedgerApi.LedgerApiMessage.Is_Transaction_Valid_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="ledger_id",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Is_Transaction_Valid_Performative.ledger_id",
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
            name="tx_digest",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Is_Transaction_Valid_Performative.tx_digest",
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1321,
    serialized_end=1394,
)

_LEDGERAPIMESSAGE_GET_TRANSACTION_RECEIPT_PERFORMATIVE = _descriptor.Descriptor(
    name="Get_Transaction_Receipt_Performative",
    full_name="fetch.aea.LedgerApi.LedgerApiMessage.Get_Transaction_Receipt_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="ledger_id",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Get_Transaction_Receipt_Performative.ledger_id",
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
            name="tx_digest",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Get_Transaction_Receipt_Performative.tx_digest",
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1396,
    serialized_end=1472,
)

_LEDGERAPIMESSAGE_GENERATE_TX_NONCE_PERFORMATIVE = _descriptor.Descriptor(
    name="Generate_Tx_Nonce_Performative",
    full_name="fetch.aea.LedgerApi.LedgerApiMessage.Generate_Tx_Nonce_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="ledger_id",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Generate_Tx_Nonce_Performative.ledger_id",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1474,
    serialized_end=1525,
)

_LEDGERAPIMESSAGE_BALANCE_PERFORMATIVE = _descriptor.Descriptor(
    name="Balance_Performative",
    full_name="fetch.aea.LedgerApi.LedgerApiMessage.Balance_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="ledger_id",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.Balance_Performative.ledger_id",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1527,
    serialized_end=1568,
)

_LEDGERAPIMESSAGE_TX_DIGEST_PERFORMATIVE = _descriptor.Descriptor(
    name="Tx_Digest_Performative",
    full_name="fetch.aea.LedgerApi.LedgerApiMessage.Tx_Digest_Performative",
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
    serialized_start=1570,
    serialized_end=1594,
)

_LEDGERAPIMESSAGE = _descriptor.Descriptor(
    name="LedgerApiMessage",
    full_name="fetch.aea.LedgerApi.LedgerApiMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="message_id",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.message_id",
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
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.dialogue_starter_reference",
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
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.dialogue_responder_reference",
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
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.target",
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
            name="balance",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.balance",
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
            name="generate_tx_nonce",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.generate_tx_nonce",
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
            name="get_balance",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.get_balance",
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
            name="get_transaction_receipt",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.get_transaction_receipt",
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
            name="is_transaction_settled",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.is_transaction_settled",
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
            name="is_transaction_valid",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.is_transaction_valid",
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
            name="transfer",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.transfer",
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
            name="tx_digest",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.tx_digest",
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
        _LEDGERAPIMESSAGE_GET_BALANCE_PERFORMATIVE,
        _LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE,
        _LEDGERAPIMESSAGE_IS_TRANSACTION_SETTLED_PERFORMATIVE,
        _LEDGERAPIMESSAGE_IS_TRANSACTION_VALID_PERFORMATIVE,
        _LEDGERAPIMESSAGE_GET_TRANSACTION_RECEIPT_PERFORMATIVE,
        _LEDGERAPIMESSAGE_GENERATE_TX_NONCE_PERFORMATIVE,
        _LEDGERAPIMESSAGE_BALANCE_PERFORMATIVE,
        _LEDGERAPIMESSAGE_TX_DIGEST_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="fetch.aea.LedgerApi.LedgerApiMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=42,
    serialized_end=1610,
)

_LEDGERAPIMESSAGE_GET_BALANCE_PERFORMATIVE.containing_type = _LEDGERAPIMESSAGE
_LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE_DATAENTRY.containing_type = (
    _LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE
)
_LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE.fields_by_name[
    "data"
].message_type = _LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE_DATAENTRY
_LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE.containing_type = _LEDGERAPIMESSAGE
_LEDGERAPIMESSAGE_IS_TRANSACTION_SETTLED_PERFORMATIVE.containing_type = (
    _LEDGERAPIMESSAGE
)
_LEDGERAPIMESSAGE_IS_TRANSACTION_VALID_PERFORMATIVE.containing_type = _LEDGERAPIMESSAGE
_LEDGERAPIMESSAGE_GET_TRANSACTION_RECEIPT_PERFORMATIVE.containing_type = (
    _LEDGERAPIMESSAGE
)
_LEDGERAPIMESSAGE_GENERATE_TX_NONCE_PERFORMATIVE.containing_type = _LEDGERAPIMESSAGE
_LEDGERAPIMESSAGE_BALANCE_PERFORMATIVE.containing_type = _LEDGERAPIMESSAGE
_LEDGERAPIMESSAGE_TX_DIGEST_PERFORMATIVE.containing_type = _LEDGERAPIMESSAGE
_LEDGERAPIMESSAGE.fields_by_name[
    "balance"
].message_type = _LEDGERAPIMESSAGE_BALANCE_PERFORMATIVE
_LEDGERAPIMESSAGE.fields_by_name[
    "generate_tx_nonce"
].message_type = _LEDGERAPIMESSAGE_GENERATE_TX_NONCE_PERFORMATIVE
_LEDGERAPIMESSAGE.fields_by_name[
    "get_balance"
].message_type = _LEDGERAPIMESSAGE_GET_BALANCE_PERFORMATIVE
_LEDGERAPIMESSAGE.fields_by_name[
    "get_transaction_receipt"
].message_type = _LEDGERAPIMESSAGE_GET_TRANSACTION_RECEIPT_PERFORMATIVE
_LEDGERAPIMESSAGE.fields_by_name[
    "is_transaction_settled"
].message_type = _LEDGERAPIMESSAGE_IS_TRANSACTION_SETTLED_PERFORMATIVE
_LEDGERAPIMESSAGE.fields_by_name[
    "is_transaction_valid"
].message_type = _LEDGERAPIMESSAGE_IS_TRANSACTION_VALID_PERFORMATIVE
_LEDGERAPIMESSAGE.fields_by_name[
    "transfer"
].message_type = _LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE
_LEDGERAPIMESSAGE.fields_by_name[
    "tx_digest"
].message_type = _LEDGERAPIMESSAGE_TX_DIGEST_PERFORMATIVE
_LEDGERAPIMESSAGE.oneofs_by_name["performative"].fields.append(
    _LEDGERAPIMESSAGE.fields_by_name["balance"]
)
_LEDGERAPIMESSAGE.fields_by_name[
    "balance"
].containing_oneof = _LEDGERAPIMESSAGE.oneofs_by_name["performative"]
_LEDGERAPIMESSAGE.oneofs_by_name["performative"].fields.append(
    _LEDGERAPIMESSAGE.fields_by_name["generate_tx_nonce"]
)
_LEDGERAPIMESSAGE.fields_by_name[
    "generate_tx_nonce"
].containing_oneof = _LEDGERAPIMESSAGE.oneofs_by_name["performative"]
_LEDGERAPIMESSAGE.oneofs_by_name["performative"].fields.append(
    _LEDGERAPIMESSAGE.fields_by_name["get_balance"]
)
_LEDGERAPIMESSAGE.fields_by_name[
    "get_balance"
].containing_oneof = _LEDGERAPIMESSAGE.oneofs_by_name["performative"]
_LEDGERAPIMESSAGE.oneofs_by_name["performative"].fields.append(
    _LEDGERAPIMESSAGE.fields_by_name["get_transaction_receipt"]
)
_LEDGERAPIMESSAGE.fields_by_name[
    "get_transaction_receipt"
].containing_oneof = _LEDGERAPIMESSAGE.oneofs_by_name["performative"]
_LEDGERAPIMESSAGE.oneofs_by_name["performative"].fields.append(
    _LEDGERAPIMESSAGE.fields_by_name["is_transaction_settled"]
)
_LEDGERAPIMESSAGE.fields_by_name[
    "is_transaction_settled"
].containing_oneof = _LEDGERAPIMESSAGE.oneofs_by_name["performative"]
_LEDGERAPIMESSAGE.oneofs_by_name["performative"].fields.append(
    _LEDGERAPIMESSAGE.fields_by_name["is_transaction_valid"]
)
_LEDGERAPIMESSAGE.fields_by_name[
    "is_transaction_valid"
].containing_oneof = _LEDGERAPIMESSAGE.oneofs_by_name["performative"]
_LEDGERAPIMESSAGE.oneofs_by_name["performative"].fields.append(
    _LEDGERAPIMESSAGE.fields_by_name["transfer"]
)
_LEDGERAPIMESSAGE.fields_by_name[
    "transfer"
].containing_oneof = _LEDGERAPIMESSAGE.oneofs_by_name["performative"]
_LEDGERAPIMESSAGE.oneofs_by_name["performative"].fields.append(
    _LEDGERAPIMESSAGE.fields_by_name["tx_digest"]
)
_LEDGERAPIMESSAGE.fields_by_name[
    "tx_digest"
].containing_oneof = _LEDGERAPIMESSAGE.oneofs_by_name["performative"]
DESCRIPTOR.message_types_by_name["LedgerApiMessage"] = _LEDGERAPIMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LedgerApiMessage = _reflection.GeneratedProtocolMessageType(
    "LedgerApiMessage",
    (_message.Message,),
    dict(
        Get_Balance_Performative=_reflection.GeneratedProtocolMessageType(
            "Get_Balance_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_LEDGERAPIMESSAGE_GET_BALANCE_PERFORMATIVE,
                __module__="ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.LedgerApi.LedgerApiMessage.Get_Balance_Performative)
            ),
        ),
        Transfer_Performative=_reflection.GeneratedProtocolMessageType(
            "Transfer_Performative",
            (_message.Message,),
            dict(
                DataEntry=_reflection.GeneratedProtocolMessageType(
                    "DataEntry",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE_DATAENTRY,
                        __module__="ledger_api_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative.DataEntry)
                    ),
                ),
                DESCRIPTOR=_LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE,
                __module__="ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.LedgerApi.LedgerApiMessage.Transfer_Performative)
            ),
        ),
        Is_Transaction_Settled_Performative=_reflection.GeneratedProtocolMessageType(
            "Is_Transaction_Settled_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_LEDGERAPIMESSAGE_IS_TRANSACTION_SETTLED_PERFORMATIVE,
                __module__="ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.LedgerApi.LedgerApiMessage.Is_Transaction_Settled_Performative)
            ),
        ),
        Is_Transaction_Valid_Performative=_reflection.GeneratedProtocolMessageType(
            "Is_Transaction_Valid_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_LEDGERAPIMESSAGE_IS_TRANSACTION_VALID_PERFORMATIVE,
                __module__="ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.LedgerApi.LedgerApiMessage.Is_Transaction_Valid_Performative)
            ),
        ),
        Get_Transaction_Receipt_Performative=_reflection.GeneratedProtocolMessageType(
            "Get_Transaction_Receipt_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_LEDGERAPIMESSAGE_GET_TRANSACTION_RECEIPT_PERFORMATIVE,
                __module__="ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.LedgerApi.LedgerApiMessage.Get_Transaction_Receipt_Performative)
            ),
        ),
        Generate_Tx_Nonce_Performative=_reflection.GeneratedProtocolMessageType(
            "Generate_Tx_Nonce_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_LEDGERAPIMESSAGE_GENERATE_TX_NONCE_PERFORMATIVE,
                __module__="ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.LedgerApi.LedgerApiMessage.Generate_Tx_Nonce_Performative)
            ),
        ),
        Balance_Performative=_reflection.GeneratedProtocolMessageType(
            "Balance_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_LEDGERAPIMESSAGE_BALANCE_PERFORMATIVE,
                __module__="ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.LedgerApi.LedgerApiMessage.Balance_Performative)
            ),
        ),
        Tx_Digest_Performative=_reflection.GeneratedProtocolMessageType(
            "Tx_Digest_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_LEDGERAPIMESSAGE_TX_DIGEST_PERFORMATIVE,
                __module__="ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.LedgerApi.LedgerApiMessage.Tx_Digest_Performative)
            ),
        ),
        DESCRIPTOR=_LEDGERAPIMESSAGE,
        __module__="ledger_api_pb2"
        # @@protoc_insertion_point(class_scope:fetch.aea.LedgerApi.LedgerApiMessage)
    ),
)
_sym_db.RegisterMessage(LedgerApiMessage)
_sym_db.RegisterMessage(LedgerApiMessage.Get_Balance_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Transfer_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Transfer_Performative.DataEntry)
_sym_db.RegisterMessage(LedgerApiMessage.Is_Transaction_Settled_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Is_Transaction_Valid_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Get_Transaction_Receipt_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Generate_Tx_Nonce_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Balance_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Tx_Digest_Performative)


_LEDGERAPIMESSAGE_TRANSFER_PERFORMATIVE_DATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
