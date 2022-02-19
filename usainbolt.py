#https://algoleague.com/contest/algorithm-training-beginner-set/problem/usain-bolt/detail

n = int(input())
arr =  [int(x) for x in input().split()]
record = arr[0]
i,count= 0,0
while i < n:
    print(arr[i])
    if arr[i] > record:
        count+=1
        record = arr[i]
    i+=1

print(count)