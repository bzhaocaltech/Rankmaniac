#!/usr/bin/env python

import sys

# Incoming data is in the form of:
# node_id \t donated_rank old_rank
# Or of the form:
# "D + node_id" [outlinks]

# Job of this map function is to combine the data together such that data of the
# form:
# node_id \t is_done new_rank old_rank [outlinks]
# is passed to the reduce function

outlinks_dict = {}
new_rank_dict = {}
old_rank_dict = {}
done_dict = {}

for line in sys.stdin:

    # Case if we are dealing with the lines that contain the outlinks
    if line[0] == "D":
        space = line.find("\t")
        node_id = line[1:space]
        outlinks = line[space:-1]
        outlinks_dict[node_id] = outlinks

    # Case if we are dealing with the lines that contain the page ranks
    else:
        # Parse
        space = line.find("\t")
        node_id = line[:space]
        value_array = line[space:-1].split(',')
        new_rank = value_array[0]
        old_rank = value_array[1]

        done_dict[node_id] = str(new_rank == old_rank)

        # Add the ranks to the corresponding dicts
        new_rank_dict[node_id] = new_rank
        old_rank_dict[node_id] = old_rank

# Output the stuff
for node_id in outlinks_dict:
    sys.stdout.write(node_id + "\t" + done_dict[node_id] + "," + \
                     new_rank_dict[node_id] + "," + old_rank_dict[node_id] \
                     + "," + outlinks_dict[node_id] + "\n")
