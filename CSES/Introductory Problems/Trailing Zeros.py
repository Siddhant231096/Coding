n=int(input())
x=2
y=4
z=5
w=10
zero=1

while(True):
    if(x>n):
        break
    elif(y>n):
        zero=zero*x
        break
    elif(z>n):
        zero=zero*y*x
        break
    elif(w>n):
        zero=zero*z*y*x
        break
    else:
        zero=zero*x*y*z*w
        x+=10
        y+=10
        z+=10
        w+=10
s=str(zero)
count=0
for i in range(len(s)-1,-1,-1):
    if(s[i]!='0'):
        break
    else:
        count+=1
print(count)

