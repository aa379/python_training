import sys
for line in sys.stdin:
    a=line.strip()
    if not a:
        continue
    n=int(a)
    reverse_n=int(a[::-1])
    is_prime=True
    if n<2:
        is_prime=False
    elif n==2:
        is_prime=True
    elif n>=3:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                is_prime=False
                break
    if not is_prime:
        print(f"{n} is not prime.")
        continue
    if n==reverse_n:
        print(f"{n} is prime.")
        continue
    is_prime_rev=True
    if reverse_n<2:
        is_prime_rev=False
    elif reverse_n>=3:
        for i in range(2,int(reverse_n**0.5)+1):
            if reverse_n%i==0:
                is_prime_rev=False
                break
    if is_prime_rev:
        print(f"{n} is emirp.")
    else:
        print(f"{n} is prime.")