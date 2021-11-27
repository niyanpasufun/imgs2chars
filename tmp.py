import sys
import time

seq = ['1', '2', '3', '4', '5']

for el in seq:
    print(el, end='', flush=True)
    time.sleep(0.5)

for idx, el in enumerate(seq):
    print('\b', end='', flush=True)
    time.sleep(0.5)

seq.reverse()

for el in seq:
    print(el, end='', flush=True)
    time.sleep(0.5)
