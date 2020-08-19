#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the factorial function below.
def factorial(n):
    fact = n
    while n >= 2:
        fact *= (n - 1)
        n -= 1
    return fact


n = int(input())
result = factorial(n)
print(result)
