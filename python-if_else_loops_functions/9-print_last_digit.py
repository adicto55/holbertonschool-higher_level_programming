#!/usr/bin/python3                                                                                                
def print_last_digit(number):
    remainder=0
    if number>=0:
        remainder=number%10
    else:
        remainder=(10-number%10)%10
    print(remainder,end='')
    return remainder
