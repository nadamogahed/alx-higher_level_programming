#!/usr/bin/python3
for i in range(0, 9):
    for x in range(1, 10):
        if i == x:
            continue
        elif x < i:
            x = i + 1
        elif i == 8 and x == 9:
            print("{}{}".format(i, x))
        else:
            print("{}{}, ".format(i, x), end='')
