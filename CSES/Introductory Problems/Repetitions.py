string=input()
maxi=0
count=1
for i in range(len(string)-1):
    if(string[i]==string[i+1]):
        count+=1
    else:
        if(count>maxi):
            maxi=count
        count=1
if(count>maxi):
    maxi=count
print(maxi)


