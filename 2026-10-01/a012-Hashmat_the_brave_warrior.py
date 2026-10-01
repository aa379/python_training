import sys
for line in sys.stdin:
    if not line.strip():
        continue
    a,b=map(int,line.split())
    ans=abs(a-b)
    print(ans)