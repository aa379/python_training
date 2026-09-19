def n_digits(num):
    count=1
    while num>9:
        num//=10
        count+=1
    return count
a=int(input("請輸入一個正整數:"))
print(f"{a}為{n_digits(a)}位數")