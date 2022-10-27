a=input()
l=input()
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    if k==l:
        print(v)
        break
else:
    print(-1)