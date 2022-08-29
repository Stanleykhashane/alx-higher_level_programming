#!/usr/bin/python3
for ch in range(97, 123):
    print("{:c}".format(ch).replace("q", "").replace("e", ""), end='')
