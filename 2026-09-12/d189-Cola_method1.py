import sys
for line in sys.stdin:
    if not line.strip():
        continue
    n=int(line)
    print(n+n//2)