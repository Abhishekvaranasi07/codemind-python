n=int(input())
a=list(map(int,input().split()))
b=max(a)
i=1
while True:
    c=0
    for j in a:
        if b*i%j==0:
            c+=1
    if c==len(a):
        print(b*i)
        break
    i+=1