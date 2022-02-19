#https://algoleague.com/contest/algorithm-training-beginner-set/problem/ice-cream-yum-yum/detail

n = int(input())
a = [int(x) for x in input().split()]

a.sort()
a[0]=0
print(sum(a))