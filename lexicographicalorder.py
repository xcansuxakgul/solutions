# Problem : https://www.hackerrank.com/challenges/bigger-is-greater/problem
import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    n = len(w)

    for i in reversed(range(n-1)):

        for j in reversed(range(i+1,n)):

            if w[j] > w[i]:

                return w[:i] + w[j] + ''.join(sorted(w[i:j] + w[j+1:]))

    return 'no answer'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()


