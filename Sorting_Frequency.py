n=int(input())
d=list(map(int,input().split()))## 6 6 4 7 5 4 4 3
c=[]
s=set(d) # 6 4 7 5 3
s=list(s) # [6 4 7 5 3]
s.sort()
for i in s:
    c.append(d.count(i)) #[1,3,1,2,1]
nw=[]
i=0
while len(c)>0:
    i1=c.index(max(c)) #nw=[4,6 3 5,7 ]
    nw.append(s[i1])
    c.remove(c[i1])
    s.remove(s[i1])
    i+=1
print(*nw)