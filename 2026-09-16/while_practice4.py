num=int(input("請輸入一個正整數:"))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print(f"{num}為質數")
else:
    print(f"{num}不是質數")