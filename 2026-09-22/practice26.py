def fib_for(n):
    a=1
    b=1
    for i in range(n-2):
        a,b=b,a+b
    return b
num=int(input("請輸入一個正整數:"))
print(fib_for(num))