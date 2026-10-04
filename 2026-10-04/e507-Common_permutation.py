import sys
data=sys.stdin.read().splitlines()
idx=0
while idx<len(data):
    s1=data[idx]
    s2=data[idx+1]
    idx+=2
    d1={}
    d2={}
    for char in s1:
        d1[char]=d1.get(char,0)+1
    for char in s2:
        d2[char]=d2.get(char,0)+1
    ans=""
    for i in range(97,123):
        char=chr(i)
        count1=d1.get(char,0)
        count2=d2.get(char,0)
        min_count=min(count1,count2)
        ans+=char*min_count
    print(ans)