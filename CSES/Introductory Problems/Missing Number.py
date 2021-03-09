n=int(input())
a=[0]*(n+1)
arr=list(map(int,input().split()))
for i in arr:
    a[i]=1
print(a[1:].index(0) + 1)