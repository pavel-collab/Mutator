# README

## How to run
Firstly you need to clone this rep to your local computer
```shell
git clone
```
You have two ways to execute file main.py. The first one is to run it by python interpritator
```shell
python3 main.py
```
The second one is to give main.py permition to execute and run it
```shell
chmod +x main.py
./main.py
```

You can run main.py with parametrs. The first parametr you may to run ,ain.py with is name of the file which programm will work with.
```shell
./main.py a.cpp
```
If you don't give this parametr, programm will work with default file h.cpp (from dir ./testcases). The second parametr you can give is a directory cantains cpp files.

```shell
./main.py a.cpp ./testcases/
```
If you don't give this parametr, programm will work with default directory ./testcases/
You can also give default parametr to the command line. If you want to do it, you need to run programm with *.
```shell
./main.py * *
```

For example, you want to work with default file, but in different directory:
```shell
./main.py * /path/tp/the/dir/
```