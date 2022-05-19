#!/bin/bash

DST_ADDR=$1
MIN_SIZE=1400
MAX_SIZE=1550

for ((i=$MIN_SIZE; i <= $MAX_SIZE; i++)); do
    python client.py $DST_ADDR $i
    if [ $? -ne 0 ]; then
	    exit 1
    fi
done

