for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    
    if(a==0 and b==0):
        print('YES')
    elif((a+b)%3==0):
        sum1=a+b
        if(a==b):
            print('YES')
        elif(sum1//3<=min(a,b)):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')