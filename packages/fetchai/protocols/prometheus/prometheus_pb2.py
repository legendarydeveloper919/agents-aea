# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prometheus.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="prometheus.proto",
    package="aea.fetchai.prometheus",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\x10prometheus.proto\x12\x16\x61\x65\x61.fetchai.prometheus"\xc1\x04\n\x11PrometheusMessage\x12W\n\nadd_metric\x18\x05 \x01(\x0b\x32\x41.aea.fetchai.prometheus.PrometheusMessage.Add_Metric_PerformativeH\x00\x12S\n\x08response\x18\x06 \x01(\x0b\x32?.aea.fetchai.prometheus.PrometheusMessage.Response_PerformativeH\x00\x12]\n\rupdate_metric\x18\x07 \x01(\x0b\x32\x44.aea.fetchai.prometheus.PrometheusMessage.Update_Metric_PerformativeH\x00\x1a[\n\x17\x41\x64\x64_Metric_Performative\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06labels\x18\x04 \x03(\t\x1a\x62\n\x1aUpdate_Metric_Performative\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61llable\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x02\x12\x14\n\x0cvalue_is_set\x18\x04 \x01(\x08\x1aN\n\x15Response_Performative\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x16\n\x0emessage_is_set\x18\x03 \x01(\x08\x42\x0e\n\x0cperformativeb\x06proto3',
)


_PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE = _descriptor.Descriptor(
    name="Add_Metric_Performative",
    full_name="aea.fetchai.prometheus.PrometheusMessage.Add_Metric_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="aea.fetchai.prometheus.PrometheusMessage.Add_Metric_Performative.type",
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
            name="title",
            full_name="aea.fetchai.prometheus.PrometheusMessage.Add_Metric_Performative.title",
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
            name="description",
            full_name="aea.fetchai.prometheus.PrometheusMessage.Add_Metric_Performative.description",
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
            name="labels",
            full_name="aea.fetchai.prometheus.PrometheusMessage.Add_Metric_Performative.labels",
            index=3,
            number=4,
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
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=335,
    serialized_end=426,
)

_PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE = _descriptor.Descriptor(
    name="Update_Metric_Performative",
    full_name="aea.fetchai.prometheus.PrometheusMessage.Update_Metric_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="title",
            full_name="aea.fetchai.prometheus.PrometheusMessage.Update_Metric_Performative.title",
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
            name="callable",
            full_name="aea.fetchai.prometheus.PrometheusMessage.Update_Metric_Performative.callable",
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
            name="value",
            full_name="aea.fetchai.prometheus.PrometheusMessage.Update_Metric_Performative.value",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value_is_set",
            full_name="aea.fetchai.prometheus.PrometheusMessage.Update_Metric_Performative.value_is_set",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    serialized_start=428,
    serialized_end=526,
)

_PROMETHEUSMESSAGE_RESPONSE_PERFORMATIVE = _descriptor.Descriptor(
    name="Response_Performative",
    full_name="aea.fetchai.prometheus.PrometheusMessage.Response_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="code",
            full_name="aea.fetchai.prometheus.PrometheusMessage.Response_Performative.code",
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
            name="message",
            full_name="aea.fetchai.prometheus.PrometheusMessage.Response_Performative.message",
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
            name="message_is_set",
            full_name="aea.fetchai.prometheus.PrometheusMessage.Response_Performative.message_is_set",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    serialized_start=528,
    serialized_end=606,
)

_PROMETHEUSMESSAGE = _descriptor.Descriptor(
    name="PrometheusMessage",
    full_name="aea.fetchai.prometheus.PrometheusMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="add_metric",
            full_name="aea.fetchai.prometheus.PrometheusMessage.add_metric",
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
            name="response",
            full_name="aea.fetchai.prometheus.PrometheusMessage.response",
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
            name="update_metric",
            full_name="aea.fetchai.prometheus.PrometheusMessage.update_metric",
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
    ],
    extensions=[],
    nested_types=[
        _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE,
        _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE,
        _PROMETHEUSMESSAGE_RESPONSE_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="aea.fetchai.prometheus.PrometheusMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=45,
    serialized_end=622,
)

_PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE.containing_type = _PROMETHEUSMESSAGE
_PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE.containing_type = _PROMETHEUSMESSAGE
_PROMETHEUSMESSAGE_RESPONSE_PERFORMATIVE.containing_type = _PROMETHEUSMESSAGE
_PROMETHEUSMESSAGE.fields_by_name[
    "add_metric"
].message_type = _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE
_PROMETHEUSMESSAGE.fields_by_name[
    "response"
].message_type = _PROMETHEUSMESSAGE_RESPONSE_PERFORMATIVE
_PROMETHEUSMESSAGE.fields_by_name[
    "update_metric"
].message_type = _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE
_PROMETHEUSMESSAGE.oneofs_by_name["performative"].fields.append(
    _PROMETHEUSMESSAGE.fields_by_name["add_metric"]
)
_PROMETHEUSMESSAGE.fields_by_name[
    "add_metric"
].containing_oneof = _PROMETHEUSMESSAGE.oneofs_by_name["performative"]
_PROMETHEUSMESSAGE.oneofs_by_name["performative"].fields.append(
    _PROMETHEUSMESSAGE.fields_by_name["response"]
)
_PROMETHEUSMESSAGE.fields_by_name[
    "response"
].containing_oneof = _PROMETHEUSMESSAGE.oneofs_by_name["performative"]
_PROMETHEUSMESSAGE.oneofs_by_name["performative"].fields.append(
    _PROMETHEUSMESSAGE.fields_by_name["update_metric"]
)
_PROMETHEUSMESSAGE.fields_by_name[
    "update_metric"
].containing_oneof = _PROMETHEUSMESSAGE.oneofs_by_name["performative"]
DESCRIPTOR.message_types_by_name["PrometheusMessage"] = _PROMETHEUSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrometheusMessage = _reflection.GeneratedProtocolMessageType(
    "PrometheusMessage",
    (_message.Message,),
    {
        "Add_Metric_Performative": _reflection.GeneratedProtocolMessageType(
            "Add_Metric_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _PROMETHEUSMESSAGE_ADD_METRIC_PERFORMATIVE,
                "__module__": "prometheus_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.prometheus.PrometheusMessage.Add_Metric_Performative)
            },
        ),
        "Update_Metric_Performative": _reflection.GeneratedProtocolMessageType(
            "Update_Metric_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _PROMETHEUSMESSAGE_UPDATE_METRIC_PERFORMATIVE,
                "__module__": "prometheus_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.prometheus.PrometheusMessage.Update_Metric_Performative)
            },
        ),
        "Response_Performative": _reflection.GeneratedProtocolMessageType(
            "Response_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _PROMETHEUSMESSAGE_RESPONSE_PERFORMATIVE,
                "__module__": "prometheus_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.prometheus.PrometheusMessage.Response_Performative)
            },
        ),
        "DESCRIPTOR": _PROMETHEUSMESSAGE,
        "__module__": "prometheus_pb2"
        # @@protoc_insertion_point(class_scope:aea.fetchai.prometheus.PrometheusMessage)
    },
)
_sym_db.RegisterMessage(PrometheusMessage)
_sym_db.RegisterMessage(PrometheusMessage.Add_Metric_Performative)
_sym_db.RegisterMessage(PrometheusMessage.Update_Metric_Performative)
_sym_db.RegisterMessage(PrometheusMessage.Response_Performative)


# @@protoc_insertion_point(module_scope)
