def add(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
num=int(input("請輸入一個正整數:"))
print(add(num))