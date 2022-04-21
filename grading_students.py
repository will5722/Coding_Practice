#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    #Create empty list to store grades
    grade_list = []
    #Loop through grades, use if/else. Check if grade needs rounding first.
    for grade in grades:
        if grade < 38 or grade%5 < 3:
            grade_list.append(grade)
        else:
            grade_list.append(grade + (5 - grade%5))
    #Return the list of grades.        
    return grade_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()