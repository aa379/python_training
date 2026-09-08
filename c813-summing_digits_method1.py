import sys
for line in sys.stdin:
    s=line.strip()
    if not s:
        continue
    if s=="0":
        break
    while len(s)>1:
        total=0
        for i in s:
            total+=int(i)
        s=str(total)
    print(s)    