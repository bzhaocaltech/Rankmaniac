#!/bin/bash

while true; do

    python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt
    if grep -x ^FinalRank.* output.txt; 
    then
        echo "It's there!"
        break
    else
        echo "No luck this time."
        cp output.txt input.txt
    fi
done
