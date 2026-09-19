def factors(n):
    a=[]
    for i in range(1,n):
        if n%i==0:
            a.append(i)
    return a
num=int(input("請輸入一個正整數:"))
print(factors(num))