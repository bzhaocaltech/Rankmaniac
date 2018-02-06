#!/bin/bash

while true; do

    python ree.py < input.txt > output.txt
    if grep -x ^FinalRank.* output.txt; 
    then
        echo "It's there!"
        break
    else
        echo "No luck this time."
        cp output.txt input.txt
    fi
done
