#!/usr/bin/python3
def delete_at(my_list=[], idx=0):    
    new_list = []
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    for i in my_list:
        if i == my_list[idx]:
            continue
        new_list.append(i)
    return new_list

