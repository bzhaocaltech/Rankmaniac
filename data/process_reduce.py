#!/usr/bin/env python

import sys

# One of the lines should either be "Done\t1" or "Done\t0" which indicates
# if we are done or not
# The other lines should be in the form of:
# node_id \t new_rank old_rank [outlinks]

input_data = []

for line in sys.stdin:
    # Encountered special "is done" line
    if line[0:4] == "Done":
        space = line.find('\t')
        is_done = int(line[space:-1])

    else:
        input_data.append(line)

# We are not done. Just output the input_data with "NodeID:" appended
if is_done == 0:
    for line in input_data:
        sys.stdout.write("NodeId:" + line)

# We are done. Output top 20 nodes
if is_done == 1:
    rank_dict = {}

    # Parse the input
    for line in input_data:
        # Get the node id
        space = line.find('\t')
        node_id = line[:space]

        # Get the current page rank
        line = line[space + 1:-1]
        line = line.split(',')
        curr_page_rank = line[0]

        rank_dict[node_id] = curr_page_rank

    # Sort rank_dict
    rank_dict = sorted([(value, key) for (key, value) in rank_dict.iteritems()], \
                reverse = True)

    count = 0
    for node_id, rank in rank_dict:
        if count >= 20:
            break;
        sys.stdout.write("FinalRank:" + rank + "\t" + node_id + "\n")
        count += 1
