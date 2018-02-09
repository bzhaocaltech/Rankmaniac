#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Special character representing iteration #. In this case, just pass the
    # data along
    if line[0] == "I":
        sys.stdout.write(line)

    else:
        # Parse the input
        line = line[7:]

        # Get the node id
        space = line.find('\t')
        node_id = line[:space]

        # Get the current page ranks
        line = line[space + 1:-1]
        line = line.split(',')
        curr_page_rank = line[0]

        # Get the previous position of the page
        position = int(float(line[1]))

        # Get the outlinks
        outlinks = line[2:]

        # Outlinks as a string (to be outputted later)
        string_outlinks = ','.join(outlinks)

        # Output:
        # If there are no outlinks, donate to itself
        if len(outlinks) == 0:
            sys.stdout.write(node_id + "\t" + curr_page_rank + "\n")
        else:
            # Keys are the outlinks the current node donates its page rank to
            # Value is the amount donated to the outlink
            for outlink in outlinks:
                donated_rank = float(curr_page_rank) / len(outlinks)
                sys.stdout.write(outlink + "\t" + str(donated_rank) + "\n")

        # Pass the outlinks along. Use the special tag "D" to identify it (so that)
        # we don't do reduce on it
        sys.stdout.write("D" + node_id + "\t" + string_outlinks + "\n")

        # Pass the position of the current node along (1 for the node with
        # best rank, 2 for the node next node ...) Use "O" to denote these
        # positions
        sys.stdout.write("O" + node_id + "\t" + str(position) + "\n")
