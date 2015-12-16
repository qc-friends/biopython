# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.
#

"""Example of connecting with exPASy and parsing SwissProt records."""

# biopython
from __future__ import print_function

from Bio import ExPASy, SwissProt

# 'O23729', 'O23730', 'O23731', Chalcone synthases from Orchid

ids = ['O23729', 'O23730', 'O23731']

for id in ids:
    handle = ExPASy.get_sprot_raw(id)
    record = SwissProt.read(handle)
    print("description: {0!s}".format(record.description))
    for ref in record.references:
        print("authors: {0!s}".format(ref.authors))
        print("title: {0!s}".format(ref.title))

    print("classification: {0!s}".format(record.organism_classification))
    print("")
