v,k=map(int,input().split())
l=0
if v>k:
    l=v
    while(l):
        if(l%v==0 and l%k==0):
           print(l)
           break
        l+=1
else:
    l=k
    while(l):
        if(l%v==0 and l%k==0):
            print(l)
            break
        l+=1