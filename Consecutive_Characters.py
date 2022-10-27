s=list(input())
k=a=0
for i in range(0,len(s)-1):
    if(s[i]==s[i+1]):
        a+=1
    else:
        a=0
    if(k<a):
        k=a
print(k+1)