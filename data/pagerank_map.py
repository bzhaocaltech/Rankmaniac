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
            sys.stdout.write("%s\t%s\n" % (node_id, curr_page_rank))
        else:
            # Keys are the outlinks the current node donates its page rank to
            # Value is the amount donated to the outlink
            for outlink in outlinks:
                donated_rank = float(curr_page_rank) / len(outlinks)
                sys.stdout.write("%s\t%f\n" % (outlink, donated_rank))

        # Pass the outlinks along. Use the special tag "D" to identify it (so that)
        # we don't do reduce on it
        sys.stdout.write("D%s\t%s\n" % (node_id, string_outlinks))

        # Pass the position of the current node along (1 for the node with
        # best rank, 2 for the node next node ...) Use "O" to denote these
        # positions
        sys.stdout.write("O%s\t%i\n" % (node_id, position))
