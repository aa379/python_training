def r_sum(n):
    if n>0:
        return n*(n-1)+r_sum(n-1)
    else:
        return 0
num=int(input("請輸入一個正整數:"))
print(r_sum(num))