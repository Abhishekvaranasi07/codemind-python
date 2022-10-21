n=int(input())
d=list(map(int,input().split()))
m=int(input())
d1=list(map(int,input().split()))
t=[]
for i in range(n):
    t.insert(d1[i],d[i]) #insert(index position,number to be insterted)
print(*t)