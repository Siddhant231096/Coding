n=int(input())
count=0
value=0
arr=list(map(int,input().split()))
for i in range(1,n):
    if(arr[i-1]>arr[i]):
        value=arr[i-1]-arr[i]
        count+=value
        arr[i]=arr[i]+value
print(count)
