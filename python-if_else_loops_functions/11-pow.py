#!/usr/bin/python3
def pow(a,b):
    s =1
    for i in range(0,b):
        s=s*a
    if b<0:
        for i in range(0,abs(b)):
            s=s*a
        s=1/s    
    return s
