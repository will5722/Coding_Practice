#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# Given a random array of numbers, print the ratio of positive, negative, and zeros
# to 6 decimal places.

def plusMinus(arr):
    # Write your code here
    pos, zero, neg = 0, 0, 0
    
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1

    print(round((pos/len(arr)), 6))
    print(round((neg/len(arr)), 6))
    print(round((zero/len(arr)), 6))
            
            
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)