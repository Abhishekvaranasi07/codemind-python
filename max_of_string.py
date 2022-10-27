v=input()
r=0
l=0
for k in range(0,len(v)):
    if r<ord(v[k]):
        r=ord(v[k])
        l=v[k]
print(l)