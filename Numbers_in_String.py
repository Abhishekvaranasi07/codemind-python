v=input()
r=0
for k in range(0,len(v)):
    if(ord(v[k])>=48 and ord(v[k])<=57):
        r+=int(v[k])
print(r)