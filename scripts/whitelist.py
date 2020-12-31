# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
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
# flake8: noqa
# type: ignore
# pylint: skip-file
# To update; run: vulture aea --exclude "*_pb2.py" --make-whitelist > tests/whitelist.py
_.dependencies_highest_version  # unused property (aea/aea_builder.py:116)
_.set_search_service_address  # unused method (aea/aea_builder.py:484)
_.remove_private_key  # unused method (aea/aea_builder.py:580)
_.add_component_instance  # unused method (aea/aea_builder.py:643)
_.set_context_namespace  # unused method (aea/aea_builder.py:663)
_.remove_protocol  # unused method (aea/aea_builder.py:694)
_.remove_connection  # unused method (aea/aea_builder.py:714)
_.remove_skill  # unused method (aea/aea_builder.py:734)
_.remove_contract  # unused method (aea/aea_builder.py:754)
_.tick  # unused property (aea/agent.py:186)
AgentLoopException  # unused class (aea/agent_loop.py:134)
set_command  # unused function (aea/cli/config.py:53)
gui  # unused function (aea/cli/core.py:84)
all_command  # unused function (aea/cli/list.py:47)
_.type_cast_value  # unused method (aea/cli/utils/click_utils.py:37)
_.get_metavar  # unused method (aea/cli/utils/click_utils.py:79)
_.convert  # unused method (aea/cli/utils/click_utils.py:83)
_.get_metavar  # unused method (aea/cli/utils/click_utils.py:100)
_.convert  # unused method (aea/cli/utils/click_utils.py:104)
_.convert  # unused method (aea/cli/utils/click_utils.py:129)
_.formatter  # unused attribute (aea/cli/utils/loggers.py:92)
is_item_present_unified  # unused function (aea/cli/utils/package_utils:394)
ui_is_starting  # unused variable (aea/cli_gui/__init__.py:86)
module_dir  # unused variable (aea/cli_gui/__init__.py:88)
get_agents  # unused function (aea/cli_gui/__init__.py:96)
get_registered_items  # unused function (aea/cli_gui/__init__.py:118)
search_registered_items  # unused function (aea/cli_gui/__init__.py:132)
create_agent  # unused function (aea/cli_gui/__init__.py:151)
delete_agent  # unused function (aea/cli_gui/__init__.py:165)
remove_local_item  # unused function (aea/cli_gui/__init__.py:215)
start_agent  # unused function (aea/cli_gui/__init__.py:273)
get_agent_status  # unused function (aea/cli_gui/__init__.py:358)
stop_agent  # unused function (aea/cli_gui/__init__.py:396)
_.ui_is_starting  # unused attribute (aea/cli_gui/__init__.py:412)
_.module_dir  # unused attribute (aea/cli_gui/__init__.py:414)
homejs  # unused function (aea/cli_gui/__init__.py:427)
favicon  # unused function (aea/cli_gui/__init__.py:434)
run_test  # unused function (aea/cli_gui/__init__.py:458)
unknown  # unused variable (aea/cli_gui/__main__.py:41)
STOPPING  # unused variable (aea/cli_gui/utils.py:35)
_call_subprocess  # unused function (aea/cli_gui/utils.py:44)
_.latest  # unused property (aea/configurations/base.py:384)
_.to_any  # unused property (aea/configurations/base.py:442)
_.to_latest  # unused property (aea/configurations/base.py:442)
_.to_uri_path  # unused property (aea/configurations/base.py:445)
_.to_uri_path  # unused property (aea/configurations/base.py:605)
_._ensure_connected  # unused method (aea/connections/base.py:104)
_._ensure_valid_envelope_for_external_comms  # unused method (aea/connections/base.py:109)
_._connect_context  # unused method (aea/connections/base.py:125)
_.has_crypto_store  # unused property (aea/connections/base.py:138)
_.from_dir  # unused method (aea/connections/base.py:200)
MyScaffoldConnection  # unused class (aea/connections/scaffold/connection.py:31)
_.get_instance  # unused method (aea/contracts/base.py:64)
_.from_dir  # unused method (aea/contracts/base.py:81)
_.get_raw_transaction  # unused method (aea/contracts/base.py:147)
_.get_raw_message  # unused method (aea/contracts/base.py:163)
MyScaffoldContract  # unused class (aea/contracts/scaffold/contract.py:25)
_.is_valid_address  # aea/crypto/cosmos.py:170: unused method 'is_valid_address' (60% confidence)
_.get_init_transaction  # unused method (aea/crypto/cosmos.py:437)
_.get_handle_transaction  # unused method (aea/crypto/cosmos.py:491)
_.try_execute_wasm_query  # unused method (aea/crypto/cosmos.py:571)
_.get_last_code_id  # unused method (aea/crypto/cosmos.py:837)
_.get_contract_address  # unused method (aea/crypto/cosmos.py:849)
CosmosFaucetApi  # unused class (aea/crypto/cosmos.py:867)
testnet_name  # unused variable (aea/crypto/cosmos.py:871)
EthereumFaucetApi  # unused class (aea/crypto/ethereum.py:507)
testnet_name  # unused variable (aea/crypto/ethereum.py:511)
FetchAIFaucetApi  # unused class (aea/crypto/fetchai.py:404)
testnet_name  # unused variable (aea/crypto/fetchai.py:408)
_.has_ledger  # unused method (aea/crypto/ledger_apis.py:55)
_.get_api  # unused method (aea/crypto/ledger_apis.py:60)
_.has_spec  # unused method (aea/crypto/registries/base.py:236)
_.main_cryptos  # unused property (aea/crypto/wallet.py:130)
AwaitableProc  # unused class (aea/helpers/async_utils.py:391)
locate  # unused function (aea/helpers/base.py:139)
sigint_crossplatform  # unused function (aea/helpers/base.py:236)
_.dwFlags  # unused attribute (aea/helpers/base.py:269)
retry_decorator  # unused function (aea/helpers/base.py:386)
_.is_empty  # unused property (aea/helpers/dialogue/base.py:431)
_.self_initiated  # unused property (aea/helpers/dialogue/base.py:687)
_.other_initiated  # unused property (aea/helpers/dialogue/base.py:692)
_.add_dialogue_endstate  # unused method (aea/helpers/dialogue/base.py:697)
_.dialogue_stats  # unused property (aea/helpers/dialogue/base.py:767)
_.is_cancelled_by_timeout  # unused method (aea/helpers/exec_timeout.py:51)
exc_tb  # unused variable (aea/helpers/exec_timeout.py:102)
exc_type  # unused variable (aea/helpers/exec_timeout.py:102)
ExecTimeoutSigAlarm  # unused class (aea/helpers/exec_timeout.py:138)
envelope_from_bytes  # unused function (aea/helpers/file_lock.py:112)
LOCK_SH  # unused variable (aea/helpers/file_lock.py:32)
LOCK_NB  # unused variable (aea/helpers/file_lock.py:33)
_.filesize  # unused attribute (aea/helpers/ipfs/base.py:92)
MultiAddr  # unused class (aea/helpers/multiaddr/base.py:82)
_.in_path  # unused property (aea/helpers/pipe.py:70)
_.out_path  # unused property (aea/helpers/pipe.py:77)
_.in_path  # unused property (aea/helpers/pipe.py:171)
_.out_path  # unused property (aea/helpers/pipe.py:175)
_.in_path  # unused property (aea/helpers/pipe.py:305)
_.out_path  # unused property (aea/helpers/pipe.py:309)
make_ipc_channel  # unused function (aea/helpers/pipe.py:647)
make_ipc_channel_client  # unused function (aea/helpers/pipe.py:663)
to_set_specifier  # unused function (aea/helpers/pypi.py:199)
GenericDataModel  # unused class (aea/helpers/search/generic.py:29)
AGENT_LOCATION_MODEL  # unused variable (aea/helpers/search/generic.py:54)
AGENT_PERSONALITY_MODEL  # unused variable (aea/helpers/search/generic.py:61)
AGENT_SET_SERVICE_MODEL  # unused variable (aea/helpers/search/generic.py:71)
SIMPLE_SERVICE_MODEL  # unused variable (aea/helpers/search/generic.py:81)
SIMPLE_DATA_MODEL  # unused variable (aea/helpers/search/generic.py:88)
AGENT_REMOVE_SERVICE_MODEL  # unused variable (aea/helpers/search/generic.py:95)
_.counterparty_hash  # unused property (aea/helpers/transaction/base.py:529)
_.sender_payable_amount_incl_fee  # unused property (aea/helpers/transaction/base.py:598)
_.counterparty_payable_amount_incl_fee  # unused property (aea/helpers/transaction/base.py:623)
_.sender_fee  # unused property (aea/helpers/transaction/base.py:673)
_.counterparty_fee  # unused property (aea/helpers/transaction/base.py:679)
_.is_connecting  # unused attribute (aea/multiplexer.py:53)
_.put_message  # unused method (aea/multiplexer.py:821)
_.has_to  # unused property (aea/protocols/base.py:100)
ProtobufSerializer  # unused class (aea/protocols/base.py:278)
JSONSerializer  # unused class (aea/protocols/base.py:304)
_.from_dir  # unused method (aea/protocols/base.py:359)
INVALID_MESSAGE  # unused variable (aea/protocols/default/custom_types.py:30)
INVALID_DIALOGUE  # unused variable (aea/protocols/default/custom_types.py:32)
_.get_all_protocols  # unused method (aea/registries/resources.py:124)
_.remove_protocol  # unused method (aea/registries/resources.py:133)
_.get_contract  # unused method (aea/registries/resources.py:153)
_.get_all_contracts  # unused method (aea/registries/resources.py:165)
_.remove_contract  # unused method (aea/registries/resources.py:174)
_.get_connection  # unused method (aea/registries/resources.py:194)
_.remove_connection  # unused method (aea/registries/resources.py:215)
_.get_skill  # unused method (aea/registries/resources.py:248)
_.remove_skill  # unused method (aea/registries/resources.py:269)
_.get_all_handlers  # unused method (aea/registries/resources.py:309)
_.get_behaviour  # unused method (aea/registries/resources.py:318)
_.get_behaviours  # unused method (aea/registries/resources.py:331)
PUBLIC_ID  # unused variable (aea/skills/__init__.py:25)
_.agent_addresses  # unused property (aea/skills/base.py:154)
_.from_dir  # unused method (aea/skills/base.py:683)
CyclicBehaviour  # unused class (aea/skills/behaviours.py:57)
_.number_of_executions  # unused property (aea/skills/behaviours.py:66)
OneShotBehaviour  # unused class (aea/skills/behaviours.py:80)
TickerBehaviour  # unused class (aea/skills/behaviours.py:99)
_.last_act_time  # unused property (aea/skills/behaviours.py:135)
SequenceBehaviour  # unused class (aea/skills/behaviours.py:159)
FSMBehaviour  # unused class (aea/skills/behaviours.py:243)
_.is_started  # unused property (aea/skills/behaviours.py:258)
_.register_state  # unused method (aea/skills/behaviours.py:263)
_.register_final_state  # unused method (aea/skills/behaviours.py:280)
_.unregister_state  # unused method (aea/skills/behaviours.py:294)
_.final_states  # unused property (aea/skills/behaviours.py:331)
_.register_transition  # unused method (aea/skills/behaviours.py:364)
_.unregister_transition  # unused method (aea/skills/behaviours.py:383)
MyScaffoldBehaviour  # unused class (aea/skills/scaffold/behaviours.py:25)
MyScaffoldHandler  # unused class (aea/skills/scaffold/handlers.py:29)
MyModel  # unused class (aea/skills/scaffold/my_model.py:25)
_.is_executed  # unused property (aea/skills/tasks.py:68)
_.is_started  # unused property (aea/skills/tasks.py:146)
_.disable_aea_logging  # unused method (aea/test_tools/test_cases.py:134)
_.start_subprocess  # unused method (aea/test_tools/test_cases.py:198)
_.difference_to_fetched_agent  # unused method (aea/test_tools/test_cases.py:256)
_.delete_agents  # unused method (aea/test_tools/test_cases.py:328)
_.run_agent  # unused method (aea/test_tools/test_cases.py:341)
_.run_interaction  # unused method (aea/test_tools/test_cases.py:354)
_.is_successfully_terminated  # unused method (aea/test_tools/test_cases.py:407)
_.fingerprint_item  # unused method (aea/test_tools/test_cases.py:457)
_.eject_item  # unused method (aea/test_tools/test_cases.py:473)
_.run_install  # unused method (aea/test_tools/test_cases.py:488)
_.replace_private_key_in_file  # unused method (aea/test_tools/test_cases.py:549)
_.replace_file_content  # unused method (aea/test_tools/test_cases.py:596)
_.send_envelope_to_agent  # unused method (aea/test_tools/test_cases.py:685)
_.read_envelope_from_agent  # unused method (aea/test_tools/test_cases.py:694)
_._is_teardown_class_called  # unused attribute (aea/test_tools/test_cases.py:801)
UseOef  # unused class (aea/test_tools/test_cases.py:804)
_._start_oef_node  # unused method (aea/test_tools/test_cases.py:808)
network_node  # unused variable (aea/test_tools/test_cases.py:809)
_.get_dialogues_with_counterparty  # unused method (aea/protocols/dialogue/base.py:999)
receiver_address  # unused variable (aea/decision_maker/default.py:70)
receiver_address  # unused variable (aea/decision_maker/default.py:99)
create_with_message  # unused method (aea/helpers/dialogue/base.py:1054)
_.is_disconnecting  # unused property (aea/multiplexer.py:67)
_.get_quantity_in_outbox  # unused method (aea/test_tools/test_skills.py:52)
_.get_message_from_outbox  # unused method (aea/test_tools/test_skills.py:56)
_.drop_messages_from_outbox  # unused method (aea/test_tools/test_skills.py:70)
_.drop_messages_from_decision_maker_inbox  # unused method (aea/test_tools/test_skills.py:86)
_.get_quantity_in_decision_maker_inbox  # unused method (aea/test_tools/test_skills.py:69)
_.get_message_from_decision_maker_inbox  # unused method (aea/test_tools/test_skills.py:73)
_.assert_quantity_in_outbox  # unused method (aea/test_tools/test_skills.py:79)
_.assert_quantity_in_decision_making_queue  # unused method (aea/test_tools/test_skills.py:86)
_.message_has_attributes  # unused method (aea/test_tools/test_skills.py:69)
_.build_incoming_message_for_skill_dialogue  # unused method (aea/test_tools/test_skills.py:155)
_.prepare_skill_dialogue  # unused method (aea/test_tools/test_skills.py:290)
_.__defaults__  # unused attribute (aea/protocols/dialogue/base.py:49)
_.build_incoming_message_for_dialogue  # unused method (aea/test_tools/test_skills.py:155)
_._has_message  # unused method (aea/protocols/dialogue/base.py:491)
MultiAgentManager  # unused class (aea/manager.py:127)
_.add_error_callback  # unused method (aea/manager.py:202)
_.start_manager  # unused method (aea/manager.py:208)
_.stop_manager  # unused method (aea/manager.py:221)
_.add_project  # unused method (aea/manager.py:263)
_.list_projects  # unused method (aea/manager.py:283)
_.list_agents_info  # unused method (aea/manager.py:283)
_.add_agent  # unused method (aea/manager.py:291)
_.start_all_agents  # unused method (aea/manager.py:396)
_.get_agent_alias  # unused method (aea/manager.py:486)
_.DEFAULT_PYPI_INDEX_URL  # unused variable (aea/configurations/base.py:85)
AEARunner  # unused class (aea/runner.py:84)
_.join_thread  # unused method (aea/helpers/multiple_executor.py:430)
_.valid_performatives  # unused property (aea/protocols/base.py:90)
_.has_dialogue_info  # unused property (aea/protocols/base.py:244)
get_state  # aea/crypto/base.py:251: unused method 'get_state' (60% confidence)
_.load_agent_config  # unused method (aea/test_tools/test_cases.py:801)
_.UseGanache  # unused class (aea/test_tools/test_cases.py:871)
_._start_ganache  # unused method (aea/test_tools/test_cases.py:875)
_.ganache  # unused variable (aea/test_tools/test_cases.py:876:)
_.unsupported_protocol_count
_.unsupported_skill_count
_.decoding_error_count
_.ErrorHandler  # unused class (aea/error_handler/scaffold.py:27)
ensure_dir  # unused function (aea/helpers/base.py:561)
_.get_agent_overridables  # unused method (aea/manager/manager.py:419)
_.set_agent_overrides  # unused method (aea/manager/manager.py:432)
by_path  # unused function (aea/cli/fingerprint.py:94)
AgentRecord  # unused class (aea/helpers/acn/agent_record.py:49)
check_validity  # unused method (aea/helpers/acn/agent_record.py:96)
signature_from_cert_request  # unused function (aea/helpers/acn/agent_record.py:51)
Uri  # unused class (aea/helpers/acn/uri.py:26)
not_before_string  # unused property (aea/helpers/base.py:724)
not_after_string  # unused property (aea/helpers/base.py:729)
