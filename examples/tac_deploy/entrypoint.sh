#!/bin/bash
set -e

LEDGER=fetchai
PEER="/dns4/acn.fetch.ai/tcp/9001/p2p/16Uiu2HAmVWnopQAqq4pniYLw44VRvYxBUoRHqjz1Hh2SoCyjbyRW"

TAC_NAME='some_tac_id'
BASE_PORT=10000


BASE_DIR=/data

if [ -z  "$COMPETITION_TIMEOUT" ];
then
	COMPETITION_TIMEOUT=86400
fi

if [ -z  "$INACTIVITY_TIMEOUT" ];
then
	INACTIVITY_TIMEOUT=3600
fi

if [ -z  "$PARTICIPANTS_AMOUNT" ];
then
	PARTICIPANTS_AMOUNT=2
fi


if [ -z  "$MINUTES_TILL_START" ];
then
	MINUTES_TILL_START=2
fi




function generate_key (){
	ledger=$1
	prefix=$2
	base_dir=$3
	connection=$4
	if [ $connection = '1' ];
	then
		connection='_connection'
	else
		connection=''
	fi
	filename="${base_dir}/${prefix}_${ledger}${connection}_private_key.txt"
	
	if [ -e "${filename}" ];
	then
		echo > /dev/null
	else
	 aea generate-key $ledger $filename $con_option
	fi
	echo ${filename}
}

function set_agent(){
	name=$1
	port=$2
	echo name $name port $port
	agent_data_dir=$BASE_DIR/$name
	mkdir -p $agent_data_dir
	key_file_name=$(generate_key $LEDGER $name $agent_data_dir 0)
	aea add-key fetchai $key_file_name	
	key_file_name=$(generate_key $LEDGER $name $agent_data_dir 1)
	aea add-key fetchai $key_file_name --connection
	aea issue-certificates
	json=$(printf '{"delegate_uri": null, "entry_peers": ["%s"], "local_uri": "127.0.0.1:%s", "public_uri": null}' "$PEER" "$port")
	aea config set --type dict vendor.fetchai.connections.p2p_libp2p.config "$json"
	log_file=$agent_data_dir/$name.log
	json=$(printf '{"version": 1, "handlers": {"console": {"class": "logging.StreamHandler", "level": "DEBUG"}, "file": {"class": "logging.FileHandler", "filename": "%s", "mode": "w", "level": "DEBUG"}}, "loggers": {"aea": {"level": "DEBUG", "handlers": ["console", "file"]}}}' "$log_file")
	aea config set --type dict agent.logging_config "$json"
	aea config set vendor.fetchai.connections.soef.config.token_storage_path $agent_data_dir/soef_token.txt
}

function set_tac_name (){
	json=$(printf '{"key": "tac", "value": "%s"}' $TAC_NAME)
	aea config set --type dict vendor.fetchai.skills.tac_control.models.parameters.args.service_data "$json"
}

function set_participant(){
	agent_id=$1
	agent_name=$2
	echo "cp -r tac_participant_template $agent_name"
	cp -r tac_participant_template $agent_name
	cd $agent_name
	# cause set agent name is not allowed!
	sed -e "s/tac_participant_template/$agent_name/" -i ./aea-config.yaml
	set_agent $agent_name $(expr $BASE_PORT + $agent_id)
	aea config set vendor.fetchai.skills.tac_participation.models.game.args.search_query.search_value $TAC_NAME
	cd ..
}


agents_list=''
for i in $(seq $PARTICIPANTS_AMOUNT);
do
	agent_name="tac_participant_$i"
	set_participant $i $agent_name
	agents_list="$agent_name $agents_list"
done



cd tac_controller
set_agent tac_controller $BASE_PORT
set_tac_name
datetime_start=$(date -d@"$(( `date +%s`+$MINUTES_TILL_START*60))" "+%d %m %Y %H:%M")
aea config set vendor.fetchai.skills.tac_control.models.parameters.args.registration_start_time "$datetime_start"
aea config set vendor.fetchai.skills.tac_control.models.parameters.args.competition_timeout $COMPETITION_TIMEOUT
aea config set vendor.fetchai.skills.tac_control.models.parameters.args.inactivity_timeout $INACTIVITY_TIMEOUT
cd ..

aea launch tac_controller $agents_list
