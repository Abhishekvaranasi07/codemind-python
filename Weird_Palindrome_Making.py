for i in range(int(input())):
    n=int(input())
    v=list(map(int,input().split()))
    k=0
    for r in v:
        a=r%2
        k=k+a
    print(k//2)