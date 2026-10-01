num=int(input())
a={}
for i in range(num):
    line=input().upper()
    for ch in line:
        if "A"<=ch<="Z":
            a[ch]=a.get(ch,0)+1
ans=sorted(a.items(),key=lambda x:(-x[1],x[0]))
for item in ans:
    print(*item)