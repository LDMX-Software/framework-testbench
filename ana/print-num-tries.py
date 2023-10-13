"""load a file and print the list of the number of tries it took to generate each event"""

import uproot
import sys

with uproot.open(sys.argv[1]) as f:
    print(f['LDMX_Events/EventHeader/tries_'].array(library='np'))

