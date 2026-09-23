def sign(x):
    if x>=0:
        return 1
    else:
        return -1
num=int(input("請輸入一個整數:"))
print(sign(num))