#!/usr/bin/env python

import sys

# Incoming data is in the form of:
# node_id \t donated_rank
# Or of the form:
# "D + node_id" [outlinks]
# Or of the form:
# "O + node_id" old_rank

# Job of this map function is to combine the data together such that data of the
# form:
# node_id \t new_rank old_rank [outlinks]
# is passed to the reduce function

# Alpha constant
a = 0.85

# Threshold for stopping
threshold = 0.02

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

    # Case if we are dealing with the lines that contain the old ranks
    if line[0] == "O":
        space = line.find("\t")
        node_id = line[1:space]
        old_rank = line[space + 1:-1]
        old_rank_dict[node_id] = old_rank

    # Case if we are dealing with the lines that contain the page ranks
    else:
        # Parse
        space = line.find("\t")
        node_id = line[:space]
        new_rank = line[space + 1:-1]
        new_rank_dict[node_id] = new_rank

# Output the stuff.
for node_id in outlinks_dict:
    # Should only occur if the node has no edges going into it. In this case,
    # the rank is simply (1 - alpha)
    if node_id not in new_rank_dict:
        new_rank_dict[node_id] = str(1 - a)

    if abs(float(new_rank_dict[node_id]) - float(old_rank_dict[node_id])) > threshold:
        done = False

    if outlinks_dict[node_id] != "":
        sys.stdout.write(node_id + "\t" + new_rank_dict[node_id] + "," + \
                         old_rank_dict[node_id] + "," + \
                         outlinks_dict[node_id] + "\n")
    else:
        sys.stdout.write(node_id + "\t" + new_rank_dict[node_id] + "," + \
                         old_rank_dict[node_id] + "\n")

# Output a "special line" which indicates if we are done or not
if done:
    sys.stdout.write("Done\t1\n")
else:
    sys.stdout.write("Done\t0\n")
