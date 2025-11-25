#!/usr/bin/python3                                                                                                
def print_last_digit(number):
    remainder=0
    if number>=0:
        remainder=number%10
    else:
        remainder=(10-number%10)%10
    print(remainder,end='')
    return remainder
    
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
