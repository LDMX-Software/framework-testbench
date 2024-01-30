from LDMX.Framework import ldmxcfg
p = ldmxcfg.Process('hist')
p.sequence = [
    ldmxcfg.Producer('MoveRootDir','bench::MoveRootDir','Bench'),
    ]
p.termLogLevel = 0
p.logFrequency = 1
import sys
if len(sys.argv) == 1:
    p.run = 1
    p.outputFiles = 'test_hist_empty.root'
else:
    p.inputFiles = sys.argv[1:]
    p.outputFiles = [ 'test_hist_merge.root' ]
p.histogramFile = 'test_hist.root'
