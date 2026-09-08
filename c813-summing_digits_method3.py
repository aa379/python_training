import sys
for line in sys.stdin:
    a=line.strip()
    if not a:
        continue
    if a=="0":
        break
    ans=1+(int(a)-1)%9
    print(ans)