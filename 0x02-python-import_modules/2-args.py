#!/usr/bin/python3
import sys


def main(argv):
    print("{} arguments".format(len(argv)), end='')
    if len(argv) < 1:
        print(".")
    else:
        print(":")
    for i in range(len(argv)):
        print("{}: {}".format(i + 1, argv[i]))


if __name__ == "__main__":
    main(sys.argv[1:])
