n=int(input())
value=1
for i in range(1,n+1):
    value=value*(2)%(10**9 + 7)
print(value)