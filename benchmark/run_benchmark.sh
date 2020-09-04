#!/bin/bash
REPO="https://github.com/fetchai/agents-aea.git"
BRANCH=feature/benchmarks
TMP_DIR="$(mktemp -d -t bench-XXXXXXXXXX)"
git clone --branch $BRANCH $REPO $TMP_DIR

CURDIR=`pwd`
cd $TMP_DIR
pip install --upgrade aea
pipenv lock --requirements > requirements.txt
pip install -r requirements.txt



DATE=`LC_ALL=C date +"%d.%m.%Y %H:%M"`
RESULT_FILE="$CURDIR\$DATE.txt"
echo "Performance report for $DATE" | tee --append "$RESULT_FILE"
echo -e "-----------------------------\n" | tee --append "$RESULT_FILE"


DURATION=10
NUM_RUNS=100


echo "Reactive: number of runs: $NUM_RUNS, duration: $DURATION" | tee --append "$RESULT_FILE"
echo "----------------------------------------------------" | tee --append "$RESULT_FILE"
echo "runtime mode        value          mean        stdev" | tee --append "$RESULT_FILE"
echo "----------------------------------------------------" | tee --append "$RESULT_FILE"
for mode in threaded async;
do
	data=`./benchmark/checks/check_reactive.py --duration=$DURATION --number_of_runs=$NUM_RUNS --runtime_mode=$mode 2>/dev/null`
	latency=`echo "$data"|grep latency|awk '{print $4 "    " $6}'`
	rate=`echo "$data"|grep rate|awk '{print $4 "    " $6}'`
	echo -e "$mode    latency     ${latency}" | tee --append "$RESULT_FILE"
	echo -e "$mode    rate     ${rate}" | tee --append "$RESULT_FILE"

done


echo -e "\nProactive: number of runs: $NUM_RUNS, duration: $DURATION" | tee --append "$RESULT_FILE"
echo "----------------------------------------------------" | tee --append "$RESULT_FILE"
echo "runtime mode        value          mean        stdev" | tee --append "$RESULT_FILE"
echo "----------------------------------------------------" | tee --append "$RESULT_FILE"
for mode in threaded async;
do
	data=`./benchmark/checks/check_proactive.py --duration=$DURATION --number_of_runs=$NUM_RUNS --runtime_mode=$mode 2>/dev/null`
	latency=`echo "$data"|grep latency|awk '{print $4 "    " $6}'`
	rate=`echo "$data"|grep rate|awk '{print $4 "    " $6}'`
	echo -e "$mode    rate     ${rate}" | tee --append "$RESULT_FILE"

done

MESSAGES=100
echo -e "\nMultiAgent: number of runs: $NUM_RUNS, duration: $DURATION, messages: $MESSAGES"
echo "------------------------------------------------------------------"
echo "runtime mode     num_agents       value          mean        stdev"
echo "------------------------------------------------------------------"
for mode in threaded async;
do
	for agent in 2 4 8 16;
	do
		data=`./benchmark/checks/check_multiagent.py --num_of_agents=$agent --duration=$DURATION --number_of_runs=$NUM_RUNS --runtime_mode=$mode --start_messages=$MESSAGES --runner_mode=threaded 2>/dev/null`
		rate=`echo "$data"|grep rate|awk '{print $5 "    " $7}'`
		mem=`echo "$data"|grep Mem|awk '{print $5 "    " $7}'`
		echo -e "$mode     $agent    rate     ${rate}" | tee --append "$RESULT_FILE"
		echo -e "$mode     $agent    mem     ${mem}" | tee --append "$RESULT_FILE"
	done
done

rm -fr $TMPDIR
cd $CURDIR
