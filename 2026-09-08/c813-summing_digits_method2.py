import sys
for line in sys.stdin:
    a=line.strip()
    if not a:
        continue
    if a=="0":
        break
    while len(a)>1:
        a=str(sum(map(int,a)))
    print(a)