from functools import partial
FIX_SIZE = 32
with open('testt.data') as f:
    records = iter(partial(f.read()),b'')
    for i in records:
        pass
