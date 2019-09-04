"""
Counting Valleys

Reference:
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

Sample Input
8
UDDDUDUU

Sample Output
1

"""

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = 0
    is_descending = False
    valley_count = 0

    for char in s:
        if char == 'U':
            altitude += 1
        else:
            altitude -= 1

        if altitude < 0:
            is_descending = True

        if is_descending and altitude == 0:
            valley_count += 1
            is_descending = False

    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
