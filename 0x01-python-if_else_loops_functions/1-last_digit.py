#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    dgit = number % 10
else:
    dgit = number % -10

if dgit > 5:
    print(f"Last digit of {number:d} is {dgit} and is greater than 5")
elif dgit == 0:
    print(f"Last digit of {number:d} is {dgit} and is 0")
elif dgit < 6:
    print(f"Last digit of {number:d} is {dgit} and is less than 6 and not 0")
