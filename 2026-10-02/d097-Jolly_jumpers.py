import sys
for line in sys.stdin:
    if not line.strip():
        continue
    line=list(map(int,line.split()))
    n=line[0]
    data=line[1:]
    if n==1:
        print("Jolly")
        continue
    a=[]
    for i in range(n-1):
        a.append(abs(data[i+1]-data[i]))
    b=sorted(a)
    if b==list(range(1,n)):
        print("Jolly")
    else:
        print("Not jolly")