#!/usr/bin/python3
for i in range(1, 9):
    for x in range(0, 10):
        if i != x:
            if i == 8 and x == 9:
                print("{}{}".format(i,x))
            else:
                print("{}{}, ".format(i,x), end='')
