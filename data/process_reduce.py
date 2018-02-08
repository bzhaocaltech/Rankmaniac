#!/usr/bin/env python

import sys

# One of the lines should either be "Done\t1" or "Done\t0" which indicates
# if we are done or not
# The other lines should be in the form of:
# node_id \t new_rank old_rank [outlinks]

# The current iteration
iteration = 1

# The maximum # of iterations possible
max_iter = 2

input_data = []

for line in sys.stdin:
    # Encountered special "is done" line
    if line[0:4] == "Done":
        space = line.find('\t')
        is_done = int(line[space:-1])
    # Special line for the iteration number
    elif line[0] == "I":
        space = line.find('\t')
        iteration = int(line[space:-1])
    else:
        input_data.append(line)

# We are done. Output top 20 nodes
if is_done == 1 or iteration >= max_iter:
    rank_dict = {}

    # Parse the input
    for line in input_data:
        # Get the node id
        space = line.find('\t')
        node_id = line[:space]

        # Get the current page rank
        line = line[space + 1:-1]
        line = line.split(',')
        curr_page_rank = float(line[0])

        rank_dict[node_id] = curr_page_rank

    # Sort rank_dict
    rank_dict = sorted([(value, key) for (key, value) in rank_dict.iteritems()], \
                reverse = True)

    count = 0
    for rank, node_id in rank_dict:
        if count >= 20:
            break;
        sys.stdout.write("FinalRank:" + str(rank) + "\t" + node_id + "\n")
        count += 1
# We are not done. Just output the input_data with "NodeID:" appended
else:
    for line in input_data:
        sys.stdout.write("NodeId:" + line)
    sys.stdout.write("I\t" + str(iteration + 1) + "\n")
