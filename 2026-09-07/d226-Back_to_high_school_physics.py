import sys
data=sys.stdin.read().split()
for index in range(0,len(data),2):
    v=int(data[index])
    t=int(data[index+1])
    print(2*v*t)