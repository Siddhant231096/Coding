n=int(input())
value=0
for i in range(1,n+1):
    if(i==1):
        print(0)
    elif(i==2):
        print(6)
    elif(i==3):
        print(28)
    elif(i==4):
        print(96)
    else:
        value=(i**2)*(i**2 - 1) - 2*4 - 3*8 - 4*(i-4)*4 -4*4 -(i-4)*4*6 - (i-4)*(i-4)*8
        print(value//2)