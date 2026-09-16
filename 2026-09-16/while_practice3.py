n=int(input("請輸入一個正整數:"))
i=1
count=0
divisor=[]
while i<=n:
    if n%i==0:
        divisor.append(i)
        count+=1
    i+=1
print(f"{n}的因數有{count}個，分別為",divisor)