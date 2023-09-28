from LDMX.Framework import ldmxcfg

p = ldmxcfg.Process('exceptions')

import sys
proc = ldmxcfg.Producer('Exceptions','bench::Exceptions','Bench')
proc.when = sys.argv[1]

p.maxEvents = 3
p.sequence = [proc]
p.termLogLevel = 0
p.logFrequency = 1
p.outputFiles = [ '/dev/null' ]
