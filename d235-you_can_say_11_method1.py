import sys
for line in sys.stdin:
    if not line.strip():
        continue
    a=int(line)
    if a==0:
        break
    if a%11==0:
        print(f"{a} is a multiple of 11.")
    else:
        print(f"{a} is not a multiple of 11.")