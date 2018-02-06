#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# Incoming data is in the form of:
# node_id \t donated_rank

# Output data is in the form of:
# node_id \t new_rank

# Occasionally incoming data will be in the form of:
# "D + node_id" [outlinks]
# or
# "O + node_id" old_rank
# ignore these lines. Just pass them along

# Alpha constant
a = 0.85

# Collect items into the dictionary
# Final form of dictionary will be:
# node_id: [new_value, prev_value]
d = {}

for line in sys.stdin:
    # If we are dealing with a line that just has the outlinks of a node or
    # the old rank of the node. Just pass it along to the next map function
    if line[0] == "D" or line[0] == "O" or line[0] == "I":
        sys.stdout.write(line)

    else:
        # Parse the input
        space = line.find("\t")
        node_id = line[:space]
        value_array = line[space:-1].split(',')
        donated_value = float(value_array[0])

        if node_id in d:
            d[node_id] += a * donated_value
        else:
            d[node_id] = a * donated_value + (1 - a)

for node, value in d.iteritems():
    sys.stdout.write(node + "\t" + str(value) + "\n")
