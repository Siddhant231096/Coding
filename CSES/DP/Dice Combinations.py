n=int(input())
x=0
if(n>6):
    if(n>8):
        x=(1*((2**2)**(n-8) -1))//(3)
    value=2**(n-1)
    sum1=(1*(2**(n-6) - 1))
    value=value - sum1 - x
    print(value%(10**9 +7))
else:
    print(2**(n-1)%(10**9 +7))