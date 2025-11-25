#!/usr/bin/python3
for i in range(0,8):
    for j in range(i*11+1,(i+1)*10):
        print("{:02d}".format(j),end=", ")
print("89")
