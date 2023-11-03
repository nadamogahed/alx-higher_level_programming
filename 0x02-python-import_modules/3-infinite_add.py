#!/usr/bin/python3
import sys


def main(argv):
    result = 0
    for i in range(len(argv)):
        result = result + int(argv[i])
    print("{}".format(result))


if __name__ == "__main__":
    main(sys.argv[1:])
