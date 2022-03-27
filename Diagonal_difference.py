#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    # Set two variables for the lines.
    diag1 = 0
    diag2 = 0
    # Need to loop through the array to locate each number for each line, add to corresponding line.
    # diag2 will be opposite of diag1 in regarding locating the correct numbers.
    # Find the difference between the two lines after finding both the sums.
    for i in range(len(arr)):
        diag1 += arr[i][i]
        diag2 += arr[i][-(i+1)]
    return abs(diag1 - diag2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
