#https://algoleague.com/contest/algorithm-training-beginner-set/problem/stringer-things/submission/3a02247c-0193-442f-b170-d0dc3679f1a0/validate
from itertools import groupby

n = int(input())
word = input().strip()
print(''.join([x[0] for x in groupby(word)]))

