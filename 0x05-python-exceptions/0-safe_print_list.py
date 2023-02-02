#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    index = 0;
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
            index +=1
        print()
        return index
    except IndexError:
        print()
        return index