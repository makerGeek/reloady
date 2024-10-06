#!/usr/bin/python

import os
import sys

from pyreload import PyReload


def main() -> None:
    if (len(sys.argv) == 1 or "--help" in sys.argv or "-h" in sys.argv) and (
           not os.path.exists(os.path.join(os.getcwd(), 'main.py'))
           ):
        PyReload().display_help()  # Changed to PyReload
    else:
        program = sys.argv[1]
        args = sys.argv[2:]
        PyReload(program, args).start()  # Changed to PyReload

if __name__ == "__main__":
    main()