from LDMX.Framework import ldmxcfg
p = ldmxcfg.Process('prod')
p.run = 1
p.maxEvents = 3
p.maxTriesPerEvent = 10
import sys
if len(sys.argv) > 1:
    p.maxTriesPerEvent = int(sys.argv[1])
p.sequence = [
    ldmxcfg.Producer('MultiTry','bench::MultiTry','Bench'),
    ]
p.termLogLevel = 0
p.logFrequency = 1
p.outputFiles = [ 'test_multitry.root' ]
