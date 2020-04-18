
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice_score=0
    bob_score=0
    i=0
    for l in a:
        if l>b[i]:
            alice_score=alice_score+1
        elif l<b[i]:
            bob_score=bob_score+1
        i=i+1
    li=[alice_score,bob_score]
    return li
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)
    