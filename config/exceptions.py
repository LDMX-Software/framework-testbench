from LDMX.Framework import ldmxcfg

p = ldmxcfg.Process('exceptions')

import sys
proc = ldmxcfg.Producer('Exceptions','bench::Exceptions','Bench')
proc.when = sys.argv[1]
proc.type = sys.argv[2]

p.maxEvents = 3
p.sequence = [
    ldmxcfg.Producer('Produce','bench::Produce','Bench'),
    proc
    ]
p.termLogLevel = 0
p.logFrequency = 1
p.outputFiles = [ 'test_exceptions.root' ]
