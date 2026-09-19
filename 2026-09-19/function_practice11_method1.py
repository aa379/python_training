def perfect_num():
    b=[]
    for i in range(1,10000):
        a=[]
        for j in range(1,i):
            if i%j==0:
                a.append(j)
        if sum(a)==i:
            b.append(i)
    return b
print(perfect_num())