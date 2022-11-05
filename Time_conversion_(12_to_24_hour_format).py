n=input()
f=n[6]+n[7]
r=''
r1=n[2]+n[3]+n[4]
if (f=="AM"):
    n=int(n[0]+n[1])
    if n==12:
        r+='00'
    elif (n<=9):
        n=str(n)
        r+='0'
        r+=n
    else:
        r+=str(n)
else:
    a=int(n[0]+n[1])
    if (a==12):
        r+=str(a)
    else:
        a+=12
        r+=str(a)
r+=r1
print(r)
    
