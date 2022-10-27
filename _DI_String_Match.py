s=list(input())
vk=[]
v,k=0,len(s)
for i in s:
    if i=='I':
        vk.append(v)
        v+=1
    else:
        vk.append(k)
        k-=1
for i in range(v,k+1):
    if i not in vk:
        vk.append(i)
print(*vk)