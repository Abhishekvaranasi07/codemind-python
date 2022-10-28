def prm(k):
    c=0
    for i in range(1,k+1):
        if k%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
b=int(input())
k=a+b
while(k):
    k+=1
    if prm(k):
        print(k-a-b)
        break