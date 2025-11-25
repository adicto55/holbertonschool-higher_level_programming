#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number>=0:
    print(number%10)
elif number<0:
    print((10-number%10)%10)
