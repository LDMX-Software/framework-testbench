"""load a file and print the performance data"""

import uproot
import sys
import json

class ReprEncoder(json.JSONEncoder):
    """if JSON can't serialize it, just use its repr string"""
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return repr(obj)


with uproot.open(sys.argv[1]) as f:
    print('absolute')
    t = f['performance/absolute'].members
    print(t['duration_'], t['start_time_'])
    for callback in [
        'onProcessStart', 'onProcessEnd',
        'onFileOpen','onFileClose',
        'beforeNewRun', 'onNewRun'
    ]:
        print(callback)
        for name, timer in f[f'performance/{callback}'].items():
            print('  ', f'{name:10s}', f'{timer.members["duration_"]:.3e}', timer.members['start_time_'])

    t = f['performance/by_event']
    events = t.arrays(library='np')
    print(json.dumps(events, cls=ReprEncoder, indent=2))
