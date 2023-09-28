from LDMX.Framework import ldmxcfg
p = ldmxcfg.Process('prod')
p.run = 1
p.maxEvents = 3
p.sequence = [
    ldmxcfg.Producer('Produce','bench::Produce','Bench'),
    ]
p.termLogLevel = 0
p.logFrequency = 1
p.outputFiles = [ 'test_produce.root' ]
