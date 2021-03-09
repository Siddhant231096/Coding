from itertools import permutations
string=input()
s=set()
for p in permutations(string):
    s.add(''.join(p))
s=sorted(list(s))
print(len(s))
for i in range(len(s)):
    print(s[i])