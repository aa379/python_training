import sys
import math
for line in sys.stdin:
    if not line.strip():
        continue
    a,b=map(int,line.split())
    if a==0 and b==0:
        break
    count=0
    for i in range(a,b+1):
        if math.sqrt(i).is_integer():
            count+=1
    print(count)