def prime_factors(x):
    a=[]
    d=2
    while d*d<=x:
        if x%d==0:
            a.append(d)
            while x%d==0:
                x//=d
        d+=1
    if x>1:
        a.append(x)
    return a
num=int(input("請輸入一個正整數:"))
print(prime_factors(num))