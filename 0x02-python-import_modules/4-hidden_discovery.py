#!/usr/bin/python3
import hidden_4


def main():
    list_name = []
    for name in dir(hidden_4):
        if name[0] != "_":
            list_name.append(name)
    list_name.sort()
    for i in range(len(list_name)):
        print("{}".format(list_name[i]))


if __name__ == "__main__":
    main()
