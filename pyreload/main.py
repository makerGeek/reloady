#!/usr/bin/python

import sys

from pyreload import PyReload


def main() -> None:
    if (len(sys.argv) == 1 or "--help" in sys.argv or "-h" in sys.argv):
        PyReload().display_help()
    else:
        program = sys.argv[1]
        args = sys.argv[2:]
        PyReload(program, args).start()

if __name__ == "__main__":
    main()