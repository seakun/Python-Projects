# 

# 2D Array - DS
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_totals = []
    for x in range(0, 4):
        for y in range(0, 4):
            hourglass_totals.append(arr[x][y] + arr[x][y + 1] + arr[x][y + 2] 
            + arr[x + 1][y + 1] 
            + arr[x + 2][y] + arr[x + 2][y + 1] + arr[x + 2][y + 2])
    print(hourglass_totals)
    return max(hourglass_totals)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# Arrays - DS
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    reverse_array = []
    for i in range(len(a) - 1, -1, -1):
        reverse_array.append(arr[i])
    return reverse_array
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
