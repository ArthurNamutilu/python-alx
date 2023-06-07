#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
ans = number % 10
if ans > 5:
    print(f"Last digit of {number} is {ans} and is greater than 5")
elif ans == 0:
    print(f"Last digit of {number} is {ans} and is 0")
elif ans < 6 and ans != 0:
    print(f"Last digit of {number} is {ans} and is less than 6 and not 0")
