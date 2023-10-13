from LDMX.Framework import ldmxcfg
p = ldmxcfg.Process('reco')
p.sequence = [
    ldmxcfg.Producer('Recon','bench::Recon','Bench'),
    ]
p.termLogLevel = 0
p.logFrequency = 1
import sys
p.inputFiles = sys.argv[1:]
p.outputFiles = [ 'test_recon.root' ]
