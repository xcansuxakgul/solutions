# problem :  https://algoleague.com/problem/palindrome-digit-sum/detail

def is_palindrome(x):
    if str(x) == str(x)[::-1]: return 1
    else: return 0
    
max = 0    
n = int(input())
for i in range(0,n):
    if is_palindrome(i):
        ls = list(str(i))
        if sum([int(a) for a in ls])> max: max= sum([int(a) for a in ls])
print(max)
