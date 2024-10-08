# python sigabrt repro

build the cpp code

on mac:
```
g++ -c -fPIC foo.cpp -o foo.o
g++ -shared -Wl,-install_name,libfoo.so -o libfoo.so  foo.o
```

on linux:
```
g++ -c -fPIC foo.cpp -o foo.o
g++ -shared -Wl,-soname,libfoo.so -o libfoo.so  foo.o
```

run it:

os.abort with try/except - no handler invoked
```
python3 hello_py_abort.py
zsh: abort      python3 hello_py_abort.py
```

cpp std:abort with try/except - no handler invoked
```
python3 hello_bad.py
Hello
zsh: abort      python3 hello_bad.py
```

ctypes add sigabrt handler for cpp std:sbort - handler invoked
```
python3 hello.py
Hello
SIGABRT handled by Ctypes
zsh: abort      python3 hello.py
```
