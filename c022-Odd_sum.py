import sys
data=sys.stdin.read().split()
T=int(data[0])
index=1
for i in range(1,T+1):
    a=int(data[index])
    b=int(data[index+1])
    index+=2
    sum=0
    for j in range(a,b+1):
       if j%2==1:
           sum+=j
    print(f"Case {i}: {sum}")