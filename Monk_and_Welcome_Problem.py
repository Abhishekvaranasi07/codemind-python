n=int(input())
d=list(map(int,input().split()))
d1=list(map(int,input().split()))
e=[]
for i in range(n):
    c=d[i]+d1[i]
    e.append(c)
print(*e)