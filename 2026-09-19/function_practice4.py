def prime(x):
    a=[]
    for i in range(2,x):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            a.append(i)
    return a
num=int(input("請輸入一個正整數:"))
print(prime(num))