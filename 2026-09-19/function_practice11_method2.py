def perfect_num():
    b=[]
    for i in range(2,10000):
        factor_sum=1
        limit=int(i**0.5)
        for j in range(2,limit+1):
            if i%j==0:
                factor_sum+=j
                if j*j!=i:
                    factor_sum+=i//j
        if factor_sum==i:
            b.append(i)
    return b
print(perfect_num())