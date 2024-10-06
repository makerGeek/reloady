# python-hotreload
automatically reexecutes python files when it detects changes

Port of [Jesper's SourceChangeMonitor.py](https://jesper.borgstrup.dk/2011/10/restart-python-program-if-source-has-been-modified/) to python 3

Instructions on how to use are [here](https://jesper.borgstrup.dk/2011/10/restart-python-program-if-source-has-been-modified/)  ( or on [Wayback machine](https://web.archive.org/web/20200804150140/https://jesper.borgstrup.dk/2011/10/restart-python-program-if-source-has-been-modified/),  just in case.. )


## Installation

```bash
pip install pyreload
```

## Use cases
This package is a command line tool that can be used to automatically restart a python program when it detects changes in the source code.
It is designed to be used in development environments where you want to make changes to your code and see the results immediately without manually restarting the program.
Some examples use cases are:
 - competitions where you want to make changes to your code and see the results immediately without manually restarting the program.
 - training for problems on [leetcode](https://leetcode.com/) or [codewars](https://www.codewars.com/) where you want to make changes to your code and see the results immediately without manually restarting the program.
 - debugging problems in a running program by making changes to the code and see the results immediately without manually restarting the program.

## Usage
```bash
pyreload main.py
```

## with arguments
```bash
pyreload main.py arg1 arg2
```

## examples
```bash
cd examples/two_sum
pyreload main.py
```
In this example, the program will automatically restart when changes are detected in either `main.py` or `two_sum.py`.


