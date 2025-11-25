#!/usr/bin/python3                                                                                                                                
for i in range(122, 96, -1):
    if i%2==0:
        print(str.lower(chr(i)),end="")
    else:
        print(str.upper(chr(i)),end="")
