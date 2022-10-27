x=0
for i in range(int(input())):
    n=input()
    if '++' in n:
        x+=1
    elif '--' in n:
        x-=1
print(x)