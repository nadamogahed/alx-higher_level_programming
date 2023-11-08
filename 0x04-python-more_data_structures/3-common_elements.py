#!/usr/bin/python3
def common_elements(set_1, set_2):
    com_set = set()
    for item in set_1:
        for sec_item in set_2:
            if item == sec_item:
                com_set.add(item)
            else:
                continue
    return com_set
