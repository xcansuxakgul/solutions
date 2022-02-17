# https://algoleague.com/problem/set-bits/detail

def decimalToBinary(n):
    return "{0:b}".format(int(n))
   
# Driver code
if __name__ == '__main__':
    num = input().strip()
    x =  decimalToBinary(num)
    ls = [ x for x in str(x)]
    print(ls.count('1'))
