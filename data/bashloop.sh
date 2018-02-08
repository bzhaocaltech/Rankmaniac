#!/bin/bash
start_time="$(date -u +%s.%N)"
python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt
if grep -x ^FinalRank.* output.txt; 
then
    echo "It's there!"
    break
else
    echo "No luck this time."
    cp output.txt temp.txt
    while true; do
		python pagerank_map.py < temp.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt
		if grep -x ^FinalRank.* output.txt; 
		then
		    echo "It's there!"
		    rm -f temp.txt
		    break
		else
		    echo "No luck this time."
		    cp output.txt temp.txt
		fi
	done

fi
end_time="$(date -u +%s.%N)"
elapsed="$(bc <<<"$end_time-$start_time")"
echo "Total of $elapsed seconds elapsed for process"

