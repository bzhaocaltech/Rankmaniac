#!/usr/bin/env python

import sys

# Incoming data is in the form of:
# node_id \t donated_rank old_rank
# Or of the form:
# "D + node_id" [outlinks]

# Job of this map function is to combine the data together such that data of the
# form:
# node_id \t new_rank old_rank [outlinks]
# is passed to the reduce function

# Alpha constant
a = 0.85

outlinks_dict = {}
new_rank_dict = {}
old_rank_dict = {}

done = True
for line in sys.stdin:
    # Case if we are dealing with the lines that contain the outlinks
    if line[0] == "D":
        space = line.find("\t")
        node_id = line[1:space]
        outlinks = line[space + 1:-1]
        outlinks_dict[node_id] = outlinks

    # Case if we are dealing with the lines that contain the page ranks
    else:
        # Parse
        space = line.find("\t")
        node_id = line[:space]
        value_array = line[space + 1:-1].split(',')
        new_rank = value_array[0]
        old_rank = value_array[1]

        if new_rank != old_rank:
            done = False

        # Add the ranks to the corresponding dicts
        new_rank_dict[node_id] = new_rank
        old_rank_dict[node_id] = old_rank

# Output a "special line" which indicates if we are done or not
if done:
    sys.stdout.write("Done\t1\n")
else:
    sys.stdout.write("Done\t0\n")

# Output the stuff.
for node_id in outlinks_dict:
    # Should only occur if the node has no edges going into it. In this case,
    # the rank is simply (1 - alpha)
    if node_id not in old_rank_dict:
        new_rank_dict[node_id] = str(1 - a)
        old_rank_dict[node_id] = str(1 - a)

    if outlinks_dict[node_id] != "":
        sys.stdout.write(node_id + "\t" + new_rank_dict[node_id] + "," + \
                         old_rank_dict[node_id] + "," + \
                         outlinks_dict[node_id] + "\n")
    else:
        sys.stdout.write(node_id + "\t" + new_rank_dict[node_id] + "," + \
                         old_rank_dict[node_id] + "\n")
