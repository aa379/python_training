def total(n):
    if n>0:
        return n+total(n-1)
    else:
        return 0
num=int(input("請輸入一個正整數:"))
print(total(num))