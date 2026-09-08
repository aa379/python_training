import sys
import math
for line in sys.stdin:
    if not line.strip():
        continue
    a,b=map(int,line.split())
    num=math.ceil((-1+math.sqrt(1-4*1*(a-a**2-2*b)))/2)
    print(num)