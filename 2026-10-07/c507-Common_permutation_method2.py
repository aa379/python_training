import sys
data=sys.stdin.read().splitlines()
for i in range(0,len(data),2):
    a=data[i]
    b=data[i+1]
    count_a=[0]*26
    count_b=[0]*26
    for char in a:
        index=ord(char)-97
        count_a[index]+=1
    for char in b:
        index=ord(char)-97
        count_b[index]+=1
    result=[]
    for j in range(0,26):
        common_count=min(count_a[j],count_b[j])
        if common_count>0:
            char=chr(j+97)
            result.append(char*common_count)
    print("".join(result))