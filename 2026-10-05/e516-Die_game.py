import sys
data=sys.stdin.read().split()
idx=0
while idx<len(data):
    n=int(data[idx])
    idx+=1
    a=data[idx:idx+n]
    idx+=n
    if n==0:
        break
    top,north,west=1,2,3
    for j in a:
        if j=="north":
            top,north=7-north,top
        if j=="south":
            top,north=north,7-top
        if j=="east":
            top,west=west,7-top
        if j=="west":
            top,west=7-west,top
    print(top)