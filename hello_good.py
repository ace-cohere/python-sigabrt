import ctypes
from signal import SIGABRT

c_globals = ctypes.CDLL(None) # POSIX

@ctypes.CFUNCTYPE(None, ctypes.c_int)
def sigabrt_handler(sig):
    print('SIGABRT handled by Ctypes')

c_globals.signal(SIGABRT, sigabrt_handler)

from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)

def main():
    f = Foo()
    try:
        f.bar()
    except Exception as e:
        print("SIGABRT handled by Python")
        print('Exception:', e)


if __name__ == "__main__":
    main()
