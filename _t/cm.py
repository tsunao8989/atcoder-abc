from contextlib import contextmanager
import sys

@contextmanager
def switch_stdout(path):
    try:
        sys.stdout = open(path, 'a')
        yield
    finally:
        sys.stdout = sys.__stdout__

print('標準出力')
with switch_stdout('/tmp/sample.log'):
    print('標準出力')
    print('標準出力')
print('標準出力')
