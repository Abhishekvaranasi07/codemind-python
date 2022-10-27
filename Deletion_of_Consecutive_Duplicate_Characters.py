for i in range(int(input())):
    s=list(input())
    k=0
    for i in range(0,len(s)-1):
        if(s[i]==s[i+1]):
            k+=1
    print(k)