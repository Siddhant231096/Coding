for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    if(x>y):
        diag=1+x*(x-1)
        if(x%2==0):
            print(diag+(x-y))
        else:
            print(diag-(x-y))
    elif(y>x):
        diag=1+y*(y-1)
        if(y%2==0):
            print(diag-(y-x))
        else:
            print(diag+(y-x))
    else:
        print(1+y*(y-1))
