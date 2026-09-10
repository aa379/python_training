import sys
def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n>=3:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
for line in sys.stdin:
    a=line.strip()
    if not a:
        continue
    n=int(a)
    reverse_n=int(a[::-1])
    if not is_prime(n):
        print(f"{a} is not prime.")
    elif n!=reverse_n and is_prime(reverse_n):
        print(f"{a} is emirp.")
    else:
        print(f"{a} is prime.")