num=int(input("請輸入一個整數:"))
count=1
while num>9:
    num=num//10
    count+=1
print(f"{count}個位數的整數")
    