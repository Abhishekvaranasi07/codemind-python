
a=int(input())
for l in range(0,a):
    r=0
    v=input()
    for k in range(0,len(v)):
        if(ord(v[k])>=48 and ord(v[k])<=57):
            r+=1
            break
    if r!=0:
        print('Yes',end='
')
    else:
        print('No',end='
')