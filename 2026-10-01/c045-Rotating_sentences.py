import sys
data=sys.stdin.read().splitlines()
if data:
    max_length=max(len(i) for i in data)
for i in range(max_length):
    a=[]
    for j in reversed(data):
        if i<len(j):
            a.append(j[i])
        else:
            a.append(" ")
    print("".join(a))