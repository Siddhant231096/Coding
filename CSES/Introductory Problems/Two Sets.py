n=int(input())
sum1=n*(1+n)//2
if(sum1%2==0):

    print('YES')

    sum1=sum1//2

    if(n%2==0):
        print(n//2)
        for i in range(1,(n//2)+1,2):
            print(i,end=' ')
            print(n-i+1,end=' ')
        print()
        print(n//2)
        for i in range(2,(n//2)+1,2):
            print(i,end=' ')
            print(n-i+1,end=' ')

    else:
        print((n-1)//2)
        arr=[0]*(n+1)

        for i in range(n,0,-1):
            if(sum1>=i):
                sum1=sum1-i
                arr[i]=1
                print(i,end=' ')
            else:
                if(sum1!=0):
                    arr[sum1]=1
                    print(sum1,end=' ')
                    break
        print()
        print((n+1)//2)
        for i in range(1,n+1):
            if(arr[i]==0):
                print(i,end=' ')


else:
    print('NO')