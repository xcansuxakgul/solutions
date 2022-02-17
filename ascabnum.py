#https://algoleague.com/problem/askab-numbers/detail

N,a,b,c = map(int, input().split())
i= 1
st = set()
while True:
    if i % a == 0 or i % b == 0 or i % c == 0:
        st.add(i)
        if len(st) == N:
            print(i)
            break
    i+=1
