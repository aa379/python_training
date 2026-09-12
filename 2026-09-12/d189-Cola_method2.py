import sys
for line in sys.stdin:
    if not line.strip():
        continue
    n=int(line)
    total=n
    empty=n
    while empty>=3:
        new_bottle=empty//3
        total+=new_bottle
        empty=empty%3+new_bottle
    if empty==2:
        total+=1
    print(total)