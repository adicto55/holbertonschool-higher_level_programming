#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list and return the number of elements printed"""
    printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
    except IndexError:
        pass
    print()
    return printed
