#!/usr/bin/env python
"""Display the SeqFeatures produced by the parser.

This produces a ton of output so it is possible to hand check what is
produced by the parser with the original GenBank file to make sure
everything is being parsed and output properly.

Usage:
./check_output.py <GenBank file to parse>

"""
# standard library
from __future__ import print_function

import sys

# GenBank stuff to test
from Bio import GenBank

if len(sys.argv) != 2:
    print("Usage ./check_output.py <GenBank file to parse>")
    sys.exit()

parser = GenBank.FeatureParser(debug_level=2)

with open(sys.argv[1], 'r') as handle:

    iterator = GenBank.Iterator(handle, parser)

    while True:
        cur_record = next(iterator)

        if not cur_record:
            break

        print("***Record")
        print("Seq: {0!s}".format(cur_record.seq))
        print("Id: {0!s}".format(cur_record.id))
        print("Name: {0!s}".format(cur_record.name))
        print("Description: {0!s}".format(cur_record.description))
        print("Annotations****")
        for annotation_key in cur_record.annotations:
            if annotation_key != 'references':
                print("Key: {0!s}".format(annotation_key))
                print("Value: {0!s}".format(cur_record.annotations[annotation_key]))
            else:
                print("References*")
                for reference in cur_record.annotations[annotation_key]:
                    print(str(reference))
        print("Feaures")
        for feature in cur_record.features:
            print(feature)
