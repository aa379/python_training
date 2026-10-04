import sys
for line in sys.stdin:
    if not line.strip():
        continue
    n,m=map(int,line.split())
    if m <= 1 or n < 2:
        print("Boring!")
        continue
    seq=[n]
    is_boring=False
    while n>1:
        if n%m!=0:
            is_boring=True
            break
        n//=m
        seq.append(n)
    if is_boring:
        print("Boring!")
    else:
        print(*seq)