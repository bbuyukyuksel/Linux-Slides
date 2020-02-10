#!/usr/bin/env python3

import sys
import time
from subprocess import Popen,PIPE

if len(sys.argv) < 2:
    raise ValueError('Yetersiz Argüman')

_oldstdout = None
_is_first = True
while True:
   
    output = Popen("tail -n5 {}".format(sys.argv[1]), stdin=PIPE, stdout=PIPE, shell=True)
    _stdout = output.stdout.read().decode("utf-8")
    if 'tail' in _stdout:
        continue
    if _is_first == True:
        _is_first = False
        _oldstdout = _stdout
        continue

    time.sleep(0.5)
    if (_stdout != _oldstdout) and (not _is_first):
        print('\033[2J')
        print(_stdout)
        if sys.argv[2] in _stdout:
            print("#Yakalandı!")
        _oldstdout = _stdout
        del _stdout
    else:
        continue

