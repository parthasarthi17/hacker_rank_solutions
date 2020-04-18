import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
        a=0
        for w in ar:
           a=a+w
           return a
    
if __name__ == '__main__':
    fptr = open(os.environ['1.txt'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    
    fptr.write(str(result) + '\n')

    fptr.close()