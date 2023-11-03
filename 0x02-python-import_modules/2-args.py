#!/usr/bin/python3
import sys


def main(argv):
    if len(argv) == 1:
        print("{} argument:".format(len(argv)))
    else:
        print("{} arguments".format(len(argv)), end='')
    if len(argv) < 1:
        print(".")
    else:
        print(":")
    for i in range(len(argv)):
        print("{}: {}".format(i + 1, argv[i]))


if __name__ == "__main__":
    main(sys.argv[1:])
