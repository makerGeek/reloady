#!/usr/bin/python

import sys

from reloady import Reloady


def main() -> None:
    if (len(sys.argv) == 1 or "--help" in sys.argv or "-h" in sys.argv):
        Reloady().display_help()
    else:
        program = sys.argv[1]
        args = sys.argv[2:]
        Reloady(program, args).start()

if __name__ == "__main__":
    main()