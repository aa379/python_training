import sys
first_line=sys.stdin.readline()
for line in sys.stdin:
    if not line.strip():
        continue
    part=line.split()
    n=int(part[0])
    p=float(part[1])
    i=int(part[2])
    if p==0:
        print(0.0000)
    else:
        prob=p*(1-p)**(i-1)/(1-(1-p)**n)
        print(f"{prob:.4f}")