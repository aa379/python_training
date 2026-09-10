import sys
for line in sys.stdin:
    a=line.strip()
    if not a:
        continue
    x=int(a)
    line_poly=sys.stdin.readline().strip()
    coeffs=[]
    for i in line_poly.split():
        coeffs.append(int(i))
    n=len(coeffs)-1
    ans=0
    for i in range(n):
        power=n-i
        new_coeff=coeffs[i]*power
        ans+=new_coeff*(x**(power-1))
    print(ans)