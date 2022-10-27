for i in range(int(input())):
    s=input()
    t=s[::-1]
    if s==t:
        print('YES',end=' ')
        if len(s)%2==0:
            print('EVEN')
        else:
            print('ODD')
    else:
        print('NO')