#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        sentence[0] = None
    tuple_re = (len(sentence), sentence[0])
    return tuple_re
