#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# Given an array of numbers, print the minimum sum and the maximum sum of the numbers.

def miniMaxSum(arr):
    # Write your code here
    # Use min and max to subtract out the necessary number.
    min_sum = sum(arr) - max(arr)
    max_sum = sum(arr) - min(arr)
    
    # Print results, min first then max.
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
