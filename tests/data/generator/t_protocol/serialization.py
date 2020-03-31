# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2020 fetchai
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Serialization module for t_protocol protocol."""

from typing import Any, Dict, cast

from aea.protocols.base import Message
from aea.protocols.base import Serializer

from tests.data.generator.t_protocol import t_protocol_pb2
from tests.data.generator.t_protocol.custom_types import DataModel
from tests.data.generator.t_protocol.message import TProtocolMessage


class TProtocolSerializer(Serializer):
    """Serialization for the 't_protocol' protocol."""

    def encode(self, msg: Message) -> bytes:
        """
        Encode a 'TProtocol' message into bytes.

        :param msg: the message object.
        :return: the bytes.
        """
        msg = cast(TProtocolMessage, msg)
        t_protocol_msg = t_protocol_pb2.TProtocolMessage()
        t_protocol_msg.message_id = msg.message_id
        dialogue_reference = msg.dialogue_reference
        t_protocol_msg.dialogue_starter_reference = dialogue_reference[0]
        t_protocol_msg.dialogue_responder_reference = dialogue_reference[1]
        t_protocol_msg.target = msg.target

        performative_id = msg.performative
        if performative_id == TProtocolMessage.Performative.PERFORMATIVE_CT:
            performative = t_protocol_pb2.TProtocolMessage.Performative_Ct_performative()  # type: ignore
            content_ct = msg.content_ct
            DataModel.encode(performative.content_ct, content_ct)
            t_protocol_msg.performative_ct.CopyFrom(performative)
        elif performative_id == TProtocolMessage.Performative.PERFORMATIVE_PT:
            performative = t_protocol_pb2.TProtocolMessage.Performative_Pt_performative()  # type: ignore
            content_bytes = msg.content_bytes
            performative.content_bytes = content_bytes
            content_int = msg.content_int
            performative.content_int = content_int
            content_float = msg.content_float
            performative.content_float = content_float
            content_bool = msg.content_bool
            performative.content_bool = content_bool
            content_str = msg.content_str
            performative.content_str = content_str
            t_protocol_msg.performative_pt.CopyFrom(performative)
        elif performative_id == TProtocolMessage.Performative.PERFORMATIVE_PCT:
            performative = t_protocol_pb2.TProtocolMessage.Performative_Pct_performative()  # type: ignore
            content_set_bytes = msg.content_set_bytes
            performative.content_set_bytes.extend(content_set_bytes)
            content_set_int = msg.content_set_int
            performative.content_set_int.extend(content_set_int)
            content_set_float = msg.content_set_float
            performative.content_set_float.extend(content_set_float)
            content_set_bool = msg.content_set_bool
            performative.content_set_bool.extend(content_set_bool)
            content_set_str = msg.content_set_str
            performative.content_set_str.extend(content_set_str)
            content_list_bytes = msg.content_list_bytes
            performative.content_list_bytes.extend(content_list_bytes)
            content_list_int = msg.content_list_int
            performative.content_list_int.extend(content_list_int)
            content_list_float = msg.content_list_float
            performative.content_list_float.extend(content_list_float)
            content_list_bool = msg.content_list_bool
            performative.content_list_bool.extend(content_list_bool)
            content_list_str = msg.content_list_str
            performative.content_list_str.extend(content_list_str)
            t_protocol_msg.performative_pct.CopyFrom(performative)
        elif performative_id == TProtocolMessage.Performative.PERFORMATIVE_PMT:
            performative = t_protocol_pb2.TProtocolMessage.Performative_Pmt_performative()  # type: ignore
            content_dict_bool_bytes = msg.content_dict_bool_bytes
            performative.content_dict_bool_bytes.update(content_dict_bool_bytes)
            content_dict_str_float = msg.content_dict_str_float
            performative.content_dict_str_float.update(content_dict_str_float)
            t_protocol_msg.performative_pmt.CopyFrom(performative)
        elif performative_id == TProtocolMessage.Performative.PERFORMATIVE_MT:
            performative = t_protocol_pb2.TProtocolMessage.Performative_Mt_performative()  # type: ignore
            if msg.is_set("content_union_1_type_DataModel"):
                performative.content_union_1_type_DataModel_is_set = True
                content_union_1_type_DataModel = msg.content_union_1_type_DataModel
                DataModel.encode(
                    performative.content_union_1_type_DataModel,
                    content_union_1_type_DataModel,
                )
            if msg.is_set("content_union_1_type_bytes"):
                performative.content_union_1_type_bytes_is_set = True
                content_union_1_type_bytes = msg.content_union_1_type_bytes
                performative.content_union_1_type_bytes = content_union_1_type_bytes
            if msg.is_set("content_union_1_type_int"):
                performative.content_union_1_type_int_is_set = True
                content_union_1_type_int = msg.content_union_1_type_int
                performative.content_union_1_type_int = content_union_1_type_int
            if msg.is_set("content_union_1_type_float"):
                performative.content_union_1_type_float_is_set = True
                content_union_1_type_float = msg.content_union_1_type_float
                performative.content_union_1_type_float = content_union_1_type_float
            if msg.is_set("content_union_1_type_bool"):
                performative.content_union_1_type_bool_is_set = True
                content_union_1_type_bool = msg.content_union_1_type_bool
                performative.content_union_1_type_bool = content_union_1_type_bool
            if msg.is_set("content_union_1_type_str"):
                performative.content_union_1_type_str_is_set = True
                content_union_1_type_str = msg.content_union_1_type_str
                performative.content_union_1_type_str = content_union_1_type_str
            if msg.is_set("content_union_1_type_set_of_int"):
                performative.content_union_1_type_set_of_int_is_set = True
                content_union_1_type_set_of_int = msg.content_union_1_type_set_of_int
                performative.content_union_1_type_set_of_int.extend(
                    content_union_1_type_set_of_int
                )
            if msg.is_set("content_union_1_type_list_of_bool"):
                performative.content_union_1_type_list_of_bool_is_set = True
                content_union_1_type_list_of_bool = (
                    msg.content_union_1_type_list_of_bool
                )
                performative.content_union_1_type_list_of_bool.extend(
                    content_union_1_type_list_of_bool
                )
            if msg.is_set("content_union_1_type_dict_of_str_int"):
                performative.content_union_1_type_dict_of_str_int_is_set = True
                content_union_1_type_dict_of_str_int = (
                    msg.content_union_1_type_dict_of_str_int
                )
                performative.content_union_1_type_dict_of_str_int.update(
                    content_union_1_type_dict_of_str_int
                )
            if msg.is_set("content_union_2_type_set_of_bytes"):
                performative.content_union_2_type_set_of_bytes_is_set = True
                content_union_2_type_set_of_bytes = (
                    msg.content_union_2_type_set_of_bytes
                )
                performative.content_union_2_type_set_of_bytes.extend(
                    content_union_2_type_set_of_bytes
                )
            if msg.is_set("content_union_2_type_set_of_int"):
                performative.content_union_2_type_set_of_int_is_set = True
                content_union_2_type_set_of_int = msg.content_union_2_type_set_of_int
                performative.content_union_2_type_set_of_int.extend(
                    content_union_2_type_set_of_int
                )
            if msg.is_set("content_union_2_type_set_of_str"):
                performative.content_union_2_type_set_of_str_is_set = True
                content_union_2_type_set_of_str = msg.content_union_2_type_set_of_str
                performative.content_union_2_type_set_of_str.extend(
                    content_union_2_type_set_of_str
                )
            if msg.is_set("content_union_2_type_list_of_float"):
                performative.content_union_2_type_list_of_float_is_set = True
                content_union_2_type_list_of_float = (
                    msg.content_union_2_type_list_of_float
                )
                performative.content_union_2_type_list_of_float.extend(
                    content_union_2_type_list_of_float
                )
            if msg.is_set("content_union_2_type_list_of_bool"):
                performative.content_union_2_type_list_of_bool_is_set = True
                content_union_2_type_list_of_bool = (
                    msg.content_union_2_type_list_of_bool
                )
                performative.content_union_2_type_list_of_bool.extend(
                    content_union_2_type_list_of_bool
                )
            if msg.is_set("content_union_2_type_list_of_bytes"):
                performative.content_union_2_type_list_of_bytes_is_set = True
                content_union_2_type_list_of_bytes = (
                    msg.content_union_2_type_list_of_bytes
                )
                performative.content_union_2_type_list_of_bytes.extend(
                    content_union_2_type_list_of_bytes
                )
            if msg.is_set("content_union_2_type_dict_of_str_int"):
                performative.content_union_2_type_dict_of_str_int_is_set = True
                content_union_2_type_dict_of_str_int = (
                    msg.content_union_2_type_dict_of_str_int
                )
                performative.content_union_2_type_dict_of_str_int.update(
                    content_union_2_type_dict_of_str_int
                )
            if msg.is_set("content_union_2_type_dict_of_int_float"):
                performative.content_union_2_type_dict_of_int_float_is_set = True
                content_union_2_type_dict_of_int_float = (
                    msg.content_union_2_type_dict_of_int_float
                )
                performative.content_union_2_type_dict_of_int_float.update(
                    content_union_2_type_dict_of_int_float
                )
            if msg.is_set("content_union_2_type_dict_of_bool_bytes"):
                performative.content_union_2_type_dict_of_bool_bytes_is_set = True
                content_union_2_type_dict_of_bool_bytes = (
                    msg.content_union_2_type_dict_of_bool_bytes
                )
                performative.content_union_2_type_dict_of_bool_bytes.update(
                    content_union_2_type_dict_of_bool_bytes
                )
            t_protocol_msg.performative_mt.CopyFrom(performative)
        elif performative_id == TProtocolMessage.Performative.PERFORMATIVE_O:
            performative = t_protocol_pb2.TProtocolMessage.Performative_O_performative()  # type: ignore
            if msg.is_set("content_o_ct"):
                performative.content_o_ct_is_set = True
                content_o_ct = msg.content_o_ct
                DataModel.encode(performative.content_o_ct, content_o_ct)
            if msg.is_set("content_o_bool"):
                performative.content_o_bool_is_set = True
                content_o_bool = msg.content_o_bool
                performative.content_o_bool = content_o_bool
            if msg.is_set("content_o_set_float"):
                performative.content_o_set_float_is_set = True
                content_o_set_float = msg.content_o_set_float
                performative.content_o_set_float.extend(content_o_set_float)
            if msg.is_set("content_o_list_bytes"):
                performative.content_o_list_bytes_is_set = True
                content_o_list_bytes = msg.content_o_list_bytes
                performative.content_o_list_bytes.extend(content_o_list_bytes)
            if msg.is_set("content_o_dict_str_int"):
                performative.content_o_dict_str_int_is_set = True
                content_o_dict_str_int = msg.content_o_dict_str_int
                performative.content_o_dict_str_int.update(content_o_dict_str_int)
            if msg.is_set("content_o_union_type_str"):
                performative.content_o_union_type_str_is_set = True
                content_o_union_type_str = msg.content_o_union_type_str
                performative.content_o_union_type_str = content_o_union_type_str
            if msg.is_set("content_o_union_type_dict_of_str_int"):
                performative.content_o_union_type_dict_of_str_int_is_set = True
                content_o_union_type_dict_of_str_int = (
                    msg.content_o_union_type_dict_of_str_int
                )
                performative.content_o_union_type_dict_of_str_int.update(
                    content_o_union_type_dict_of_str_int
                )
            if msg.is_set("content_o_union_type_set_of_int"):
                performative.content_o_union_type_set_of_int_is_set = True
                content_o_union_type_set_of_int = msg.content_o_union_type_set_of_int
                performative.content_o_union_type_set_of_int.extend(
                    content_o_union_type_set_of_int
                )
            if msg.is_set("content_o_union_type_set_of_bytes"):
                performative.content_o_union_type_set_of_bytes_is_set = True
                content_o_union_type_set_of_bytes = (
                    msg.content_o_union_type_set_of_bytes
                )
                performative.content_o_union_type_set_of_bytes.extend(
                    content_o_union_type_set_of_bytes
                )
            if msg.is_set("content_o_union_type_list_of_bool"):
                performative.content_o_union_type_list_of_bool_is_set = True
                content_o_union_type_list_of_bool = (
                    msg.content_o_union_type_list_of_bool
                )
                performative.content_o_union_type_list_of_bool.extend(
                    content_o_union_type_list_of_bool
                )
            if msg.is_set("content_o_union_type_dict_of_str_float"):
                performative.content_o_union_type_dict_of_str_float_is_set = True
                content_o_union_type_dict_of_str_float = (
                    msg.content_o_union_type_dict_of_str_float
                )
                performative.content_o_union_type_dict_of_str_float.update(
                    content_o_union_type_dict_of_str_float
                )
            t_protocol_msg.performative_o.CopyFrom(performative)
        elif (
            performative_id == TProtocolMessage.Performative.PERFORMATIVE_EMPTY_CONTENTS
        ):
            performative = t_protocol_pb2.TProtocolMessage.Performative_Empty_Contents_performative()  # type: ignore
            t_protocol_msg.performative_empty_contents.CopyFrom(performative)
        else:
            raise ValueError("Performative not valid: {}".format(performative_id))

        t_protocol_bytes = t_protocol_msg.SerializeToString()
        return t_protocol_bytes

    def decode(self, obj: bytes) -> Message:
        """
        Decode bytes into a 'TProtocol' message.

        :param obj: the bytes object.
        :return: the 'TProtocol' message.
        """
        t_protocol_pb = t_protocol_pb2.TProtocolMessage()
        t_protocol_pb.ParseFromString(obj)
        message_id = t_protocol_pb.message_id
        dialogue_reference = (
            t_protocol_pb.dialogue_starter_reference,
            t_protocol_pb.dialogue_responder_reference,
        )
        target = t_protocol_pb.target

        performative = t_protocol_pb.WhichOneof("performative")
        performative_id = TProtocolMessage.Performative(str(performative))
        performative_content = dict()  # type: Dict[str, Any]
        if performative_id == TProtocolMessage.Performative.PERFORMATIVE_CT:
            pb2_content_ct = t_protocol_pb.performative_ct.content_ct
            content_ct = DataModel.decode(pb2_content_ct)
            performative_content["content_ct"] = content_ct
        elif performative_id == TProtocolMessage.Performative.PERFORMATIVE_PT:
            content_bytes = t_protocol_pb.performative_pt.content_bytes
            performative_content["content_bytes"] = content_bytes
            content_int = t_protocol_pb.performative_pt.content_int
            performative_content["content_int"] = content_int
            content_float = t_protocol_pb.performative_pt.content_float
            performative_content["content_float"] = content_float
            content_bool = t_protocol_pb.performative_pt.content_bool
            performative_content["content_bool"] = content_bool
            content_str = t_protocol_pb.performative_pt.content_str
            performative_content["content_str"] = content_str
        elif performative_id == TProtocolMessage.Performative.PERFORMATIVE_PCT:
            content_set_bytes = t_protocol_pb.performative_pct.content_set_bytes
            content_set_bytes_frozenset = frozenset(content_set_bytes)
            performative_content["content_set_bytes"] = content_set_bytes_frozenset
            content_set_int = t_protocol_pb.performative_pct.content_set_int
            content_set_int_frozenset = frozenset(content_set_int)
            performative_content["content_set_int"] = content_set_int_frozenset
            content_set_float = t_protocol_pb.performative_pct.content_set_float
            content_set_float_frozenset = frozenset(content_set_float)
            performative_content["content_set_float"] = content_set_float_frozenset
            content_set_bool = t_protocol_pb.performative_pct.content_set_bool
            content_set_bool_frozenset = frozenset(content_set_bool)
            performative_content["content_set_bool"] = content_set_bool_frozenset
            content_set_str = t_protocol_pb.performative_pct.content_set_str
            content_set_str_frozenset = frozenset(content_set_str)
            performative_content["content_set_str"] = content_set_str_frozenset
            content_list_bytes = t_protocol_pb.performative_pct.content_list_bytes
            content_list_bytes_tuple = tuple(content_list_bytes)
            performative_content["content_list_bytes"] = content_list_bytes_tuple
            content_list_int = t_protocol_pb.performative_pct.content_list_int
            content_list_int_tuple = tuple(content_list_int)
            performative_content["content_list_int"] = content_list_int_tuple
            content_list_float = t_protocol_pb.performative_pct.content_list_float
            content_list_float_tuple = tuple(content_list_float)
            performative_content["content_list_float"] = content_list_float_tuple
            content_list_bool = t_protocol_pb.performative_pct.content_list_bool
            content_list_bool_tuple = tuple(content_list_bool)
            performative_content["content_list_bool"] = content_list_bool_tuple
            content_list_str = t_protocol_pb.performative_pct.content_list_str
            content_list_str_tuple = tuple(content_list_str)
            performative_content["content_list_str"] = content_list_str_tuple
        elif performative_id == TProtocolMessage.Performative.PERFORMATIVE_PMT:
            content_dict_bool_bytes = (
                t_protocol_pb.performative_pmt.content_dict_bool_bytes
            )
            content_dict_bool_bytes_dict = dict(content_dict_bool_bytes)
            performative_content[
                "content_dict_bool_bytes"
            ] = content_dict_bool_bytes_dict
            content_dict_str_float = (
                t_protocol_pb.performative_pmt.content_dict_str_float
            )
            content_dict_str_float_dict = dict(content_dict_str_float)
            performative_content["content_dict_str_float"] = content_dict_str_float_dict
        elif performative_id == TProtocolMessage.Performative.PERFORMATIVE_MT:
            if t_protocol_pb.performative_mt.content_union_1_type_DataModel_is_set:
                pb2_content_union_1_type_DataModel = (
                    t_protocol_pb.performative_mt.content_union_1_type_DataModel
                )
                content_union_1 = DataModel.decode(pb2_content_union_1_type_DataModel)
                performative_content["content_union_1"] = content_union_1
            if t_protocol_pb.performative_mt.content_union_1_type_bytes_is_set:
                content_union_1 = (
                    t_protocol_pb.performative_mt.content_union_1_type_bytes
                )
                performative_content["content_union_1"] = content_union_1
            if t_protocol_pb.performative_mt.content_union_1_type_int_is_set:
                content_union_1 = t_protocol_pb.performative_mt.content_union_1_type_int
                performative_content["content_union_1"] = content_union_1
            if t_protocol_pb.performative_mt.content_union_1_type_float_is_set:
                content_union_1 = (
                    t_protocol_pb.performative_mt.content_union_1_type_float
                )
                performative_content["content_union_1"] = content_union_1
            if t_protocol_pb.performative_mt.content_union_1_type_bool_is_set:
                content_union_1 = (
                    t_protocol_pb.performative_mt.content_union_1_type_bool
                )
                performative_content["content_union_1"] = content_union_1
            if t_protocol_pb.performative_mt.content_union_1_type_str_is_set:
                content_union_1 = t_protocol_pb.performative_mt.content_union_1_type_str
                performative_content["content_union_1"] = content_union_1
            if t_protocol_pb.performative_mt.content_union_1_type_set_of_int_is_set:
                content_union_1 = t_protocol_pb.performative_mt.content_union_1
                content_union_1_frozenset = frozenset(content_union_1)
                performative_content["content_union_1"] = content_union_1_frozenset
            if t_protocol_pb.performative_mt.content_union_1_type_list_of_bool_is_set:
                content_union_1 = t_protocol_pb.performative_mt.content_union_1
                content_union_1_tuple = tuple(content_union_1)
                performative_content["content_union_1"] = content_union_1_tuple
            if (
                t_protocol_pb.performative_mt.content_union_1_type_dict_of_str_int_is_set
            ):
                content_union_1 = t_protocol_pb.performative_mt.content_union_1
                content_union_1_dict = dict(content_union_1)
                performative_content["content_union_1"] = content_union_1_dict
            if t_protocol_pb.performative_mt.content_union_2_type_set_of_bytes_is_set:
                content_union_2 = t_protocol_pb.performative_mt.content_union_2
                content_union_2_frozenset = frozenset(content_union_2)
                performative_content["content_union_2"] = content_union_2_frozenset
            if t_protocol_pb.performative_mt.content_union_2_type_set_of_int_is_set:
                content_union_2 = t_protocol_pb.performative_mt.content_union_2
                content_union_2_frozenset = frozenset(content_union_2)
                performative_content["content_union_2"] = content_union_2_frozenset
            if t_protocol_pb.performative_mt.content_union_2_type_set_of_str_is_set:
                content_union_2 = t_protocol_pb.performative_mt.content_union_2
                content_union_2_frozenset = frozenset(content_union_2)
                performative_content["content_union_2"] = content_union_2_frozenset
            if t_protocol_pb.performative_mt.content_union_2_type_list_of_float_is_set:
                content_union_2 = t_protocol_pb.performative_mt.content_union_2
                content_union_2_tuple = tuple(content_union_2)
                performative_content["content_union_2"] = content_union_2_tuple
            if t_protocol_pb.performative_mt.content_union_2_type_list_of_bool_is_set:
                content_union_2 = t_protocol_pb.performative_mt.content_union_2
                content_union_2_tuple = tuple(content_union_2)
                performative_content["content_union_2"] = content_union_2_tuple
            if t_protocol_pb.performative_mt.content_union_2_type_list_of_bytes_is_set:
                content_union_2 = t_protocol_pb.performative_mt.content_union_2
                content_union_2_tuple = tuple(content_union_2)
                performative_content["content_union_2"] = content_union_2_tuple
            if (
                t_protocol_pb.performative_mt.content_union_2_type_dict_of_str_int_is_set
            ):
                content_union_2 = t_protocol_pb.performative_mt.content_union_2
                content_union_2_dict = dict(content_union_2)
                performative_content["content_union_2"] = content_union_2_dict
            if (
                t_protocol_pb.performative_mt.content_union_2_type_dict_of_int_float_is_set
            ):
                content_union_2 = t_protocol_pb.performative_mt.content_union_2
                content_union_2_dict = dict(content_union_2)
                performative_content["content_union_2"] = content_union_2_dict
            if (
                t_protocol_pb.performative_mt.content_union_2_type_dict_of_bool_bytes_is_set
            ):
                content_union_2 = t_protocol_pb.performative_mt.content_union_2
                content_union_2_dict = dict(content_union_2)
                performative_content["content_union_2"] = content_union_2_dict
        elif performative_id == TProtocolMessage.Performative.PERFORMATIVE_O:
            if t_protocol_pb.performative_o.content_o_ct_is_set:
                pb2_content_o_ct = t_protocol_pb.performative_o.content_o_ct
                content_o_ct = DataModel.decode(pb2_content_o_ct)
                performative_content["content_o_ct"] = content_o_ct
            if t_protocol_pb.performative_o.content_o_bool_is_set:
                content_o_bool = t_protocol_pb.performative_o.content_o_bool
                performative_content["content_o_bool"] = content_o_bool
            if t_protocol_pb.performative_o.content_o_set_float_is_set:
                content_o_set_float = t_protocol_pb.performative_o.content_o_set_float
                content_o_set_float_frozenset = frozenset(content_o_set_float)
                performative_content[
                    "content_o_set_float"
                ] = content_o_set_float_frozenset
            if t_protocol_pb.performative_o.content_o_list_bytes_is_set:
                content_o_list_bytes = t_protocol_pb.performative_o.content_o_list_bytes
                content_o_list_bytes_tuple = tuple(content_o_list_bytes)
                performative_content[
                    "content_o_list_bytes"
                ] = content_o_list_bytes_tuple
            if t_protocol_pb.performative_o.content_o_dict_str_int_is_set:
                content_o_dict_str_int = (
                    t_protocol_pb.performative_o.content_o_dict_str_int
                )
                content_o_dict_str_int_dict = dict(content_o_dict_str_int)
                performative_content[
                    "content_o_dict_str_int"
                ] = content_o_dict_str_int_dict
            if t_protocol_pb.performative_o.content_o_union_type_str_is_set:
                content_o_union = t_protocol_pb.performative_o.content_o_union_type_str
                performative_content["content_o_union"] = content_o_union
            if t_protocol_pb.performative_o.content_o_union_type_dict_of_str_int_is_set:
                content_o_union = t_protocol_pb.performative_o.content_o_union
                content_o_union_dict = dict(content_o_union)
                performative_content["content_o_union"] = content_o_union_dict
            if t_protocol_pb.performative_o.content_o_union_type_set_of_int_is_set:
                content_o_union = t_protocol_pb.performative_o.content_o_union
                content_o_union_frozenset = frozenset(content_o_union)
                performative_content["content_o_union"] = content_o_union_frozenset
            if t_protocol_pb.performative_o.content_o_union_type_set_of_bytes_is_set:
                content_o_union = t_protocol_pb.performative_o.content_o_union
                content_o_union_frozenset = frozenset(content_o_union)
                performative_content["content_o_union"] = content_o_union_frozenset
            if t_protocol_pb.performative_o.content_o_union_type_list_of_bool_is_set:
                content_o_union = t_protocol_pb.performative_o.content_o_union
                content_o_union_tuple = tuple(content_o_union)
                performative_content["content_o_union"] = content_o_union_tuple
            if (
                t_protocol_pb.performative_o.content_o_union_type_dict_of_str_float_is_set
            ):
                content_o_union = t_protocol_pb.performative_o.content_o_union
                content_o_union_dict = dict(content_o_union)
                performative_content["content_o_union"] = content_o_union_dict
        elif (
            performative_id == TProtocolMessage.Performative.PERFORMATIVE_EMPTY_CONTENTS
        ):
            pass
        else:
            raise ValueError("Performative not valid: {}.".format(performative_id))

        return TProtocolMessage(
            message_id=message_id,
            dialogue_reference=dialogue_reference,
            target=target,
            performative=performative,
            **performative_content
        )
