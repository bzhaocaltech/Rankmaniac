#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Parse the input
    line = line[7:]

    # Get the node id
    space = line.find('\t')
    node_id = line[:space]

    # Get the current and previous page ranks
    line = line[space + 1:-1]
    line = line.split(',')
    curr_page_rank = float(line[0])
    prev_page_rank = float(line[1])

    # Get the outlinks
    outlinks = line[2:]

    # Outlinks as a string (to be outputted later)
    string_outlinks = ','.join(outlinks)

    # Output:
    # Keys are the outlinks the current node donates its page rank to
    # Value is the amount donated to the outlink
    for outlink in outlinks:
        donated_rank = curr_page_rank / len(outlinks)
        sys.stdout.write(outlink + "\t" + str(donated_rank) + \
                         "," + str(curr_page_rank) + "\n")

    # Pass the outlinks along. Use the special tag "D" to identify it (so that)
    # we don't do reduce on it
    sys.stdout.write("D" + node_id + "\t" + string_outlinks + "\n")
