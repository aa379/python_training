def fib_recursive(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)
num=int(input("請輸入一個正整數:"))
print(fib_recursive(num))