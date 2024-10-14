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

try except doesn't catch external sigterm (perhaps obvious)
```
$ python3 hello_py_term.py &
[1] 49723
$ pid=$!
$ echo $pid
49723
$ kill -TERM $pid
[1]  + terminated  python3 hello_py_term.py # no exception handler invoked
```

with python signal handler
```
$ python3 hello_py_term.py &
[1] 50845
$ kill -TERM $(pgrep -i python)
Exiting gracefully
[1]  + done       python3 term_good.py
```