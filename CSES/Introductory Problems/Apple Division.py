def app(arr,total,n):
    if(n==0 or total==0):
        #print('1 ',total)
        return total
        
    if(arr[n-1]<=total):
        #print('2 ',total)
        return max(app(arr,total-arr[n-1],n-1),app(arr,total,n-1))

    elif(arr[n-1]>total):
        #print('3 ',total)
        return app(arr,total,n-1)



n=int(input())
arr=list(map(int,input().split()))
arr.sort()
sum1=sum(arr)
total=sum1//2
total1=sum1//2
to=sum1-total
print(to-(app(arr,total,n)))
