def isprime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
num=int(input("請輸入一個正整數:"))
print(isprime(num))