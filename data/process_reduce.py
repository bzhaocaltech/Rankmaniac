#!/usr/bin/env python

import sys

# Incoming data is in the form of:
# node_id \t donated_rank
# Or of the form:
# "D + node_id" [outlinks]
# Or of the form:
# "O + node_id" position

# Job of this map function is to combine the data together such that data of the
# form:
# node_id \t new_rank old_rank [outlinks]
# is passed to the reduce function

is_done = True

# The current iteration
iteration = 1

# The maximum # of iterations possible
max_iter = 50

# Threshold to determine if we are done with a node
threshold = 0.001

# The number of nodes to check if they switched positions
num_checked = 25

# Alpha constant
a = 0.85

outlinks_dict = {}
rank_dict = {}
position_dict = {}

for line in sys.stdin:
    # Case if we are dealing with the lines that contain the outlinks
    if line[0] == "D":
        space = line.find("\t")
        node_id = line[1:space]
        outlinks = line[space + 1:-1]
        outlinks_dict[node_id] = outlinks
    # Case if we are dealing with the lines that contain the old ranks
    elif line[0] == "O":
        space = line.find("\t")
        node_id = line[1:space]
        position = line[space + 1:-1]
        position_dict[node_id] = position
    # Special line for the iteration number
    elif line[0] == "I":
        space = line.find('\t')
        iteration = int(line[space:-1])
    # Case if we are dealing with the lines that contain the page ranks
    else:
        # Parse
        space = line.find("\t")
        node_id = line[:space]
        rank = line[space + 1:-1]
        rank_dict[node_id] = float(rank)

# Sort the data
sorted_rank_dict = sorted([(value, key) for (key, value) in rank_dict.iteritems()], \
                    reverse = True)

# Check if we are done by checking the old and new position of the nodes
curr_position = 1
for rank, node_id in sorted_rank_dict:
    if num_checked == 0:
        break;
    if curr_position != int(position_dict[node_id]):
        is_done = False
    num_checked -= 1
    curr_position += 1

# We are done. Output top 20 nodes
if is_done == 1 or iteration >= max_iter:
    nodes_outputted = 0
    for rank, node_id in sorted_rank_dict:
        if nodes_outputted >= 20:
            break;
        sys.stdout.write("FinalRank:" + str(rank) + "\t" + node_id + "\n")
        nodes_outputted += 1


# We are not done. Output the line in the correct format
else:
    # Assign ranks to the node ids without any nodes pointing to it
    for node_id in outlinks_dict:
        if node_id not in rank_dict:
            rank_dict[node_id] = 1 - a

    curr_position = 1
    for rank, node_id in sorted_rank_dict:
        if outlinks_dict[node_id] != "":
            sys.stdout.write("NodeId:" + node_id + "\t" + str(rank_dict[node_id]) + "," + \
                             str(curr_position) + "," + \
                             outlinks_dict[node_id] + "\n")
        else:
            sys.stdout.write("NodeId:" + node_id + "\t" + str(rank_dict[node_id]) + "," + \
                             str(curr_position) + "\n")
        curr_position += 1

    sys.stdout.write("I\t" + str(iteration + 1) + "\n")
