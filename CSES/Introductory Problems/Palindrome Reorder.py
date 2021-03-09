string=input()
dic={}
for i in string:
    if(i in dic.keys()):
        dic[i]+=1
    else:
        dic[i]=1
count=0
n=len(string)
flag=0
new=''
value=''
for i in dic.keys():
    if(dic[i]%2==0):
        new+=i*(dic[i]//2)
        
    else:
        value=i*dic[i]
        count+=1
        if(count>1):
            flag=1
            break
if(flag==0):
    final=''
    final=new+value+new[::-1]
    print(final)
else:
    print('NO SOLUTION')
