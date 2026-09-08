import sys
for line in sys.stdin:
    if not line.strip():
        continue
    a=line.strip()
    if a=="0":
        break
    odd_sum=sum(map(int,a[::2]))
    even_sum=sum(map(int,a[1::2]))
    if abs(odd_sum-even_sum)%11==0:
        print(f"{a} is a multiple of 11.")
    else:
        print(f"{a} is not a multiple of 11.")