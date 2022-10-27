k=0
for i in input():
    if i=='R' or i=='U':
        k+=1
    else:
        k-=1
if(k==0):
    print('True')
else:
    print('False')